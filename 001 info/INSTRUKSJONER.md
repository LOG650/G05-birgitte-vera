# Prosjektinstruksjoner – G05 Birgitte & Vera
**LOG650 – Høgskolen i Molde**
**Innlevering: 2026-05-31**

---

## Om prosjektet

Bacheloroppgave om bruk av maskinlæring (Random Forest-klassifisering) for å forbedre kanaliseringsbeslutninger for brukte mobilenheter hos **Modino AS** — en nordisk recommerce-aktør som kjøper, renoverer og videreselger brukte smarttelefoner.

Den aktive rapporten er **`005 report/Prosjektoppgave_LOG650_G05_BETA.md`**. Den gamle rapporten (`Prosjektoppgave_LOG650_G05.md`) er forkastet pga. feil datapipeline og feil klassifiseringslogikk.

---

## Kritiske regler

1. **Slå aldri sammen dataffilene.** CellDe og SAP er to separate filer med to separate flows. De kobles kun i minnet (`merged = cellde.merge(sap_clean, ...)`) og lagres aldri som én kombinert fil.
2. **Bruk alltid `kunnr` (numerisk kunde-ID) for identifisering** — ikke kundenavn (`name1`), som er upålitelig pga. tegnsett og varianter.
3. **Be om tillatelse før du skriver innhold i rapporten** — ett kapittel om gangen.
4. **Ikke bruk SAP-data som features i modellen** (target leakage). Kun CellDe-data er tilgjengelig ved mottakstidspunktet.

---

## Dataarkitektur

### To kildefiler (i `004 data/data may 2026/`)

| Fil | Kilde | Innhold | Rader |
|---|---|---|---|
| `InspectedDeviceREport_cleaned_anon.xlsx` | CellDe | Mottak og gradering | 2024: 45 676, 2025: 57 867 |
| `Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx` | SAP S/4HANA | Salg og fakturering | 93 580 (én rad per IMEI) |

**Koblingsnøkkel:** IMEI (15-sifret tekststreng)

### Standardkode for innlasting

```python
import pandas as pd

cellde_path = '004 data/data may 2026/InspectedDeviceREport_cleaned_anon.xlsx'
sap_path    = '004 data/data may 2026/Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx'

cd24 = pd.read_excel(cellde_path, sheet_name='2024', dtype={'IMEI': str})
cd25 = pd.read_excel(cellde_path, sheet_name='2025', dtype={'IMEI': str})
cellde = pd.concat([cd24, cd25], ignore_index=True).drop_duplicates(subset='IMEI', keep='first')

sap = pd.read_excel(sap_path, sheet_name='Sheet1', dtype={'imei': str, 'kunag': str, 'kunnr': str})
```

---

## Klassifiseringslogikk (målvariabel)

Tre klasser basert på SAP-data. Sjekkes i denne rekkefølgen:

| Klasse | Regel | Forklaring |
|---|---|---|
| **C – Skrap** | `kunnr == '1365865'` | Alltid sjekket først. Kunde = "Modino vareuttak" |
| **A – Sluttkunde** | `matnr` matcher `^\d+$` | Rent numerisk = 2nd-artikkel = renovert, solgt via Teleoutlet |
| **B – Tredjepartshandler** | `kunag` i trader-mengden | Buy-back-artikkel solgt til kjent B2B-aktør |

### Kjente tradere (kunag som streng)
```python
traders = {'544127','707086','995702','498232','1533558','1536986',
           '1550704','715038','1530444','1530472','1602135','1602088'}
```

### Klassifiseringsresultat
- B: 58 388 (62,4 %)
- A: 34 648 (37,0 %)
- C: 539 (0,6 %)
- Uklassifisert (ekskludert): 5 rader

---

## Artikkelnummerlogikk i SAP

| Type | Format | Eksempel | Kanal |
|---|---|---|---|
| Buy-back | `nummer_variant_grad` | `16854_2_0` | Trader eller skrap |
| 2nd | Rent numerisk | `47731` | Teleoutlet (sluttkunde) |

Grade i 2nd-artikkel: bokstaven rett etter `2nd-` i `maktx`-kolonnen. Eks: `2nd-C iPhone 13 128GB Midnight` → grad C.

---

## Feature engineering

Kun CellDe-features brukes (tilgjengelig ved mottak):

| Feature | Kolonne | Transformasjon |
|---|---|---|
| `grade_num` | `Grade` | Ordinal: A=6, B=5, C=4, D=3, E=2, F=1 |
| `device_value` | `Inspected Device Value` | Norsk format (`'3 954,04'`) → float |
| `model_encoded` | `Device Model` | Alle 557 modeller; kodet med median `device_value` per modell |
| `color_group_enc` | `Inspection Color` | 246 farger → 10 grupper → label encoding |
| `Transaction Type_enc` | `Transaction Type` | 21 kategorier → label encoding |
| `Channel_enc` | `Channel` | 20 kategorier → label encoding |
| `Device Category_enc` | `Device Category` | 3 kategorier → label encoding |
| `har_feil` | `InspectedFaults` | Binær: 1 = feil registrert, 0 = ikke registrert |

### Fargegruppering
Black, White/Silver, Gray, Blue, Gold, Green, Purple/Violet, Red/Pink, Yellow, Other

### Norsk tallformat
```python
def parse_no_number(s):
    if pd.isna(s): return np.nan
    s = str(s).strip().replace('\xa0','').replace(' ','').replace(',','.')
    try: return float(s)
    except: return np.nan
```

---

## Modell

- **Baseline:** `DecisionTreeClassifier(class_weight='balanced', random_state=42)`
- **Primær:** `RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1)`
- **Train/test-split:** 80/20, stratifisert (`stratify=y`)

### Resultater (testsett, 18 713 rader)

| Modell | Accuracy | F1 A | F1 B | F1 C |
|---|---|---|---|---|
| Decision Tree | 80 % | 0.75 | 0.83 | 0.74 |
| Random Forest | 80 % | 0.75 | 0.84 | 0.75 |

### Feature importance (Random Forest)
1. `device_value` – 30,7 %
2. `Device Category` – 20,7 %
3. `grade_num` – 15,4 %
4. `model_encoded` – 14,0 %
5. `color_group` – 7,1 %
6. `Transaction Type` – 6,5 %
7. `Channel` – 3,5 %
8. `har_feil` – 2,1 %

---

## Metodisk begrensning: geografisk konfund

`ship_country` fra SAP er near-perfekt prediktor (NO → 98,5 % klasse A, andre land → ~100 % klasse B), men kan ikke brukes som feature — den eksisterer først etter at salget er gjennomført (target leakage). CellDe har ingen geografisk proxy (samme butikker leverer til både Norge og Estland). Denne begrensningen forklarer A/B-forvirringen i modellen og dokumenteres eksplisitt i diskusjonskapittelet.

---

## Rapportstruktur (BETA)

Fil: `005 report/Prosjektoppgave_LOG650_G05_BETA.md`

| Kapittel | Status | Merknad |
|---|---|---|
| 1 Innledning | Placeholder | Skrives sist |
| 2 Litteratur | ✅ Ferdig | |
| 3 Teori | ✅ Ferdig | |
| 4 Casebeskrivelse | ⬜ Neste | |
| 5 Metode og data | ⬜ | |
| 6 Modellering | ⬜ | |
| 7 Analyse | ⬜ | |
| 8 Resultat | ⬜ | Figurer i `005 report/` |
| 9 Diskusjon | ⬜ | |
| 10 Konklusjon | Placeholder | Skrives sist |
| Bibliografi | ⬜ | |

Figurer lagret i `005 report/`:
- `figur_konfusjonsmatriser.png`
- `figur_feature_importance.png`

---

## Filstruktur

```
G05-birgitte-vera/
├── 001 info/
│   ├── INSTRUKSJONER.md        ← denne filen
│   └── work_summary.md         ← detaljert arbeidslogg
├── 004 data/
│   └── data may 2026/
│       ├── InspectedDeviceREport_cleaned_anon.xlsx   ← CellDe
│       ├── Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx       ← SAP
│       └── HANDOVER_CONTEXT.md                        ← prosessdokumentasjon
├── 005 report/
│   ├── Prosjektoppgave_LOG650_G05_BETA.md            ← aktiv rapport
│   ├── Prosjektoppgave_LOG650_G05.md                 ← gammel rapport (forkastet)
│   ├── figur_konfusjonsmatriser.png
│   └── figur_feature_importance.png
└── 012 fase 2 - plan/
    └── Prosjektstatus_G05_BETA.md                    ← fremdriftsstatus
```

**NB:** `004 data/` er i `.gitignore` — datafiler versjonskontrolleres ikke.

---

## Viktige kontekstfiler å lese ved oppstart

1. `001 info/INSTRUKSJONER.md` — denne filen
2. `004 data/data may 2026/HANDOVER_CONTEXT.md` — fullstendig prosessflyt og databeskrivelse
3. `012 fase 2 - plan/Prosjektstatus_G05_BETA.md` — fremdriftsstatus
4. `001 info/work_summary.md` — detaljert arbeidslogg
