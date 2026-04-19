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
