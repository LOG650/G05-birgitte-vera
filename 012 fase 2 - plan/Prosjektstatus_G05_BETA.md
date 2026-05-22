# Status for G05 – Modino-prosjektet
**Statusdato:** 2026-05-21
**Gruppe:** G05 – Birgitte & Vera
**Fag:** LOG650

Denne statusen gjenspeiler faktisk fremdrift per 2026-05-21. Den opprinnelige rapporten (`Prosjektoppgave_LOG650_G05.md`) er forkastet pga. feil datapipeline og feil klassifiseringslogikk. En ny BETA-rapport (`Prosjektoppgave_LOG650_G05_BETA.md`) er under utarbeidelse med korrekt data og metodikk.

---

## ⚠️ Viktig kontekstendring – BETA-rapport

Den opprinnelige analysen brukte en feil tilnærming:
- Datarensingen slo feilaktig sammen CellDe og SAP til én fil
- Klassifiseringen var basert på inspeksjonsgrad (A–F), ikke faktisk salgskanal
- Revenue, cost og margin ble brukt som features (target leakage)
- Accuracy på 92,4 % var kunstig høy pga. lekkasje

**Ny tilnærming (BETA):**
- CellDe (`InspectedDeviceREport_cleaned_anon.xlsx`) og SAP (`Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx`) behandles som separate filer og kobles kun i minnet
- Klassifiseringen er basert på faktisk observert salgskanal via artikkelnummertype og kunnr
- Kun features tilgjengelig ved mottak (CellDe-data) brukes — ingen target leakage
- Ny accuracy: 80 % (Decision Tree og Random Forest er tilnærmet like)

---

## Kort status

BETA-rapporten er påbegynt. Data er analysert, klassifiseringslogikk er fastlagt, feature engineering er gjennomført og modeller er trent. Kapittel 2 (Litteratur) og kapittel 3 (Teori) er skrevet inn. Gjenstående kapitler: Casebeskrivelse (4), Metode og data (5), Modellering (6), Analyse (7), Resultat (8), Diskusjon (9). Innledning (1) og Konklusjon (10) skrives sist.

Innleveringsfrist: **2026-05-31**.

---

## BETA-fremdrift per 2026-05-21

| Aktivitet | Status | Kommentar |
|---|---|---|
| BETA-1 Ny klassifiseringslogikk fastlagt | ✅ Ferdig | kunnr + artikkelnummertype; 93 575 rader klassifisert |
| BETA-2 Geografisk analyse (StoreName-proxy) | ✅ Ferdig | Ingen geografisk proxy i CellDe — dokumentert som begrensning |
| BETA-3 Feature engineering | ✅ Ferdig | 8 features, alle fra CellDe, ingen target leakage |
| BETA-4 Modelltrening (DT + RF) | ✅ Ferdig | 80 % accuracy, F1 A=0.75, B=0.84, C=0.75 |
| BETA-5 Figurer generert | ✅ Ferdig | `figur_konfusjonsmatriser.png`, `figur_feature_importance.png` |
| BETA-6 Kap. 2 Litteratur | ✅ Ferdig | Empiriske bidrag, posisjonering av prosjektet |
| BETA-7 Kap. 3 Teori | ✅ Ferdig | 9R oppdatert, kostnadsforhold fjernet, CellDe-features |
| BETA-8 Kap. 4 Casebeskrivelse | ✅ Ferdig | Ny, basert på CellDe/SAP-prosessforståelse |
| BETA-9 Kap. 5 Metode og data | ✅ Ferdig | Ny pipeline, to separate filer |
| BETA-10 Kap. 6 Modellering | ✅ Ferdig | |
| BETA-11 Kap. 7 Analyse | ⬜ Ikke startet | |
| BETA-12 Kap. 8 Resultat | ⬜ Ikke startet | |
| BETA-13 Kap. 9 Diskusjon | ⬜ Ikke startet | Inkl. geografisk begrensning og class C-imbalanse |
| BETA-14 Kap. 1 Innledning | ⬜ Sist | Overfladisk til å begynne med |
| BETA-15 Kap. 10 Konklusjon | ⬜ Sist | Overfladisk til å begynne med |
| BETA-16 Bibliografi, sammendrag, abstract, forside | ⬜ Ikke startet | |

---

## Faktisk fremdrift per arbeidskopi

| Aktivitet | Planlagt periode | Faktisk status | Kommentar |
|---|---|---|---|
| ACT-1.1 Analysere case og databehov | 2026-01-12 til 2026-01-16 | Ferdig | Fase 1 fullført |
| ACT-1.2 Utarbeide proposal | 2026-01-16 til 2026-01-21 | Ferdig | Fase 1 fullført |
| ACT-2.1 Etablere planbaseline | 2026-02-11 til 2026-02-13 | Ferdig | Fase 2 fullført |
| ACT-3.1 Hente og rense data fra Modino | 2026-04-07 til 2026-04-11 | Ferdig 2026-04-17 | IMEI-validering, merge og duplikatanalyse |
| ACT-3.2 Feature engineering og klassemapping | 2026-04-14 til 2026-04-17 | Ferdig 2026-04-19 | 6→3-klassemapping og 11 features |
| ACT-3.3 Trene og evaluere modell | 2026-04-14 til 2026-04-17 | Ferdig 2026-04-19 | Decision Tree, Random Forest, GridSearchCV |
| ACT-3.4 Tolke resultater og lage anbefalinger | 2026-04-17 til 2026-04-19 | Ferdig 2026-04-19 | Feature importance og begrensninger dokumentert |
| ACT-3.5 Skrive kapittel 1 Innledning | 2026-04-14 til 2026-04-17 | Ferdig 2026-04-18 | Problemstilling, avgrensninger og antagelser |
| ACT-3.6 Skrive kapittel 2 Teori og litteratur | 2026-04-14 til 2026-04-17 | Ferdig 2026-04-18 | Tre pilarer med APA7-referanser |
| ACT-3.7 Skrive kapittel 3 Casebeskrivelse | 2026-04-17 til 2026-04-19 | Ferdig 2026-04-19 | Modino, recommerce-prosess, datagrunnlag |
| ACT-3.8 Skrive kapittel 4 Data og metode | 2026-04-14 til 2026-04-17 | Ferdig 2026-04-18 | Forskningsdesign, features og evalueringsrammeverk |
| ACT-3.9 Skrive kapittel 5 Modellering | 2026-04-17 til 2026-04-19 | Ferdig 2026-04-19 | Matematisk formulering og tre modelltyper |
| ACT-3.10 Skrive kapittel 6 Analyse | 2026-04-17 til 2026-04-19 | Ferdig 2026-04-19 | Klasser, features, split og trening |
| ACT-3.11 Skrive kapittel 7 Resultat | 2026-04-17 til 2026-04-19 | Ferdig 2026-04-19 | Tabeller, confusion matrix og feature importance |
| ACT-3.12 Skrive kapittel 8 Diskusjon | 2026-04-17 til 2026-04-19 | Ferdig 2026-04-19 | Funn, litteratur, Modino-implikasjoner og begrensninger |
| ACT-3.13 Skrive kapittel 9 Konklusjon | 2026-04-21 til 2026-04-22 | Ferdig 2026-04-19 | To dager foran plan |
| ACT-3.14 Beregne kostnadsbesparelse | 2026-04-19 til 2026-04-21 | Ikke startet | Høyest prioritet – krever avklaring av marginer per kanal |
| ACT-3.15 Sammenstille rapportutkast | 2026-04-21 til 2026-04-27 | Pågår | Tekniske rettinger gjenstår. Knyttet til MS-006 |
| ACT-4.1 Gjennomføre peer review og revisjon | 2026-04-27 til 2026-04-29 | Ikke startet | Avhenger av ACT-3.15 |
| ACT-4.2 Ferdigstille rapport og presentasjon | 2026-04-29 til 2026-05-31 | Ikke startet | Sluttfasen |

---

## Avhukingsliste for aktiviteter

### Fullført

**ACT-1.1 Analysere case og databehov**
- [x] Gjennomgå casebeskrivelsen (Modino AS og recommerce-prosessen)
- [x] Avklare problemstilling i proposal
- [x] Identifisere beslutningsbehov (kanalisering A/B/C)
- [x] Avklare forventet datagrunnlag (SAP-system)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-1.2 Utarbeide proposal**
- [x] Beskrive problem og bakgrunn
- [x] Definere mål og avgrensninger
- [x] Begrunne metodevalg (prediktiv klassifisering) på overordnet nivå
- [x] Levere proposal til fasegodkjenning
- [x] Gjennomføre review og lukke aktiviteten

**ACT-2.1 Etablere planbaseline**
- [x] Etablere prosjektplan (Prosjektstyringsplan_G05.md)
- [x] Ferdigstille fremdriftsplan (Prosjekt_GANTT_G05.mpp)
- [x] Etablere WBS, milepæler og risikoregister
- [x] Justere fra optimaliseringsmodell til prediktiv klassifisering (V2)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.1 Hente og rense data fra Modino**
- [x] Laste ned og inspisere rådata (InspectedDeviceReport.xlsx og SAP-filer)
- [x] IMEI-validering (15-sifret lengde + Luhn-algoritme)
- [x] Standardisere gradering og Transaction Type på tvers av 2024 og 2025
- [x] Merge Excel og SAP-data på IMEI-nøkkel (left join)
- [x] Dokumentere merge-statistikk (90,8 % SAP-match i 2024, 89,8 % i 2025)
- [x] Gjennomføre duplikatanalyse (Type A, B og C identifisert)
- [x] Kartlegge geografisk fordeling (10 land; 5 inkludert med ≥ 1 000 transaksjoner)
- [x] Lagre filtrert datasett som modino_filtered.csv (92 119 rader)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.2 Feature engineering og klassemapping**
- [x] Mappe 6 inspeksjonsgradene (A–F) til 3 lønnsomhetsklasser (A+B→A, C→B, D–F→C)
- [x] Konvertere norske tallformat (cost, vat, Inspected Device Value) til float
- [x] Lage avledede variabler: kostnadsforhold, margin, revenue_cost_ratio, gjennomløpstid
- [x] Anvende target encoding for Transaction Type, brand og Inspection Color
- [x] Skalere features med StandardScaler
- [x] Dokumentere 11 features (8 numeriske + 3 target-enkodede kategoriske)

**ACT-3.3 Trene og evaluere modell**
- [x] Dele data i treningssett (80 %) og testsett (20 %)
- [x] Trene Decision Tree (baseline) – accuracy 88,8 %
- [x] Trene Random Forest (default) – accuracy 92,2 %
- [x] Optimere Random Forest med GridSearchCV (5-fold CV) – accuracy 92,4 %
- [x] Bekrefte at 80 %-kravet er oppfylt (92,4 % > 80 %)
- [x] Verifisere Recall klasse C (0,967)
- [x] Generere confusion matrix for alle tre modeller
- [x] Beregne feature importance (topp 10)
- [x] Lagre trent modell (modino_rf_model.pkl) og LabelEncoder (label_encoder.pkl)
- [x] Lagre evalueringsmetrikker i resultater.csv
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.4 Tolke resultater og lage anbefalinger**
- [x] Identifisere topp 3 prediktorer (Inspected Device Value, kostnadsforhold, Device Category)
- [x] Dokumentere overraskende funn (brand har lav forklaringskraft)
- [x] Identifisere target leakage-risiko (revenue, cost, margin er post-beslutningsvariabler)
- [x] Flagge grade-til-klasse-mappingen for validering med Modino
- [x] Formulere 5 anbefalinger til videre forskning i kap. 9

**ACT-3.5 Skrive kapittel 1 Innledning**
- [x] Skrive innledning fra sirkulærøkonomi til Modinos spesifikke problem
- [x] Fylle inn 1.1 Problemstilling (primær + to delproblemer)
- [x] Skrive 1.2 Avgrensninger (geografisk, tidsperiode, produktkategori, beslutningsomfang)
- [x] Skrive 1.3 Antagelser (historiske utfall, stabile markedsforhold)
- [x] Oppdatere geografisk avgrensning etter faktisk datasettgjennomgang (EE/NO/FI/SE/RO)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.6 Skrive kapittel 2 Teori og litteratur**
- [x] Pilar 1: Sirkulærøkonomi og recommerce (Stahel, Geissdoerfer, Potting 9R, Proske)
- [x] Pilar 2: Beslutningsstøtte og verdifall i reverse logistics (Ferguson, Guide & Van Wassenhove, Teunter & Flapper, Govindan)
- [x] Pilar 3: Maskinlæring og klassifisering (Ibrahim & Abdul-Kader, Turkolmez, Breiman)
- [x] Oppsummering og kobling til problemstilling (figur 2.2)
- [x] Koble 9R-rammeverket til Modinos lønnsomhetsklasser A/B/C (figur 2.1)
- [x] Verifisere at alle referanser er i APA7-format
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.7 Skrive kapittel 3 Casebeskrivelse**
- [x] Beskrive Modino AS og recommerce-markedet (3.1)
- [x] Beskrive produkter og graderingssystem (3.2)
- [x] Beskrive dagens 4-stegs klassifiseringsprosess (3.3)
- [x] Beskrive faktorer som påvirker klassifisering (3.4)
- [x] Beskrive tilgjengelige data (3.5)
- [x] Beskrive antatt årsak til feilklassifisering (3.6)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.8 Skrive kapittel 4 Data og metode**
- [x] Beskrive forskningsdesign (4.1)
- [x] Beskrive datagrunnlag og kildefilene fra Modino SAP (4.2)
- [x] Beskrive datarensing og feature engineering (4.3)
- [x] Beskrive analysemetode og modellvalg (4.4)
- [x] Beskrive evalueringsrammeverk (accuracy, precision, recall per klasse) (4.5)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.9 Skrive kapittel 5 Modellering**
- [x] Formulere klassifiseringsproblemet matematisk (feature-vektor → klasse)
- [x] Beskrive Decision Tree med Gini-indeks (baseline)
- [x] Beskrive Random Forest med majoritetsstemme og class_weight-vekting
- [x] Beskrive feature importance via Gini-reduksjon
- [x] Beskrive Gradient Boosting som reservemodell
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.10 Skrive kapittel 6 Analyse**
- [x] Beskrive datagrunnlag og klassefordeling (94 096 obs., 6→3-mapping)
- [x] Dokumentere feature engineering (11 features med target encoding)
- [x] Dokumentere train/test-split (80/20)
- [x] Dokumentere modelltrening (Decision Tree, RF default, RF optimert)
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.11 Skrive kapittel 7 Resultat**
- [x] Presentere modellsammenligning (tabell med accuracy/precision/recall/F1 per klasse)
- [x] Dokumentere beste hyperparametere fra GridSearchCV
- [x] Presentere confusion matrix for beste modell
- [x] Dokumentere håndtering av klasseimbalanse (class_weight: balanced)
- [x] Presentere feature importance (topp 10)
- [x] Bekrefte at 80 %-kravet er oppfylt
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.12 Skrive kapittel 8 Diskusjon**
- [x] Drøfte funn opp mot problemstilling
- [x] Sammenligne med litteraturen (Ibrahim & Abdul-Kader, Ferguson, Turkolmez)
- [x] Drøfte forretningsmessig betydning for Modino
- [x] Drøfte metodiske begrensninger (target leakage, grade-mapping, validitet)
- [x] Drøfte geografisk utvidelse fra Norge til 5 land
- [x] Gjennomføre review og lukke aktiviteten

**ACT-3.13 Skrive kapittel 9 Konklusjon**
- [x] Svare direkte på primær problemstilling
- [x] Svare på delproblem 1 (klassifiseringsnøyaktighet – 92,4 %)
- [x] Løfte frem viktigste funn og implikasjoner
- [x] Formulere 5 anbefalinger til videre forskning
- [x] Gjennomføre review og lukke aktiviteten

---

### Neste aktiviteter

**ACT-3.14 Beregne kostnadsbesparelse / lønnsomhetseffekt**
- [x] Avklare gjennomsnittsmarginer per kanal (A, B, C) – beregnet fra SAP-data (A: 484 NOK, B: 197 NOK, C: 195 NOK)
- [x] Beregne estimert lønnsomhetseffekt ved å sammenligne modellprediksjoner mot historisk kanalvalg på testsettet (+156 072 NOK / ~390 000 NOK per år)
- [x] Integrere beregningen i kap. 7 Resultat (ny seksjon 7.7, fire underavsnitt)
- [x] Oppdatere kap. 9 Konklusjon med endelig lønnsomhetskonklusjon (delproblem 2 besvart)
- [ ] Gjennomføre review og lukke aktiviteten

**ACT-3.15 Sammenstille rapportutkast**
- [ ] Rette kryssreferanser med feil avsnittnummer (3.5 → 4.5, 3.4.4 → 4.4.4, 3.4.2 → 4.4.2)
- [ ] Rette tabell- og figurnavn i kap. 4 (Tabell 3.1–3.4 → 4.1–4.4, FIGUR 3.1–3.2 → 4.1–4.2)
- [ ] Rette faktafeil i avsnitt 4.1.3 (geografisk avgrensning er utvidet til 5 land, ikke kun Norge)
- [ ] Rette faktafeil i avsnitt 4.2.2 (datasett: 94 096 observasjoner, ikke 10 000–15 000)
- [ ] Konvertere ASCII-figurer til ekte figurer (figur 2.1, 2.2, 4.1, 4.2, 7.1, 7.2)
- [ ] Ferdigstille Bibliografi (samle alle "Verifiserte kilder:" i APA7, fjern duplikater)
- [ ] Skrive sammendrag (norsk, ca. 150–250 ord)
- [ ] Skrive abstract (engelsk, ca. 150–250 ord)
- [ ] Fylle ut forside (tittel, forfatternavn, dato, studiepoeng, veileder)
- [ ] Oppdatere innholdsfortegnelse til faktisk kapittelnummerering og -titler
- [ ] Avgjøre innhold i Vedlegg (kode, tabeller, figurer i full størrelse)
- [ ] Intern kvalitetssjekk av hele utkastet
- [ ] Gjennomføre review og lukke aktiviteten

**ACT-4.1 Gjennomføre peer review og revisjon**
- [ ] Innhente tilbakemeldinger fra peer review (planlagt 2026-04-27 til 2026-04-29)
- [ ] Oppsummere funn og forbedringspunkter
- [ ] Revidere analyse, tekst og presentasjon av resultater
- [ ] Lukke avvik før sluttføring
- [ ] Gjennomføre review og lukke aktiviteten

**ACT-4.2 Ferdigstille rapport og presentasjon**
- [ ] Ferdigstille konklusjon – besvar problemstillingen eksplisitt
- [ ] Ferdigstille innledning (skrives til slutt etter alle kapitler er låst)
- [ ] Kvalitetssikring, korrektur og ferdigstilling av referanseliste
- [ ] Ferdigstille presentasjonsmateriell
- [ ] Klargjøre endelig innlevering og muntlig presentasjon (frist 2026-05-31)
- [ ] Gjennomføre review og lukke aktiviteten

---

## Analyseartefakter

| Aktivitet | Skript | Figurer | Resultatfiler | Vurdering |
|---|---|---|---|---|
| ACT-3.1 Hente og rense data | 1 (clean_data.py) | 0 | 2 (cleansed_baseline.xlsx, duplikat_analyse.md) | Fullført |
| ACT-3.2 Feature engineering | 1 | 0 | 1 (modino_filtered.csv) | Fullført; mapping avventer validering med Modino |
| ACT-3.3 Trene og evaluere modell | 1 | 4 (3× confusion matrix + feature importance) | 3 (modino_rf_model.pkl, label_encoder.pkl, resultater.csv) | Fullført med dokumenterte artefakter |
| ACT-3.4 Tolke resultater | 0 | 0 | 0 | Dokumentert som analyse i kap. 8 |

---

## Rapportstatus – BETA-rapport

| Kapittel | Status | Kommentar |
|---|---|---|
| 1 Innledning | ⬜ Placeholder | Skrives sist |
| 2 Litteratur | ✅ Ferdig | Empiriske bidrag, posisjonering av prosjektet |
| 3 Teori | ✅ Ferdig | 9R oppdatert, CellDe-features, ingen target leakage |
| 4 Casebeskrivelse | ✅ Ferdig | Ny — CellDe/SAP to-kilde-arkitektur, tre kanaler |
| 5 Metode og data | ✅ Ferdig | Ny pipeline — ingen sammenslåing av filer |
| 6 Modellering | ✅ Ferdig | |
| 7 Analyse | ⬜ Ikke startet | |
| 8 Resultat | ⬜ Ikke startet | Inkl. figurer fra `005 report/` |
| 9 Diskusjon | ⬜ Ikke startet | Inkl. geografisk begrensning og class C-imbalanse |
| 10 Konklusjon | ⬜ Placeholder | Skrives sist |
| Bibliografi | ⬜ Ikke startet | Referanser ligger i kap. 2 og 3 |
| Vedlegg | ⬜ Ikke startet | |
| Sammendrag | ⬜ Ikke startet | Skrives etter alle kapitler |
| Abstract | ⬜ Ikke startet | Skrives etter sammendrag |
| Forside | ⬜ Ikke startet | Tittel, forfatternavn, dato, veileder, studiepoeng |

---

## Milepæler

| Milepæl | Baseline | Arbeidskopi-status | Vurdering |
|---|---|---|---|
| MS-001 Case og problemstilling avklart | 2026-01-16 | Oppnådd | Problemstilling fastsatt i proposal og rapport kap. 1.1 |
| MS-002 Godkjent proposal | 2026-01-21 | Oppnådd | Ingen avvik |
| MS-003 Godkjent prosjektplan | 2026-02-13 | Oppnådd | Ingen avvik |
| MS-004 Data fra Modino SAP ferdigstilt | 2026-04-11 | Oppnådd 2026-04-17 | Seks dager sent; hentet inn før modelltrening |
| MS-005 Prediktiv modell trent og evaluert | 2026-04-17 | Oppnådd 2026-04-19 | 92,4 % accuracy – 80 %-kravet oppfylt |
| MS-006 Godkjent rapportutkast klart for review | 2026-04-27 | Planlagt | Avhenger av ACT-3.14 og ACT-3.15 |
| MS-007 Peer review gjennomført | 2026-04-29 | Planlagt | Ingen endring |
| MS-008 Endelig innlevering og presentasjon | 2026-05-31 | Planlagt | Fase 4-frist |

---

## Avvik mellom arbeidskopi og styringsgrunnlag

- MS-004 er oppnådd 2026-04-17, seks dager etter baseline 2026-04-11. Forsinkelsen skyldes større datamengde og kompleksitet enn antatt (SAP-merge, duplikatanalyse, geografisk kartlegging). Forsinkelsen er ikke videreført til kritisk sti.
- ACT-3.14 Kostnadsbesparelse er ikke gjennomført innen planlagt periode. Høyest prioritet nå – krever avklaring av marginer per kanal med Vera.

---

## Viktigste risikoer – BETA

**Geografisk begrensning (ingen proxy tilgjengelig).** `ship_country` fra SAP er near-perfekt prediktor for A vs. B, men er target leakage. CellDe har ingen geografisk proxy — dette er en reell metodisk begrensning som gir A/B-forvirring i modellen. Dokumenteres eksplisitt i diskusjonskapittelet.

**Class C ekstrem imbalanse.** Klasse C (skrap) utgjør kun 0,6 % av datasettet (539 obs.). `class_weight='balanced'` brukes som tiltak. Recall på 75 % er akseptabelt, men begrensningen dokumenteres.

**Modellnøyaktighet lavere enn gammel rapport.** 80 % accuracy (ny BETA) vs. 92,4 % (gammel rapport). Forskjellen skyldes at target leakage er fjernet. 80 % er realistisk og ærlig — og fortsatt over 80 %-kravet.

**Tid.** Innlevering 2026-05-31. Ni dager gjenstår. Fem kapitler gjenstår (7–9 + 1 + 10). Realistisk men stramt.

**Label encoding for uordnede kategorier.** `Transaction Type`, `Channel` og `Device Category` er label-kodet. For trebaserte metoder er dette akseptabelt i praksis, men begrensningen er dokumentert i kap. 5.2.4 og skal diskuteres i kap. 9.

**Klassetall i treningssettet uverifisert mot kjørt kode.** Korrigert til A: 27 720, B: 46 711, C: 431 basert på aritmetikk. Bør verifiseres når ML-pipeline kjøres.

---

## Vurdering – per 2026-05-22

Kapittel 4 (Casebeskrivelse), 5 (Metode og data) og 6 (Modellering) er skrevet inn i BETA-rapporten. Sensor-gjennomgang av kap. 2–6 er gjennomført og syv rettinger er lagt inn (tabellnumre, skrivefeil, klassetall, label encoding-merknad, hyperparametervalg, kompendiereferanse, Modino-kilde). Kompendiet (Rekdal & Pettersen, 2026) er lest og integrert. Gjenstående arbeid: kap. 7 (Analyse), 8 (Resultat), 9 (Diskusjon), deretter ML-pipeline-verifisering, og til slutt kap. 1, 10, bibliografi, sammendrag og forside.
