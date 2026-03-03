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
- [ ] Partnergodkjenning av V2 før den eventuelt erstatter originalfilen
