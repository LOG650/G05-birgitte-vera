Du er en erfaren dataanalytiker og maskinlærings-ekspert.

## Kontekst
Vi jobber med et forskningsprosjekt (LOG650) i samarbeid med Modino AS – en nordisk 
recommerce-aktør som kjøper, renoverer og videreselger brukte mobilenheter. 

Målet er å bygge en supervised learning klassifiseringsmodell som predikerer 
lønnsomhetsklasse for innkommende brukte mobilenheter:

- Klasse A: Lønnsom å reparere og selge i nettbutikk
- Klasse B: Direkte til B2B eller reservedeler  
- Klasse C: BER – avhend

## Data
Vi har et renset datasett fra Modinos SAP-system (2024–2025) som en CSV-fil.
Variablene inkluderer enhetsattributter (merke, modell, alder, tilstandsgrad), 
reparasjonskostnader (arbeidstimer, delkostnader), estimert markedsverdi og 
historisk kanalvalg (målvariabel: klasse A, B eller C).

## ⚠️ FØR DU STARTER – obligatoriske plassholdere
Datasettet heter:     [SETT INN FILNAVN HER – f.eks. modino_data.csv]
Målvariabelen heter:  [SETT INN KOLONNENAVN HER – f.eks. "klasse"]

Erstatt begge før du sender prompten.
Hvis disse mangler vil hele analysen feile på første steg.

---

## Gjennomfør følgende steg i rekkefølge.
## Vis kode + output for hvert steg før du går videre.

---

### Steg 1 – Last inn og inspiser data
- Last inn CSV-filen
- Vis shape, kolonnenavn, dtypes og de første 5 radene
- Vis klassefordeling for målvariabelen (antall og prosent per klasse)
- Rapporter antall manglende verdier per kolonne

### Steg 2 – Enkod målvariabelen
- Sjekk om målvariabelen er numerisk eller tekststreng
- Hvis tekststreng: enkod med LabelEncoder og vis mappingen tydelig, f.eks.:
    A → 0, B → 1, C → 2
- Lagre mappingen slik at den kan brukes til å tolke prediksjoner senere

### Steg 3 – Feature engineering
- Beregn enhetsalder i måneder fra lanseringsår til mottaksdato (hvis tilgjengelig)
- Beregn kostnadsforhold: reparasjonskostnad / markedsverdi
- Kode kategoriske variabler:
    Lav kardinalitet (≤ 10 unike verdier): one-hot encoding
    Høy kardinalitet (> 10 unike verdier): target encoding
- Skaler numeriske variabler med StandardScaler

### Steg 4 – Train/test-split
- Sjekk antall observasjoner i datasettet:
    Hvis ≥ 500 observasjoner: stratifisert 80/20-split (random_state=42)
    Hvis < 500 observasjoner: bruk 10-fold kryssvalidering i stedet,
    informer oss eksplisitt om dette valget og fortsett deretter
- Vis klassefordeling i trenings- og testsett for å bekrefte stratifiseringen

### Steg 5 – Baseline: Decision Tree
- Tren en Decision Tree med default parametere (random_state=42)
- Rapporter: accuracy, precision, recall og F1 per klasse
- Vis confusion matrix som heatmap med klassenavn (A, B, C)

### Steg 6 – Primærmodell: Random Forest
- Tren en Random Forest med default parametere (random_state=42)
- Rapporter samme metrikker som i steg 5
- Sammenlign Decision Tree vs. Random Forest i én felles tabell

### Steg 7 – Håndter klasseimbalanse
- Sjekk om noen klasse utgjør mindre enn 20 % av datasettet
- Hvis ja: tren Random Forest på nytt med class_weight='balanced'
- Sammenlign precision og recall per klasse før og etter i en tabell
- Bruk følgende beslutningsregel for å velge mellom 'balanced' og None:

    Hvis class_weight='balanced' gir høyere recall for klasse C
    OG accuracy-fallet er mindre enn 5 prosentpoeng:
        → Behold 'balanced' og dokumenter avveiningen eksplisitt

    Hvis accuracy-fallet er større enn 5 prosentpoeng:
        → Bruk None og noter at klasseimbalansen ikke lot seg løse
          med vekting alene – foreslå SMOTE som alternativ

- Forklar forretningsmessig hvorfor høy recall for klasse C prioriteres:
  en C→A-feil (BER-enhet repareres unødvendig) binder opp tekniker-
  og deleressurser uten inntekt, og er derfor mer kostbar for Modino
  enn en A→C-feil (lønnsom enhet avhendes for tidlig)

### Steg 8 – Hyperparameteroptimering
- Kjør GridSearchCV på Random Forest med 5-fold CV på treningssettet
- Søkerom:
    n_estimators: [100, 200, 500]
    max_depth: [5, 10, 20, None]
    min_samples_split: [2, 5, 10]
    class_weight: ['balanced', None]
- Rapporter beste parametere og beste CV-score

### Steg 9 – Endelig evaluering på testsett
- Evaluer den beste modellen på testsettet
- Rapporter: accuracy, precision, recall, F1 per klasse
- Vis confusion matrix med klassenavn (A, B, C)
- Sjekk eksplisitt om accuracy ≥ 80 % og skriv én av følgende:
    ✅ Kravet er oppfylt: accuracy = XX %
    ❌ Kravet er IKKE oppfylt: accuracy = XX %

- Hvis accuracy < 80 %:
    Tren en Gradient Boosting-modell (XGBoost eller LightGBM) som alternativ
    Sammenlign alle tre modeller (Decision Tree, Random Forest, Gradient Boosting)
    i én tabell og anbefal den beste basert på accuracy og recall for klasse C

### Steg 10 – Feature importance
- Vis de 10 viktigste variablene som et horisontalt stolpediagram
- Kommenter eksplisitt:
    Er alder, kostnadsforhold eller tilstandsgrad blant de tre viktigste?
    Hva betyr dette konkret for Modinos klassifiseringsprosess?
    Hvilke variabler har overraskende lav eller høy viktighet?

### Steg 11 – Lagre alle resultater
- Lagre den trente modellen som:            modino_rf_model.pkl
- Lagre LabelEncoder-mappingen som:         label_encoder.pkl
- Lagre alle figurer som PNG med navn:
    confusion_matrix_baseline.png
    confusion_matrix_rf.png
    confusion_matrix_final.png
    feature_importance.png
- Lagre alle evalueringsmetrikker i:        resultater.csv
  med kolonnene:
    modell, klasse, accuracy, precision, recall, F1, beste_hyperparametere

- Hvis kryssvalidering ble valgt i steg 4:
    Lagre også CV-scores per fold i:        cv_resultater.csv
  med kolonnene:
    fold, accuracy, precision_A, recall_A,
    precision_B, recall_B, precision_C, recall_C

### Steg 12 – Oppsummering
Skriv en strukturert oppsummering med følgende punkter:

1. Datasettets størrelse og klassefordeling
2. Valgt analyseopplegg (80/20-split eller kryssvalidering) og begrunnelse
3. Beste modell og dens accuracy på testsettet
4. Precision og recall for klasse C – vurder mot følgende terskel:
     recall for klasse C ≥ 0.75 = forretningsmessig tilfredsstillende for Modino
     recall for klasse C < 0.75 = utilfredsstillende, forklar konsekvensen
5. De tre viktigste prediktorene og hva de betyr for Modino
6. Om 80 %-kravet ble nådd – og hvilken modell som ble valgt og hvorfor
7. Anbefalinger til videre arbeid basert på funnene

---

## Tekniske krav
- Språk: Python 3.11+
- Biblioteker: pandas, scikit-learn, matplotlib, seaborn
- random_state=42 i alle steg som involverer tilfeldighet
- All kode skal være kommentert på norsk
- Vis output etter hvert steg – ikke bare kode
- Ikke hopp over steg selv om et tidligere steg gir gode resultater
