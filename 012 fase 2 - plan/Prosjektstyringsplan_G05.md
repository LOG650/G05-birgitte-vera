# Prosjektstyringsplan for G05 – Birgitte & Vera
**Dato:** 2026-02-27
**Utarbeidet av:** Birgitte & Vera
**Autorisert av:** Faglærer

---

## Innhold

1. Sammendrag
2. Behov
3. Omfang
   - 3.1 Mål
   - 3.2 Krav
   - 3.3 Løsning
   - 3.4 Arbeidsnedbrytningsstruktur (WBS)
4. Fremdrift
   - 4.1 Gantt-plan
   - 4.2 Kritisk sti
   - 4.3 Milepæler
5. Risiko
6. Ressurser
   - 6.1 Prosjektteam og roller
   - 6.2 Ansvarsfordeling
   - 6.3 Verktøy
7. Kommunikasjon
8. Kvalitet

---

## 1. Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for G05 sitt forskningsprosjekt i samarbeid med Modino AS. Planen dokumenterer omfang, fremdrift og risiko, og gir støtte til gjennomføringen av prosjektet.

Recommerce-markedet for brukte mobilenheter har vokst betydelig de siste årene, særlig som følge av økt fokus på bærekraft og sirkulærøkonomi. Brukte mobilenheter faller raskt i verdi, og beslutninger om hvorvidt en enhet skal repareres, selges direkte eller avhendes må tas raskt og på et godt informasjonsgrunnlag. Feil prioriteringer kan føre til økt kapitalbinding og redusert lønnsomhet.

Prosjektet benytter prediktiv modellering (klassifisering) som hovedmetode, med følgende røde tråd:

**Data → Prediksjon → Prioritering → Økt lønnsomhet**

**Hvordan kan en AI-basert klassifiseringsmodell predikere lønnsomhetsklasse for brukte mobilenheter, og dermed støtte smartere prioritering av testing og reparasjon i Modinos recommerce-prosess?**

Modellen klassifiserer innkommende enheter i én av tre lønnsomhetsklasser:
- **Klasse A:** Lønnsom å reparere og selge i nettbutikk
- **Klasse B:** Direkte til B2B/reservedeler
- **Klasse C:** BER – avhend

Klassifiseringen kobler prediksjon direkte til kanalvalg og lønnsomhet, og gir et konkret grunnlag for prioritering av tekniker- og testressurser.

Den konkrete definisjonen av *økt lønnsomhet* fastsettes etter mottak av Modinos data, slik at målsettingen forankres direkte i bedriftens egne tall og forutsetninger.

---

## 2. Behov

Modino AS er en nordisk distributør av mobilenheter og forbrukerelektronikk. Selskapet kjøper, renoverer og videreselger brukte mobilenheter gjennom sin nettbutikk, og driver dermed overgangen mot en sirkulærøkonomi. Håndteringen av brukte enheter innebærer imidlertid flere logistiske og økonomiske utfordringer, knyttet til lagerstyring, verdifall og prioritering av reparasjoner.

Prosjektet svarer på behovet for en mer datadrevet og kostnadsoptimalisert beslutningsprosess i Modinos recommerce-prosess. Ved å benytte prediktiv modellering og AI-basert prioritering ønsker vi å redusere kapitalbinding, verdifall og unødvendige reparasjonskostnader.

---

## 3. Omfang

### 3.1 Mål

Målet for dette prosjektet er å utvikle og evaluere en AI-basert klassifiseringsmodell som predikerer lønnsomhetsklasse (A, B eller C) for brukte mobilenheter hos Modino AS. Modellens prediksjoner brukes som grunnlag for å prioritere testing og reparasjon, med mål om å redusere unødvendige reparasjonskostnader og øke netto dekningsbidrag.

Prosjektets forutsetninger:
- Data mottatt fra Modino AS inneholder informasjon om hvilke enheter som er reparert og solgt, og hvilke som er avhendet eller kanalisert til B2B.
- Vi har tilgang på menneskelige ressurser som kan avklare spørsmål underveis.
- Gruppen har tilstrekkelig kompetanse til å benytte AI og Python for kvantitativ analyse og modellering.

Prosjektets begrensninger:
- Geografisk avgrenset til Norge.
- Tidsperiode begrenset til 2024–2025.
- Prosjektet bygger en klassifiseringsmodell for beslutningsstøtte – ikke en full optimaliseringsmodell. Ressursallokering og kapasitetsplanlegging ligger utenfor omfanget.

### 3.2 Krav

Krav for at prosjektet skal anses som vellykket:

- Modellen skal klassifisere brukte mobilenheter i lønnsomhetsklasse A, B eller C, basert på variabler som inkluderer enhetsattributter (merke, modell, alder, tilstand) og reparasjonskostnader (arbeidstimer og deler). Klassifiseringen skal gi grunnlag for prioritering av testing og reparasjon.
- Datainnsamling og analyse gjennomføres korrekt og etterprøvbart.
- Verktøyene Claude Code CLI, Python og Excel benyttes strukturert og konsistent.
- Resultater dokumenteres transparent med tydelige forutsetninger og avgrensninger.
- Problemstillingen er operasjonaliserbar, og det er klar sammenheng mellom resultater og konklusjoner.
- Modellen skal oppnå en nøyaktighet på minimum 80 %. Øvrige ytelseskrav fastsettes etter gjennomgang av datagrunnlaget i fase 3.

### 3.3 Løsning

Løsningen som skal utvikles for å oppfylle prosjektmålet er en AI-basert klassifiseringsmodell som predikerer lønnsomhetsklasse for brukte mobilenheter i Modinos recommerce-prosess. Modellen følger en klar rød tråd: Data → Prediksjon → Prioritering → Økt lønnsomhet.

Løsningen bygger på historiske transaksjons- og enhetsnivådata fra Modinos interne SAP-system for perioden 2024–2025, og består av følgende hoveddeler:

**Datagrunnlag og feature engineering:** Strukturering og klargjøring av enhetsattributter (merke, modell, alder, tilstand) og reparasjonskostnader som grunnlag for modelltrening. Historiske utfall brukes til å merke enheter med lønnsomhetsklasse A, B eller C.

**Prediktiv modell:** En supervised learning klassifiseringsmodell som predikerer lønnsomhetsklasse (A: lønnsom å reparere og selge i nettbutikk, B: direkte til B2B/reservedeler, C: BER – avhend). Valg av algoritme avgjøres etter gjennomgang av datagrunnlaget.

**Prioriteringslogikk:** Modellens klasseprediksjoner brukes direkte til å bestemme kanalvalg for hver enhet og rekkefølge for testing og reparasjon. Enheter med høy sannsynlighet for klasse C prioriteres ut av reparasjonskøen tidlig.

**Evalueringsrammeverk:** Modellen evalueres med klassifiseringsmetrikker (accuracy, precision og recall per klasse) og estimert kostnadsbesparelse sammenlignet med dagens praksis.

Den kvantitative analysen gjennomføres ved hjelp av Claude Code CLI, med gruppen som faglige overstyrer og kvalitetssikrere. Gruppen er ansvarlige for å formulere presise instruksjoner, vurdere output og omsette funnene til meningsfulle konklusjoner knyttet til problemstillingen.

### 3.4 Arbeidsnedbrytningsstruktur (WBS)

**Fase 1 – Initiering:**
Definisjon av problemstilling knyttet til sirkulærøkonomi og recommerce hos Modino, og identifisering av enhets- og kostnadsvariabler som grunnlag for klassifiseringsmodellen.
*Leveranse: Godkjent problemstilling*

**Fase 2 – Planlegging:**
Utarbeidelse av prosjektplan, Gantt-diagram og kravspesifikasjon for den prediktive modellen. Klargjøring av forskningsdesign, identifisering av relevante datakilder fra Modino og innhenting av litterære kilder om KI-basert lagerstyring og reparasjonsressursallokering.
*Leveranse: Godkjent prosjektplan og Gantt-diagram*

**Fase 3 – Gjennomføring:**
Iverksetting av prosjektplanen. Innhenting av operasjonelle data fra Modino, analyser av BER-klassifisering og bruk av Claude Code CLI for å predikere lønnsomhet og kanalisering. Løpende dokumentasjon av prosess og resultater, samt arbeid med struktur og innhold i forskningsrapporten.
*Leveranse: Godkjent hovedutkast til forskningsrapport*

**Fase 4 – Avslutning:**
Kvalitetssikring og ferdigstillelse av forskningsrapporten, samt forberedelse og gjennomføring av muntlig presentasjon. Presentasjonen vil belyse hvordan AI-basert prioritering av lagerstyring og tekniske ressurser kan redusere totalkostnader og øke netto lønnsomhet i livssyklusstyringen av mobilenheter.
*Leveranse: Endelig forskningsrapport og muntlig presentasjon*

---

## 4. Fremdrift

### 4.1 Gantt-plan

Gantt-diagrammet er utarbeidet i MS Project og dokumenterer prosjektets oppgaver, tidsplan og avhengigheter. Se egen MS Project-fil for detaljer.

### 4.2 Kritisk sti

Den kritiske stien identifiseres i MS Project og viser hvilke oppgaver som må fullføres i tide for å unngå forsinkelser. Dette gir teamet oversikt over prioriteringer og hjelper til med å håndtere risiko knyttet til tidsbruk.

### 4.3 Milepæler

| Milepæl | Beskrivelse | Fase |
|--------|-------------|------|
| M1 | Godkjent problemstilling | Fase 1 |
| M2 | Godkjent prosjektplan og Gantt-diagram | Fase 2 |
| M3 | Datauttrekk fra Modino SAP ferdigstilt | Fase 3 |
| M4 | Prediktiv modell trent og evaluert | Fase 3 |
| M5 | Godkjent hovedutkast til forskningsrapport | Fase 3 |
| M6 | Endelig forskningsrapport og muntlig presentasjon | Fase 4 |

---

## 5. Risiko

### Risikoregister

**Risiko 1: Ufullstendig eller lite strukturert datagrunnlag**
Prosjektet er avhengig av tilgang til relevante og tilstrekkelig detaljerte data fra Modino. En sentral risiko er at datagrunnlaget enten er ufullstendig, lite strukturert eller mangler variabler som er nødvendige for modellering. Dette kan påvirke både analysens presisjon og modellens forklaringskraft.

*Tiltak:* Tidlig avklaring av hvilke data som faktisk er tilgjengelige, samt systematisk gjennomgang av datastrukturen. Eventuelle antakelser og avgrensninger dokumenteres tydelig. Dersom datagrunnlaget er mer begrenset enn forventet, tilpasses modellens kompleksitet og forenklede scenarier eller simulering benyttes.

**Risiko 2: For omfattende modell i forhold til tidsrammen**
Det er risiko for at modellen blir for kompleks i forhold til prosjektets tidsramme.

*Tiltak:* Tydelig avgrensning av problemstillingen og prioritering av variablene med størst økonomisk betydning. Vi arbeider trinnvis ved å etablere en grunnmodell som dekker kjernebeslutningene, og videreutvikler den dersom tiden tillater.

**Risiko 3: Fremdrift og koordinering i gruppen**
Generell risiko knyttet til intern koordinering og fremdrift i en to-personers gruppe.

*Tiltak:* Interne milepæler er satt opp og ukentlige statusmøter avholdes. Eventuelle forsinkelser tas opp tidlig, slik at arbeidsfordeling eller prioriteringer kan justeres underveis.

---

## 6. Ressurser

### 6.1 Prosjektteam og roller

Prosjektgruppen består av to medlemmer med bakgrunn innen logistikk, økonomi, analyse og IT/KI. Birgitte fungerer som prosjektkoordinator med ansvar for kontakt med bedriften. Begge gruppemedlemmene bidrar aktivt til metodevalg, datainnsamling, analyse og tolkning av resultater.

| Navn | Rolle | Ansvar |
|------|-------|--------|
| Birgitte | Prosjektkoordinator | Kontakt med Modino, koordinering, rapportskriving |
| Vera | Prosjektmedlem | Metode, analyse, rapportskriving |

### 6.2 Ansvarsfordeling

Ansvarsfordelingen baseres på både kompetanse og kapasitet. Hver deltaker har hovedansvar for sitt område, men større leveranser gjennomgås i fellesskap før ferdigstillelse. Dette gjelder spesielt modellforutsetninger, beregninger og sentrale analyser, slik at begge sikrer eierskap og forståelse for helheten.

### 6.3 Verktøy

| Verktøy | Bruksområde |
|---------|-------------|
| Microsoft Teams | Intern kommunikasjon og dokumentdeling |
| GitHub | Lagring og versjonskontroll av kode og analyser |
| Claude Code CLI | Databehandling, modellering og kvantitativ analyse |
| Python | Databehandling og automatisering |
| Excel | Datastrukturering og visualisering |
| MS Project | Gantt-diagram og kritisk sti |
| PowerPoint / Power BI | Visualisering av resultater |
| SAP (Modino) | Kildedatasystem for uttrekk |

---

## 7. Kommunikasjon

**Intern kommunikasjon** foregår i en dedikert Teams-kanal for prosjektet, der dokumenter og diskusjoner organiseres tematisk for enkel gjenfinning.

**Ukentlige arbeidsmøter** gjennomføres for å avklare fremdrift, diskutere metodiske valg og fordele videre oppgaver. I perioder med høy arbeidsbelastning settes det opp ekstra møter ved behov.

**Veiledningsmøter** med faglærer gjennomføres etter avtale. Konkrete spørsmål forberedes på forhånd for å få mest mulig ut av veiledningen.

**Statusrapportering** følges opp gjennom milepælsplanen og korte oppdateringer i de ukentlige møtene og via Teams-chat. Dersom deler av arbeidet tar lengre tid enn planlagt, vurderes omfordeling av oppgaver eller justering av omfang.

---

## 8. Kvalitet

### Peer-to-peer review

For å sikre faglig kvalitet gjennomfører vi intern gjennomlesning av hverandres arbeid. Dette gjelder både teoretiske deler og den kvantitative modellen. Vi legger særlig vekt på å kontrollere forutsetninger, logikk i modellen og konsistens mellom analyse og konklusjon.

### Godkjenningskriterier

Før innlevering vurderes prosjektet opp mot følgende kriterier:

- Problemstillingen er tydelig og operasjonaliserbar.
- Metodevalget er konsistent med formålet.
- Analysen er transparent og etterprøvbar.
- Det er klar sammenheng mellom resultater og konklusjoner.
- Begrensninger og videre arbeid er reflektert over.
- Rapporten fremstår helhetlig med korrekt språk, struktur og referanser.
