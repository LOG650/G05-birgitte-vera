"""
Modino-pipeline — full kjøring på ny data fra 2026-05-31
Reproduserer rapportens analyse + CV, temporal split og permutation importance.
"""
import re
import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.inspection import permutation_importance

DATA_DIR = "/Users/vera/repos/G05-birgitte-vera/004 data/ny data"
CELLDE = f"{DATA_DIR}/InspectedDeviceREport_cleaned_anon.xlsx"
SAP    = f"{DATA_DIR}/Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx"

t0 = time.time()
print(f"=== Modino pipeline (ny data) — start ===\n")

# ---------- 1. INNLASTING ----------
print("Innlasting CellDe...")
cd24 = pd.read_excel(CELLDE, sheet_name='2024', dtype={'IMEI': str})
cd25 = pd.read_excel(CELLDE, sheet_name='2025', dtype={'IMEI': str})
print(f"  CellDe 2024: {len(cd24):,} rader")
print(f"  CellDe 2025: {len(cd25):,} rader")
cellde = pd.concat([cd24, cd25], ignore_index=True) \
            .drop_duplicates(subset='IMEI', keep='first')
print(f"  CellDe etter dedup: {len(cellde):,} unike IMEI")

print("Innlasting SAP...")
sap = pd.read_excel(SAP, sheet_name='Sheet1',
                    dtype={'imei': str, 'kunag': str, 'kunnr': str})
print(f"  SAP: {len(sap):,} rader")

print(f"\nKolonner CellDe: {list(cellde.columns)[:15]}...")
print(f"Kolonner SAP: {list(sap.columns)[:15]}...")

# ---------- 2. IN-MEMORY JOIN ----------
print("\nJoin på IMEI...")
merged = sap.merge(cellde, left_on='imei', right_on='IMEI', how='left')
print(f"  Sammenslått datasett: {len(merged):,} rader")

# Sjekk overlapping
matched = merged['IMEI'].notna().sum()
print(f"  SAP-rader med CellDe-match: {matched:,} ({matched/len(merged)*100:.1f}%)")

# Sjekk 0-IMEI-overlapp mellom buy-back og 2nd (handover-funn)
buyback_pattern = re.compile(r'.*_.*_.*')
sap['matnr_str'] = sap['matnr'].astype(str)
sap['is_2nd'] = sap['matnr_str'].str.match(r'^\d+$')
sap['is_buyback'] = sap['matnr_str'].str.contains('_')
buyback_imei = set(sap[sap['is_buyback']]['imei'])
nd_imei = set(sap[sap['is_2nd']]['imei'])
overlap = buyback_imei & nd_imei
print(f"  Buy-back IMEIer: {len(buyback_imei):,}")
print(f"  2nd-IMEIer: {len(nd_imei):,}")
print(f"  Overlapp: {len(overlap):,} (handover sier 0)")

# ---------- 3. KLASSIFISERING ----------
print("\nKlassifisering (3-trinns SAP-regel)...")
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
print("  Klassefordeling (alle rader):")
print(merged['klasse'].value_counts(dropna=False))

df = merged.dropna(subset=['klasse']).copy()
print(f"  Etter eksklusjon av uklassifiserte: {len(df):,} rader")

# ---------- 4. TIME-TO-SALE-STATISTIKK (handover-funn) ----------
print("\nTime-to-sale-statistikk...")
if 'Inspected Date' in df.columns and 'fkdat' in df.columns:
    df['inspect_dt'] = pd.to_datetime(df['Inspected Date'], errors='coerce')
    df['sale_dt']    = pd.to_datetime(df['fkdat'], errors='coerce')
    df['days_to_sale'] = (df['sale_dt'] - df['inspect_dt']).dt.days
    valid = df['days_to_sale'].dropna()
    print(f"  Median: {valid.median():.0f} dager")
    print(f"  P50/P75/P90/P95/P99: "
          f"{valid.quantile(0.50):.0f} / {valid.quantile(0.75):.0f} / "
          f"{valid.quantile(0.90):.0f} / {valid.quantile(0.95):.0f} / "
          f"{valid.quantile(0.99):.0f}")
    print(f"  Andel innen 60 dager: {(valid <= 60).mean()*100:.1f}%")
    print(f"  Max: {valid.max():.0f} dager")
    print(f"  Anomalier (negativ): {(valid < 0).sum()}")

# ---------- 5. FEATURE ENGINEERING ----------
print("\nFeature engineering...")

# grade_num
grade_map = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2, 'F': 1}
df['grade_num'] = df['Grade'].map(grade_map)

# device_value (norsk format)
def parse_no(s):
    if pd.isna(s):
        return np.nan
    s = str(s).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    try:
        return float(s)
    except (ValueError, TypeError):
        return np.nan

df['device_value'] = df['Inspected Device Value'].apply(parse_no)

# model_encoded (median device_value per modell — beregnes på FULLDATAEN)
model_median = df.groupby('Device Model')['device_value'].median()
df['model_encoded'] = df['Device Model'].map(model_median)

# color_group_enc
color_groups = {
    'black': 'Black', 'jet black': 'Black', 'midnight': 'Black',
    'space black': 'Black', 'space grey': 'Gray', 'space gray': 'Gray',
    'gray': 'Gray', 'grey': 'Gray', 'graphite': 'Gray', 'titanium': 'Gray',
    'silver': 'White/Silver', 'white': 'White/Silver', 'starlight': 'White/Silver',
    'pearl': 'White/Silver',
    'blue': 'Blue', 'navy': 'Blue', 'pacific blue': 'Blue', 'sierra blue': 'Blue',
    'alpine green': 'Green', 'green': 'Green', 'mint': 'Green',
    'gold': 'Gold', 'rose gold': 'Gold',
    'purple': 'Purple/Violet', 'violet': 'Purple/Violet', 'deep purple': 'Purple/Violet',
    'red': 'Red/Pink', 'pink': 'Red/Pink', 'coral': 'Red/Pink',
    'yellow': 'Yellow',
}
def group_color(c):
    if pd.isna(c):
        return 'Other'
    cl = str(c).lower().strip()
    for k, v in color_groups.items():
        if k in cl:
            return v
    return 'Other'

df['color_group'] = df['Inspection Color'].apply(group_color)
color_to_int = {g: i for i, g in enumerate(sorted(df['color_group'].unique()))}
df['color_group_enc'] = df['color_group'].map(color_to_int)

# Label-encoding av kategoriske
for col in ['Transaction Type', 'Channel', 'Device Category']:
    if col in df.columns:
        mapping = {v: i for i, v in enumerate(df[col].fillna('Unknown').unique())}
        df[f'{col}_enc'] = df[col].fillna('Unknown').map(mapping)
    else:
        df[f'{col}_enc'] = 0

# har_feil & fault_count
df['har_feil']    = df['InspectedFaults'].notna() & (df['InspectedFaults'].astype(str).str.strip() != '')
df['har_feil']    = df['har_feil'].astype(int)
df['fault_count'] = df['InspectedFaults'].fillna('').astype(str).apply(
    lambda s: 0 if s == '' or s == 'nan' else len([x for x in s.split(',') if x.strip()])
)

# storage_gb
def extract_gb(model):
    if pd.isna(model):
        return 0
    m = re.search(r'(\d+)\s*GB', str(model), re.IGNORECASE)
    return int(m.group(1)) if m else 0

df['storage_gb'] = df['Device Model'].apply(extract_gb)

# inspect_month og inspect_year
df['inspect_month'] = df['inspect_dt'].dt.month
df['inspect_year']  = df['inspect_dt'].dt.year

# brand
df['brand'] = df['Device Model'].fillna('Unknown').astype(str).str.split().str[0]
brand_map = {v: i for i, v in enumerate(df['brand'].unique())}
df['brand_enc'] = df['brand'].map(brand_map)

# Drop rows with missing features
features = ['grade_num', 'device_value', 'model_encoded', 'color_group_enc',
            'Transaction Type_enc', 'Channel_enc', 'Device Category_enc',
            'har_feil', 'fault_count', 'storage_gb', 'inspect_month',
            'inspect_year', 'brand_enc']

before = len(df)
df = df.dropna(subset=features + ['klasse'])
print(f"  Droppet {before - len(df)} rader med manglende verdier")
print(f"  Analyseklart datasett: {len(df):,} rader")

# Klassefordeling
print("\nKlassefordeling i analyseklart datasett:")
print(df['klasse'].value_counts(normalize=True).round(4) * 100)
print(df['klasse'].value_counts())

# ---------- 6. SPLIT + TARGET ENCODING for dealer_rates ----------
print("\nSplit (80/20 stratifisert)...")
X = df[features].copy()
y = df['klasse'].copy()
dealer_id = df['DealerId'] if 'DealerId' in df.columns else pd.Series(['unknown']*len(df), index=df.index)

X_train, X_test, y_train, y_test, dealer_train, dealer_test = train_test_split(
    X, y, dealer_id, test_size=0.20, stratify=y, random_state=42)

# Target encoding på treningssett
def target_enc(dealer_train_, y_train_, target_class, dealer_test_):
    train_df = pd.DataFrame({'dealer': dealer_train_, 'y': y_train_})
    rate = (train_df['y'] == target_class).groupby(train_df['dealer']).mean()
    global_rate = (y_train_ == target_class).mean()
    return dealer_test_.map(rate).fillna(global_rate)

X_train['dealer_A_rate'] = target_enc(dealer_train, y_train, 'A', dealer_train)
X_train['dealer_B_rate'] = target_enc(dealer_train, y_train, 'B', dealer_train)
X_test['dealer_A_rate']  = target_enc(dealer_train, y_train, 'A', dealer_test)
X_test['dealer_B_rate']  = target_enc(dealer_train, y_train, 'B', dealer_test)

features_full = features + ['dealer_A_rate', 'dealer_B_rate']
print(f"  Treningssett: {len(X_train):,} rader; Testsett: {len(X_test):,} rader")
print(f"  Features (15): {features_full}")

# ---------- 7. DECISION TREE BASELINE ----------
print("\nDecision Tree (baseline)...")
dt = DecisionTreeClassifier(class_weight='balanced', random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_acc = (dt_pred == y_test).mean()
print(f"  Accuracy: {dt_acc:.4f}")
print("  Classification report:")
print(classification_report(y_test, dt_pred, digits=3))

# ---------- 8. RANDOM FOREST PRIMÆR ----------
print("\nRandom Forest (primær, 100 trær)...")
rf = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = (rf_pred == y_test).mean()
print(f"  Accuracy: {rf_acc:.4f}")
print("  Classification report:")
print(classification_report(y_test, rf_pred, digits=3))
print("  Confusion matrix:")
cm = confusion_matrix(y_test, rf_pred, labels=['A','B','C'])
print(pd.DataFrame(cm, index=['A','B','C'], columns=['A','B','C']))

# Feature importance (Gini)
print("\nFeature importance (Gini):")
imp = pd.Series(rf.feature_importances_, index=features_full).sort_values(ascending=False)
for f, v in imp.items():
    print(f"  {f:30s}  {v*100:5.2f} %")

# ---------- 9. 5-FOLD STRATIFISERT CV ----------
print("\n5-fold stratifisert CV på treningssett...")
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_acc = cross_val_score(rf, X_train, y_train, cv=skf, scoring='accuracy', n_jobs=-1)
cv_f1m = cross_val_score(rf, X_train, y_train, cv=skf, scoring='f1_macro', n_jobs=-1)
print(f"  CV accuracy per fold: {cv_acc}")
print(f"  CV accuracy mean ± std: {cv_acc.mean():.4f} ± {cv_acc.std():.4f}")
print(f"  CV macro-F1 mean ± std: {cv_f1m.mean():.4f} ± {cv_f1m.std():.4f}")

# ---------- 10. TEMPORAL VALIDERING ----------
print("\nTemporal validering — tren 2024, test 2025...")
df_2024 = df[df['inspect_year'] == 2024]
df_2025 = df[df['inspect_year'] == 2025]
print(f"  2024-data: {len(df_2024):,} rader")
print(f"  2025-data: {len(df_2025):,} rader")

X24 = df_2024[features].copy()
y24 = df_2024['klasse']
dealer24 = df_2024['DealerId'] if 'DealerId' in df_2024.columns else pd.Series(['unknown']*len(df_2024))
X25 = df_2025[features].copy()
y25 = df_2025['klasse']
dealer25 = df_2025['DealerId'] if 'DealerId' in df_2025.columns else pd.Series(['unknown']*len(df_2025))

X24['dealer_A_rate'] = target_enc(dealer24, y24, 'A', dealer24)
X24['dealer_B_rate'] = target_enc(dealer24, y24, 'B', dealer24)
X25['dealer_A_rate'] = target_enc(dealer24, y24, 'A', dealer25)
X25['dealer_B_rate'] = target_enc(dealer24, y24, 'B', dealer25)

rf_temp = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                  random_state=42, n_jobs=-1)
rf_temp.fit(X24, y24)
y25_pred = rf_temp.predict(X25)
temp_acc = (y25_pred == y25).mean()
print(f"  Temporal accuracy (2024→2025): {temp_acc:.4f}")
print("  Classification report (2025):")
print(classification_report(y25, y25_pred, digits=3))

# ---------- 11. PERMUTATION IMPORTANCE ----------
print("\nPermutation importance (5 repetisjoner — kan ta tid)...")
perm = permutation_importance(rf, X_test, y_test,
                              n_repeats=5, random_state=42, n_jobs=-1)
perm_imp = pd.Series(perm.importances_mean, index=features_full).sort_values(ascending=False)
print("Permutation importance (mean decrease in accuracy):")
for f, v in perm_imp.items():
    std = perm.importances_std[features_full.index(f)]
    print(f"  {f:30s}  {v*100:5.2f} % (± {std*100:.2f})")

print(f"\n=== Total tid: {time.time()-t0:.1f}s ===")
