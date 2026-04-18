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

## Oppdatering – 2026-04-18 (session 2)

**Utarbeidet av:** Birgitte (med Claude Code CLI)

### Dataeksplorasjon – Modino data

Leste og analyserte alle 6 filer i `004 data/Modino data/`:

| Fil | Innhold | Rader |
|-----|---------|-------|
| `InspectedDeviceREport.xlsx` | Inspeksjonsdata (ark: 2024, 2025) | 104 038 |
| `Z_BBTI_IMEI_TRACK_2024_01.txt` | SAP-salgsdata | 18 500 |
| `Z_BBTI_IMEI_TRACK_2024_02.txt` | SAP-salgsdata | 23 308 |
| `Z_BBTI_IMEI_TRACK_2025_01.txt` | SAP-salgsdata | 23 139 |
| `Z_BBTI_IMEI_TRACK_2025_02.txt` | SAP-salgsdata | 22 544 |
| `Z_BBTI_IMEI_TRACK_2025_03.txt` | SAP-salgsdata | 7 090 |

**Korrelasjonsanalyse:** IMEI er join-nøkkelen mellom de to datasettene. ~100 % av SAP-IMEI-ene finnes i xlsx. xlsx = enheter inn (inspeksjon ved innbytte), SAP = enheter ut (salg). Datasettet representerer hele livssyklusen til én enhet.

### TeleOutlet-graderingssystem

Kartlagt graderingssystemet på teleoutlet.no:

| Grad | Batteri | Tilstand |
|------|---------|----------|
| Premium | 100 % | Ny i original emballasje |
| A | >90 % | Ser ut som ny, ingen synlige riper |
| B | >85 % | Minimal slitasje på skjerm/bakdeksel |
| C | >80 % | Kosmetisk slitasje, påvirker ikke bruk |
| D | >80 % | Synlige riper og bulker, kun utseende |

Mapping til prosjektets datalag: inspeksjonsgrad A–F (xlsx) → SAP-produktkode 2nd-A/B/C → TeleOutlet-salgsgrad Premium/A/B/C/D. Inspeksjonsgrad E og F har ingen tilsvarende TeleOutlet-grad og representerer BER/reservedeler.

**BER-funn:** Modino mottar enheter som er BER. Grade E og F utgjør ~10 % av innkommende enheter. Disse selges til reservedelskjøpere (bl.a. Foxway OÜ i Estland og Concord Service Center i Romania) til delpriser (€10–30), ikke til TeleOutlet-nettbutikken.

### Personopplysninger og anonymisering

Kartlagt hvilke kolonner som inneholder personopplysninger:

- **Slettet fra xlsx:** `EmailID`, `SerialNumber`, `Asset ID`, `Box ID`, `Transaction ID`, `Evidence`, alle `Repaired/Replaced*`-kolonner, `IncidentDate`, `Deductible`, `DamageReasonList`, `DamageReason`
- **Slettet fra SAP:** `ship_name`, `ship_street`, `ship_post`, `bill_name`, `bill_street`, `bill_city`, `bill_post`, `bill_country`
- **IMEI:** Erstattet med anonymt løpende `device_id` etter join
- **Butikknavn:** Beholdes foreløpig i klartekst – avklares med Modino om de skal anonymiseres

### Sammenslåing til én CSV-fil

Alle 6 kildefiler merget til `004 data/modino_merged.csv` via følgende steg:

1. Lastet xlsx (begge ark) og stablet vertikalt
2. Lastet og stablet alle 5 SAP txt-filer
3. Renset SAP: fjernet nettbrett (iPad/Tab), beholdt kun vbtyp 5 og M, fjernet personopplysninger
4. Slått sammen `turn` (B2B) og `turn_iv01` (retail) til én `revenue`-kolonne
5. Left join fra SAP til xlsx på IMEI → 100 % match
6. Erstattet IMEI med `device_id`
7. Fylt `InspectedFaults`-null med `"Ingen feil"` og `QuotedFaults`-null med `"Ingen"`
8. Fjernet 15 rader med logisk inkonsistente datoer (inspeksjonsdato > salgsdato + 1 år)

**Resultat:** `modino_merged.csv` – 94 098 rader, 29 kolonner, 33,6 MB

| Kolonne | Kilde | Beskrivelse |
|---------|-------|-------------|
| `device_id` | Generert | Anonym enhets-ID |
| `matnr` / `maktx` | SAP | Produktkode og -beskrivelse (inneholder salgskategori 2nd-A/B/C) |
| `erdat` / `fkdat` | SAP | Opprettelses- og faktureringsdato |
| `prctr` | SAP | Profit center (60121=Norge) |
| `revenue` / `revenue_waers` | SAP | Omsetning (kombinert turn + turn_iv01) |
| `vat` / `cost` | SAP | MVA og kostpris |
| `vbtyp` | SAP | Transaksjonstype: 5=retail, M=B2B |
| `kunnr` / `name1` | SAP | Kundebedrift |
| `ship_city` / `ship_country` | SAP | Leveringsby og -land |
| `Transaction Type` / `Channel` | xlsx | Innbyttetype og -kanal |
| `Device Model` | xlsx | Modellnavn fra inspeksjon |
| `Grade` | xlsx | **Inspeksjonsgrad A–F** (nøkkelvariabel/feature) |
| `Inspected Device Value` | xlsx | Estimert verdi ved innbytte |
| `Inspected Date` | xlsx | Inspeksjonsdato |
| `StoreName` / `DealerId` | xlsx | Butikknavn og forhandler-ID |
| `InspectedFaults` / `QuotedFaults` | xlsx | Feil funnet / oppgitt av kunde |

### Viktige observasjoner for fase 3

- **Datoperiode:** Filen inneholder data fra 2022–2026. Prosjektscopet er 2024–2025 – filtrer på `erdat` ved ML-trening.
- **Estland (EE):** 38 845 enheter sendt til Foxway OÜ (stor europeisk recommerce-aktør) – alle B2B. Disse representerer trolig Klasse B i modellen.
- **602 duplikate enheter:** Samme IMEI registrert fra to ulike kanaler i xlsx (832 ekstra rader). Avklar hvilken inspeksjonsrad som skal beholdes før modelltrening.
- **Nullverdier som gjenstår:** `Inspection Color` (2 569), `DealerId` (2 571), `Transaction Type` (1 194), `Device Category` (976) – alle under 3 %, håndteres i fase 3.
- **`Inspected Device Value = 0`:** 931 rader, hvorav 915 er Grade F. Korrekt – BER-enheter har ingen innbytteverdi.
