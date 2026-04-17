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
