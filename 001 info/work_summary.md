# Work Summary – Revisjon av Prosjektstyringsplan G05

**Dato:** 2026-03-03
**Utarbeidet av:** Birgitte (med Claude Code CLI)

---

## Hva ble gjort

Vi gjennomgikk prosjektstyringsplanen og besluttet å avgrense metodevalget fra en full optimaliseringsmodell til prediktiv modellering (klassifisering) som hovedmetode. Endringene er dokumentert i en ny versjon av planen (V2).

### Metodisk beslutning

**Valgt tilnærming:** Prediktiv modellering – supervised learning klassifisering

**Begrunnelse:**
- En optimaliseringsmodell (lineær programmering e.l.) krever eksplisitt målfunksjon, beslutningsvariabler og restriksjoner, og er for kompleks innenfor prosjektets tidsramme.
- En klassifiseringsmodell lærer direkte fra historiske data og er enklere å gjennomføre, tolke og forsvare metodisk.
- Klassifiseringen gir en klar rød tråd: **Data → Prediksjon → Prioritering → Økt lønnsomhet**

### Modellbeskrivelse

Modellen klassifiserer innkommende enheter i én av tre lønnsomhetsklasser:

| Klasse | Beskrivelse |
|--------|-------------|
| A | Lønnsom å reparere og selge i nettbutikk |
| B | Direkte til B2B/reservedeler |
| C | BER – avhend |

Valg av algoritme (f.eks. logistisk regresjon, decision tree eller random forest) avgjøres etter gjennomgang av datagrunnlaget fra Modino.

---

## Endringer i V2 (Prosjektstyringsplan_G05_V2.md)

| Seksjon | Endring |
|---------|---------|
| **1 – Sammendrag** | Problemstillingen er oppdatert til 3-klasse klassifisering. Den røde tråden er lagt inn. Referansen til optimaliseringsmodell er fjernet. |
| **3.1 – Mål** | Målet er endret fra "optimalisere livssyklusen" til å utvikle og evaluere en klassifiseringsmodell. Begrensning lagt til: ikke en full optimaliseringsmodell. |
| **3.2 – Krav** | Krav til modellen er endret til 3-klasse klassifisering (A/B/C) basert på enhetsattributter og reparasjonskostnader. Variabellisten er kortet ned. |
| **3.3 – Løsning** | Løsningen er omskrevet til supervised learning klassifisering. "Beslutningsrammeverk" erstattet med "Prioriteringslogikk". Evalueringsrammeverk justert til klassifiseringsmetrikker (accuracy, precision, recall). |
| **3.4 – WBS** | "Målfunksjon"-terminologi fjernet fra Fase 1-beskrivelsen. |
| **4.1 – Gantt** | Forkortet til én setning med referanse til MS Project-fil. Unngår duplisering av innhold. |

---

## Status

- [x] Seksjon 1 – Sammendrag
- [x] Seksjon 3.1 – Mål
- [x] Seksjon 3.2 – Krav
- [x] Seksjon 3.3 – Løsning
- [x] Seksjon 3.4 – WBS
- [x] Seksjon 4.1 – Gantt
- [x] Partnergodkjenning av V2 – filen er nå gjeldende versjon (omdøpt til Prosjektstyringsplan_G05.md)

---

## Oppdatering – 2026-03-05

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Endringer i Prosjektstyringsplan_G05.md

| Seksjon | Endring |
|---------|---------|
| **1 – Sammendrag** | Lagt til setning om at konkret definisjon av økt lønnsomhet fastsettes etter mottak av Modinos data. |
| **3.2 – Krav** | Lagt til kvantitativt ytelseskrav: modellen skal oppnå minimum 80 % nøyaktighet. Øvrige ytelseskrav fastsettes i fase 3. |

### Filstruktur og versjonskontroll

- Prosjektstyringsplan_G05_V2.md omdøpt til Prosjektstyringsplan_G05.md (gjeldende versjon)
- Prosjektstyringsplan_G05.md (tidligere V1) flyttet til 000 templates/Obsolete/ og omdøpt til Prosjektstyringsplan_G05_v1.md
- Mappe Obsolete opprettet under 000 templates for arkiverte filer
- Litteraturkilder (11 PDF-er og 1 Word-dokument) lastet opp til 003 references/Litteratur/
- Gantt-fil (Prosjekt_GANTT_G05.mpp) lastet opp til 012 fase 2 - plan/

---

## Oppdatering – 2026-04-07

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Gjennomgang av prosjektmappen

Claude Code CLI leste igjennom hele G05-birgitte-vera-mappen (unntatt Thesis Birgitte) for å få full oversikt over prosjektstatus ved oppstart av fase 3.

### 20-dagers fremdriftsplan

Det ble utarbeidet en detaljert plan frem mot innlevering av utkast til rapport **27. april 2026**. Planen dekker:

- Uke 1 (7.–13. april): Datarensing og teoriskriving parallelt
- Uke 2 (14.–20. april): Modelltrening, evaluering og rapportskriving
- Uke 3 (21.–27. april): Ferdigstilling av rapportutkast og innlevering

Foreslått oppgavefordeling: Birgitte tar datarensing, datagrunnlag og innledning/diskusjon. Vera tar metode, modellering og resultater.

### Datarensing og sammenslåing (Steg 1–3)

Data mottatt fra Modino AS ble utforsket og renset ved hjelp av Python-skriptet `clean_data.py` (lagret i 004 data/).

**Datagrunnlag:**

| Fil | Innhold |
|-----|---------|
| InspectedDeviceREport.xlsx | Inspeksjonsdata, 2 ark: 2024 (45 720 rader) og 2025 (58 318 rader) |
| Z_BBTI_IMEI_TRACK_2024_01/02.txt | SAP-salgsdata 2024 (41 808 rader totalt) |
| Z_BBTI_IMEI_TRACK_2025_01/02/03.txt | SAP-salgsdata 2025 (52 773 rader totalt) |

**Steg 1 – IMEI-validering (fjernet dummies):**

| Årsak til fjerning | 2024 | 2025 |
|--------------------|------|------|
| Null IMEI | 3 | 0 |
| Feil lengde (ikke 15 sifre) | 7 | 7 |
| Dummy-mønster (alle like sifre e.l.) | 0 | 0 |
| Luhn-algoritme-feil | 34 | 444 |
| **Gjenstår** | **45 676** | **57 867** |

Valideringsmetode: 15-sifret lengdesjekk + Luhn-algoritmen (bransjestandardvalidering av IMEI).

**Steg 2 – Gradering 2024:**

- Grade-verdiene A–F er konsistente i begge år og ble beholdt uendret.
- Transaction Type standardisert til lowercase for 2024 (inkonsistent stor/liten bokstav i kildedata, f.eks. `"Swap-in"` → `"swap-in"`).

**Steg 3 – Matching og basisfil:**

- Excel-data (begge år) matchet mot alle SAP-filer på IMEI-nummer.
- 35 053 rader fikk SAP-match; 69 455 rader hadde ingen SAP-match (forventet – ikke alle innleverte enheter selges gjennom nettbutikk).
- 7 863 rader har avvikende grade mellom Excel (inspeksjonsgrad) og SAP (salgsgrad) – flagget i kolonnen `grade_mismatch_flag`.

**Output:**

Renset basisfil lagret som `cleansed_baseline.xlsx` i 004 data/ med tre faner:
- `cleansed_baseline` – 104 508 rader med Excel + SAP-data kombinert
- `rensing_statistikk` – oversikt over hva som ble fjernet
- `grade_oversikt` – gradefordeling per år

### Åpent spørsmål

Hvilken grade skal brukes som målvariabel i modellen – inspeksjonsgraden (Excel, ved mottak) eller salgsgraden (SAP, etter reparasjon)? Dette må avklares med Vera og eventuelt faglærer før modellering starter.

---

## Oppdatering – 2026-04-17

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Dataeksplorasjon og profilering

Gjennomførte en fullstendig dataprofilering av `InspectedDeviceREport.xlsx` (begge ark) og de 5 SAP-filene:

- Kartlagt alle kolonner, datatyper, antall rader, andel manglende verdier per kolonne, fordeling av kategoriske variabler og statistisk oppsummering av numeriske variabler.
- Identifiserte at 6 kolonner er 100 % tomme i begge ark (SerialNumber, Asset ID, IncidentDate, DamageReason, DamageReasonList, Deductible).
- `Inspected Device Value`, `RepairValue` og datofelt er lagret som streng (norsk kommaformat) og må konverteres ved modellering.

### Sammenslåing av Excel og SAP-data

Mergede `InspectedDeviceREport.xlsx` med de 5 SAP-filene på IMEI-nøkkel (left join). 2024 og 2025 holdt adskilt.

| Ark | Excel-rader | SAP-rader (input) | Rader etter merge | SAP-match |
|-----|-------------|-------------------|-------------------|-----------|
| 2024 | 45 720 | 41 808 | 46 100 | 41 881 (90.8%) |
| 2025 | 58 318 | 52 773 | 58 766 | 52 793 (89.8%) |

Økning i radantall skyldes at noen IMEI-er matcher flere SAP-rader (én enhet fakturert flere ganger). Alle SAP-kolonner fikk prefiks `sap_` for å skille fra Excel-kolonner. Rådata er ikke endret.

**Output:** `merged_data_modino.xlsx` (lagret i 004 data/, to ark: 2024 og 2025, 69 kolonner per ark)

### Mappestruktur – 004 data

- Råfiler (InspectedDeviceREport.xlsx og alle .txt-filer) flyttet til `004 data/obsolete data/`
- `merged_data_modino.xlsx` er nå eneste arbeidsfil i `004 data/`

### Duplikatanalyse

Kartla omfang og type duplikater i `merged_data_modino.xlsx`. Ingen data er slettet – avventer avklaring med datakilde.

| Type duplikat | 2024 | 2025 |
|---|---|---|
| Helt identiske rader | 0 | 4 |
| Duplikate Transaction ID | 598 rader / 218 ID-er | 770 rader / 318 ID-er |
| Duplikate IMEI | 703 rader / 232 IMEI-er | 1 228 rader / 319 IMEI-er |
| Duplikate IMEI + Transaction Type | 655 rader | 1 215 rader |
| Duplikate IMEI + SAP-fakturanr | 146 rader / 52 kombi. | 40 rader / 13 kombi. |
| IMEI-dup kun fra SAP-siden | 105 rader | 458 rader |

Tre typer identifisert:
- **Type A** – Én IMEI → flere SAP-rader (konsekvens av left join, avklares med kilde)
- **Type B** – Duplikate Transaction ID-er (mulig retur/re-inspeksjon eller feilregistrering)
- **Type C** – Helt identiske rader (4 rader i 2025, trygge å slette)

Funn dokumentert i `004 data/duplikat_analyse.md`.

### Åpne spørsmål

- Avklar med datakilde: kan én IMEI ha flere SAP-transaksjoner legitimt, og hvilken skal beholdes?
- Avklar med datakilde: kan Transaction ID forekomme flere ganger legitimt (retur/re-inspeksjon)?
- Godkjenn sletting av 4 helt identiske rader i 2025-arket.

### Rapportmal konvertert til Markdown

Konverterte `000 templates/Mal prosjekt LOG650 v2.docx` til Markdown ved hjelp av python-docx. Originalfilen er uendret. Markdown-versjonen er lagret som `005 report/Mal prosjekt LOG650 v2.md` med bevarte overskrifter (Heading 1 → #, Heading 2 → ##), tabeller og lister.

### Git

- `.gitignore` opprettet: `004 data/` er ekskludert fra versjonskontroll (sensitiv informasjon).
- Pushet til main: `work_summary.md`, `.gitignore` og `005 report/Mal prosjekt LOG650 v2.md`.

---

## Oppdatering – 2026-04-18

**Utarbeidet av:** Vera (med Claude Code CLI)

### Rapportmal fylt ut med innledning, teori og metode

Tre hoveddeler ble skrevet inn i `005 report/Mal prosjekt LOG650 v2.md`, som erstatter malens veiledningstekster med faktisk rapportinnhold:

**Kapittel 1 – Innledning (nyskrevet)**

Innledningen ble skrevet basert på prosjektets proposal (`011 fase 1 - proposal/Proposal.md`) og teorien som allerede var utarbeidet. Inkluderer:

- Introduksjon fra generelt tema (sirkulærøkonomi, recommerce) til spesifikt problem (Modinos klassifiseringsutfordring)
- Referanser til nøkkellitteratur (Ferguson et al., Guide & Van Wassenhove, Ibrahim & Abdul-Kader, Govindan et al.)
- Rapportens struktur (kapitteloversikt)
- **1.1 Problemstilling:** «Hvordan kan en AI-basert klassifiseringsmodell forbedre kanaliseringsbeslutninger for brukte mobilenheter hos Modino AS?» med to operasjonaliserte delproblemer (klassifiseringsnøyaktighet og lønnsomhetseffekt)
- **1.2 Avgrensninger:** Geografisk (Norge), tidsperiode (2024–2025), produktkategori (mobilenheter) og beslutningsomfang
- **1.3 Antagelser:** Historiske utfall reflekterer lønnsomhet; stabile markedsforhold

**Kapittel 2 – Teori og litteratur (satt inn fra ferdig utkast)**

Innholdet fra `005 report/teoridel_G05_v3-2.md` ble satt inn og erstatter malens Litteratur- og Teori-plassholdere. Dekker tre pilarer: sirkulærøkonomi og recommerce (2.1), beslutningsstøtte og verdifall (2.2), og maskinlæring og klassifisering (2.3), med oppsummering og kobling til problemstilling (2.4).

**Kapittel 3 – Data og metode (satt inn fra ferdig utkast)**

Innholdet fra `005 report/metodeseksjon_G05_v2-2.md` ble satt inn og erstatter malens Metode og data-plassholder. Dekker forskningsdesign (3.1), datagrunnlag (3.2), datarensing og feature engineering (3.3), analysemetode og modellvalg (3.4) og evalueringsrammeverk (3.5).

### Git

- Committet og pushet til main: `005 report/Mal prosjekt LOG650 v2.md` (552 innsettinger, 95 slettinger).

---

## Oppdatering – 2026-04-19

**Utarbeidet av:** Vera (med Claude Code CLI)

### Maskinlæringsanalyse – fullstendig pipeline (12 steg)

Gjennomførte komplett ML-pipeline på `004 data/modino_merged.csv` (94 096 rader × 29 kolonner).

**Datafunn og mapping:**

Grade-kolonnen inneholdt 6 inspeksjonsgrader (A–F), ikke 3 klasser som forventet. Mappet til 3 lønnsomhetsklasser basert på revenue-mønstre og maktx-prefiks:

| Inspeksjonsgrad | → Lønnsomhetsklasse | Antall | Andel |
|---|---|---|---|
| A, B | Klasse A (nettbutikk) | 40 929 | 43.5 % |
| C | Klasse B (B2B/reservedeler) | 39 271 | 41.7 % |
| D, E, F | Klasse C (BER/avhend) | 13 896 | 14.8 % |

⚠️ Mappingen bør valideres med Modino mot faktisk kanalvalg.

**Feature engineering:**

- 11 features: 8 numeriske + 3 target-enkodede kategoriske
- Konverterte norsk tallformat (cost, vat, Inspected Device Value) til float
- Avledede variabler: kostnadsforhold (cost/markedsverdi), margin, revenue_cost_ratio, gjennomløpstid
- Target encoding for Transaction Type (21 verdier), brand (18), Inspection Color (240)
- StandardScaler på alle features

**Modellresultater (testsett, 18 820 rader):**

| Modell | Accuracy | Precision C | Recall C | F1 C |
|---|---|---|---|---|
| Decision Tree (baseline) | 88.8 % | 0.964 | 0.947 | 0.956 |
| Random Forest (default) | 92.2 % | 0.980 | 0.966 | 0.973 |
| **Random Forest (optimert)** | **92.4 %** | **0.981** | **0.967** | **0.974** |

- ✅ 80 %-kravet oppfylt (92.4 %)
- ✅ Recall klasse C (0.97) >> 0.75-terskelen
- Gradient Boosting var ikke nødvendig

**Beste hyperparametere (GridSearchCV, 5-fold CV):**

- n_estimators: 500, max_depth: None, min_samples_split: 2, class_weight: balanced

**Topp 3 prediktorer (feature importance):**

1. Inspected Device Value (0.217) – estimert markedsverdi
2. Kostnadsforhold (0.124) – cost/markedsverdi, definerer BER-terskel
3. Device Category (0.107) – enhetskategori

Overraskende lavt: brand (0.025) – merke har liten påvirkning sammenlignet med økonomiske variabler.

**Lagrede filer i 004 data/:**

- `modino_rf_model.pkl` – trent Random Forest-modell
- `label_encoder.pkl` – LabelEncoder (A→0, B→1, C→2)
- `resultater.csv` – alle evalueringsmetrikker
- `confusion_matrix_baseline.png`, `confusion_matrix_rf.png`, `confusion_matrix_final.png`
- `feature_importance.png`

### Åpne spørsmål

- Validering av grade-til-klasse-mapping (A+B→A, C→B, D+E+F→C) med Modino
- Estimert kostnadsbesparelse (steg fra metodekapitlet) er ennå ikke beregnet
- Device Model (518 unike) ble ikke brukt direkte – vurder embeddings/gruppering
- Target leakage: revenue, cost, margin og revenue_cost_ratio er post-beslutningsvariabler – bør kjøres uten disse for å vurdere realistisk accuracy

---

## Oppdatering – 2026-04-19 (del 2)

**Utarbeidet av:** Vera (med Claude Code CLI)

### Rapportmal fylt ut med analyse, resultat, diskusjon og konklusjon

Følgende kapitler ble skrevet inn i `005 report/Mal prosjekt LOG650 v2.md` basert på `004 data/resultater.csv`:

**Kapittel 5 – Modellering (nyskrevet)**

Matematisk formulering av klassifiseringsproblemet: problemformulering (feature-vektor → klasse), Decision Tree med Gini-indeks (baseline), Random Forest med majoritetsstemme og class_weight-vekting (primærmodell), feature importance via Gini-reduksjon, og Gradient Boosting som reservemodell. Refererer til kap. 3.5 for evalueringsmetrikker for å unngå overlapp.

**Kapittel 6 – Analyse**

Datagrunnlag og klassefordeling (94 096 obs., 6→3 mapping), feature engineering (11 features med target encoding), train/test-split (80/20) og modelltrening (Decision Tree, Random Forest default, Random Forest optimert).

**Kapittel 7 – Resultat**

Modellsammenligning (tabell med accuracy/precision/recall/F1 per klasse for alle tre modeller), beste hyperparametere, confusion matrix, klasseimbalanse-håndtering, feature importance (topp 10) og accuracy-sjekk (92,4 % > 80 %).

**Kapittel 8 – Diskusjon**

Funn opp mot problemstilling, sammenligning med litteraturen (Ibrahim & Abdul-Kader, Ferguson et al., Turkolmez et al.), forretningsmessig betydning for Modino, og metodiske begrensninger: target leakage-risiko, grade-mapping-usikkerhet, intern/ekstern validitet.

**Kapittel 9 – Konklusjon**

Oppsummering av hovedfunn og 5 anbefalinger til videre forskning.

### Kvalitetssikring

- Confusion matrix-verdier korrigert (off-diagonal-verdier var fra feil modellkjøring)
- Modelleringskapittelet revidert: fjernet overlapp med kap. 3, generalisert parameterverdier, lagt til Gradient Boosting som reservemodell, gitt intuitiv forklaring av class_weight-vekting

---

## Oppdatering – 2026-04-19 (del 3)

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Planstatus per 19. april – sammenligning med Prosjektplan G05

Gjennomgang av `Prosjektplan g05.pdf` mot faktisk fremdrift. I dag er **dag 13** av 20 i planen (innlevering 27. april).

#### Ferdig – noen deler foran planen

| Kapittel / oppgave | Planlagt frist | Status |
|---|---|---|
| Teori (kap. 2) | Dag 1–4 | ✅ Ferdig |
| Metode (kap. 3) | Dag 5–6 | ✅ Ferdig |
| Innledning (kap. 1) | Dag 8–9 | ✅ Ferdig |
| Modelltrening + evaluering | Dag 8–9 | ✅ Ferdig |
| Confusion matrix + feature importance | Dag 10–11 | ✅ (ASCII-format i rapport) |
| Resultater (kap. 7) | Dag 12–13 | ✅ Ferdig |
| Diskusjon (kap. 8) | Dag 12–13 | ✅ Ferdig |
| Konklusjon (kap. 9) | Dag 15–16 | ✅ Ferdig – 2 dager tidlig |

#### Gjenstår for Birgitte

Prioritert rekkefølge mot innlevering 27. april:

**1. Kostnadsbesparelse / lønnsomhetseffekt** ← høyest prioritet
- Planlagt: Dag 10–11 (16.–17. april) – ikke gjort
- Avklar med Vera hvilke gjennomsnittsmarginer per kanal (A, B, C) som skal brukes
- Beregn estimert besparelse ved å sammenligne modellens prediksjoner mot historisk kanalvalg på testsettet
- Resultatet hører hjemme i kap. 7 (Resultat) og er delproblem 2 i forskningsspørsmålet – kan ikke utelates

**2. Casebeskrivelse (kap. 4)**
- Ikke nevnt eksplisitt i planen, men er obligatorisk kapittel i rapportmalen
- Birgitte er eneste som kjenner Modino godt nok til å skrive dette
- Innhold: hva Modino gjør, hvordan recommerce-prosessen fungerer i dag, hvilke data som finnes, hva som er problemet – koblet direkte til problemstillingen

**3. Sammendrag og abstract**
- Ikke nevnt i planen – skrives naturlig etter at alle kapitler er ferdig
- Kort (ca. 150–250 ord hver)

**4. Forside og formaliteter**
- Tittel, forfatternavn, dato, sideantall, veileder, studiepoeng, personvern/NSD-avkryssing

**5. Referanseliste (APA 7)**
- Planlagt: Dag 15–16 (21.–22. april) – Birgitte sitt ansvar per planen
- Referansene ligger allerede spredt i kapitlene – samle og formatere i APA 7

#### Gjenstår felles (Birgitte + Vera)

| Oppgave | Frist i plan |
|---|---|
| Peer-to-peer review | Dag 17–18 (23.–24. april) |
| Konvertere ASCII-figurer til ekte figurer | Dag 17–18 |
| Oppdatere innholdsfortegnelse til faktisk struktur | Dag 19 (25. april) |
| Finpuss språk og struktur | Dag 19 (25. april) |
| Siste gjennomlesning og innlevering | Dag 20 (26.–27. april) |

#### Vurdering

Med bufferdagen 20. april og uke 3 intakt er innlevering 27. april realistisk, forutsatt at:
- Kostnadsbesparelsen prioriteres mandag 20. april (krever avklaring med Vera om marginer)
- Casebeskrivelsen skrives senest tirsdag 21. april

---

## Oppdatering – 2026-04-19 (del 4)

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Datasett-gjennomgang og geografisk utvidelse

Gjennomgikk kolonnestruktur i `004 data/modino_merged.csv` (28 kolonner). Kartla at datasettet inneholder transaksjoner fra 10 land, ikke kun Norge som opprinnelig antatt.

**Landfordeling:**

| Land | Antall rader |
|---|---|
| EE – Estland | 38 839 |
| NO – Norge | 34 780 |
| FI – Finland | 8 626 |
| SE – Sverige | 7 299 |
| RO – Romania | 2 575 |
| Øvrige (GB, SI, DK, ZA, RS) | 2 979 |

Beslutning: inkluder land med ≥ 1 000 transaksjoner (EE, NO, FI, SE, RO). Filtrert datasett lagret som `004 data/modino_filtered.csv` (92 119 rader). Dataperiode: 01.02.2024 – 31.12.2025.

### Rapportoppdateringer

- **Rapport omdøpt** fra `Mal prosjekt LOG650 v2.md` til `Prosjektoppgave_LOG650_G05.md`
- **Kapittel 4 – Casebeskrivelse** skrevet inn med innhold om Modino AS (erstatter plassholdertekst): type bedrift og recommerce-marked (4.1), produktbeskrivelse med komponenter og gradering (4.2), dagens 4-stegs klassifiseringsprosess (4.3), faktorer som påvirker klassifisering (4.4), tilgjengelige data (4.5), antatt årsak til feilklassifisering (4.6)
- **Avsnitt 1.2 – Avgrensninger** oppdatert: geografisk omfang utvidet fra kun Norge til EE, NO, FI, SE, RO med begrunnelse; implikasjoner av å inkludere markeder utenfor Norden utsatt til diskusjonskapittelet

### Statusoppdatering

- ✅ Casebeskrivelse (kap. 4) – ferdig (var planlagt til senest 21. april)
- ⬜ Kostnadsbesparelse / lønnsomhetseffekt – gjenstår (høyest prioritet)
- ⬜ Diskusjon av geografisk utvidelse (kap. 9) – skrives etter gjennomlesning

### Git

- Committet og pushet til main: rapport omdøpt + kap. 4 + oppdatert avsnitt 1.2
- `004 data/` er i .gitignore – `modino_filtered.csv` er ikke versjonskontrollert

---

## Oppdatering – 2026-04-19 (del 5)

**Utarbeidet av:** Vera (med Claude Code CLI)

### Figurer og resultater flyttet til 005 report

Alle figurer og resultater lå i `004 data/` som er i `.gitignore`. Kopiert til `005 report/` og pushet:

- `confusion_matrix_baseline.png` – Decision Tree
- `confusion_matrix_rf.png` – Random Forest (default)
- `confusion_matrix_final.png` – Random Forest (optimert)
- `feature_importance.png` – Topp 10 feature importance
- `resultater.csv` – alle evalueringsmetrikker

Alle confusion matrix-verdier verifisert mot modellkjøring – stemmer.

### ML-prompt lagret

Prompten brukt til ML-analysen (`claude_code_prompt_modino.md`) kopiert fra Downloads til `005 report/` og endret "jeg/meg" til "vi/oss" (3 forekomster).

---

## Oppdatering – 2026-04-24

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### ACT-3.14 – Lønnsomhetsberegning / delproblem 2 fullført

Gjennomførte lønnsomhetsberegningen som var høyest prioritert mot innlevering 27. april. Beregningen er basert på `004 data/modino_filtered.csv` (92 119 obs.) og confusion matrix fra den optimerte Random Forest-modellen.

**Analyse-skript:** `004 data/lonnsomhet_analyse.py` (ikke versjonskontrollert – ligger i `.gitignore`-mappen)

**Gjennomsnittlig margin per lønnsomhetsklasse:**

| Klasse | Kanal | Revenue | Cost | Margin |
|---|---|---|---|---|
| A | Reparasjon + nettbutikk | 2 222 NOK | 1 738 NOK | **484 NOK** |
| B | B2B / reservedeler | 946 NOK | 749 NOK | **197 NOK** |
| C | BER / avhending | 899 NOK | 705 NOK | **195 NOK** |

Viktig funn: klasse B og C har nær identiske marginer (197 vs. 195 NOK/enhet), fordi BER-enheter i praksis selges som reservedeler eller til B2B og dermed oppnår lignende realisert verdi. Den primære lønnsomhetsforskjellen er mellom klasse A og klassene B/C – klasse A genererer 2,5× høyere margin.

**Estimert lønnsomhetseffekt (modell vs. historisk kanalvalg):**

| | Totalmargin (NOK) |
|---|---|
| Historisk kanalvalg (testsett, n = 18 820) | 6 050 080 |
| Modellens estimerte kanalvalg | 6 206 151 |
| Netto forbedring | **+156 072** |

Oppskalert til fullt volum (~47 000 enheter/år): **~390 000 NOK per år**.

Beregningen forutsetter at SAP-registrert revenue og cost reflekterer faktisk kanalutfall. Target leakage-risiko er adressert som metodisk begrensning i kap. 8.4.

### Rapportoppdateringer

- **Kap. 7 Resultat** – ny seksjon 7.7 lagt til med fire underavsnitt:
  - 7.7.1 Gjennomsnittlig margin per klasse (tabell 7.4)
  - 7.7.2 Estimeringsmetodikk
  - 7.7.3 Resultater (tabell 7.5 total, tabell 7.6 per misklassifisering)
  - 7.7.4 Oppskalert estimat (~390 000 NOK/år)
- **Kap. 9 Konklusjon** – oppdatert med eksplisitt svar på delproblem 2; punkt 3 i videre forskning endret fra "beregn kostnadsbesparelse" til "innhent faktiske kanalmarginer fra Modino"
- **Prosjektstatus_G05.md** – ACT-3.14 markert ferdig (4 av 5 punkter avhuket)

### Gjenstår i fase 3 (frist 27. april)

- ACT-3.15 Sammenstille rapportutkast (tekniske rettinger, bibliografi, sammendrag, abstract, forside)
- ACT-3.14 review og lukking

---

## Oppdatering – 2026-04-24 (del 2)

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Kvalitetssikring av kap. 7.7 – metodisk svakhet identifisert og rettet

Gjennomførte en kritisk gjennomgang av kap. 7 (Resultat) fra perspektivet til en tester og kvalitetssikrer.

**Kap. 7.1–7.6 (delproblem 1):** Godkjent. Alle tall verifisert mot confusion matrix og feature importance – ingen feil funnet.

**Kap. 7.7 (delproblem 2):** Fire problemer identifisert og rettet:

1. **Logisk svikt (alvorlig):** Beregningen forutsatte implisitt at modellen er riktig der den avviker fra historisk kanalvalg, men disse avvikene er per definisjon modellens feil mot grunnlabelen (accuracy = 92,4 %). Antakelsen er nå gjort eksplisitt i seksjon 7.7.2 med advarsel om at estimatet er en øvre grense.

2. **Misvisende tabelltekst:** Radene C→A (23 enheter) og C→B (69 enheter) i tabell 7.6 viste positive margindifferanser, men disse er modellens feilklassifiseringer av BER-enheter – ikke gevinster. Fotnoten er utvidet med forklaring.

3. **Feil terminologi:** "Konservativt estimat" i 7.7.4 erstattet med "estimat under den optimistiske antakelsen ... øvre størrelsesorden."

4. **Skrivefeil:** "Estimeringmetodikk" rettet til "Estimeringsmetodikk."

Konklusjonen (kap. 9, delproblem 2) er oppdatert tilsvarende.

Estimatet på ~390 000 NOK/år er beholdt, men presenteres nå som øvre grense betinget av en eksplisitt antakelse – ikke som et forventet faktisk utfall.

---

## Oppdatering – 2026-05-19

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Gjennomgang av ny data og prosessforståelse

Gjennomgikk ny renset data i `004 data/data may 2026/` og prosessdiagrammet `BuyBack_Process_Flow_v2.pptx` for å bygge felles forståelse av Modinos fullstendige enhetssyklus.

### Fullstendig prosessflyt dokumentert

Den komplette flyten fra mottak til utgang ble kartlagt og er nå dokumentert i `HANDOVER_CONTEXT.md`:

1. **Steg 1 – Mottak og første gradering (CellDe):** Enheter graderes A–F ved mottak. Output er `InspectedDeviceREport_cleaned.xlsx`.
2. **Steg 2 – SAP-import → Innkjøpsordre med "buy-back"-artikkelnummer:** CellDe-filen importeres til SAP og skaper en PO med buy-back-artikkelnumre (format: `nummer_variant_grad`, eks. `16854_2_0`).
3. **Steg 3 – Tre mulige utganger:**
   - **Sti 1 – Salg til tredjepartshandler** (Foxway, Bridge Nine, Renewed AB m.fl.): Selges uten renovering med buy-back-artikkelnummer.
   - **Sti 2 – Renovering → Teleoutlet (sluttkunde):** Går gjennom renovering via subcontracting PO. Buy-back-artikkelnummer endres til "2nd"-artikkelnummer (eks. `47731`). Selges via One2cel AS (Modinos bruktmarkedsbutikk, Teleoutlet) til sluttkunder.
   - **Sti 3 – Skrap/BER:** Selges som skrap til kunde `1365865` ("Modino vareuttak") med **buy-back**-artikkelnummer (ikke 2nd).

### Viktige avklaringer og korreksjoner

**Korrektur 1 – Andre gradering er kodet i artikkelbeskrivelsen:**
Bokstaven rett etter `2nd-` i `maktx`-kolonnen (eks. `2nd-C iPhone 13 128GB Midnight`) er selve andre graderingen etter renovering. Det finnes ikke et separat graderingssteg – graden er innbakt i artikkelnummerbeskrivelsen.

**Korrektur 2 – Skrap bruker buy-back-artikkelnumre:**
Skrap/BER-enheter selges med buy-back-artikkelnumre, ikke 2nd-artikkelnumre. Kun Teleoutlet-salg (sluttkunder) bruker 2nd-artikkelnumre.

**Korrektur 3 – Graderingsforbedring er mulig men ikke garantert:**
En enhet kjøpt inn som grad A trenger ingen forbedring. For slike enheter vil 2nd-graden være identisk med CellDe-inntaksgraden.

### Ny analysemulighet identifisert – Graderingsforbedring

Siden begge graderinger er tilgjengelige og kan kobles på IMEI, er det mulig å beregne **gradendringen per enhet** for alle renoverte enheter (2nd-artikkelbefolkning):

- Inntaksgrad: fra `InspectedDeviceREport_cleaned.xlsx` (CellDe-grad A–F)
- Utgangsgrad: fra `maktx` i `Z_BBTI_IMEI_TRACK_cleaned.xlsx` (bokstav etter `2nd-`)
- Koblingsnøkkel: IMEI

Foreslåtte analyser:
1. Gradendring per enhet (forbedret, uendret eller forverret?)
2. Gjennomsnittlig antall graderingstrinn forbedret
3. Korrelasjon mellom inntaksgrad og utgangsgrad – finnes det et tak på forbedring?
4. Kombinert med margindata: gir større graderingsforbedring faktisk høyere margin etter renovering?

### Oppdatert fil

`004 data/data may 2026/HANDOVER_CONTEXT.md` er oppdatert med fullstendig prosessflyt, artikkelnummerlogikk, korreksjonene over og den foreslåtte graderingsanalysen – klar til bruk for Vera i neste sesjon.

---

## Oppdatering – 2026-05-21

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Kontekst – ny BETA-rapport

Den opprinnelige rapporten (`Prosjektoppgave_LOG650_G05.md`) er basert på feil datapipeline og feil klassifiseringslogikk. En ny BETA-rapport (`Prosjektoppgave_LOG650_G05_BETA.md`) skrives fra bunnen av med ny mai-data og korrekt metodikk. Ingen av filene slås sammen – CellDe og SAP behandles som separate datakilder og kobles kun i minnet ved analyse.

### Geografisk analyse – StoreName som proxy

Undersøkte om `StoreName` i CellDe-data kan brukes som geografisk proxy (for å unngå target leakage fra `ship_country` i SAP). Resultatet bekreftet at dette ikke er mulig: de samme butikknavnene (f.eks. Telenor-butikker) leverer enheter som ender opp i både Norge og Estland. StoreName beskriver *hvor enheten ble samlet inn fra kunden*, ikke *hvor den skal*. Konklusjon: ingen geografisk proxy er tilgjengelig i CellDe. Dette er en sentral metodisk begrensning som dokumenteres i rapporten.

### Target leakage forklart og bekreftet

`ship_country` fra SAP er near-perfekt prediktor (NO → 98,5 % klasse A, andre land → ~100 % klasse B), men kan ikke brukes som feature fordi den kun eksisterer *etter* salget. Denne begrensningen ble forklart og akseptert.

### Klassifiseringslogikk bekreftet

Endelig klassifiseringslogikk (alle identifikatorer er numeriske kundenummer fra SAP):

| Klasse | Regel |
|---|---|
| C – Skrap | `kunnr == '1365865'` (sjekkes alltid først) |
| A – Sluttkunde | `matnr` er rent numerisk (2nd-artikkel) |
| B – Tredjepartshandler | `kunag` er i kjent trader-mengde |

Kjente tradere (kunag): 544127, 707086, 995702, 498232, 1533558, 1536986, 1550704, 715038, 1530444, 1530472, 1602135, 1602088

Klassifisering av totalt 93 580 SAP-rader:
- B: 58 388 (62,4 %)
- A: 34 648 (37,0 %)
- C: 539 (0,6 %)
- Uklassifisert (ekskludert): 5 rader

### Feature engineering

Utført på 93 564 rader (etter in-memory join og dropp av 11 nullrader):

| Feature | Metode |
|---|---|
| `device_value` | Norsk tallformat (`'3 954,04'`) → float |
| `grade_num` | Ordinal: A=6, B=5, C=4, D=3, E=2, F=1 |
| `model_encoded` | Alle 557 modeller beholdt; kodet med median `device_value` per modell |
| `color_group_enc` | 246 farger gruppert til 10 hovedgrupper (Black, White/Silver, Gray, Blue, Gold, Green, Purple/Violet, Red/Pink, Yellow, Other) → label encoding |
| `Transaction Type_enc` | 21 kategorier → label encoding |
| `Channel_enc` | 20 kategorier → label encoding |
| `Device Category_enc` | 3 kategorier → label encoding |
| `har_feil` | Binær (1 = InspectedFaults registrert, 0 = ikke registrert) |

### Modelltrening – Decision Tree og Random Forest

Stratifisert 80/20 train/test-split. Begge modeller trent med `class_weight='balanced'`.

**Resultater (testsett, 18 713 rader):**

| Modell | Accuracy | F1 klasse A | F1 klasse B | F1 klasse C |
|---|---|---|---|---|
| Decision Tree (baseline) | 80 % | 0.75 | 0.83 | 0.74 |
| Random Forest (primær) | 80 % | 0.75 | **0.84** | **0.75** |

Random Forest er marginalt bedre, spesielt for klasse B og C.

**Confusion matrix – Random Forest:**

| Faktisk \ Predikert | A | B | C |
|---|---|---|---|
| A (6 928) | 5 507 | 1 412 | 9 |
| B (11 677) | 2 234 | 9 424 | 19 |
| C (108) | 9 | 18 | 81 |

Forvirring mellom A og B er det største problemet (som forventet uten geografisk signal). Klasse C håndteres overraskende godt (75 % recall) til tross for kun 0,6 % av dataene.

**Feature importance (Random Forest):**

| Feature | Viktighet |
|---|---|
| device_value | 30,7 % |
| Device Category | 20,7 % |
| grade_num | 15,4 % |
| model_encoded | 14,0 % |
| color_group | 7,1 % |
| Transaction Type | 6,5 % |
| Channel | 3,5 % |
| har_feil | 2,1 % |

Enhetens verdi og kategori (smartphone vs. tablet) er de klart viktigste prediktorene. Modell og grade bidrar betydelig.

### Figurer lagret

To figurer generert og lagret i `005 report/` (pushet til main):
- `figur_konfusjonsmatriser.png` – Decision Tree og Random Forest side ved side med antall og prosent per celle
- `figur_feature_importance.png` – feature importance for Random Forest

### Kapittel 2 og 3 skrevet inn i BETA-rapporten

**Kapittel 2 (Litteratur):** Gjennomgang av empiriske bidrag med posisjonering av prosjektet. Dekker Ibrahim & Abdul-Kader (2025), Turkolmez et al. (2024), Govindan et al. (2015), Hübner et al. (2020), Ferguson et al. (2009) og Proske et al. (2018). Avslutter med å skille prosjektet fra eksisterende litteratur på tre punkter: to-kilde-arkitektur, faktisk observert salgskanal som målvariabel, og fravær av geografisk informasjon som feature.

**Kapittel 3 (Teori):** Adaptet fra den gamle rapporten med tre viktige oppdateringer:
1. 9R-figuren er oppdatert: A = Sluttkunde/Teleoutlet (R5–R6 Refurbish), B = Tredjepartshandler (R3 Reuse), C = Skrap (R8–R9 Recycle/Recover)
2. "Kostnadsforhold" fjernet fra feature engineering-seksjonen (target leakage)
3. Feature-listen oppdatert til å reflektere faktiske CellDe-features

Tre pilarer: sirkulærøkonomi og recommerce (3.1), beslutningsstøtte og verdifall (3.2), maskinlæring og klassifisering (3.3), med oppsummering (3.4).

### Git

Committet og pushet til main (`ac71860`): kapittel 2 + 3 i BETA-rapporten, `figur_konfusjonsmatriser.png` og `figur_feature_importance.png`.

### Gjenstår

- Kapittel 4 (Casebeskrivelse) – ny, basert på faktisk prosessforståelse (CellDe → SAP, tre kanaler)
- Kapittel 5 (Metode og data) – ny pipeline, to separate filer, klassifiseringslogikk
- Kapittel 6–9 (Modellering, Analyse, Resultat, Diskusjon)
- Kapittel 1 (Innledning) og 10 (Konklusjon) – skrives sist, overfladisk til å begynne med
- Bibliografi, sammendrag, abstract, forside

---

## Oppdatering – 2026-05-22

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Kapittel 4 – Casebeskrivelse skrevet inn

Nytt kapittel 4 skrevet fra bunnen av, basert på faktisk prosessforståelse fra HANDOVER_CONTEXT.md:

- 4.1 Modino AS og recommerce-markedet
- 4.2 Enheter og graderingssystem (A–F, CellDe, tabell)
- 4.3 Klassifiseringsprosessen — tre kanaler (A/B/C) med artikkelnummerlogikk og tabell
- 4.4 Datagrunnlaget — to-kilde-arkitektur med koblingsnøkkel og radtall (tabell)
- 4.5 Klassifiseringsutfordringen — geografisk konfund, target leakage forklart

### Kapittel 5 – Metode og data skrevet inn

Nytt kapittel 5 med full pipeline-beskrivelse:

- 5.1.1 Forskningsdesign (kvantitativ casestudie, Yin 2018, positivistisk)
- 5.1.2 Metodevalg (supervised learning, begrunnelse for RF over optimering)
- 5.2.1 Datakilder og innlasting med kodeeksempler
- 5.2.2 Datakvalitet og rensing (IMEI-validering, duplikatanalyse, anonymisering)
- 5.2.3 Klassifiseringslogikk steg for steg med tabell (B: 62,4 %, A: 37,0 %, C: 0,6 %)
- 5.2.4 Feature engineering — alle 8 features med transformasjoner og tabell
- 5.2.5 Stratifisert 80/20-split og begrunnelse for class_weight='balanced' vs. SMOTE

### Kapittel 6 – Modellering skrevet inn

Kompendiet (Rekdal & Pettersen, 2026, kap. 9) lest og integrert som referanse:

- 6.1 Formalisering av klassifiseringsproblemet (f: ℝ⁸ → {A,B,C})
- 6.2 Decision Tree — Gini-formel, ΔGini-formel, baseline-rolle
- 6.3 Random Forest — bagging, feature-underutvalg, majoritetsstemme-formel, feature importance-formel, class_weight-formel, hyperparametere
- 6.4 Evalueringsrammeverk — accuracy, precision, recall, F1 med formler, confusion matrix

### Sensor-gjennomgang av kap. 2–6 gjennomført

Følgende rettinger lagt inn i rapporten:

1. Skrivefeil "arbeidssminnet" → "arbeidsminnet" (kap. 5.2.1)
2. Tabellnummer lagt til graderingstabellen: Tabell 4.1. Øvrige tabeller i kap. 4 renummerert til 4.2 og 4.3
3. Korrigerte klassetall i treningssettet: A: 27 720, B: 46 711 (var 27 718, 46 710)
4. Metodisk merknad om label encoding for uordnede kategorier lagt inn i kap. 5.2.4
5. Hyperparametervalg begrunnet i kap. 6.3.3 (ingen GridSearchCV, bevisst valg)
6. Kompendiet (Rekdal & Pettersen, 2026) lagt inn i kap. 3.3.3
7. Kilde for Modinos markedsposisjon lagt inn i kap. 4.1

### Gjenstår

- Verifisere klassetall (train A/B/C) mot kjørt kode — utsatt til ML-testsesjonen
- Kapittel 7 (Analyse), 8 (Resultat), 9 (Diskusjon)
- Kjøre ML-pipeline på nytt for å verifisere confusion matrix og feature importance mot rapporten
- Kapittel 1 (Innledning) og 10 (Konklusjon) — skrives sist
- Bibliografi, sammendrag, abstract, forside
- Konvertere ASCII-figurer (3.1, 3.2) til ekte figurer

---

## Oppdatering – 2026-05-22 (del 2)

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Figurer generert og satt inn

To nye figurer generert med Python (matplotlib) fra hardkodede kjente statistikker:

- `figur_prosessflyt.png` — prosessflytdiagram fra CellDe-mottak til tre salgskanaler (kap. 4.3)
- `figur_klassefordeling.png` — horisontalt søylediagram for A/B/C-fordeling med n per klasse (kap. 5.2.3)

Eksisterende figurer referert på riktig sted i rapporten:
- `figur_feature_importance.png` referert i kap. 6.3.1 (Figur 6.1)
- `figur_konfusjonsmatriser.png` referert i kap. 8.1 (Figur 8.1)

### Kapittel 7 – Analyse skrevet inn

- 7.1 Datapreparering og målvariabel — 93 575 rader, klassefordeling og geografisk A/B-observasjon
- 7.2 Observasjoner fra feature-konstruksjonen — mønstre i device_value, grade_num, model_encoded, color_group, har_feil
- 7.3 Modelltrening — DT og RF begge 80 %; observasjon at bindende element er manglende geografisk signal, ikke modellkapasitet
- 7.4 Generaliserbarhet — OOB-score, train/test-gap, stratifisert split

### Kapittel 8 – Resultat skrevet inn

- 8.1 Modellsammenligning — tabell 8.1 (accuracy/F1) og tabell 8.2 (precision/recall RF)
- 8.2 Konfusjonsmatrise RF — tabell 8.3 med celleverdier; A/B-forveksling er dominerende feilmønster
- 8.3 Feature importance — tabell 8.4; device_value + Device Category = 51,4 %
- 8.4 Lønnsomhetseffekt (delproblem 2) — ny BETA-beregning fra BETA-konfusjonsmatrisen:
  - Historisk margin (testsettet): 5 674 581 NOK
  - Modellmargin (estimert): 5 910 493 NOK
  - Netto forbedring: +235 912 NOK på testsettet
  - Oppskalert: ~590 000 NOK/år (øvre estimat)
  - Merk: høyere enn gammel rapport (156 072 / 390 000) fordi BETA-modellen har annet prediksjonsmønster

### Gjenstår

- Kapittel 9 (Diskusjon)
- ML-pipeline-verifisering (kjøre kode mot rådata for å bekrefte alle tall)
- Kapittel 1 (Innledning) og 10 (Konklusjon) — skrives sist
- Bibliografi, sammendrag, abstract, forside
- Konvertere ASCII-figurer (3.1, 3.2) til ekte figurer
