"""
To eksperimenter på toppen av hovedpipelinen:
  E1: RF uten dealer_A_rate / dealer_B_rate (13 features) — bekreft permutation-funn
  E2: Temporal split UTEN inspect_year — krymper drift?
"""
import re, time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

DATA_DIR = "/Users/vera/repos/G05-birgitte-vera/004 data/ny data"
CELLDE = f"{DATA_DIR}/InspectedDeviceREport_cleaned_anon.xlsx"
SAP    = f"{DATA_DIR}/Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx"

t0 = time.time()
print("=== Eksperimenter på ny data ===\n")

# ---- 1. INNLASTING + KLASSIFISERING (identisk med hovedpipeline) ----
cd24 = pd.read_excel(CELLDE, sheet_name='2024', dtype={'IMEI': str})
cd25 = pd.read_excel(CELLDE, sheet_name='2025', dtype={'IMEI': str})
cellde = pd.concat([cd24, cd25], ignore_index=True).drop_duplicates(subset='IMEI', keep='first')
sap = pd.read_excel(SAP, sheet_name='Sheet1',
                    dtype={'imei': str, 'kunag': str, 'kunnr': str})
merged = sap.merge(cellde, left_on='imei', right_on='IMEI', how='left')

traders = {'544127', '707086', '995702', '498232', '1533558', '1536986',
           '1550704', '715038', '1530444', '1530472', '1602135', '1602088'}

def classify(row):
    if row['kunnr'] == '1365865':
        return 'C'
    if re.fullmatch(r'\d+', str(row['matnr'])):
        return 'A'
    if row['kunag'] in traders:
        return 'B'
    return None

merged['klasse'] = merged.apply(classify, axis=1)
df = merged.dropna(subset=['klasse']).copy()
df['inspect_dt'] = pd.to_datetime(df['Inspected Date'], errors='coerce')
df['sale_dt']    = pd.to_datetime(df['fkdat'], errors='coerce', dayfirst=True)

# ---- FEATURES (identisk med hovedpipeline) ----
df['grade_num'] = df['Grade'].map({'A':6,'B':5,'C':4,'D':3,'E':2,'F':1})

def parse_no(s):
    if pd.isna(s): return np.nan
    s = str(s).strip().replace('\xa0','').replace(' ','').replace(',','.')
    try: return float(s)
    except: return np.nan
df['device_value'] = df['Inspected Device Value'].apply(parse_no)

model_median = df.groupby('Device Model')['device_value'].median()
df['model_encoded'] = df['Device Model'].map(model_median)

color_groups = {
    'black':'Black','jet black':'Black','midnight':'Black','space black':'Black',
    'space grey':'Gray','space gray':'Gray','gray':'Gray','grey':'Gray',
    'graphite':'Gray','titanium':'Gray',
    'silver':'White/Silver','white':'White/Silver','starlight':'White/Silver','pearl':'White/Silver',
    'blue':'Blue','navy':'Blue','pacific blue':'Blue','sierra blue':'Blue',
    'alpine green':'Green','green':'Green','mint':'Green',
    'gold':'Gold','rose gold':'Gold',
    'purple':'Purple/Violet','violet':'Purple/Violet','deep purple':'Purple/Violet',
    'red':'Red/Pink','pink':'Red/Pink','coral':'Red/Pink',
    'yellow':'Yellow',
}
def group_color(c):
    if pd.isna(c): return 'Other'
    cl = str(c).lower().strip()
    for k,v in color_groups.items():
        if k in cl: return v
    return 'Other'

df['color_group'] = df['Inspection Color'].apply(group_color)
color_to_int = {g:i for i,g in enumerate(sorted(df['color_group'].unique()))}
df['color_group_enc'] = df['color_group'].map(color_to_int)

for col in ['Transaction Type','Channel','Device Category']:
    if col in df.columns:
        m = {v:i for i,v in enumerate(df[col].fillna('Unknown').unique())}
        df[f'{col}_enc'] = df[col].fillna('Unknown').map(m)

df['har_feil'] = (df['InspectedFaults'].notna() &
                  (df['InspectedFaults'].astype(str).str.strip()!='')).astype(int)
df['fault_count'] = df['InspectedFaults'].fillna('').astype(str).apply(
    lambda s: 0 if s in ('','nan') else len([x for x in s.split(',') if x.strip()]))

def extract_gb(model):
    if pd.isna(model): return 0
    m = re.search(r'(\d+)\s*GB', str(model), re.IGNORECASE)
    return int(m.group(1)) if m else 0
df['storage_gb'] = df['Device Model'].apply(extract_gb)

df['inspect_month'] = df['inspect_dt'].dt.month
df['inspect_year']  = df['inspect_dt'].dt.year
df['brand'] = df['Device Model'].fillna('Unknown').astype(str).str.split().str[0]
brand_map = {v:i for i,v in enumerate(df['brand'].unique())}
df['brand_enc'] = df['brand'].map(brand_map)

features_base = ['grade_num','device_value','model_encoded','color_group_enc',
                 'Transaction Type_enc','Channel_enc','Device Category_enc',
                 'har_feil','fault_count','storage_gb','inspect_month',
                 'inspect_year','brand_enc']
df = df.dropna(subset=features_base + ['klasse'])
print(f"Analyseklart datasett: {len(df):,} rader\n")

def target_enc(d_train, y_train_, target_class, d_apply):
    rate = pd.DataFrame({'d':d_train,'y':y_train_})
    rate = (rate['y']==target_class).groupby(rate['d']).mean()
    global_rate = (y_train_==target_class).mean()
    return d_apply.map(rate).fillna(global_rate)

# ===========================================================
# E1: RANDOM FOREST UTEN dealer-features (13 features)
# ===========================================================
print("="*65)
print("EKSPERIMENT 1: RF uten dealer_A_rate / dealer_B_rate")
print("="*65)

X = df[features_base].copy()
y = df['klasse'].copy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42)

rf_13 = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                random_state=42, n_jobs=-1)
rf_13.fit(X_train, y_train)
pred_13 = rf_13.predict(X_test)
acc_13 = (pred_13==y_test).mean()
print(f"\n13-feature RF accuracy: {acc_13:.4f}")
print("Classification report:")
print(classification_report(y_test, pred_13, digits=3))
print("Konfusjonsmatrise:")
print(pd.DataFrame(confusion_matrix(y_test, pred_13, labels=['A','B','C']),
                   index=['A','B','C'], columns=['A','B','C']))

# Til sammenligning: 15-feature RF
print("\n--- Sammenligning: 15-feature RF (med dealer-rates) ---")
X_train_15 = X_train.copy()
X_test_15  = X_test.copy()
dealer_train = df.loc[X_train.index, 'DealerId']
dealer_test  = df.loc[X_test.index,  'DealerId']
X_train_15['dealer_A_rate'] = target_enc(dealer_train, y_train, 'A', dealer_train)
X_train_15['dealer_B_rate'] = target_enc(dealer_train, y_train, 'B', dealer_train)
X_test_15['dealer_A_rate']  = target_enc(dealer_train, y_train, 'A', dealer_test)
X_test_15['dealer_B_rate']  = target_enc(dealer_train, y_train, 'B', dealer_test)

rf_15 = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                random_state=42, n_jobs=-1)
rf_15.fit(X_train_15, y_train)
acc_15 = (rf_15.predict(X_test_15)==y_test).mean()
print(f"15-feature RF accuracy: {acc_15:.4f}")
print(f"\nDIFF: {(acc_13-acc_15)*100:+.2f} pp (13-feature minus 15-feature)")
if acc_13 >= acc_15 - 0.002:
    print("=> Permutation-funn BEKREFTET: dealer-features tilfører ikke verdi")
else:
    print(f"=> Dealer-features tilfører {(acc_15-acc_13)*100:.2f} pp accuracy")

# ===========================================================
# E2: TEMPORAL UTEN inspect_year
# ===========================================================
print("\n" + "="*65)
print("EKSPERIMENT 2: Temporal validering UTEN inspect_year")
print("="*65)

features_no_year = [f for f in features_base if f != 'inspect_year']
df_2024 = df[df['inspect_year']==2024]
df_2025 = df[df['inspect_year']==2025]
print(f"2024-data: {len(df_2024):,} rader")
print(f"2025-data: {len(df_2025):,} rader")

# E2a: TEMPORAL MED inspect_year (referansescenarioet, identisk med tabell 7.2)
X24 = df_2024[features_base].copy()
y24 = df_2024['klasse']
X25 = df_2025[features_base].copy()
y25 = df_2025['klasse']
d24 = df_2024['DealerId']
d25 = df_2025['DealerId']
X24['dealer_A_rate'] = target_enc(d24, y24, 'A', d24)
X24['dealer_B_rate'] = target_enc(d24, y24, 'B', d24)
X25['dealer_A_rate'] = target_enc(d24, y24, 'A', d25)
X25['dealer_B_rate'] = target_enc(d24, y24, 'B', d25)
rf_t1 = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                random_state=42, n_jobs=-1)
rf_t1.fit(X24, y24)
acc_t1 = (rf_t1.predict(X25)==y25).mean()
print(f"\nTemporal MED inspect_year: {acc_t1:.4f}")

# E2b: TEMPORAL UTEN inspect_year
X24_ny = df_2024[features_no_year].copy()
X25_ny = df_2025[features_no_year].copy()
X24_ny['dealer_A_rate'] = target_enc(d24, y24, 'A', d24)
X24_ny['dealer_B_rate'] = target_enc(d24, y24, 'B', d24)
X25_ny['dealer_A_rate'] = target_enc(d24, y24, 'A', d25)
X25_ny['dealer_B_rate'] = target_enc(d24, y24, 'B', d25)
rf_t2 = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                random_state=42, n_jobs=-1)
rf_t2.fit(X24_ny, y24)
pred_t2 = rf_t2.predict(X25_ny)
acc_t2 = (pred_t2==y25).mean()
print(f"Temporal UTEN inspect_year: {acc_t2:.4f}")
print("Classification report (UTEN inspect_year):")
print(classification_report(y25, pred_t2, digits=3))

# E2c: TEMPORAL UTEN BÅDE inspect_year OG dealer-features
features_minimal = [f for f in features_no_year if 'dealer' not in f.lower()]
X24_min = df_2024[features_no_year].copy()
X25_min = df_2025[features_no_year].copy()
rf_t3 = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                random_state=42, n_jobs=-1)
rf_t3.fit(X24_min, y24)
acc_t3 = (rf_t3.predict(X25_min)==y25).mean()
print(f"\nTemporal UTEN inspect_year OG UTEN dealer-rates (rensere): {acc_t3:.4f}")

# Oppsummering
print("\n" + "="*65)
print("OPPSUMMERING")
print("="*65)
print(f"Tilfeldig 80/20-split (15 features):       0,8376")
print(f"Tilfeldig 80/20-split (13 features):       {acc_13:.4f}")
print()
print(f"Temporal 2024→2025 (15 features):          {acc_t1:.4f}  (drift -13,3 pp)")
print(f"Temporal 2024→2025 (uten inspect_year):    {acc_t2:.4f}  (drift {(acc_t2-acc_15)*100:+.1f} pp)")
print(f"Temporal 2024→2025 (uten year+dealer):     {acc_t3:.4f}  (drift {(acc_t3-acc_13)*100:+.1f} pp)")

print(f"\nTotal tid: {time.time()-t0:.1f}s")
