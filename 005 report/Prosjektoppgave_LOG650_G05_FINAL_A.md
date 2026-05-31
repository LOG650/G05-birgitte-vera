# Tittel (norsk og/eller engelsk)

**Forfatter(e):**

**Totalt antall sider inkludert forsiden:**

**Molde, Innleveringsdato:**

---

## Obligatorisk egenerklæring/gruppeerklæring

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk. Erklæringen skal bevisstgjøre studentene på deres ansvar og hvilke konsekvenser fusk kan medføre. Manglende erklæring fritar ikke studentene fra sitt ansvar.

Du/dere fyller ut erklæringen ved å klikke i ruten til høyre for den enkelte del 1-6:

**1.** Jeg/vi erklærer herved at min/vår besvarelse er mitt/vårt eget arbeid, og at jeg/vi ikke har brukt andre kilder eller har mottatt annen hjelp enn det som er nevnt i besvarelsen.

**2.** Jeg/vi erklærer videre at denne besvarelsen:

- ikke har vært brukt til annen eksamen ved annen avdeling/universitet/høgskole innenlands eller utenlands.
- ikke refererer til andres arbeid uten at det er oppgitt.
- ikke refererer til eget tidligere arbeid uten at det er oppgitt.
- har alle referansene oppgitt i litteraturlisten.
- ikke er en kopi, duplikat eller avskrift av andres arbeid eller besvarelse.

**3.** Jeg/vi er kjent med at brudd på ovennevnte er å betrakte som fusk og kan medføre annullering av eksamen og utestengelse fra universiteter og høgskoler i Norge, jf. §§4-7 og 4-8 og §§14 og 15.

**4.** Jeg/vi er kjent med at alle innleverte oppgaver kan bli plagiatkontrollert i URKUND.

**5.** Jeg/vi er kjent med at høgskolen vil behandle alle saker hvor det forligger mistanke om fusk etter høgskolens retningslinjer.

**6.** Jeg/vi har satt oss inn i regler og retningslinjer i bruk av kilder og referanser.

---

## Personvern

### Personopplysningsloven

Forskningsprosjekt som innebærer behandling av personopplysninger iht. Personopplysningsloven skal meldes til Norsk senter for forskningsdata, NSD, for vurdering.

**Har oppgaven vært vurdert av NSD?** ja / nei

- Hvis ja – Referansenummer:
- Hvis nei – Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven:

### Helseforskningsloven

Dersom prosjektet faller inn under Helseforskningsloven, skal det også søkes om forhåndsgodkjenning fra Regionale komiteer for medisinsk og helsefaglig forskningsetikk, REK, i din region.

**Har oppgaven vært til behandling hos REK?** ja / nei

- Hvis ja – Referansenummer:

---

## Publiseringsavtale

**Studiepoeng:**

**Veileder:**

### Fullmakt til elektronisk publisering av oppgaven

Forfatter(ne) har opphavsrett til oppgaven. Det betyr blant annet enerett til å gjøre verket tilgjengelig for allmennheten (Åndsverkloven. §2).

Alle oppgaver som fyller kriteriene vil bli registrert og publisert i Brage HiM med forfatter(ne)s godkjennelse.

Oppgaver som er unntatt offentlighet eller båndlagt vil ikke bli publisert.

**Jeg/vi gir herved Høgskolen i Molde en vederlagsfri rett til å gjøre oppgaven tilgjengelig for elektronisk publisering:** ja / nei

**Er oppgaven båndlagt (konfidensiell)?** ja / nei
(Båndleggingsavtale må fylles ut)

- Hvis ja – Kan oppgaven publiseres når båndleggingsperioden er over? ja / nei

**Dato:**

---

*Antall ord: Marker denne setningen, og skriv inn antall ord dersom det er et krav at antall ord skal oppgis. Hvis det ikke er et krav at antall ord skal oppgis slettes hele dette avsnittet, og i begge tilfeller slettes denne setning.*

*Forfattererklæring: Marker denne setningen, og skriv inn forfattererklæring dersom det er et krav til oppgaven. Hvis det ikke er krav om forfattererklæring slettes hele dette avsnitt, og i begge tilfeller slettes denne setning.*

---

## Sammendrag

Recommerce-markedet for brukte mobilenheter er i vekst, og evnen til å kanalisere innkommende enheter til riktig salgskanal er direkte avgjørende for lønnsomheten. Denne oppgaven undersøker hvordan en AI-basert klassifiseringsmodell kan forbedre kanaliseringsbeslutninger hos Modino AS — en nordisk recommerce-aktør som kjøper, renoverer og videreselger brukte smarttelefoner og nettbrett.

Datagrunnlaget er hentet fra to separate operasjonelle systemer: CellDe (inspeksjon og gradering ved mottak) og SAP S/4HANA (salg og fakturering). Totalt 93 575 enheter fra 2024 og 2025 er analysert. Klassifiseringslogikken bygger på faktisk observert salgskanal — sluttkunde via Teleoutlet (klasse A), tredjepartshandler (klasse B) eller skrap/BER (klasse C) — definert fra SAP-data. En Random Forest-modell er trent på femten features hentet utelukkende fra CellDe på mottakstidspunktet, slik at target leakage unngås.

Modellen oppnår 83,76 % accuracy på testsettet, med F1-score på 0,78 (klasse A), 0,87 (klasse B) og 0,88 (klasse C). Minimumskravet på 80 % er oppfylt med god margin, og resultatet er stabilt over 5-fold kryssvalidering (83,34 % ± 0,41 %). Permutation importance avdekker at enhetskategori er den viktigste enkeltprediktoren (11,0 %), etterfulgt av innleveringsmåned (6,6 %) og modellverdi (6,1 %); leverandørratene er identifisert som ren støy, og et kontrolleksperiment bekrefter at en redusert 13-feature modell oppnår **84,42 % accuracy** — bedre enn 15-feature-modellen. Det dominerende feilmønsteret er forveksling mellom klasse A og B — et strukturelt problem fordi de samme enhetstypene faktisk havner i begge kanaler avhengig av Modinos lagerstyring. **Temporal validering (tren 2024 → test 2025) avdekker en concept drift på 13 prosentpoeng** (accuracy faller til 70,43 %), noe som krever kvartalsvis retrening i drift. Den estimerte lønnsomhetseffekten er presentert som et intervall (~−225 000 til ~+225 000 NOK per år, realistisk midtestimat omtrent +110 000 NOK) og er marginal sett mot Modinos totalvolum. Den primære operative verdien av modellen er derfor **standardisering** av kanaliseringsbeslutninger, ikke direkte profittforbedring. Et metodisk hovedfunn er identifisering og korrigering av target leakage i en tidlig analyseversjon, dokumentert eksplisitt som metodisk bidrag.

---

## Abstract

The recommerce market for used mobile devices is growing rapidly, and the ability to route incoming devices to the correct sales channel is directly linked to profitability. This thesis examines how an AI-based classification model can improve channeling decisions at Modino AS — a Nordic recommerce company that purchases, refurbishes and resells used smartphones and tablets.

The data set is based on two separate operational systems: CellDe (inspection and grading data at intake) and SAP S/4HANA (sales and invoicing). A total of 93 575 devices from 2024 and 2025 are analysed. The target variable is the actually observed sales channel — end customer through Teleoutlet (class A), third-party trader (class B) or scrap/BER (class C) — derived from SAP data. A Random Forest model is trained on fifteen features taken exclusively from CellDe at the time of intake, thereby avoiding target leakage.

The model achieves 83.76 % accuracy on the test set, with F1-scores of 0.78 (class A), 0.87 (class B) and 0.88 (class C). The predefined minimum requirement of 80 % is met with a clear margin and confirmed by 5-fold stratified cross-validation (83.34 % ± 0.41 %). Permutation importance identifies device category as the single most important predictor (11.0 %), followed by intake month (6.6 %) and model value (6.1 %); the dealer-rate features are identified as functional noise, and a control experiment confirms that a reduced 13-feature model achieves **84.42 % accuracy** — better than the 15-feature model. The dominant error pattern is confusion between classes A and B — a structural limitation because the same device profiles can end up in either channel depending on Modino's inventory management. **A temporal validation (train 2024 → test 2025) reveals concept drift of 13 percentage points** (accuracy falls to 70.43 %), implying quarterly retraining in operation. The estimated profitability effect is reported as an interval (approximately −225 000 to +225 000 NOK per year; realistic midpoint about +110 000 NOK), which is marginal relative to Modino's total volume. The primary operational value of the model is therefore **standardisation** of channel decisions, not direct profit improvement. A central methodological finding is the identification and correction of target leakage in an early analysis version, documented explicitly as a methodological contribution.

---

## Innhold

- [1. Innledning](#1-innledning)
  - [1.1 Problemstilling](#11-problemstilling)
  - [1.2 Delproblemer](#12-delproblemer)
  - [1.3 Avgrensinger](#13-avgrensinger)
  - [1.4 Antagelser](#14-antagelser)
- [2. Litteratur](#2-litteratur)
  - [2.1 Maskinlæring for klassifisering av returnerte forbrukerelektronikk](#21-maskinlæring-for-klassifisering-av-returnerte-forbrukerelektronikk)
  - [2.2 Integrert beslutningsstøtte i reverse logistics](#22-integrert-beslutningsstøtte-i-reverse-logistics)
  - [2.3 Recommerce og sirkulær økonomi for mobilenheter](#23-recommerce-og-sirkulær-økonomi-for-mobilenheter)
  - [2.4 Posisjonering av dette prosjektet](#24-posisjonering-av-dette-prosjektet)
- [3. Teori](#3-teori)
  - [3.1 Sirkulærøkonomi og recommerce](#31-sirkulærøkonomi-og-recommerce)
  - [3.2 Beslutningsstøtte og verdifall](#32-beslutningsstøtte-og-verdifall)
  - [3.3 Maskinlæring og klassifisering](#33-maskinlæring-og-klassifisering)
  - [3.4 Oppsummering og kobling til problemstilling](#34-oppsummering-og-kobling-til-problemstilling)
- [4. Casebeskrivelse](#4-casebeskrivelse)
  - [4.1 Modino AS og recommerce-markedet](#41-modino-as-og-recommerce-markedet)
  - [4.2 Enheter og graderingssystem](#42-enheter-og-graderingssystem)
  - [4.3 Klassifiseringsprosessen — tre kanaler ut av Modino](#43-klassifiseringsprosessen--tre-kanaler-ut-av-modino)
  - [4.4 Datagrunnlaget — to-kilde-arkitektur](#44-datagrunnlaget--to-kilde-arkitektur)
  - [4.5 Klassifiseringsutfordringen](#45-klassifiseringsutfordringen)
- [5. Metode og data](#5-metode-og-data)
  - [5.1 Metode](#51-metode)
    - [5.1.1 Forskningsdesign](#511-forskningsdesign)
    - [5.1.2 Validitet, reliabilitet og objektivitet](#512-validitet-reliabilitet-og-objektivitet)
    - [5.1.3 Valg av metode](#513-valg-av-metode)
  - [5.2 Data](#52-data)
- [6. Modellering](#6-modellering)
  - [6.1 Formalisering av klassifiseringsproblemet](#61-formalisering-av-klassifiseringsproblemet)
  - [6.2 Decision Tree (baseline)](#62-decision-tree-baseline)
  - [6.3 Random Forest (primærmodell)](#63-random-forest-primærmodell)
  - [6.4 Evalueringsrammeverk](#64-evalueringsrammeverk)
- [7. Analyse](#7-analyse)
  - [7.1 Datapreparering og målvariabel](#71-datapreparering-og-målvariabel)
  - [7.2 Observasjoner fra feature-konstruksjonen](#72-observasjoner-fra-feature-konstruksjonen)
  - [7.3 Modelltrening](#73-modelltrening)
  - [7.4 Generaliserbarhet og intern validering](#74-generaliserbarhet-og-intern-validering)
- [8. Resultat](#8-resultat)
  - [8.1 Modellytelse — sammenligning av Decision Tree og Random Forest](#81-modellytelse--sammenligning-av-decision-tree-og-random-forest)
  - [8.2 Konfusjonsmatrise — Random Forest](#82-konfusjonsmatrise--random-forest)
  - [8.3 Feature importance — Random Forest](#83-feature-importance--random-forest)
  - [8.4 Estimert lønnsomhetseffekt (delproblem 2)](#84-estimert-lønnsomhetseffekt-delproblem-2)
- [9. Diskusjon](#9-diskusjon)
  - [9.1 Svar på problemstillingen](#91-svar-på-problemstillingen)
  - [9.2 Sammenligning med litteraturen](#92-sammenligning-med-litteraturen)
  - [9.3 Forretningsmessig betydning for Modino](#93-forretningsmessig-betydning-for-modino)
  - [9.4 Metodiske begrensninger](#94-metodiske-begrensninger)
  - [9.5 Videre forskning](#95-videre-forskning)
- [10. Konklusjon](#10-konklusjon)
- [Referanser](#referanser)
- [Vedlegg](#vedlegg)

---

## 1. Innledning

Markedet for brukte forbrukerelektronikk er i sterk vekst. Økt bevissthet om ressursbruk, regulatoriske krav til produktlevetid og voksende etterspørsel etter rimeligere alternativer til nye enheter driver en rask ekspansjon av recommerce — kjøp, renovering og videresalg av brukte produkter (Proske et al., 2018). For recommerce-aktører som kjøper inn brukte mobilenheter i stort volum, er evnen til å bestemme hva som skal skje med hver enkelt enhet ved mottak, direkte avgjørende for lønnsomheten. En enhet som sendes til renovering og videresalg til sluttkunde gir vesentlig høyere margin enn en enhet solgt direkte til en B2B-aktør — men renovering er bare lønnsomt dersom enhetens tilstand og markedsverdi gjør det forsvarlig (Ferguson et al., 2009).

Beslutningen om hvilken kanal en innkommende enhet skal til — renovering, direkte B2B-salg eller skrap — må i praksis tas raskt, basert på begrenset informasjon og under tidspress. Guide og Van Wassenhove (2009) dokumenterer at 10 ukers forsinkelse i å få en brukt mobilenhet tilbake på markedet kan tilsvare et tap på omtrent 10 % av enhetens totalverdi. Feil kanalvalg er dermed ikke bare et operasjonelt problem, men et lønnsomhetsproblem med direkte konsekvenser for virksomhetens resultat.

Maskinlæring tilbyr en løsning: ved å trene en klassifiseringsmodell på historiske kanalutfall kan systemet lære hvilke enhetsattributter — tilstandsgrad, estimert markedsverdi, modell, farge — som predikerer hvilken kanal en enhet vil havne i. Ibrahim og Abdul-Kader (2025) demonstrerer at trebaserte klassifiseringsmodeller gir høy nøyaktighet på returdata for mobiltelefoner med tre disponeringskategorier. Turkolmez et al. (2024) finner tilsvarende resultater for refabrikerte laptoper. Govindan et al. (2015) identifiserer datadrevne tilnærminger til operasjonelle graderingsbeslutninger som et anerkjent gap i reverse logistics-litteraturen.

Det som mangler i eksisterende litteratur er en studie som (1) benytter en to-kilde-arkitektur med separate innkjøps- og salgsdata, (2) bruker faktisk observert salgskanal — ikke en lønnsomhetsberegning — som målvariabel, og (3) eksplisitt ekskluderer geografisk salgsinformasjon fra features for å sikre en modell som er anvendbar på beslutningstidspunktet. Dette prosjektet fyller dette gapet gjennom en casestudie hos **Modino AS** — en nordisk recommerce-aktør som kjøper, renoverer og videreselger brukte mobilenheter i Norge, Sverige, Finland og Estland.

Rapporten er strukturert som følger: Kapittel 2 gjennomgår relevant empirisk litteratur. Kapittel 3 presenterer det teoretiske rammeverket. Kapittel 4 beskriver Modino AS og datagrunnlaget. Kapittel 5 redegjør for metode og datapipeline. Kapittel 6 formaliserer og beskriver modellene. Kapittel 7 dokumenterer analysegjennomføringen. Kapittel 8 presenterer resultatene. Kapittel 9 diskuterer funnene. Kapittel 10 konkluderer.

### 1.1 Problemstilling

Hvordan kan en AI-basert klassifiseringsmodell forbedre kanaliseringsbeslutninger for brukte mobilenheter hos Modino AS?

### 1.2 Delproblemer

Problemstillingen operasjonaliseres gjennom to delproblemer:

**Delproblem 1:** I hvilken grad kan en klassifiseringsmodell basert på CellDe-inntaksdata korrekt predikere hvilken salgskanal en brukt mobilenhet vil ende i?

**Delproblem 2:** I hvilken grad kan en mer presis klassifisering øke netto lønnsomhet sammenlignet med historisk kanalvalg?

### 1.3 Avgrensinger

**Produktkategori:** Analysen omfatter utelukkende brukte smarttelefoner og nettbrett håndtert av Modino AS. Andre produktkategorier er ikke inkludert.

**Tidsperiode:** Datagrunnlaget dekker perioden 2024–2025. Konklusjoner om fremtidig ytelse forutsetter at markedsforholdene og Modinos kanalstruktur er tilstrekkelig stabile.

**Beslutningsomfang:** Prosjektet omhandler utelukkende klassifisering av innkommende enheter i tre kanalklasser. Prisingsbeslutninger, lageroptimering og logistikkplanlegging er ikke inkludert.

**Datagrunnlag:** Analysen er basert utelukkende på historiske transaksjonsdata fra Modinos operasjonelle systemer (CellDe og SAP). Det er ikke gjennomført intervjuer, spørreundersøkelser eller innsamling fra andre virksomheter.

**Features:** Kun informasjon tilgjengelig i CellDe på mottakstidspunktet benyttes som input til modellen. SAP-data — inkludert destinasjonsland, salgspris og kostnad — er ekskludert som features.

### 1.4 Antagelser

**Historiske utfall som etiketter:** Det antas at Modinos historisk observerte kanalvalg er konsistente nok til å fungere som treningsetiketter. Modellen lærer av det Modino faktisk har gjort — ikke nødvendigvis det optimale kanalvalget. Konsekvensen er at systematiske historiske feilklassifiseringer potensielt videreføres i modellen, noe som diskuteres i avsnitt 9.4.3.

**Stabile markedsforhold:** Det antas at verdifall, kanalstruktur og graderingslogikk er tilstrekkelig stabile i analyseperioden til at mønstre lært på 2024-data er gyldige på 2025-data og fremover. Endringer i Modinos salgsstruktur — for eksempel nye tredjepartshandlere eller nye geografiske markeder — vil kreve ny modelltrening.

---

## 2. Litteratur

Dette kapittelet gjennomgår de viktigste empiriske bidragene innen maskinlæring i reverse logistics og recommerce, med særlig vekt på forskning fra de siste årene. Målet er å posisjonere denne rapporten i forhold til eksisterende kunnskap og identifisere det gapet som prosjektet søker å fylle.

### 2.1 Maskinlæring for klassifisering av returnerte forbrukerelektronikk

Den empirisk nærmeste studien til dette prosjektet er Ibrahim og Abdul-Kader (2025), som kombinerer prediktiv og preskriptiv analyse for håndtering av returnerte mobiltelefoner. Forfatterne bruker maskinlæring til å predikere returvolum og kvalitetsfordeling, og kobler dette til en simuleringsmodell som anbefaler disponeringsstrategi. Studien deler produktkategori (mobiltelefoner) og reverse logistics-kontekst med Modino-prosjektet og bekrefter at datadrevne tilnærminger er anvendbare på dette segmentet. To viktige forskjeller bør likevel påpekes: (1) Ibrahim og Abdul-Kader bygger på aggregerte returstrømmer snarere enn enhetsnivå, og (2) deres modellstruktur er bredere preskriptiv, mens dette prosjektet fokuserer på den operasjonelle klassifiseringsbeslutningen ved mottak. Resultatene er dermed komplementære, ikke direkte sammenlignbare.

Turkolmez et al. (2024) anvender maskinlæringsalgoritmer — inkludert CART og Random Forest — på prising av refabrikerte laptoper ved livssluttsiden. Studien viser at trebaserte metoder gir praktisk beslutningsstøtte for forbrukerelektronikk med varierende alder og tilstand. Funnet underbygger metodevalget i dette prosjektet, men sammenligningen er begrenset av to forhold: laptoper og mobiltelefoner har ulike verdifallsprofiler og komponentstrukturer, og Turkolmez et al. behandler prising (kontinuerlig output) snarere enn diskret kanalvalg.

Govindan et al. (2015) gjennomgår 382 artikler innen reverse logistics og closed-loop supply chains og identifiserer datadrevne tilnærminger til operasjonelle graderingsbeslutninger som et anerkjent gap i forskningen. Studien posisjonerer automatisert klassifisering som ett av de mest lovende anvendelsesområdene for data-analyse i reverse supply chains. Dette gir akademisk begrunnelse for relevansen av Modino-prosjektet — det adresserer et eksplisitt identifisert kunnskapsbehov.

### 2.2 Integrert beslutningsstøtte i reverse logistics

Hübner et al. (2020) demonstrerer at integrert optimering av innkjøp, gradering og disponering gir vesentlig bedre lønnsomhet enn å behandle disse som isolerte, sekvensielle beslutninger. Studien underbygger at en helhetlig klassifiseringsmodell — som tar hensyn til enhetens tilstand allerede ved mottakstidspunktet — er mer verdifull enn separate manuelle vurderinger i hvert steg. Dette er direkte relevant for Modinos situasjon: klassifiseringsbeslutningen tas ved mottak, men konsekvensene materialiseres i salgskanalen.

Ferguson et al. (2009) viser empirisk at gradering av returnerte produkter *før* reprosessering reduserer totalkostnader med omtrent 11 %. Studien dokumenterer at verdien av gradering øker med variasjonen i returkvalitet og med asymmetrien i feilkostnadene — to kjennetegn som begge er til stede i Modinos operasjon. Det prinsipielle funnet er direkte overførbart, selv om studien er gjennomført i en annen industrikontekst.

Galbreth og Blackburn (2006) komplementerer dette med en formell modell for optimal sorteringspolitikk: når enheter har heterogen tilstand, bør gradering skje tidlig i prosessen for å sortere ut lavverdige enheter før ressurser investeres i testing og reparasjon. Studien gir det teoretiske fundamentet for hvorfor klassifisering ved mottak (slik Modino-prosjektet operasjonaliserer) gir høyere lønnsomhet enn å la klassifiseringen utkrystallisere seg sent i prosessen.

Teunter og Flapper (2011) viser at manuell BER-vurdering er inkonsistent og tidkrevende under usikker kvalitetsfordeling i returstrømmen. Dette gir empirisk støtte til at en datadrevet, konsistent klassifiseringsmodell har operasjonell merverdi utover ren accuracy-forbedring — selve standardiseringen er verdiskapende.

### 2.3 Recommerce og sirkulær økonomi for mobilenheter

Proske et al. (2018) analyserer recommerce-markedet for smarttelefoner og dokumenterer at gjenbruk gir betydelig levetidsforlengelse og ressursbesparelse, men at lønnsomheten er sterkt avhengig av korrekt kanalisering av enheter. Studien understreker at feilkanalisering ikke bare er et økonomisk problem for virksomheten, men også reduserer den faktiske miljøgevinsten av recommerce — noe som forankrer prosjektets problemstilling i en bredere sirkulærøkonomisk kontekst.

Guide og Van Wassenhove (2009) gir det operasjonelle motargumentet for hvorfor *raske* og *presise* graderingsbeslutninger er kritiske i recommerce: 10 ukers forsinkelse i å få en brukt mobilenhet tilbake på markedet tilsvarer omtrent 10 % verditap — et tap som ofte overstiger fortjenestemarginen per enhet. Dette gjør tidsdimensjonen til en sentral driver for verdiskaping og forsterker argumentet for automatisert klassifisering.

### 2.4 Posisjonering av dette prosjektet

Den gjennomgåtte litteraturen viser at maskinlæring og datadrevet beslutningsstøtte i reverse logistics og recommerce er et empirisk bekreftet anvendelsesområde (Ibrahim & Abdul-Kader, 2025; Turkolmez et al., 2024), at automatisert gradering har dokumentert lønnsomhetseffekt (Ferguson et al., 2009; Hübner et al., 2020), og at tidsdimensjonen i kanaliseringsbeslutningen er kritisk for verdiskaping (Guide & Van Wassenhove, 2009).

Det som skiller dette prosjektet fra eksisterende litteratur er kombinasjonen av fire forhold: (1) datagrunnlaget er hentet fra to separate operasjonelle systemer — CellDe for inntak og SAP for salg — og analyseres uten sammenslåing til én fil; (2) klassifiseringen er basert på *faktisk observert salgskanal* og ikke på en lønnsomhetsberegning eller en intern gradering; (3) modellen er trent eksplisitt uten post-salgsdata, slik at den er anvendbar på beslutningstidspunktet; og (4) prosjektet dokumenterer eksplisitt et target leakage-funn som metodisk bidrag — noe som ikke alltid gjøres synlig i sammenlignbar litteratur. Denne kombinasjonen gir en modell med høy intern validitet og direkte operasjonell relevans for en konkret recommerce-aktør.

---

## 3. Teori

Dette kapittelet presenterer det teoretiske rammeverket som danner grunnlaget for prosjektets problemstilling, metodevalg og analyse. Kapittelet er strukturert rundt tre faglige pilarer: (1) sirkulærøkonomi og recommerce, (2) beslutningsstøtte og verdifall i reverse logistics, og (3) maskinlæring og klassifisering. Avslutningsvis oppsummeres teoriens kobling til problemstillingen.

Et gjennomgående forbehold er at mye av litteraturen om maskinlæring i reverse logistics er gjennomført i andre industrikontekster enn brukte mobilenheter — for eksempel hvitevarer, bildeler og industrimaskiner. Overførbarheten av konkrete funn må vurderes kritisk opp mot Modinos spesifikke datagrunnlag, og dette adresseres løpende gjennom kapittelet.

---

### 3.1 Sirkulærøkonomi og recommerce

#### 3.1.1 Sirkulærøkonomi

Sirkulærøkonomi er et overordnet rammeverk for ressursbruk som tar sikte på å erstatte den tradisjonelle lineære modellen — produksjon, bruk og kassering — med et system der ressurser holdes i bruk så lenge som mulig. Walter Stahel, som regnes som sirkulærøkonomiens grunnlegger, beskriver overgangen som en bevegelse mot en ytelsesøkonomi der målet er å forlenge produkters levetid gjennom gjenbruk, reparasjon og refabrikasjon (Stahel, 2016). Hans fire mål — produktlivsforlengelse, langtidsbruksvarer, rekondisjonering og avfallsforebygging — er direkte operasjonalisert i Modinos virksomhet.

Geissdoerfer et al. (2017) definerer sirkulærøkonomi som et regenerativt system som søker å minimere ressursinnsats, avfall og energilekkasje ved å bremse, innsnevre og lukke material- og energisløyfer. En kjent svakhet i litteraturen er at begrepet mangler en entydig definisjon: Kirchherr et al. (2017) identifiserte over 100 ulike definisjoner i akademisk litteratur, noe som utfordrer konseptuell klarhet og sammenlignbarhet på tvers av studier.

Et praktisk verktøy for å operasjonalisere sirkulærøkonomiske strategier er **9R-rammeverket**, utviklet av Potting et al. (2017). Rammeverket beskriver ni sirkulære strategier rangert fra mest til minst sirkulær: Refuse, Rethink, Reduce, Reuse, Repair, Refurbish, Remanufacture, Repurpose og Recycle/Recover. Rammeverket er i dag et av de mest brukte verktøyene for å klassifisere og måle sirkulærøkonomiske tiltak internasjonalt. Det er direkte anvendbart på prosjektets klassifiseringssystem:

```
Figur 3.1: Kobling mellom 9R-rammeverket og Modinos salgskanaler

  9R-strategi              Modinos salgskanal
  ─────────────────────────────────────────────────
  R5–R6 – Refurbish /  →   Klasse A: Sluttkunde (Teleoutlet)
           Remanufacture     — enheten renoveres og selges til privatkunde
  R3 – Reuse           →   Klasse B: Tredjepartshandler
                             — enheten selges uten renovering til B2B-aktør
  R8–R9 – Recycle /    →   Klasse C: Skrap
           Recover           — enheten avhendes som skrap/BER

Egenprodusert. Basert på Potting et al. (2017).
```

Ved å forankre klassifiseringssystemet i 9R-rammeverket får modellens predikerte klasser et internasjonalt anerkjent begrepsapparat, og koblingen mellom prosjektet og sirkulærøkonomisk teori blir eksplisitt.

#### 3.1.2 Recommerce og markedet for brukte mobilenheter

Recommerce — kjøp, renovering og videresalg av brukte produkter — er en voksende del av den sirkulære økonomien for forbrukerelektronikk. Proske et al. (2018) analyserer recommerce-markedet for smarttelefoner spesifikt og dokumenterer at gjenbruk av brukte mobilenheter gir betydelig levetidsforlengelse og ressursbesparelse, men at lønnsomheten er sterkt avhengig av at enheter kanaliseres til riktig bruk basert på faktisk tilstand og gjenværende verdi.

En sentral utfordring i recommerce er verdifall over tid. For brukte mobilenheter akselererer verdifallet særlig ved lansering av nye modeller, noe som gjør tidsbruk i feil behandlingskø direkte kostbart (Guide & Van Wassenhove, 2009). En viktig distinksjon i recommerce-litteraturen er mellom *grading* (tilstandsvurdering) og *disposition* (kanalvalg). Galbreth og Blackburn (2006) viser at optimal lønnsomhet forutsetter at gradering skjer tidlig, slik at enheter med lavt potensial sorteres ut før ressurser investeres i testing og reparasjon. Dette er direkte relevant for prosjektets klassifiseringsmodell.

#### 3.1.3 Reverse logistics

Reverse logistics er prosessene knyttet til tilbakeflyt av produkter fra sluttbruker mot produsent eller mellomledd, med formål om å gjenvinne verdi. Rogers og Tibben-Lembke (1999, s. 2) definerer det som prosessen med planlegging, gjennomføring og kontroll av effektiv og kostnadseffektiv strøm av produkter og informasjon fra forbrukerpunktet tilbake mot opprinnelsespunktet for å gjenvinne verdi eller sikre korrekt disponering. Definisjonen dekker nøyaktig det Modino gjør.

Fleischmann et al. (1997) skiller mellom tre hovedaktiviteter i reverse logistics: innsamling, sortering og redistribusjon. For Modino tilsvarer disse innkjøp av brukte enheter, grading og klassifisering i CellDe, og videresalg gjennom ulike kanaler. Govindan et al. (2015) identifiserer i en systematisk gjennomgang datadrevne tilnærminger til operasjonelle graderingsbeslutninger som et anerkjent gap i litteraturen — noe som direkte posisjonerer Modino-prosjektet som et bidrag til et uløst og relevant forskningsproblem.

---

### 3.2 Beslutningsstøtte og verdifall

#### 3.2.1 BER og den økonomiske verdien av gradering

BER (Beyond Economical Repair) beskriver tilstanden der estimerte reparasjonskostnader overstiger enhetens forventede markedsverdi etter reparasjon. En BER-klassifisering innebærer at det er mer lønnsomt å avhende enheten som skrap enn å fullføre reparasjonen (Guide & Van Wassenhove, 2009). I Modinos klassifiseringssystem tilsvarer dette klasse C.

Den mest direkte akademiske begrunnelsen for at nøyaktig gradering har målbar økonomisk verdi, kommer fra Ferguson et al. (2009). I en empirisk studie demonstrerer de at gradering av returnerte produkter *før* reprosessering reduserer totalkostnadene med omtrent 11 % sammenlignet med ingen gradering. Studien viser at verdien av gradering øker med variasjonen i kvalitet på returnerte enheter og med kostnaden per feilklassifisering. Dette er kjerneargumentet som begrunner hele Modino-prosjektet: nøyaktig klassifisering av innkommende enheter har direkte, målbar effekt.

Manuell BER-vurdering er dokumentert som inkonsistent og tidkrevende (Teunter & Flapper, 2011), noe som underbygger behovet for en datadrevet klassifiseringsmodell.

#### 3.2.2 Verdifall og kapitalbinding

Verdifall er en av de viktigste driverne av lønnsomhet i recommerce. Guide og Van Wassenhove (2009) dokumenterer at for forbrukerelektronikk kan 10 ukers forsinkelse i å få et produkt tilbake på markedet tilsvare et tap på omtrent 10 % av produktets totalverdi — et tap som overstiger de fleste fortjenestemarginer. Dette understreker at rask og presis klassifisering er kritisk.

Geyer et al. (2007) viser at lønnsomheten av refabrikasjon er bestemt av samspillet mellom komponentkvalitet, refabrikasjonskostnad og markedspris — og at ikke alle returnerte enheter bør behandles likt. Dette er det bedriftsøkonomiske grunnlaget for at en klassifiseringsmodell som skiller mellom klasse A, B og C er mer lønnsomt enn en flat behandlingspolicy.

Kapitalbinding oppstår når enheter som burde sorteres ut tidlig i stedet belastes reparasjonskøen. Galbreth og Blackburn (2006) viser formelt at optimal sorteringspolitikk innebærer å sette en minste kvalitetsterskel for hvilke enheter som tas inn i reparasjonsprosessen, og at gevinsten av tidlig sortering øker med hastigheten på verdifallet. Hübner et al. (2020) utdyper dette ved å vise at integrert optimering av innkjøp, gradering og disponering gir vesentlig bedre lønnsomhet enn sekvensielle isolerte beslutninger.

#### 3.2.3 Beslutningsstøttesystemer i logistikk

Beslutningsstøttesystemer (DSS) er informasjonssystemer designet for å støtte semi-strukturerte beslutninger der store datamengder og komplekse avveininger gjør manuell beslutningstaking ineffektiv (Turban et al., 2011). Analytikkbaserte systemer gir størst gevinst når de er tett integrert i eksisterende beslutningsprosesser slik at output omsettes til konkrete handlinger uten ekstra manuelle steg. I dette prosjektet operasjonaliseres dette ved at klassifiseringsmodellens predikerte klasse (A, B eller C) direkte reflekterer den historisk observerte salgskanalen for enheter med tilsvarende egenskaper.

---

### 3.3 Maskinlæring og klassifisering

#### 3.3.1 Supervised learning

Maskinlæring er en del av kunstig intelligens der algoritmer lærer mønstre fra data uten at reglene eksplisitt programmeres (Hastie et al., 2009). Innen maskinlæring skilles det mellom supervised learning, unsupervised learning og reinforcement learning. Supervised learning benyttes i dette prosjektet fordi Modinos historiske data inneholder dokumenterte utfall — det er kjent hvilken salgskanal hver enhet faktisk gikk til. Algoritmen lærer å identifisere mønstre mellom input-variabler fra inntak og observert salgskanal, slik at den kan predikere klassen for nye, ukjente enheter (James et al., 2021).

En viktig forutsetning er at historiske utfall er korrekte etiketter på faktisk kanalvalg — og ikke bare et speil av tilfeldig eller inkonsistent praksis. Denne risikoen adresseres i metodekapittelet.

#### 3.3.2 Feature engineering og klasseimbalanse

Feature engineering er prosessen med å velge, transformere og konstruere input-variabler for å maksimere modellens prediktive kraft (Zheng & Casari, 2018). For dette prosjektet inkluderer sentrale features enhetens tilstandsgrad ved mottak, estimert innkjøpsverdi, enhetsmodell, -kategori, -farge, transaksjonstype og kanal — alle hentet fra CellDe-systemet på mottakstidspunktet. Et gjennomgående designprinsipp er at kun informasjon som er tilgjengelig *ved mottak* kan brukes som feature, for å unngå target leakage.

En praktisk utfordring er klasseimbalanse: klasse C (skrap) utgjør kun 0,6 % av det klassifiserte datasettet. Chawla et al. (2002) introduserte SMOTE (Synthetic Minority Over-sampling Technique) som én løsning, men i dette prosjektet benyttes klassevekting via `class_weight='balanced'` i scikit-learn, som justerer vekten på hver observasjon omvendt proporsjonalt med klassens frekvens uten å generere syntetiske datapunkter.

#### 3.3.3 Klassifiseringsalgoritmer

Klassifisering er en type supervised learning der målet er å predikere hvilken kategori en observasjon tilhører (Hastie et al., 2009). I dette prosjektet er problemet et multiclass classification-problem med tre klasser (A, B og C).

**Decision Tree** (Quinlan, 1986) benyttes som basismodell. Den er enkel og tolkbar, men utsatt for overfitting.

**Random Forest** (Breiman, 2001) er primærkandidaten. Metoden bygger et stort antall decision trees på tilfeldige underutvalg av data og variabler, og kombinerer prediksjonene gjennom majoritetsstemme. Metoden er robust mot overfitting, håndterer kategoriske variabler og klasseimbalanse godt, og produserer feature importance-verdier som angir hvilke enhetsattributter som driver kanalklassen. Ibrahim og Abdul-Kader (2025) og Turkolmez et al. (2024) demonstrerer begge at trebaserte metoder gir høy nøyaktighet på klassifisering av returnert forbrukerelektronikk, noe som støtter dette valget empirisk. Rekdal og Pettersen (2026, kap. 9) viser i tillegg at CART-beslutningstrær for disposisjonsbeslutninger i returlogistikk gir 92,4 % treff mot optimale etiketter — en direkte parallell til dette prosjektets problemstruktur.

#### 3.3.4 Evalueringsmetrikker

For å vurdere modellens ytelse benyttes standard klassifiseringsmetrikker (Sokolova & Lapalme, 2009):

**Accuracy** angir andelen korrekte prediksjoner totalt. Accuracy kan gi et misvisende bilde ved sterk klasseimbalanse og suppleres derfor alltid av precision og recall.

**Precision per klasse** angir andelen av de enhetene som ble predikert til klasse X som faktisk tilhørte klasse X.

**Recall per klasse** angir andelen av enhetene som faktisk tilhørte klasse X som modellen korrekt identifiserte.

**F1-score** er det harmoniske gjennomsnittet av precision og recall, og gir ett samlet mål per klasse.

**Confusion matrix** visualiserer fordelingen av korrekte og feilaktige prediksjoner for alle klasser og er nyttig for å identifisere systematiske feilklassifiseringer (Fawcett, 2006).

---

### 3.4 Oppsummering og kobling til problemstilling

```
Figur 3.2: Teorirammeverkets tre pilarer og kobling til prosjektets røde tråd

  PILAR 1                    PILAR 2                    PILAR 3
  Sirkulærøkonomi      →     Verdifall &          →     Maskinlæring &
  & Recommerce               BER-beslutning              Klassifisering
  ─────────────────          ─────────────────           ─────────────────
  Stahel (2016)              Ferguson et al.             Breiman (2001)
  Potting et al. (2017)      (2009)                      James et al. (2021)
  Geissdoerfer et al.        Geyer et al. (2007)         Ibrahim &
  (2017)                     Galbreth &                  Abdul-Kader (2025)
  Proske et al. (2018)       Blackburn (2006)            Turkolmez et al.
                             Hübner et al. (2020)        (2024)
        │                          │                           │
        └──────────────────────────┴───────────────────────────┘
                                   │
                      ┌────────────▼────────────┐
                      │  INNTAK (CellDe-data)   │
                      │  → PREDIKSJON (RF)      │
                      │  → SALGSKANAL A/B/C     │
                      └─────────────────────────┘

Egenprodusert.
```

Sirkulærøkonomi-litteraturen (Stahel, 2016; Potting et al., 2017; Geissdoerfer et al., 2017) gir den strategiske begrunnelsen for Modinos virksomhet og forankrer klassifiseringssystemet A/B/C i 9R-rammeverket. Reverse logistics-teorien (Galbreth & Blackburn, 2006; Ferguson et al., 2009; Hübner et al., 2020) definerer det operasjonelle beslutningsproblemet og dokumenterer at nøyaktig gradering har direkte, målbar effekt — noe Ferguson et al. (2009) beviser empirisk med ~11 % kostnadsreduksjon. Maskinlæringslitteraturen (Breiman, 2001; James et al., 2021; Ibrahim & Abdul-Kader, 2025) gir det metodiske verktøyet og den empiriske begrunnelsen for at trebaserte klassifiseringsmodeller er egnet for nettopp denne typen problem.

---

## 4. Casebeskrivelse

### 4.1 Modino AS og recommerce-markedet

Modino AS er en nordisk recommerce-aktør med virksomhet i Norge, Sverige, Finland og Estland (basert på prosjektinformasjon fra Modino AS). Selskapet kjøper brukte mobilenheter fra mobiloperatører, forsikringsselskaper og privatpersoner, og videreseller dem enten direkte til profesjonelle kjøpere (B2B) eller etter renovering til sluttkunder via sin netthandelsplattform Teleoutlet (One2cel AS). Modino opererer dermed i skjæringspunktet mellom reverse logistics og recommerce, og håndterer hele kjeden fra innkjøp og gradering til reparasjon og distribusjon.

Markedet for brukte mobilenheter er i vekst og drives av økt bevissthet om ressursbruk, regulatoriske krav til produktlevetid og voksende etterspørsel etter rimelige alternativer til nye enheter (Proske et al., 2018). Recommerce skiller seg fra tradisjonell lineær handel ved at produktets verdi ikke avskrives fullt ut ved første salg — gjenværende bruksverdi kan realiseres gjennom renovering og videresalg. For Modino er evnen til å identifisere hvilken kanal en enhet passer best for, direkte avgjørende for lønnsomheten i hvert enkelt produkt.

### 4.2 Enheter og graderingssystem

Modinos sortiment består utelukkende av brukte smarttelefoner og nettbrett. Enhetene ankommer i varierende tilstand — fra tilnærmet nye enheter med kosmetiske skjønnhetsfeil til enheter med alvorlige funksjonsfeil eller strukturelle skader.

Ved mottak gjennomgår hver enhet en automatisert inspeksjon i **CellDe** — Modinos digitale inspeksjons- og graderingsverktøy. CellDe tester enhetens funksjoner (skjerm, batteri, kamera, tilkobling m.m.) og registrerer eventuelle feil. På bakgrunn av denne inspeksjonen tildeles enheten en **inntaksgrad** på skalaen A–F, der A representerer best tilstand og F representerer enhet med alvorlige feil som gjør reparasjon ulønnsom:

**Tabell 4.1: CellDe-graderingsskala**

| Grad | Beskrivelse |
|---|---|
| A | Tilnærmet som ny — ingen eller minimale kosmetiske feil |
| B | Lettere slitasje — mindre riper, fullt funksjonell |
| C | Merkbar slitasje — synlige riper eller skader, funksjoner intakte |
| D | Betydelig slitasje eller enkeltfeil som krever reparasjon |
| E | Alvorlige feil — krever omfattende reparasjon |
| F | BER-kandidat — reparasjon ikke lønnsomt |

Inntaksgraden er den primære informasjonen om enhetens tilstand på det tidspunktet en kanaliseringsbeslutning må tas. Den registreres alltid, og er tilgjengelig for alle enheter i datasettet. CellDe registrerer i tillegg enhetens estimerte markedsverdi (`Inspected Device Value`), enhetsmodell, farge, enhetskategori, transaksjonstype og kanal — informasjon som alle er tilgjengelig ved mottakstidspunktet.

### 4.3 Klassifiseringsprosessen — tre kanaler ut av Modino

Etter inntak og CellDe-gradering importeres enhetens data til Modinos ERP-system, **SAP S/4HANA**. SAP oppretter en innkjøpsordre (Purchase Order) for enheten med et *buy-back*-artikkelnummer på formen `nummer_variant_grad` (for eksempel `16854_2_0`). Dette artikkelnummeret identifiserer enheten i SAP frem til den eventuelt gjennomgår renovering.

Fra dette punktet kan enheten ta én av tre veier ut av Modino:

**Kanal A — Sluttkunde via Teleoutlet (renovering)**
Enheten sendes til renovering gjennom en underleverandørordre (Subcontracting PO). Etter vellykket renovering endres artikkelnummeret fra buy-back-format til et *2nd*-artikkelnummer (rent numerisk, for eksempel `47731`). Den nye artikkelbeskrivelsen i SAP (`maktx`) koder eksplisitt inn post-renoverings-graden: en beskrivelse som `2nd-C iPhone 13 128GB Midnight` angir at enheten er gradert C etter renovering. Enheten selges deretter til privatkunder gjennom One2cel AS / Teleoutlet. Denne kanalen representerer 37,0 % av klassifiserte enheter i datasettet.

**Kanal B — Tredjepartshandler (direkte salg)**
Enheten selges uten renovering til en profesjonell B2B-aktør (tredjepartshandler) ved hjelp av det opprinnelige buy-back-artikkelnummeret. Selskapet faktureres direkte, og enheten forlater Modino uten ytterligere behandling. Kjente tredjepartshandlere i datasettet inkluderer Foxway OÜ, Bridge Nine OÜ, Renewed AB og Care1 A/S, identifisert via numerisk kunde-ID (`kunag`). Denne kanalen er den dominerende og representerer 62,4 % av klassifiserte enheter.

**Kanal C — Skrap/BER**
Enheten er vurdert som Beyond Economical Repair — reparasjonskostnadene overstiger forventet markedsverdi etter renovering. Enheten selges som skrap til kunde `1365865` («Modino vareuttak»), alltid med buy-back-artikkelnummer. BER-enheter gjennomgår aldri renovering og tildeles aldri et 2nd-artikkelnummer. Denne kanalen utgjør 0,6 % av klassifiserte enheter — en sterk klasseimbalanse som adresseres metodisk i kapittel 5.

Figur 4.1 illustrerer den fullstendige prosessflyten fra mottak til salgskanal.

![Figur 4.1: Prosessflyt fra mottak til salgskanal](figur_prosessflyt.png)

*Figur 4.1: Prosessflyt — fra inntak og CellDe-gradering til de tre salgskanaler A, B og C. Egenprodusert.*

Forholdet mellom artikkelnummertype og salgskanal er oppsummert i tabell 4.2.

**Tabell 4.2: Artikkelnummertype og salgskanal**

| Artikkelnummertype | Format | Eksempel | Salgskanal |
|---|---|---|---|
| Buy-back | `nummer_variant_grad` | `16854_2_0` | Tredjepartshandler eller Skrap/BER |
| 2nd | Rent numerisk | `47731` | Sluttkunde (Teleoutlet) |

### 4.4 Datagrunnlaget — to-kilde-arkitektur

Modinos operasjon genererer data i to separate systemer, og disse utgjør prosjektets to kildefiler:

**CellDe-filen** (`InspectedDeviceREport_cleaned_anon.xlsx`) representerer enhetens tilstand *ved inntak*. Filen inneholder én rad per inspeksjon og dekker 103 400 unike enheter fordelt på 2024 (45 676 rader) og 2025 (57 867 rader). Nøkkelfeltet er `IMEI` (15-sifret tekststreng), og relevante kolonner er blant annet `Grade`, `Inspected Device Value`, `Device Model`, `Device Category`, `Inspection Color`, `Transaction Type`, `Channel` og `InspectedFaults`.

**SAP-filen** (`Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx`) representerer enhetens *utgang* — hvilken kanal den faktisk gikk til, til hvilken pris og med hvilken kostnad. Filen inneholder én rad per unike IMEI og dekker 93 580 enheter. Nøkkelfeltet er `imei`, og relevante kolonner inkluderer `kunag` (selge-til kunde-ID), `kunnr` (sende-til kunde-ID), `matnr` (artikkelnummer) og `maktx` (artikkelbeskrivelse).

De to filene kobles utelukkende i minnet under analyse, via IMEI som koblingsnøkkel. De lagres aldri som én sammenslått fil. Av 103 400 CellDe-registrerte enheter har 93 580 (90,5 %) en tilsvarende SAP-rad — de resterende 9 820 antas å være i lager, under renovering eller avskrevet. Tabellen under oppsummerer datagrunnlaget.

**Tabell 4.3: Datagrunnlag**

| Fil | Kilde | Periode | Rader | Unike IMEI |
|---|---|---|---|---|
| `InspectedDeviceREport_cleaned_anon.xlsx` | CellDe | 2024–2025 | 103 543 (rådata) | 103 400 |
| `Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx` | SAP S/4HANA | 2024–2025 | 93 580 | 93 580 |
| Koblet datasett (i minnet) | CellDe + SAP | 2024–2025 | 93 575 | 93 575 |

*Merk: 93 575 rader etter frafall av 5 uklassifiserte enheter og 11 rader med manglende verdier i features.*

**Tidsdimensjon i datasettet.** Tiden fra mottak (CellDe) til salg (SAP) er en sentral operasjonell indikator for Modinos verdikjede. For de 93 575 ferdigsolgte enhetene er:

- Median: **37 dager**
- 74,1 % solgt innen 60 dager (P75 = 62 dager)
- P90 = 123 dager, P95 = 197 dager, P99 = 358 dager
- Maksimum: 765 dager (langtidsliggere)
- 36 anomalier (0,04 %) der salgsdato er før mottaksdato — sannsynligvis dataregistreringsfeil

Den korte mediantiden (37 dager) bekrefter at Modino opererer med rask omløpshastighet, men halen av langtidsliggere ut mot 765 dager indikerer at det finnes en gruppe enheter med betydelig verditapseksponering — i tråd med Guide og Van Wassenhove (2009) om at 10 ukers forsinkelse tilsvarer ~10 % verditap.

**Eksklusivitet mellom artikkeltyper.** Buy-back- og 2nd-artikler representerer to fullstendig adskilte populasjoner: av 58 928 IMEIer med buy-back-artikkel og 34 652 IMEIer med 2nd-artikkel er **null IMEIer registrert i begge**. Dette bekrefter at en enhet enten selges direkte i kanal B/C (buy-back) eller renoveres og selges i kanal A (2nd-artikkel) — det er ikke to sekvensielle stadier av samme enhet. Dette validerer den deterministiske klassifiseringsregelen i avsnitt 5.2.3.

### 4.5 Klassifiseringsutfordringen

Kanalvalget for en enhet bestemmes i prinsippet av enhetens verdi og tilstand og bør ideelt sett kunne predikeres fra CellDe-data som foreligger ved mottak. To kjennetegn ved Modinos data gjør imidlertid problemet ikke-trivielt.

For det første er `ship_country` fra SAP en *etikett på kjøpergruppen*, ikke en uavhengig forklaring: klasse A-enheter sendes i 98,5 % av tilfellene til Norge, og klasse B-enheter sendes i nærmere 100 % av tilfellene til andre land — primært Estland. Dette er fordi kanal A *er* norske sluttkunder via Teleoutlet og kanal B *er* europeiske B2B-kjøpere. `ship_country` kan derfor ikke benyttes som feature — variabelen registreres etter at salget er gjennomført (target leakage), og inneholder uansett ingen ekstra informasjon utover selve kanaldefinisjonen.

For det andre — og det er den substansielle utfordringen — leverer de samme innleveringsbutikkene (typisk Telenor-butikker) enheter som ender i begge kanaler avhengig av Modinos øyeblikkelige lagerstyring og markedssituasjon. En enhet med høy verdi og lav slitasje kan altså selges *både* til Teleoutlet (klasse A) og til en europeisk B2B-aktør (klasse B) — kanalvalget styres delvis av faktorer som ikke fanges opp av tilstandsdataene CellDe registrerer. Dette setter en strukturell øvre grense for hvor presist en CellDe-basert modell kan skille A fra B, uavhengig av metodevalg. Begrensningen diskuteres nærmere i avsnitt 9.4.1.

---

## 5. Metode og data

### 5.1 Metode

#### 5.1.1 Forskningsdesign

Prosjektet er utformet som en kvantitativ casestudie (Yin, 2018). Datagrunnlaget er historiske transaksjonsdata fra Modinos operasjonelle systemer, og analysen er gjennomført på et ferdig avgrenset datasett uten innsamling gjennom intervju eller spørreskjema. Den vitenskapelige tilnærmingen er positivistisk: det antas at observerte mønstre i historiske utfall er systematiske og stabile nok til at en modell trent på dem kan generalisere til fremtidige enheter (James et al., 2021).

Problemstillingen er prediktiv — målet er ikke å forklare *hvorfor* enheter havner i ulike kanaler, men å predikere *hvilken* kanal en enhet med gitte egenskaper vil ende i. Dette skiller prosjektet fra en tradisjonell forklarende studie og motiverer valget av maskinlæring fremfor regresjonsanalyse.

Prosjektet kan også forstås innenfor en kvantitativ logistikkstruktur der område, problemstilling, modell, prosess og metode skilles fra hverandre (Rekdal & Pettersen, 2026). I denne rapporten er **området** returlogistikk og recommerce, **problemstillingen** kanaliseringsbeslutningen for brukte mobilenheter, **modellen** en supervised learning-klassifiseringsmodell, og **metoden** Decision Tree og Random Forest.

#### 5.1.2 Validitet, reliabilitet og objektivitet

For en kvantitativ casestudie kreves det at forskningsdesignet vurderes opp mot fire standardkriterier (Yin, 2018):

**Konstruktvaliditet** — om målvariabelen faktisk måler det den hevdes å måle. Kanalklassene A, B og C er operasjonalisert gjennom tre deterministiske SAP-regler (artikkelnummertype, sende-til kunde-ID og trader-mengde, se 5.2.3). Hver enhet får en entydig klassifisering basert på faktisk observert utfall, ikke skjønnsmessig vurdering. Dette gir høy konstruktvaliditet for selve klassifiseringsdefinisjonen. En begrensning er at definisjonen forutsetter at salget er gjennomført — enheter på lager eller under renovering faller utenfor (se 9.4.7 om survivor-bias).

**Intern validitet** — om observerte sammenhenger mellom features og målvariabel er kausalt meningsfulle innenfor datasettet. Stratifisert 80/20-split og `random_state=42` sikrer reproduserbar separasjon mellom trening og test. Target encoding for leverandørrater er beregnet utelukkende på treningssettet for å unngå leakage. Den eksplisitte ekskluderingen av SAP-features (kap. 9.4.6) er det viktigste grepet for intern validitet — modellen kan ikke "fuske" ved å lese svaret fra post-salgsdata.

**Ekstern validitet** — om funnene kan generaliseres utover datasettet. Funnene er direkte gyldige for Modinos egen drift i analyseperioden (2024–2025). Generalisering til andre recommerce-aktører eller fremtidige tidsperioder krever forsiktighet og diskuteres i 9.4.5.

**Reliabilitet** — om en uavhengig forsker som følger samme prosedyre ville fått samme resultat. Hele datapipelinen — innlasting, rensing, klassifisering, feature engineering, modellering og evaluering — er gjennomført i Python-kode med eksplisitte parametere og fast `random_state=42`. Koden produserer identiske resultater ved gjentatt kjøring, og kildedataene er bevart i uendret form. Reliabiliteten er dermed høy.

**Objektivitet** ivaretas ved at alle modellbeslutninger (feature-valg, hyperparametere, klassifiseringsregler) er begrunnet i kapittel 5 og 6, og at alle vurderingsmetrikker rapporteres på testsettet — ikke valgt etter at resultatene var kjent.

#### 5.1.3 Valg av metode

Supervised learning klassifisering er valgt fordi Modinos historiske data inneholder dokumenterte utfall: det er kjent hvilken salgskanal hver enhet faktisk gikk til. Dette gir grunnlag for en etikettert treningsdataset, som er en forutsetning for supervised learning (Hastie et al., 2009).

Alternativet — en optimaliseringsmodell (for eksempel lineær programmering) — ble vurdert og forkastet. En optimaliseringsmodell krever en eksplisitt målfunksjon, beslutningsvariabler og restriksjoner, og forutsetter at kanalenes relative lønnsomhet er kjent og stabil. Klassifisering er metodisk enklere å begrunne og gjennomføre innenfor prosjektets rammer, og gir en direkte operasjonell output — predikert kanal — som kan integreres i Modinos eksisterende arbeidsflyt.

**Decision Tree** (Quinlan, 1986) benyttes som basismodell (baseline) fordi den er transparent og enkelt tolkbar. **Random Forest** (Breiman, 2001) er primærmodellen, valgt for sin robusthet mot overfitting, evne til å håndtere klasseubalanse og produksjon av feature importance-verdier.

Analysene er gjennomført i **Python 3** med bibliotekene `pandas` (databehandling), `scikit-learn` (modellering) og `openpyxl` (Excel-innlasting).

### 5.2 Data

#### 5.2.1 Datakilder og innlasting

Datagrunnlaget er hentet direkte fra Modinos operasjonelle systemer og stilt til rådighet for prosjektet i anonymisert form. Dataperioden er 2024–2025. Filene er i Excel-format (.xlsx) og leses inn separat:

CellDe-filen inneholder to regneark — ett per år — som konkatenteres til ett samlet datasett. Duplikater på IMEI-nivå fjernes ved å beholde den første forekomsten:

```python
cd24 = pd.read_excel(cellde_path, sheet_name='2024', dtype={'IMEI': str})
cd25 = pd.read_excel(cellde_path, sheet_name='2025', dtype={'IMEI': str})
cellde = pd.concat([cd24, cd25], ignore_index=True).drop_duplicates(subset='IMEI', keep='first')
```

SAP-filen leses inn med `kunag` og `kunnr` som tekststrenger for å bevare ledende nuller i kunde-ID:

```python
sap = pd.read_excel(sap_path, sheet_name='Sheet1',
                    dtype={'imei': str, 'kunag': str, 'kunnr': str})
```

De to filene kobles deretter i minnet via en venstrejoin på IMEI. Filene lagres aldri sammenslått — sammenslåingen eksisterer kun i arbeidsminnet under analysen. Av 103 400 CellDe-enheter har 93 580 (90,5 %) en tilsvarende SAP-rad. Etter sammenkobling og frafall av rader med manglende feature-verdier utgjør det analyseklare datasettet 93 575 rader.

#### 5.2.2 Datakvalitet og rensing

Begge kildefiler er levert i forhåndsrenset form. Rensingen som er gjennomført på rådata inkluderer:

- Fjerning av rader med blankt IMEI
- Fjerning av rader med ugyldig IMEI (ikke nøyaktig 15 sifre)
- Fjerning av dummy-IMEI `101010101010101` (oppsto 478 ganger totalt)
- IMEI lagret som 15-sifret tekststreng (eliminerer problemer med vitenskapelig notasjon fra Excel)
- For SAP-filen: fjerning av 864 duplikate IMEI-rader (samme enhet fakturert flere ganger samme dato); deduplisering beholder tidligste fakturadato per IMEI

Dataene er anonymisert av Modino: kundenavn er fjernet, og alle identifikatorer er numeriske kunde-IDer. I prosjektet benyttes utelukkende `kunnr` (numerisk sende-til kunde-ID) og `kunag` (numerisk selge-til kunde-ID) for klassifisering — ikke kundenavn, som er upålitelig som følge av tegnsettproblem i kildesystemet.

#### 5.2.3 Klassifisering — definisjon av målvariabelen

Målvariabelen `klasse` defineres på bakgrunn av SAP-data og angir hvilken salgskanal enheten faktisk gikk til. Klassifiseringen gjennomføres i tre trinn som sjekkes i fast prioritetsrekkefølge:

**Trinn 1 — Klasse C (Skrap/BER):** Enheten er klassifisert som skrap dersom `kunnr == '1365865'`. Denne kunden («Modino vareuttak») er mottaker for alle BER-enheter. Sjekken utføres alltid først for å forhindre feilklassifisering dersom en BER-enhet skulle sammenfalle med andre betingelser.

**Trinn 2 — Klasse A (Sluttkunde):** Enheten er klassifisert som sluttkunde-salg dersom `matnr` er rent numerisk (regulært uttrykk: `^\d+$`). Et rent numerisk artikkelnummer identifiserer et 2nd-artikkel, som per Modinos prosess utelukkende brukes for enheter som har gjennomgått renovering og selges via Teleoutlet.

**Trinn 3 — Klasse B (Tredjepartshandler):** Enheten er klassifisert som B2B-salg dersom `kunag` tilhører den kjente trader-mengden. Trader-IDene er numeriske kunde-IDer identifisert fra SAP:

```python
traders = {'544127', '707086', '995702', '498232', '1533558', '1536986',
            '1550704', '715038', '1530444', '1530472', '1602135', '1602088'}
```

Enheter som ikke tilfredsstiller noen av de tre betingelsene (5 rader) ekskluderes fra analysen. Klassifiseringsresultatet er oppsummert i tabell 5.1.

**Tabell 5.1: Klassifiseringsresultat**

| Klasse | Kanal | Antall | Andel |
|---|---|---|---|
| A | Sluttkunde (Teleoutlet) | 34 648 | 37,0 % |
| B | Tredjepartshandler | 58 388 | 62,4 % |
| C | Skrap/BER | 539 | 0,6 % |
| Uklassifisert (ekskludert) | — | 5 | < 0,1 % |
| **Totalt** | | **93 580** | **100 %** |

Den sterke dominansen til klasse B og den svært lave andelen til klasse C er tydelig illustrert i figur 5.1.

![Figur 5.1: Klassefordeling](figur_klassefordeling.png)

*Figur 5.1: Klassefordeling i det analyseklare datasettet (n = 93 575). Klasse B (tredjepartshandler) dominerer med 62,4 %, mens klasse C (skrap/BER) utgjør kun 0,6 %. Egenprodusert.*

#### 5.2.4 Feature engineering

Et gjennomgående designprinsipp er at kun informasjon som er tilgjengelig i CellDe *ved mottakstidspunktet* kan benyttes som feature. SAP-data (pris, kostnad, artikkelnummer, destinasjonsland) tilhører salgstidspunktet og er utilgjengelig på beslutningstidspunktet — bruk av slike variabler ville innebære target leakage og gi en modell uten praktisk anvendbarhet.

Femten features er konstruert fra CellDe-data:

**`grade_num`** — Inntaksgraden konverteres til en ordinal numerisk variabel: A=6, B=5, C=4, D=3, E=2, F=1. Ordinal koding bevarer den rangmessige relasjonen mellom graderingstrinnene.

**`device_value`** — `Inspected Device Value` er lagret i norsk tallformat med komma som desimalskilletegn og mellomrom som tusenskille (for eksempel `'3 954,04'`). Verdien parses til float med følgende funksjon:

```python
def parse_no_number(s):
    if pd.isna(s): return np.nan
    s = str(s).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    try: return float(s)
    except: return np.nan
```

**`model_encoded`** — `Device Model` inneholder 557 unike modellnavn. For å ivareta all modellinformasjon uten å introdusere svært høy dimensjonalitet, kodes hver modell med medianverdien av `device_value` for alle enheter av den modellen. Dette gir en kontinuerlig variabel som rangerer modeller etter typisk markedsverdi.

**`color_group_enc`** — `Inspection Color` inneholder 246 ulike fargenavn. Fargene grupperes i ti semantiske grupper — Black, White/Silver, Gray, Blue, Gold, Green, Purple/Violet, Red/Pink, Yellow og Other — og kodes deretter med label encoding (0–9).

**`Transaction Type_enc`** — 21 kategorier label-kodet (0–20).

**`Channel_enc`** — 20 kategorier label-kodet (0–19).

**`Device Category_enc`** — 3 kategorier (for eksempel smarttelefon, nettbrett) label-kodet (0–2).

**`har_feil`** — Binær variabel: 1 dersom `InspectedFaults` inneholder registrerte feil, 0 ellers.

**`fault_count`** — Antall individuelle feil registrert i `InspectedFaults`, telt som antall kommaseparerte elementer. Erstatter den binære `har_feil` med en mer granulær representasjon av skadeomfanget.

**`storage_gb`** — Lagringskapasitet i GB, ekstrahert fra modellnavnet med regulært uttrykk (`\d+ GB`). Enheter med høy lagringskapasitet er gjennomgående mer verdifulle og har høyere sannsynlighet for klasse A.

**`inspect_month`** — Måneden innleveringen ble gjennomført (1–12), avledet fra `Inspected Date`. Fanger opp sesongmessige variasjoner i enhetsmiks og markedsverdi.

**`inspect_year`** — Innleveringsår (2024 eller 2025). Reflekterer generelt verdiskift over tid ettersom nye modellgenerasjoner introduseres.

**`brand_enc`** — Merkevarenavn (Apple, Samsung, Google m.fl.) ekstrahert fra første ord i `Device Model` og label-kodet. Fanger opp merkespesifikke verdiprofiler som ikke fullt ut er ivaretatt av `model_encoded`.

**`dealer_A_rate`** — Historisk andel klasse A-enheter per leverandør (`DealerId`), beregnet utelukkende på treningssettet og deretter anvendt på testsettet (target encoding). Fanger opp at ulike leverandørkanaler systematisk leverer enheter av ulik kvalitet.

**`dealer_B_rate`** — Tilsvarende historisk andel klasse B-enheter per leverandør.

Det bemerkes at label encoding for `Transaction Type`, `Channel` og `Device Category` teknisk sett impliserer en ordinal relasjon mellom kategorier som ikke nødvendigvis eksisterer. For trebaserte metoder (Decision Tree og Random Forest) har dette i praksis begrenset betydning, ettersom splittepunktvalget ikke forutsetter noen lineær avstandsrelasjon mellom koder. Bruken av label encoding for uordnede kategorier i trebaserte modeller er et kjent og akseptert forenklingsvalg i litteraturen (Zheng & Casari, 2018), men begrensningen dokumenteres i diskusjonskapittelet.

Alle 15 features er oppsummert i tabell 5.2.

**Tabell 5.2: Feature-oversikt**

| Feature | Kilde (CellDe-kolonne) | Transformasjon |
|---|---|---|
| `grade_num` | `Grade` | Ordinal: A=6 … F=1 |
| `device_value` | `Inspected Device Value` | Norsk format → float |
| `model_encoded` | `Device Model` | Median `device_value` per modell |
| `color_group_enc` | `Inspection Color` | 246 farger → 10 grupper → label encoding |
| `Transaction Type_enc` | `Transaction Type` | 21 kategorier → label encoding |
| `Channel_enc` | `Channel` | 20 kategorier → label encoding |
| `Device Category_enc` | `Device Category` | 3 kategorier → label encoding |
| `har_feil` | `InspectedFaults` | Binær (1 = feil registrert) |
| `fault_count` | `InspectedFaults` | Antall kommaseparerte feil (0–N) |
| `storage_gb` | `Device Model` | GB-verdi ekstrahert med regex |
| `inspect_month` | `Inspected Date` | Måned (1–12) |
| `inspect_year` | `Inspected Date` | År (2024/2025) |
| `brand_enc` | `Device Model` | Merke label-kodet |
| `dealer_A_rate` | `DealerId` | Historisk A-andel per leverandør (target encoding, treningssett) |
| `dealer_B_rate` | `DealerId` | Historisk B-andel per leverandør (target encoding, treningssett) |

#### 5.2.5 Train/test-split og håndtering av klasseimbalanse

Datasettet deles i et treningssett (80 %) og et testsett (20 %) med stratifisert sampling (`stratify=y`). Stratifisering sikrer at klassenes relative fordeling er lik i begge sett — særlig viktig for klasse C som kun utgjør 0,6 % av dataene. Det stratifiserte splittet gir:

- Treningssett: 74 851 rader (A: 27 714 / B: 46 706 / C: 431)
- Testsett: 18 713 rader (A: 6 928 / B: 11 677 / C: 108)

Klasseimbalansen (C utgjør 0,6 %) håndteres ved `class_weight='balanced'` i scikit-learn. Dette justerer hver enkelt observasjons vekt omvendt proporsjonalt med klassens frekvens under trening, uten å generere syntetiske datapunkter. SMOTE (Chawla et al., 2002) ble vurdert som alternativ men forkastet da `class_weight='balanced'` er enklere å implementere, ikke introduserer risiko for overfitting på syntetiske punkter, og gir sammenlignbare resultater i litteraturen.

---

## 6. Modellering

### 6.1 Formalisering av klassifiseringsproblemet

La hver enhet *i* representeres ved en feature-vektor **x**_i ∈ ℝ¹⁵, der de femten elementene tilsvarer de CellDe-baserte variablene beskrevet i avsnitt 5.2.4. Målvariabelen *y*_i ∈ {A, B, C} angir den observerte salgskanalen. Klassifiseringsproblemet er å lære en funksjon

```
f : ℝ¹⁵ → {A, B, C}
```

slik at *f*(**x**_i) ≈ *y*_i for treningsdataene, og at *f* generaliserer til nye, ukjente enheter. Problemet er et multiclass classification-problem (tre klasser) innen supervised learning (James et al., 2021).

Rekdal og Pettersen (2026, kap. 9) beskriver en strukturelt analog problemstilling — disposisjonsbeslutning for returnerte enheter — der samme trebaserte tilnærming benyttes for å velge mellom reparere, refurbishe, resirkulere og deponere. Denne parallellen støtter valget av metodikk i dette prosjektet.

### 6.2 Decision Tree (baseline)

Et beslutningstre partisjonerer feature-rommet rekursivt ved å velge, i hvert node, den feature og terskelverdi som minimerer urenheten i de resulterende undernodene (Quinlan, 1986). Urenheten måles med **Gini-indeksen**:

```
Gini(t) = 1 - Σ_k p(k|t)²
```

der *p(k|t)* er andelen observasjoner av klasse *k* i node *t*, og summen går over alle klasser. En Gini-verdi på 0 betyr at noden er ren (alle observasjoner tilhører samme klasse); verdien er maksimal når klassene er likt fordelt. Ved hvert splittepunkt velges den feature *j* og terskel *s* som gir størst vektet Gini-reduksjon:

```
ΔGini = Gini(t) - [|t_L|/|t| · Gini(t_L) + |t_R|/|t| · Gini(t_R)]
```

Rekursjonen fortsetter til et stoppkriterium er nådd — i dette prosjektet er ingen eksplisitt dybdebegrensning satt, slik at treet vokser til alle løvnoder er rene eller ikke kan splittes videre. Prediksjonen for en ny enhet er klassen med flertall i den løvnoden enheten havner i.

Decision Tree benyttes som basismodell (baseline) fordi den er enkel å tolke og gir et referansepunkt for å vurdere gevinsten av en mer kompleks modell. En kjent svakhet er at treet er utsatt for overfitting: det tilpasser seg treningsdataene så nøyaktig at generaliseringsevnen svekkes (Breiman, 2001). Random Forest adresserer dette.

I kompendiet (Rekdal & Pettersen, 2026, kap. 9, Eksempel 3) demonstreres at et CART-beslutningstre med maksimal dybde 4 oppnår 92,4 % treff mot oracle-etiketter i en analog disposisjonsbeslutning for returnert elektronikk — noe som bekrefter metodens egnethet for denne typen problem.

Basismodellen er konfigurert som følger:

```python
DecisionTreeClassifier(class_weight='balanced', random_state=42)
```

### 6.3 Random Forest (primærmodell)

Random Forest er en ensemblemetode som bygger *B* uavhengige beslutningstrær og kombinerer prediksjonene gjennom **majoritetsstemme** (Breiman, 2001). To mekanismer sikrer at trærne er uavhengige:

**Bagging (Bootstrap Aggregating):** Hvert tre trenes på et tilfeldig utvalg med tilbakelegging (*bootstrap sample*) av treningsdataene. Omtrent én tredel av observasjonene holdes utenfor hvert tre (out-of-bag, OOB) og kan brukes til intern validering.

**Feature-underutvalg:** Ved hvert splittepunkt vurderes kun et tilfeldig underutvalg av features — typisk √*p* av totalt *p* features. Dette reduserer korrelasjonen mellom trærne, som er den primære årsaken til at ensemblet er mer robust enn ett enkelt tre.

Den endelige prediksjonen er klassen som flest trær stemmer på:

```
ŷ = argmax_k Σ_{b=1}^{B} 𝟙[f_b(x) = k]
```

#### 6.3.1 Feature importance

Random Forest produserer feature importance-verdier som angir hvilke variabler som bidrar mest til klassifiseringsnøyaktigheten. Viktigheten til feature *j* beregnes som gjennomsnittlig Gini-reduksjon over alle splittepunkter og alle trær der feature *j* benyttes:

```
Importance(j) = (1/B) · Σ_{b=1}^{B} Σ_{t: split on j} ΔGini(t, j)
```

Verdiene normaliseres slik at de summerer til 1, og tolkes som andelen av total Gini-reduksjon som kan tilskrives feature *j*. Feature importance gir innsikt i hvilke enhetsattributter som driver kanalvalget, og er dermed direkte verdifull for Modino utover selve klassifiseringsprediksjonene. Resultatene presenteres i figur 8.2 i kapittel 8.

![Figur 6.1: Feature importance — Random Forest](figur_feature_importance.png)

*Figur 6.1: Feature importance for Random Forest-modellen. `device_value` (estimert markedsverdi) og `Device Category` er de to viktigste prediktorene. Egenprodusert.*

#### 6.3.2 Håndtering av klasseimbalanse

Med `class_weight='balanced'` justeres observasjonsvektene omvendt proporsjonalt med klassens frekvens:

```
w_k = n / (K · n_k)
```

der *n* er totalt antall observasjoner, *K* er antall klasser og *n_k* er antall observasjoner i klasse *k*. For klasse C (539 av 93 575 observasjoner) gir dette en vekt på omtrent 58 × gjennomsnittet, som gjør at modellen «ser» klasse C-feil som langt mer kostbare under trening.

#### 6.3.3 Hyperparametere

Primærmodellen er konfigurert som følger:

```python
RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
```

`n_estimators=100` er valgt som et veletablert standardnivå der ensemblet er stabilt; i litteraturen er det vist at gevinsten av ytterligere trær avtar raskt etter 100–200 (Breiman, 2001). Det er ikke gjennomført systematisk hyperparametertuning (GridSearchCV) i denne analysen — prosjektets formål er å demonstrere klassifiseringstilnærmingens egnethet for Modinos kontekst, ikke å maksimere ytelse gjennom ekshaustivt parametersøk. Begrensningen diskuteres i kapittel 9. `random_state=42` sikrer reproduserbarhet. `n_jobs=-1` aktiverer parallell trening på alle tilgjengelige CPU-kjerner.

### 6.4 Evalueringsrammeverk

Modellenes ytelse vurderes på testsettet (18 713 rader) med fire komplementære metrikker (Sokolova & Lapalme, 2009):

**Accuracy** angir andelen korrekte prediksjoner totalt:

```
Accuracy = (TP_A + TP_B + TP_C) / n
```

Accuracy er enkel å tolke, men kan være misvisende ved sterk klasseimbalanse: en modell som alltid predikerer klasse B vil oppnå 62,4 % accuracy uten å lære noe nyttig.

**Precision per klasse** angir andelen av de enhetene som ble predikert til klasse *k* som faktisk tilhørte klasse *k*:

```
Precision_k = TP_k / (TP_k + FP_k)
```

**Recall per klasse** angir andelen av de enhetene som faktisk tilhørte klasse *k* som modellen korrekt identifiserte:

```
Recall_k = TP_k / (TP_k + FN_k)
```

**F1-score** er det harmoniske gjennomsnittet av precision og recall, og gir ett samlet mål per klasse:

```
F1_k = 2 · (Precision_k · Recall_k) / (Precision_k + Recall_k)
```

F1-score er særlig nyttig for klasse C, der precision og recall kan avvike betydelig. Recall for klasse C er spesielt kritisk operasjonelt: en BER-enhet som feilklassifiseres som A eller B vil belastes unødvendig med renoveringskostnader.

**Confusion matrix** visualiserer fordelingen av korrekte og feilaktige prediksjoner for alle tre klasser, og gjør det mulig å identifisere systematiske feilklassifiseringsmønstre — for eksempel om A og B forveksles hyppig (Fawcett, 2006).

---

## 7. Analyse

Dette kapittelet beskriver gjennomføringen av analysen — hva som faktisk ble gjort, og hvilke observasjoner som ble gjort underveis. Kapittelet bygger på metodebeskrivelsen i kapittel 5 og modellbeskrivelsen i kapittel 6, og leder frem til resultatpresentasjonen i kapittel 8.

### 7.1 Datapreparering og målvariabel

Etter innlasting og in-memory-join av CellDe- og SAP-filene på IMEI-nøkkel ble klassifiseringslogikken (avsnitt 5.2.3) applisert på 93 580 SAP-rader. Fem rader tilfredsstilte ingen av de tre betingelsene og ble ekskludert. Ytterligere 11 rader med manglende verdier i en eller flere features ble droppet under feature-konstruksjonen, slik at det endelige analyseklare datasettet utgjorde **93 575 rader**.

Den resulterende klassefordelingen — B: 62,4 %, A: 37,0 %, C: 0,6 % — reflekterer Modinos faktiske operasjonelle realitet i perioden 2024–2025. Klasse B utgjør majoriteten av SAP-volumet (tredjepartshandlere), mens klasse A (norske sluttkunder via Teleoutlet) er en klar minoritet. Klasse C er svært sjelden — kun 539 av 93 575 enheter ble klassifisert som skrap — noe som er realistisk gitt at BER-enheter kun utgjør en liten andel av innkommende volum.

Et sentralt analytisk funn er at `ship_country` fra SAP korrelerer nær-deterministisk med kanalklassen (NO → 98,5 % klasse A, andre land → ~100 % klasse B). Dette reflekterer at kanalen bestemmer destinasjonen — kanal A selges til norske sluttkunder, kanal B til europeiske B2B-kjøpere — ikke at geografi forklarer kanalvalget. Siden `ship_country` registreres etter salget, er den utilgjengelig som feature ved mottakstidspunktet. CellDe-dataene inneholder likevel et reelt prediktivt signal for A/B-skillet — noe som bekreftes av at modellen oppnår 83,76 % accuracy.

### 7.2 Observasjoner fra feature-konstruksjonen

Gjennomgangen av de femten feature-variablene avdekket følgende mønstre i det faktiske datasettet:

**`device_value`** viste betydelig spredning på tvers av klassene. Enheter i klasse A (sluttkunde) hadde gjennomgående høyere estimert markedsverdi enn enheter i klasse B (tredjepartshandler), som igjen lå noe høyere enn klasse C (skrap). Dette gir intuitiv mening: høyverdige enheter har større potensial for lønnsomhet etter renovering, mens lavverdige enheter raskere passerer BER-terskelen eller selges direkte til B2B.

**`grade_num`** viste at de fleste enheter i datasettet er gradert B eller C ved mottak — enheter i topp-tilstand (grad A) er relativt sjeldne, mens enheter med svært lav grad (E, F) utgjør BER-kandidatene. Graden er sterkere korrelert med klasse C enn med skillet mellom A og B, noe som er konsistent med at graderingsdata alene ikke fullt ut skiller de to kanalene.

**`model_encoded`** kodingen samlet 557 unike modellnavn i én kontinuerlig variabel basert på median `device_value` per modell. iPhone-modeller tenderte mot høye verdier, eldre Android-modeller mot lave. Kodingen bevarer den verdimessige rangeringen uten å introdusere 557 binære dummyvariabler.

**`color_group_enc`** — grupperingen av 246 fargenavn til 10 kategorier viste at Black og White/Silver dominerte datasettet med til sammen over halvparten av enhetene. De resterende gruppene (Gray, Blue, Gold m.fl.) hadde mer jevn fordeling. Fargegruppen hadde lav forklaringskraft for kanalklasse, noe som ble bekreftet av feature importance-resultatene.

**`har_feil`** — om enheten hadde registrerte feil i CellDe — var positivt korrelert med klasse C (BER-enheter har naturligvis hyppigere registrerte feil) og negativt korrelert med klasse A (renoverte sluttkunde-enheter er gjerne uten alvorlige feil). Variabelen er enkel men informativ.

### 7.3 Modelltrening

Begge modeller ble trent på treningssettet (74 851 rader) med `class_weight='balanced'` og `random_state=42` for reproduserbarhet.

**Decision Tree** ble trent uten dybdebegrensning, noe som innebærer at treet vokser til alle løvnoder er rene på treningsdataene. Dette gir tilnærmet perfekt nøyaktighet på treningssettet, men forventes å prestere dårligere på testsettet som følge av overfitting. Baseline-rollen er å etablere et referansepunkt for Random Forest.

**Random Forest** ble trent med 100 trær (`n_estimators=100`). Ensemblet er langt mer robust mot overfitting enn et enkelt tre: ved at hvert tre trenes på et bootstrap-utvalg og kun et tilfeldig underutvalg av features vurderes per splittepunkt, reduseres korrelasjonen mellom trærne og variansen i prediksjonene dempes.

En viktig analytisk observasjon er at Random Forest oppnår **83,76 % accuracy** på testsettet, mot Decision Trees 79,92 %. Forbedringen er særlig tydelig for klasse C (F1: 0,75 → 0,88) og klasse A (0,73 → 0,78). Dette bekrefter at det utvidede feature-settet tilfører reell prediktiv kraft — modellen er ikke begrenset av manglende informasjon alene, men drar nytte av bredere CellDe-data.

#### 7.3.1 Stratifisert 5-fold kryssvalidering

For å vurdere stabiliteten i accuracy-estimatet utover én tilfeldig 80/20-split er det gjennomført en stratifisert 5-fold kryssvalidering på treningssettet. Hver fold deler treningssettet i et internt trenings- og valideringssett med samme klassefordeling, og Random Forest trenes og evalueres fem ganger på ulike kombinasjoner.

**Tabell 7.1: Stratifisert 5-fold CV-resultat — Random Forest på treningssettet**

| Fold | Accuracy |
|---|---|
| 1 | 0,833 |
| 2 | 0,826 |
| 3 | 0,839 |
| 4 | 0,834 |
| 5 | 0,835 |
| **Gjennomsnitt ± std** | **0,8334 ± 0,0041** |
| **Macro-F1 (5-fold)** | **0,8414 ± 0,0090** |

Standardavviket på 0,41 prosentpoeng over de fem foldene viser at modellytelsen er **stabil og ikke et resultat av en heldig seed**. CV-gjennomsnittet (83,34 %) sammenfaller godt med testsett-resultatet (83,76 %), noe som styrker tilliten til generaliseringsevnen.

### 7.4 Generaliserbarhet og intern validering

For å vurdere om Random Forest-modellen generaliserer utover treningsdataene benyttes to indikatorer:

**Out-of-bag (OOB) score:** Ved bagging holdes omtrent én tredel av observasjonene utenfor hvert enkelt tre. Disse out-of-bag-observasjonene kan brukes som en intern valideringsmekanisme uten å berøre testsettet. OOB-scoren gir et uavhengig estimat på generaliseringsevnen og forventes å ligge nær test-accuracy for en veltilpasset modell.

**Train/test-gap:** Et stort gap mellom treningsaccuracy og testaccuracy er et tegn på overfitting. For Random Forest er treningsaccuracy nær 100 % (et ubeskåret ensemble tilpasser seg treningsdataene nesten perfekt), mens testaccuracy er 83,76 %. Gapet på ~16 prosentpoeng reflekterer primært at Random Forest tilpasser seg treningsdataene svært tett — ikke at modellen mislykkes på usynlige data. Den tilsvarende CV-accuracy (83,34 % ± 0,41 %, avsnitt 7.3.1) bekrefter at testresultatet på 83,76 % er stabilt.

**Stratifisert split:** Den stratifiserte 80/20-delingen sikrer at klassefordelingen i testsett og treningssett er representativ for populasjonen. For klasse C (109 observasjoner i testsettet, 436 i treningssettet) er dette særlig viktig: uten stratifisering ville tilfeldig variasjon i hvem av C-enhetene som havner i test- versus treningssettet, gi ustabile estimater for F1 klasse C.

#### 7.4.1 Temporal validering — tren 2024, test 2025

Den primære evalueringen bruker en tilfeldig 80/20-split der trenings- og testsettet er blandet på tvers av 2024 og 2025. For en modell som skal brukes på fremtidige enheter er det imidlertid mer realistisk å teste **temporal generaliseringsevne**: kan modellen trent på 2024-data predikere kanalvalg for 2025-enheter?

For å adressere dette er det gjennomført et supplerende eksperiment der Random Forest trenes utelukkende på enheter med `inspect_year == 2024` (41 312 rader) og testes på enheter med `inspect_year == 2025` (52 252 rader). Resultatet er oppsummert i tabell 7.2.

**Tabell 7.2: Temporal validering — tren på 2024, test på 2025**

| Modell | Accuracy | Macro-F1 | F1 klasse A | F1 klasse B | F1 klasse C |
|---|---|---|---|---|---|
| Random Forest (tilfeldig split, referanse) | 83,76 % | 0,84 | 0,78 | 0,87 | 0,88 |
| Random Forest (temporal: 2024 → 2025) | **70,43 %** | 0,69 | 0,60 | 0,77 | 0,70 |
| **Drift (prosentpoeng)** | **−13,3** | **−0,15** | **−0,18** | **−0,10** | **−0,18** |

Nedgangen på **13 prosentpoeng accuracy** fra tilfeldig split til temporal split avdekker **betydelig concept drift** — markedsforhold, modellgenerasjoner og enhetsmiks har endret seg vesentlig mellom 2024 og 2025, og en modell trent utelukkende på fjorårets data har klart svakere prediktiv kraft for inneværende år.

En naturlig kontrolltest er om driften skyldes at modellen bruker `inspect_year` som feature — i 2024-treningssettet er denne verdien konstant (alle observasjoner = 2024), så featuren har ingen prediktiv kraft i trening, men 2025-observasjoner får en aldri-sett verdi. For å utelukke at denne mekanismen forklarer driften er modellen retrenet uten `inspect_year`-featuren, med tilnærmet identisk resultat: 70,58 % accuracy (vs. 70,43 % med featuren). Driften er dermed **strukturell** — den reflekterer reelle endringer i datasettet mellom 2024 og 2025 (enhetsmiks, kanalfordeling, markedsverdi), ikke en featurespesifikk artefakt. Dette har sterke implikasjoner for hvordan modellen kan settes i drift:

1. **Rapportert 83,76 % er et optimistisk estimat** for modellens forventede ytelse i drift, der treningsdata per definisjon vil være eldre enn enhetene som klassifiseres. Et mer realistisk forventet driftsnivå første år etter trening — uten retrening — er **omkring 70 %**.
2. **Modellens prediksjoner for nye enhetsmodeller** (iPhone 16, Samsung Galaxy S25 osv. lansert etter treningsdataenes slutt) vil ha enda lavere konfidens. En cold-start-strategi — der nye modellnavn håndteres via fallback-regler eller eksplisitt flagges for manuell vurdering — bør utvikles før produktivsetting.
3. **Rask retreningssyklus er nødvendig**, ikke valgfri. Modellen bør retrenes minst kvartalsvis, ikke årlig som først foreslått, for å motvirke den observerte driften (kap. 9.5).

---

## 8. Resultat

Dette kapittelet presenterer resultatene av modelltreningen og evalueringen objektivt. Tolkning og diskusjon av funnene er forbeholdt kapittel 9.

### 8.1 Modellytelse — sammenligning av Decision Tree og Random Forest

Tabell 8.1 viser ytelsesmetrikker for begge modeller på testsettet (18 713 rader). F1-score per klasse er hovedmålet ettersom det balanserer precision og recall, noe som er særlig relevant ved den sterke klasseimbalansen i datasettet.

**Tabell 8.1: Modellsammenligning — testsett (n = 18 713)**

| Modell | Accuracy | Macro-F1 | F1 klasse A | F1 klasse B | F1 klasse C |
|---|---|---|---|---|---|
| Majority class baseline (alltid B) | 62,4 % | 0,26 | 0,00 | 0,77 | 0,00 |
| Decision Tree (baseline) | 79,9 % | 0,77 | 0,73 | 0,84 | 0,75 |
| **Random Forest (primær)** | **83,8 %** | **0,84** | **0,78** | **0,87** | **0,88** |

Random Forest oppnår 83,8 % accuracy mot Decision Trees 79,9 % og majority-baseline 62,4 %. Random Forest overgår Decision Tree på alle tre klasser, med særlig stor forbedring for klasse C (F1: 0,88 vs. 0,75). 80 %-kravet definert i prosjektplanen er oppfylt, og løftet over majority-baseline (+21,4 prosentpoeng) viser at modellen tilfører reell prediktiv kraft.

Tabell 8.2 viser precision og recall separat for Random Forest, beregnet fra konfusjonsmatrisen i avsnitt 8.2.

**Tabell 8.2: Precision og recall per klasse — Random Forest**

| Klasse | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| A — Sluttkunde | 0,78 | 0,79 | 0,78 | 6 928 |
| B — Tredjepartshandler | 0,88 | 0,86 | 0,87 | 11 677 |
| C — Skrap/BER | 0,94 | 0,83 | 0,88 | 108 |
| **Macro avg** | **0,86** | **0,83** | **0,84** | 18 713 |

Klasse C har den høyeste precision (0,94): av alle enheter modellen klassifiserer som skrap, er 94 % korrekte. Klasse B oppnår den beste balansen mellom precision og recall (0,88/0,86). Skrap-klassen viser høy precision men lavere recall (0,83) — operasjonell implikasjon drøftes i avsnitt 9.4.7.

Figur 8.1 viser konfusjonsmatrisene for begge modeller side ved side.

![Figur 8.1: Konfusjonsmatriser — Decision Tree og Random Forest](figur_konfusjonsmatriser.png)

*Figur 8.1: Konfusjonsmatriser for Decision Tree (venstre) og Random Forest (høyre) på testsettet. Diagonalverdier er korrekte prediksjoner. Egenprodusert.*

### 8.2 Konfusjonsmatrise — Random Forest

Tabell 8.3 viser den fullstendige konfusjonsmatrisen for Random Forest på testsettet. Rader angir faktisk klasse, kolonner angir predikert klasse.

**Tabell 8.3: Konfusjonsmatrise — Random Forest (testsett, n = 18 713)**

| Faktisk \ Predikert | A | B | C |
|---|---|---|---|
| **A** (n = 6 928) | 5 497 | 1 428 | 3 |
| **B** (n = 11 677) | 1 587 | 10 087 | 3 |
| **C** (n = 108) | 7 | 11 | 90 |

Det dominerende feilmønsteret er forvekslingen mellom klasse A og klasse B: 1 428 faktiske A-enheter predikeres som B, og 1 587 faktiske B-enheter predikeres som A. Antall A/B-forvekslinger er nær symmetrisk (forholdstall 1,11). Klasse C er godt identifisert: 90 av 108 skrap-enheter (83 %) klassifiseres korrekt, og kun 6 ekstra enheter feilklassifiseres inn i klasse C — den lave falsk-positive-raten for C er operasjonelt verdifull (se 9.4.7).

### 8.3 Feature importance — Random Forest

Tabell 8.4 viser feature importance for Random Forest, normalisert slik at verdiene summerer til 100 %.

**Tabell 8.4: Feature importance — Random Forest (Gini)**

| Rang | Feature | Viktighet |
|---|---|---|
| 1 | `device_value` (estimert markedsverdi) | 18,9 % |
| 2 | `Device Category` (enhetskategori) | 15,9 % |
| 3 | `grade_num` (inntaksgrad) | 13,8 % |
| 4 | `model_encoded` (modellverdi) | 9,2 % |
| 5 | `inspect_month` (innleveringsmåned) | 6,9 % |
| 6 | `color_group_enc` (fargegruppe) | 6,7 % |
| 7 | `dealer_B_rate` (historisk B-andel per leverandør) | 5,7 % |
| 8 | `dealer_A_rate` (historisk A-andel per leverandør) | 5,6 % |
| 9 | `Transaction Type_enc` | 3,8 % |
| 10 | `fault_count` (antall registrerte feil) | 3,6 % |
| 11 | `storage_gb` (lagringskapasitet) | 2,5 % |
| 12 | `Channel_enc` | 2,0 % |
| 13 | `brand_enc` (merke) | 1,9 % |
| 14 | `har_feil` (binær feil-indikator) | 1,7 % |
| 15 | `inspect_year` (innleveringsår) | 1,7 % |

De fire øverste features (`device_value`, `Device Category`, `grade_num`, `model_encoded`) forklarer til sammen 57,8 % av total Gini-reduksjon. `device_value` er den viktigste enkeltprediktoren under Gini-målet (18,9 %), men permutation importance (se avsnitt 9.2.2) viser en annen rangering der enhetskategori er primærprediktoren. Figur 8.2 illustrerer fordelingen.

![Figur 8.2: Feature importance — Random Forest](figur_feature_importance.png)

*Figur 8.2: Feature importance for Random Forest. `device_value` og `Device Category` er de to viktigste prediktorene under Gini-målet med til sammen 34,8 % av forklaringskraften. Permutation importance i avsnitt 9.2.2 gir en korrigert rangering. Egenprodusert.*

### 8.4 Estimert lønnsomhetseffekt (delproblem 2)

For å besvare delproblem 2 — om en klassifiseringsmodell kan forbedre lønnsomheten — beregnes den estimerte marginforbedringen dersom Random Forests prediksjoner hadde styrt kanalvalgene i stedet for det historisk observerte kanalvalget.

#### 8.4.1 Gjennomsnittlig margin per klasse

Gjennomsnittlig margin per enhet per klasse er beregnet fra SAP-dataene som gjennomsnitt av (salgspris − kostnad) per kanal:

**Tabell 8.5: Gjennomsnittlig margin per klasse**

| Klasse | Kanal | Gjennomsnittlig salgspris | Gjennomsnittlig kostnad | Margin per enhet |
|---|---|---|---|---|
| A | Sluttkunde (Teleoutlet) | 2 222 NOK | 1 738 NOK | **484 NOK** |
| B | Tredjepartshandler | 946 NOK | 749 NOK | **197 NOK** |
| C | Skrap/BER | 899 NOK | 705 NOK | **195 NOK** |

Klasse A genererer 2,5 × høyere margin enn klasse B og C. Klasse B og C har nær identiske marginer (197 vs. 195 NOK/enhet), noe som innebærer at feilklassifisering mellom B og C har svært liten lønnsomhetseffekt. Den kritiske feilklassifiseringen er A/B-forvekslingen.

#### 8.4.2 Estimeringsmetodikk og scenarioer

Lønnsomhetseffekten estimeres ved å sammenligne totalmargin under tre scenarioer på testsettet:

- **Historisk scenario (referanse):** total margin = Σ margin(faktisk klasse_i) for alle *i*. Dette representerer hva Modino faktisk tjente i perioden.
- **Modellscenario (optimistisk):** total margin = Σ margin(predikert klasse_i). Forutsetter at *alle* modellens avvik fra historisk kanalvalg er korrekte forbedringer.
- **Modellscenario (realistisk):** antar at 50 % av modellens avvik er korrekte forbedringer og 50 % er feil. Dette er et nøytralt midtestimat når man ikke har en uavhengig fasit for hva som var "riktig" kanalvalg.

Det er sentralt å være eksplisitt om at modellen er trent på de samme historiske etikettene som utgjør sammenligningsgrunnlaget. Per konstruksjon er modellens fasit Modinos faktiske historiske valg, og når modellen avviker er det per definisjon en feil mot fasiten — *med mindre* man antar at Modinos historiske valg ikke alltid var optimale. Lønnsomhetsregningens validitet hviler dermed på sannsynligheten for at modellens avvik representerer reelle forbedringer i forhold til det historiske valget.

#### 8.4.3 Resultater under tre antakelser

**Tabell 8.6: Estimert lønnsomhetseffekt på testsettet (n = 18 713)**

| Scenario | Antakelse om modellens avvik | Netto effekt (testsett) | Oppskalert til årsvolum |
|---|---|---|---|
| Historisk (referanse) | — | 0 NOK | 0 NOK |
| Modellscenario (realistisk) | 50 % av avvikene er forbedringer | ~+22 800 NOK | **~+110 000 NOK per år** |
| Modellscenario (optimistisk) | 100 % av avvikene er forbedringer | +45 633 NOK | ~+225 000 NOK per år |
| Modellscenario (pessimistisk) | 0 % — modellen bare introduserer støy | ~−45 633 NOK | ~−225 000 NOK per år |

Bruttoverdiene er drevet av to motsatte feilstrømmer mellom klasse A og klasse B: modellen reklassifiserer 1 587 faktiske B-enheter som A (potensiell gevinst: 1 587 × 287 NOK = +455 000 NOK), delvis oppveid av 1 428 faktiske A-enheter feilklassifisert som B (potensielt tap: 1 428 × 287 NOK = −410 000 NOK). Asymmetrien i forholdstall (1 587 : 1 428 = 1,11) gir nå et marginalt positivt fortegn på brutto-differansen — modellen tenderer mot å «oppgradere» grenseenheter til klasse A oftere enn å «nedgradere» dem til klasse B. En netto lønnsomhetsforbedring forutsetter likevel at modellens avvik er systematisk *mer korrekte* enn de historiske valgene de erstatter, ikke bare statistisk skjeve.

#### 8.4.4 Tolkning og forbehold

Det realistiske midtestimatet på **omtrent 110 000 NOK per år** er fortsatt marginalt sett mot Modinos totalvolum (årlig margin fra de tre kanalene er om lag 28 MNOK basert på testsettet ekstrapolert — dvs. ~0,4 % marginforbedring). Det operasjonelt meningsfulle tallet er derfor ikke kronebeløpet i seg selv, men *størrelsesordenen*: modellen forbedrer ikke lønnsomheten vesentlig, og lønnsomhetsdimensjonen alene er ikke det sterkeste argumentet for å implementere den.

Den primære verdien av modellen er **standardisering** — konsistente, datadrevne kanalvalg som utnytter mønstre på tvers av 93 575 historiske enheter. Dette argumentet utdypes i kapittel 9.

For sammenligning er det illustrerende å nevne at en tidligere analyseversjon — der SAP-data (salgsinntekt, kostnad, destinasjon) ble brukt som features — estimerte en gevinst på rundt 390 000 NOK per år. Da disse post-salgsvariablene ble identifisert som target leakage og fjernet, falt estimatet til den marginale størrelsesorden som rapporteres her. Nedgangen er et diagnostisk funn: den tilsynelatende gevinsten i den tidligere analysen var drevet av informasjon modellen ikke kan ha tilgang til i drift.

---

## 9. Diskusjon

Dette kapittelet drøfter funnene fra analysen og resultatene opp mot prosjektets problemstilling og delproblemer, sammenligner med eksisterende litteratur, vurderer den forretningsmessige betydningen for Modino, og diskuterer metodiske begrensninger og muligheter for videre forskning.

### 9.1 Svar på problemstillingen

Prosjektets problemstilling spør hvordan en AI-basert klassifiseringsmodell kan forbedre kanaliseringsbeslutninger for brukte mobilenheter hos Modino AS. Analysen viser at Random Forest-modellen klassifiserer innkommende enheter i de tre kanalklassene A, B og C med **83,76 % accuracy** på et testsett på 18 713 enheter — godt over det definerte minimumskravet på 80 %. Modellen er dermed i stand til å automatisere og standardisere en beslutning som i dag ikke er datadrevet, og den gjør det med tilstrekkelig nøyaktighet til at prosjektets formål er faglig begrunnet.

Resultatet må tolkes i lys av hvilken informasjon modellen faktisk har tilgang til. Modellen opererer utelukkende på CellDe-data fra mottakstidspunktet — det er nettopp dette som gjør den praktisk anvendbar. Tidligere analyseforsøk oppnådde 92,4 % accuracy, men brukte SAP-data som features. SAP-data eksisterer kun etter at salget er gjennomført, og en modell basert på slike data kan ikke benyttes til å ta beslutningen *ved mottak*. Reduksjonen fra 92,4 % til 83,76 % er dermed ikke et tegn på en dårligere modell — det er et tegn på en *ærlig* modell som opererer under de rammebetingelsene som faktisk gjelder i en driftssetting.

#### 9.1.1 Delproblem 1 — Klassifiseringsnøyaktighet

Det definerte minimumskravet på 80 % accuracy er oppfylt med 83,76 % på den tilfeldige 80/20-testsplit. F1-score for de tre klassene er 0,78 (A), 0,87 (B) og 0,88 (C). Klasse B oppnår fremdeles den høyeste F1-scoren, men klasse C er nå på linje med klasse B — et markant forbedret resultat. At klasse C oppnår F1 på 0,88 til tross for at den utgjør kun 0,6 % av datasettet, er et sterkt positivt funn — `class_weight='balanced'` og det utvidede feature-settet fungerer etter hensikten. Kryssvalidering med 5-fold stratifisert split (avsnitt 7.3.1) bekrefter at resultatet er stabilt: 83,34 % ± 0,41 %.

**Et viktig forbehold er imidlertid avdekket gjennom temporal validering** (avsnitt 7.4.1): når modellen trenes utelukkende på 2024-data og testes på 2025-data, faller accuracy til 70,43 % — en drift på 13 prosentpoeng. Dette innebærer at 83,76 % er et noe optimistisk estimat for hva modellen vil oppnå i en faktisk driftssetting der treningsdata per definisjon er eldre enn enhetene som klassifiseres. Det realistiske forventede driftsnivået er ~70 %, og minimumskravet på 80 % overholdes kun dersom modellen retrenes hyppig (anbefalt kvartalsvis, se 9.5).

Det dominerende feilmønsteret er fremdeles forvekslingen mellom klasse A og klasse B: 1 428 faktiske A-enheter predikeres som B, og 1 587 faktiske B-enheter predikeres som A. Feilfordelingen er nå nær symmetrisk — i kontrast til den asymmetriske fordelingen i den opprinnelige modellen. Dette er ikke tilfeldig støy — det er et strukturelt problem som diskuteres nærmere i avsnitt 9.4.

#### 9.1.2 Delproblem 2 — Lønnsomhetseffekt

Den estimerte lønnsomhetseffekten er presentert som et intervall (kap. 8.4.3): et **realistisk midtestimat** på omtrent +110 000 NOK per år (under antakelsen om at halvparten av modellens avvik er reelle forbedringer), avgrenset av en optimistisk øvre grense på ~+225 000 NOK og en pessimistisk nedre grense på ~−225 000 NOK. Bredden i intervallet — og det faktum at det inkluderer null — er det viktigste funnet for delproblem 2: lønnsomhetsdimensjonen i seg selv gir ikke et entydig positivt argument for modellbasert klassifisering. Selv det optimistiske estimatet utgjør kun ~0,8 % av Modinos årlige bruttomargin.

Den tekniske forklaringen er at modellen gjør nær symmetriske feil mellom klasse A og klasse B: gevinstene fra B→A-omruting (~455 000 NOK brutto) oppveies delvis av tapene fra A→B-feilklassifisering (~410 000 NOK brutto). Modellen har et marginalt positivt skjevhetsfortegn (forholdstall 1,11) — den tenderer mot å «oppgradere» grenseenheter til klasse A oftere enn å «nedgradere» dem. En mer presis modell som tydeligere kunne bryte A/B-symmetrien ville gi et vesentlig høyere lønnsomhetsestimat.

Det er også illustrerende at en tidligere analyseversjon — der SAP-data ble inkludert som features — estimerte en gevinst på rundt 390 000 NOK per år. Da target leakage ble identifisert og korrigert, falt estimatet til den marginale størrelsesordenen vi rapporterer her. Dette er et diagnostisk funn i seg selv: den apparente lønnsomhetsgevinsten i den tidligere analysen var drevet av informasjon modellen ikke kan ha i drift. Den ærlige konklusjonen er derfor at **den primære verdien av modellen er standardisering av beslutninger, ikke direkte profittforbedring**. Standardiseringsverdien — at samme input alltid gir samme output, basert på mønstre på tvers av 93 575 historiske enheter — er kvalitativt forankret i Teunter og Flapper (2011), som dokumenterer at manuell BER-vurdering er inkonsistent.

---

### 9.2 Sammenligning med litteraturen

#### 9.2.1 Klassifiseringsnøyaktighet

Ibrahim og Abdul-Kader (2025) viser at maskinlæring og simuleringsbasert beslutningsstøtte kan brukes til å analysere returflyt, enhetskvalitet og disponeringsutfall for mobiltelefoner. Sammenligningen med dette prosjektet er relevant, men ikke direkte: deres studie har en bredere preskriptiv modellstruktur og bygger på aggregerte returstrømmer, mens Modino-prosjektet tester en operasjonell klassifiseringsmodell på enhetsnivå basert utelukkende på informasjon tilgjengelig ved mottakstidspunktet. Den realistiske sammenligningen er at begge studier bekrefter at datadrevne metoder er egnet for reverse logistics-beslutninger — og at nøyaktigheten er sterkt avhengig av hvilken informasjon som foreligger ved beslutningstidspunktet.

Turkolmez et al. (2024) finner tilsvarende at trebaserte metoder kan gi praktisk beslutningsstøtte for prising av refabrikerte laptoper. Studien underbygger metodevalgene i dette prosjektet, selv om laptoper og mobiltelefoner har ulike verdifallsprofiler og problemstillingen (prising vs. kanalvalg) ikke er identisk.

#### 9.2.2 Feature importance og praktisk innsikt

Det sterkeste enkeltfunnet fra feature importance-analysen er at **enhetens estimerte markedsverdi** (`device_value`, 18,5 %) og **enhetskategori** (`Device Category`, 17,0 %) fremdeles er de to viktigste prediktorene, men med et utvidet feature-sett distribueres forklaringskraften bredere. Inntaksgraden (`grade_num`, 13,7 %) er fremdeles viktig. Dette er konsistent med Galbreth og Blackburn (2006), som viser at optimal sorteringspolitikk er drevet av enhetens realiserte verdi snarere enn av tilstandsgrad alene.

Et nytt og interessant funn er at **innleveringsmåneden** (`inspect_month`, 6,9 %) er den femte viktigste prediktoren. Dette indikerer at enhetsmiksen varierer sesongmessig — noe som er operasjonelt plausibelt gitt at nye modellgenerasjoner typisk lanseres om høsten og driver innbytte-topper for eldre modeller. At `inspect_year` separat rangeres som #14 (1,7 %) tyder på at månedseffekten er en *intra-årlig* sesongkomponent, ikke en proxy for strukturell endring 2024→2025 — månedsfordelingen er trolig en reell driver av A/B-fordelingen heller enn et leakage-symptom. En formell sensitivitetsanalyse (modell trent uten `inspect_month`) ville styrket dette funnet ytterligere, men ble ikke gjennomført i prosjektets omfang.

**Leverandørrater** (`dealer_A_rate` og `dealer_B_rate`, 5,5 % hver) bekrefter at hvem som leverer inn enheter er informativt for kanalutfallet — ulike leverandørkanaler har ulik kvalitetsprofil. Stabiliteten i disse encodingverdiene for leverandører med små volum drøftes i avsnitt 9.4.8.

**Validering med permutation importance.** Verdiene rapportert i tabell 8.4 er beregnet med scikit-learns innebygde `feature_importances_`, som måler gjennomsnittlig Gini-reduksjon over alle splittepunkter. Strobl et al. (2007) viser at denne metrikken er systematisk biased mot kontinuerlige features og features med høy kardinalitet. For å validere rangeringen er det gjennomført en kontrollanalyse med **permutation importance** (`sklearn.inspection.permutation_importance`, 5 repetisjoner på testsettet), som måler det reelle accuracy-fallet når en feature shuffles. Resultatet er oppsummert i tabell 9.1.

**Tabell 9.1: Sammenligning av Gini- og permutation importance**

| Feature | Gini-importance | Permutation importance |
|---|---|---|
| `Device Category` | 15,9 % | **11,0 %** (#1) |
| `inspect_month` | 6,9 % | 6,6 % (#2) |
| `model_encoded` | 9,2 % | 6,1 % (#3) |
| `brand_enc` | 1,9 % | 5,5 % (#4) |
| `inspect_year` | 1,7 % | 4,0 % (#5) |
| `device_value` | **18,9 %** | 3,6 % (#6) |
| `grade_num` | 13,8 % | 3,3 % (#7) |
| `dealer_A_rate` | 5,6 % | **−0,3 %** |
| `dealer_B_rate` | 5,7 % | **−0,2 %** |

Permutation importance avdekker to viktige nyanser som ikke synes i Gini-analysen:

1. **Enhetskategori (`Device Category`) er den faktiske primærprediktoren** — ikke `device_value`. Gini overdrev `device_value` fordi det er en kontinuerlig variabel med mange potensielle splittepunkter. Funnet er i tråd med Strobl et al. (2007) og betyr at modellens prediksjoner først og fremst drives av om enheten er smarttelefon, nettbrett eller annet.

2. **Leverandørratene (`dealer_A_rate`, `dealer_B_rate`) er funksjonell støy, ikke signal.** Begge har *negativ* permutation importance, som betyr at modellen presterer marginalt bedre når disse features shuffles. Den positive Gini-verdien (5,5 %) er sannsynligvis et overfittingsartefakt — target encoding produserer ustabile rater for leverandører med små volum, og Random Forest fanger opp denne støyen som "splittepunktsverdi" uten at den generaliserer. Konsekvensen er at **disse to features bør fjernes fra produksjonsmodellen** — det vil gi en enklere modell uten ytelsesfall. Dette adresserer den smoothing-bekymringen som er drøftet i avsnitt 9.4.8.

Den kvalitative hovedkonklusjonen om at enhetsattributter (kategori, modell, merke, månedlig sesongmønster) er de viktigste prediktorene er fremdeles solid forankret, men prioriteringen mellom features har endret seg vesentlig sammenlignet med Gini-rangeringen.

Det er fortsatt bemerkelsesverdig at `har_feil` (binær feil-indikator) nå bidrar med kun 1,4 %, da `fault_count` (3,5 %) tar over mye av signalet og gir mer granulær informasjon om skadeomfanget. `device_value` og `grade_num` fanger uansett opp det meste av felinformasjonen implisitt.

---

### 9.3 Forretningsmessig betydning for Modino

#### 9.3.1 Fra manuell til modellbasert klassifisering

I Modinos nåværende prosess inspiseres og graderes enheter ved mottak av CellDe — et robotbasert testesystem som automatisk tester enhetens funksjoner (skjerm, batteri, kamera, tilkobling m.m.) uten menneskelig operatørvurdering. Selve kanaliseringsbeslutningen — A, B eller C — er i dag ikke systematisk datadrevet. En klassifiseringsmodell som systematisk benytter alle femten CellDe-features har to klare fordeler: den er konsistent (samme input gir alltid samme output), og den utnytter mønstre på tvers av 93 575 historiske enheter.

Hübner et al. (2020) viser at integrert automatisert beslutningsstøtte for innkjøp, gradering og disponering gir vesentlig bedre lønnsomhet enn sekvensielle manuelle beslutninger. Modino-prosjektet er et steg i denne retningen: klassifiseringsmodellen integrerer inntaksdata direkte i en kanalanbefaling, uten manuell skjønnsmessig vurdering.

#### 9.3.2 Praktisk implementering

For at modellen skal ha operasjonell verdi må den integreres i Modinos CellDe-arbeidsflyt slik at en predikert klasse (A, B eller C) presenteres automatisk for operatøren etter at inspeksjonen er fullført. Modellen bør ikke erstatte operatørens vurdering i sin helhet — særlig for grensetilfeller med lav prediksjonskonfidens bør den menneskelige vurderingen opprettholdes. En konfidensterskel, der modellen kun presenterer en anbefaling dersom prediksjonssannsynligheten overstiger for eksempel 70 %, kan redusere antallet tvilsomme prediksjoner som presenteres som fakta.

Videre bør modellen oppdateres jevnlig ettersom markedsforholdene for brukte mobilenheter endres — verdifallet for eldre modeller akselererer ved lanseringen av nye generasjoner, og en modell trent utelukkende på 2024–2025-data vil miste presisjon over tid (Guide & Van Wassenhove, 2009).

---

### 9.4 Metodiske begrensninger

#### 9.4.1 Strukturell A/B-grense i CellDe-dataene

Den viktigste metodiske begrensningen for klassifiseringsnøyaktigheten er at CellDe-data alene ikke fullt ut skiller mellom kanal A (sluttkunde via Teleoutlet) og kanal B (tredjepartshandler). Som påpekt i avsnitt 4.5 leverer de samme innleveringsbutikkene enheter som faktisk ender i begge kanaler, avhengig av Modinos lagerstyring og markedssituasjon. Dette setter en strukturell øvre grense for A/B-nøyaktigheten: en enhet med moderat verdi og god tilstand kan med samme inntaksprofil havne i begge kanaler, og kanalvalget bestemmes da av faktorer modellen ikke ser.

Dette forklarer den nær-symmetriske feilfordelingen i konfusjonsmatrisen (tabell 8.3): 1 428 faktiske A-enheter predikeres som B, og 1 587 faktiske B-enheter predikeres som A. Feilene er ikke tilfeldig støy, men reflekterer at modellen ikke har tilgang til den informasjonen som *i ettertid* skiller A fra B mest konsekvent (kjøperidentitet og destinasjonsland — som først er kjent etter at beslutningen er tatt). At Random Forest med 15 CellDe-features likevel oppnår 83,76 % accuracy mot Decision Trees 79,9 % viser at øvrig CellDe-informasjon — sesongmønster, leverandørhistorikk, feilantall — *inneholder* reell prediktiv kraft. Begrensningen er reell, men ikke absolutt.

En mulig vei videre er å undersøke om informasjon om hvem Modino selger til kan gjøres tilgjengelig *på eller nær mottakstidspunktet* — for eksempel om leverandørens kontraktstype (norsk B2C-kontrakt vs. europeisk B2B-kontrakt) er tilgjengelig i CellDe eller i Modinos innkjøpssystem. Dersom en slik proxy eksisterer, vil den trolig løfte A/B-nøyaktigheten betydelig.

#### 9.4.2 Label encoding for uordnede kategorier

`Transaction Type`, `Channel` og `Device Category` er label-kodet med heltall (0, 1, 2, …). Label encoding impliserer en ordinal relasjon mellom kategoriene som ikke nødvendigvis eksisterer — kode 0 er ikke «mindre enn» kode 1 i noen meningsfull forstand for uordnede kategorier. For trebaserte metoder er dette i praksis et begrenset problem, ettersom splittepunktvalget i hvert node vurderer alle mulige terskelverdier langs hver feature, og dermed i prinsippet kan skille mellom hvilken som helst kombinasjon av kategorier (Zheng & Casari, 2018). Begrensningen er reell for lineære modeller, men marginalt relevant for Random Forest. En alternativ fremgangsmåte er one-hot encoding, som øker dimensjonaliteten uten å introdusere ordinalantakelsen. For fremtidige iterasjoner av modellen kan det være verdt å sammenligne ytelsen med og uten one-hot encoding for å kvantifisere den faktiske effekten.

#### 9.4.3 Historiske etiketter som grunnlag

Modellen er trent på historisk observert kanalvalg — det vil si at etikett A, B eller C for hver enhet gjenspeiler den kanalen Modino *faktisk* valgte, ikke nødvendigvis den optimale kanalen. Dersom Modinos historiske klassifisering inneholder systematiske feil (enheter som burde ha vært i klasse A men ble sendt til klasse B), vil modellen lære disse feilene og videreføre dem. Dette er en iboende svakhet ved supervised learning basert på operasjonelle data (James et al., 2021). En mulig kvalitetssikring er å identifisere historiske enheter der modellens prediksjon avviker sterkt fra det observerte kanalvalget, og undersøke disse manuelt for å avdekke om de representerer feilklassifiseringer i historien eller legitime grensetilfeller.

#### 9.4.4 Manglende hyperparametertuning

Det er ikke gjennomført systematisk hyperparametertuning (GridSearchCV) i dette prosjektet. Standardparametere (`n_estimators=100`, ingen dybdebegrensning) er valgt basert på etablert praksis i litteraturen (Breiman, 2001). En systematisk søk over hyperparametere som `max_depth`, `min_samples_split` og `max_features` kan potensielt forbedre ytelsen — særlig for klasse C, der selv en marginal forbedring i recall er operasjonelt verdifull. Gitt at prosjektets primære formål er å demonstrere metodens egnethet snarere enn å maksimere ytelsen, er valget av standardparametere faglig begrunnet, men begrensningen bør anerkjennes.

#### 9.4.5 Generaliserbarhet (tverrsnittlig og temporal)

Analysen er gjennomført på data fra én bedrift (Modino AS) i én bransje (brukte mobilenheter) over en bestemt tidsperiode (2024–2025). Funnene er direkte generaliserbare til Modinos egen operasjon, men må tolkes med forsiktighet ved overføring til andre recommerce-aktører med annen salgsstruktur, annet produktmix eller andre geografiske markeder. Den metodiske tilnærmingen — å bruke to-kilde-arkitektur, faktisk observert salgskanal som målvariabel og kun inntaksdata som features — er imidlertid prinsipielt overførbar til andre recommerce-virksomheter med tilsvarende data.

**Temporal generaliserbarhet er begrenset.** Avsnitt 7.4.1 dokumenterer at en modell trent på 2024-data og testet på 2025-data faller fra 83,76 % til 70,43 % accuracy. Driften er størst for klasse C (F1 0,88 → 0,70) og klasse A (F1 0,78 → 0,60), og reflekterer at enhetsmiks, modellgenerasjoner og markedsverdier endrer seg vesentlig over relativt korte tidsperioder. Praktisk konsekvens: modellen bør retrenes minst kvartalsvis, og prediksjoner for nye enhetsmodeller bør håndteres med fallback-regler eller manuell vurdering.

#### 9.4.6 Survivor-bias i datagrunnlaget

Datasettet inkluderer kun de 90,5 % av CellDe-registrerte enheter som har en korresponderende SAP-rad — altså enheter som er *ferdig solgt eller skrapet* i analyseperioden. De resterende 9,5 % (9 820 enheter) antas å være på lager, under renovering eller avskrevet, og er ekskludert. Dette er en form for *survivor-bias*: modellen lærer av enheter som har passert gjennom hele verdikjeden, ikke fra alle enheter som faktisk ble mottatt.

Implikasjonen er at hvis høyverdige enheter systematisk ligger lenger på lager før salg (for eksempel fordi de venter på den beste markedstimingen), kan treningsdataene være skjeve mot enheter som ble *raskt* solgt — som ofte er enheter med lavere verdi i kanal B. Et fremtidig arbeid bør undersøke om de 9 820 ufakturerte enhetene har en annen verdi- eller graderingsprofil enn de 93 575 ferdigsolgte. Hvis ja, vil modellens prediksjoner for høyverdige nyinntak være systematisk skjeve. I praksis er dette mest sannsynlig et lite problem fordi gjennomsnittstid fra inntak til salg er kort i Modinos operasjon, men det er en forutsetning som ikke er formelt testet.

#### 9.4.7 Asymmetriske feilkostnader for klasse C

Tabell 8.2 viser at klasse C oppnår precision 0,94 og recall 0,83. Dette innebærer at modellen er *konservativ* — den predikerer C kun når den er sikker, og misser dermed 18 av 108 reelle BER-enheter (17 %). Disse blir feilklassifisert som A (7 stk.) eller B (11 stk.) og går unødvendig inn i renoverings- eller salgskøen.

Operasjonelt er dette potensielt en uheldig avveining. En BER-enhet som rutes til renovering vil belastes en renoveringskostnad (gjennomsnittlig 1 738 NOK for klasse A-enheter, jf. tabell 8.5) som per definisjon ikke kan dekkes av salgspris, og frigjør kapasitet i en knapp ressurs (renoveringskø). Det motsatte feilfortegnet — en grenseenhet som feilklassifiseres som C i stedet for B — koster derimot kun differansen mellom B- og C-margin (197 − 195 = 2 NOK), altså marginalt.

Den asymmetriske feilkostnadsstrukturen tilsier at en *cost-sensitive* hyperparameterkonfigurasjon — der C-prediksjoner gis høyere vekt enn dagens `class_weight='balanced'` (som kun balanserer på frekvens, ikke kostnad) — kunne forbedre nettoeffekten. Dette anbefales som videre arbeid (9.5).

#### 9.4.8 Stabilitet i target encoding for leverandørrater

`dealer_A_rate` og `dealer_B_rate` er beregnet ved å ta gjennomsnittlig A/B-andel per leverandør (`DealerId`) på treningssettet, og deretter applisere på testsettet (target encoding). Dette er metodisk korrekt med hensyn til leakage. En kjent svakhet er imidlertid at leverandører med få enheter i treningssettet gir ustabile rater — i ytterpunktet vil en leverandør med kun én enhet få rate 0,0 eller 1,0, som er en overfit-estimat.

**Permutation importance bekrefter denne bekymringen empirisk** (tabell 9.1): begge dealer-features har *negativ* permutation importance (henholdsvis −0,3 % og −0,2 %), som innebærer at modellens accuracy *forbedres* marginalt når disse features shuffles. Den positive Gini-verdien (5,5–5,7 %) er dermed et overfittingsartefakt — Random Forest fanger opp leverandørspesifikk støy som splittpunktverdi uten at det generaliserer til testsettet.

For å verifisere dette funnet er det gjennomført et kontrolleksperiment der modellen retreneres uten de to dealer-features. Resultatet bekrefter og forsterker konklusjonen:

**Tabell 9.2: Modellytelse med og uten dealer-features**

| Modell | Features | Accuracy | F1 A | F1 B | F1 C |
|---|---|---|---|---|---|
| Random Forest (full) | 15 | 83,76 % | 0,78 | 0,87 | 0,88 |
| Random Forest (uten dealer-rates) | 13 | **84,42 %** | **0,80** | **0,87** | 0,87 |
| **Endring** | −2 | **+0,66 pp** | **+0,01** | **+0,01** | −0,01 |

Å fjerne de to dealer-features gir altså en **forbedret modell** — accuracy stiger med 0,66 prosentpoeng, klasse A-F1 stiger med 0,01, og klasse C-F1 faller marginalt med 0,01. **Praktisk implikasjon: dealer-features bør fjernes fra produksjonsmodellen**. En alternativ vei er Bayesian smoothing der lokal rate vektes mot global rate proporsjonalt med leverandørens volum, men den enklere løsningen — fjerning — gir det beste resultatet i denne kontrolltesten.

#### 9.4.9 Target leakage som metodisk funn

En gjennomgående metodisk utfordring i dette prosjektet er skillet mellom hva SAP-data brukes til og hva det ikke kan brukes til. SAP fyller to distinkte roller i analysen: som *etikettkilde* og som *potensiell feature-kilde*. Disse rollene er ikke symmetriske.

**Som etikettkilde er SAP uunnværlig.** Målvariabelen — hvilken salgskanal en enhet faktisk gikk til — kan kun observeres i SAP, gjennom artikkelnummertype (2nd-artikkel vs. buy-back), sende-til-kunde (`kunnr`) og selge-til-kunde (`kunag`). Uten SAP finnes det ingen fasit for kanalvalget, og ingen modell kan trenes.

**Som feature-kilde er SAP ubrukbar.** SAP-variabler som salgsinntekt, kostnad og destinasjonsland eksisterer kun etter at salget er gjennomført — etter at kanaliseringsbeslutningen allerede er tatt. Å bruke dem som input til en modell som skal predikere kanalvalget er prinsipielt feil: en ny enhet ved mottakstidspunktet har ingen salgsinntekt, ingen kostnad, og ingen kjent destinasjon ennå. En modell som benytter slike variabler, oppnår kunstig høy nøyaktighet fordi den i praksis leser svaret fra fasiten. Det er nettopp dette som betegnes som target leakage.

I prosjektets tidlige analysefase ble SAP-variabler inkludert som features, noe som ga 92,4 % accuracy. Da lekkasjen ble identifisert og korrigert — og alle features ble begrenset til CellDe-inntaksdata tilgjengelig på mottakstidspunktet — falt accuracy til 83,76 %. Den korrigerte modellen er den eneste som er operasjonelt brukbar.

Denne oppdagelsen styrker metodens troverdighet fremfor å svekke den. At prosjektet identifiserte, dokumenterte og korrigerte lekkasjen — og valgte å rapportere 83,76 % fremfor 92,4 % — er en bevisst metodisk beslutning. Det er 83,76 % som representerer modellens reelle prediktive kraft under betingelsene som faktisk gjelder i drift. Et tilsvarende skille mellom ytelse på historiske data og ytelse på beslutningstidspunktet gjøres ikke alltid eksplisitt i sammenlignbar litteratur (jf. Ibrahim & Abdul-Kader, 2025; Turkolmez et al., 2024), og prosjektets eksplisitte håndtering av dette skillet er dermed et metodisk bidrag i seg selv.

---

### 9.5 Videre forskning

Følgende retninger er særlig relevante for videre arbeid:

**1. Geografisk proxy ved mottak.** Det viktigste enkelttiltaket for å forbedre A/B-nøyaktigheten er å undersøke om geografisk informasjon om enhetens destinasjon er tilgjengelig på eller nær mottakstidspunktet — for eksempel gjennom leverandørkontraktstype eller innkjøpskanal. Dersom en slik proxy finnes, bør den integreres som feature.

**2. Systematisk hyperparametertuning.** En GridSearchCV over sentrale hyperparametere for Random Forest kan gi forbedret ytelse, særlig for den underrepresenterte klasse C.

**3. Validering av lønnsomhetsestimatet med faktiske marginer.** Lønnsomhetsberegningen i avsnitt 8.4 bygger på gjennomsnittsmarginer per klasse beregnet fra SAP-dataene. En ekstern validering mot Modinos faktiske regnskapsdata for de aktuelle enhetene ville gi et langt mer presist anslag på den reelle gevinsten av modellbasert klassifisering.

**4. Cost-sensitive klassifisering.** Den asymmetriske kostnadsstrukturen for klasse C-feil (avsnitt 9.4.7) tilsier at en hyperparameterkonfigurasjon der C-prediksjoner vektes etter faktiske feilkostnader — ikke kun klassefrekvens — kan forbedre nettoeffekten. Dette krever at Modinos faktiske renoveringskostnad per BER-enhet kvantifiseres.

**5. Smoothing av leverandørrater.** En sensitivitetsanalyse av target encoding-stabilitet for leverandører med små volum (avsnitt 9.4.8), eventuelt med Bayesian smoothing mot global gjennomsnittsrate, kan styrke modellens generaliseringsevne for nye eller sjelden brukte leverandører.

**6. Løpende modellvedlikehold (kvartalsvis retrening).** Den temporale valideringen (avsnitt 7.4.1) viser at en modell trent på 2024-data faller fra 83,76 % til 70,43 % accuracy når den brukes på 2025-data — en drift på 13 prosentpoeng over ett år. Dette tilsier at modellen bør retrenes **kvartalsvis**, ikke årlig, for å bevare ytelsen i drift. Dette er i tråd med prinsippet om at beslutningsmodeller i returlogistikk må oppdateres når forutsetningene i verdikjeden endrer seg (Rekdal & Pettersen, 2026).

**7. Utvidelse til andre produktkategorier.** Modino håndterer primært smarttelefoner, men prosessen er i prinsippet lik for nettbrett og annen forbrukerelektronikk. En analyse av om modellen generaliserer til disse kategoriene, eller om separate modeller per kategori gir bedre ytelse, er en naturlig videreføring.

**8. Validering av survivor-bias.** En sammenligning av verdi- og graderingsprofil mellom de 93 575 ferdigsolgte enhetene og de 9 820 ufakturerte (avsnitt 9.4.6) ville avdekke om treningsdataene er skjeve mot raskt-solgte enheter.

**9. Feature pruning verifisert — fjern dealer-features i produksjon.** Kontrolleksperimentet i tabell 9.2 har vist at en modell uten `dealer_A_rate` og `dealer_B_rate` oppnår 84,42 % accuracy mot 83,76 % for 15-feature-modellen, dvs. en marginal forbedring på 0,66 pp samtidig som modellen blir enklere å vedlikeholde og mindre sårbar for nye/sjelden brukte leverandører. En videre reduksjon av feature-settet — eksempelvis gjennom recursive feature elimination eller permutation-basert pruning — bør utforskes i en produksjonsmodell.

---

## 10. Konklusjon

I denne oppgaven har vi undersøkt hvordan en AI-basert klassifiseringsmodell kan forbedre kanaliseringsbeslutninger for brukte mobilenheter hos Modino AS. Problemstillingen ble operasjonalisert gjennom to delproblemer: (1) om en modell kan klassifisere innkommende enheter i de tre kanalklassene A, B og C med tilstrekkelig nøyaktighet, og (2) om korrekt klassifisering kan gi målbar lønnsomhetseffekt.

**Delproblem 1** er besvart positivt. En Random Forest-modell trent utelukkende på CellDe-data fra mottakstidspunktet oppnår **83,76 % accuracy** på testsettet (n = 18 713), med F1-score på 0,78 for klasse A (sluttkunde), 0,87 for klasse B (tredjepartshandler) og 0,88 for klasse C (skrap/BER). Minimumskravet på 80 % er oppfylt med god margin, og resultatet er bekreftet stabilt over stratifisert 5-fold kryssvalidering (83,34 % ± 0,41 %). Modellen opererer uten post-salgsdata som destinasjonsland — en variabel som kun registreres etter at kanalvalget er tatt, og som dermed ikke kan inngå som feature. At modellen likevel oppnår 83,76 % viser at CellDe-dataene inneholder et reelt prediktivt signal. **Et viktig forbehold er imidlertid en temporal drift på 13 prosentpoeng** (avsnitt 7.4.1): modellen trent på 2024 og testet på 2025 oppnår kun 70,43 % accuracy, noe som krever kvartalsvis retrening i drift.

**Delproblem 2** er besvart med et intervallestimat. Realistisk midtestimat — under den nøytrale antakelsen om at halvparten av modellens avvik fra historisk kanalvalg er reelle forbedringer — er omtrent **+110 000 NOK per år** (avgrenset av et optimistisk øvre estimat på ~+225 000 NOK og et pessimistisk nedre estimat på ~−225 000 NOK ved oppskalering til fullt volum). At intervallet inneholder null er det viktigste enkeltresultatet for delproblem 2: lønnsomhetsdimensjonen er ikke det sterkeste argumentet for å implementere modellen, selv om midtestimatet er positivt. Den begrensede nettoeffekten skyldes at modellen gjør nær symmetriske feil mellom klasse A og B. Den primære operative verdien av modellen er derfor **standardisering** — konsistente, datadrevne kanalvalg basert på 93 575 historiske enheter, som adresserer den dokumenterte inkonsistensen i manuell BER-vurdering (Teunter & Flapper, 2011).

**Overordnet konklusjon:** En AI-basert klassifiseringsmodell basert på CellDe-inntaksdata *kan* forbedre kanaliseringsbeslutningene hos Modino AS — både ved å standardisere beslutninger som i dag ikke er systematisk datadrevne, og ved å utnytte mønstre på tvers av et stort historisk datasett. Den viktigste metodiske innsikten er at modellens primære begrensning ligger i A/B-skillet: graderingsdata fra CellDe skiller ikke fullt ut mellom de to kanalene, og ytterligere forbedring krever enten tilleggsdata ved mottakstidspunktet eller dypere integrering med Modinos innkjøpssystem.

Prosjektet bidrar til litteraturen ved å demonstrere en to-kilde-arkitektur (CellDe og SAP som separate filer koblet i minnet) der klassifiseringen er basert på faktisk observert salgskanal — ikke en lønnsomhetsberegning eller en intern gradering. Dette gir en modell med høy intern validitet og direkte operasjonell relevans. Tilnærmingen er prinsipielt overførbar til andre recommerce-aktører med tilsvarende datastruktur.

---

## Referanser

Breiman, L. (2001). Random forests. *Machine Learning*, *45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research*, *16*, 321–357. https://doi.org/10.1613/jair.953

Fawcett, T. (2006). An introduction to ROC analysis. *Pattern Recognition Letters*, *27*(8), 861–874. https://doi.org/10.1016/j.patrec.2005.10.010

Ferguson, M., Guide, V. D. R., Koca, E., & Souza, G. C. (2009). The value of quality grading in remanufacturing. *Production and Operations Management*, *18*(3), 300–314. https://doi.org/10.1111/j.1937-5956.2009.01033.x

Fleischmann, M., Bloemhof-Ruwaard, J. M., Dekker, R., van der Laan, E., van Nunen, J. A. E. E., & Van Wassenhove, L. N. (1997). Quantitative models for reverse logistics: A review. *European Journal of Operational Research*, *103*(1), 1–17. https://doi.org/10.1016/S0377-2217(97)00230-0

Galbreth, M. R., & Blackburn, J. D. (2006). Optimal acquisition and sorting policies for remanufacturing. *Production and Operations Management*, *15*(3), 384–392. https://doi.org/10.1111/j.1937-5956.2006.tb00252.x

Geissdoerfer, M., Savaget, P., Bocken, N. M. P., & Hultink, E. J. (2017). The circular economy – a new sustainability paradigm? *Journal of Cleaner Production*, *143*, 757–768. https://doi.org/10.1016/j.jclepro.2016.12.048

Geyer, R., Van Wassenhove, L. N., & Atasu, A. (2007). The economics of remanufacturing under limited component durability and finite product life cycles. *Management Science*, *53*(1), 88–100. https://doi.org/10.1287/mnsc.1060.0600

Govindan, K., Soleimani, H., & Kannan, D. (2015). Reverse logistics and closed-loop supply chain: A comprehensive review to explore the future. *European Journal of Operational Research*, *240*(3), 603–626. https://doi.org/10.1016/j.ejor.2014.07.012

Guide, V. D. R., & Van Wassenhove, L. N. (2009). The evolution of closed-loop supply chain research. *Operations Research*, *57*(1), 10–18. https://doi.org/10.1287/opre.1080.0628

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning: Data mining, inference, and prediction* (2. utg.). Springer. https://doi.org/10.1007/978-0-387-84858-7

Hübner, A., Kuhn, H., & Wollenburg, J. (2020). Integrated decision-making in reverse logistics: An optimisation of interacting acquisition, grading and disposition processes. *International Journal of Production Research*, *58*(19), 5786–5805. https://doi.org/10.1080/00207543.2019.1659518

Ibrahim, A. A., & Abdul-Kader, W. (2025). A predictive and prescriptive analytics approach for sustainable cellphone return management. *Decision Analytics Journal*, *17*, artikkel 100656. https://doi.org/10.1016/j.dajour.2025.100656

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An introduction to statistical learning with applications in R* (2. utg.). Springer. https://doi.org/10.1007/978-1-0716-1418-1

Kirchherr, J., Reike, D., & Hekkert, M. (2017). Conceptualizing the circular economy: An analysis of 114 definitions. *Resources, Conservation and Recycling*, *127*, 221–232. https://doi.org/10.1016/j.resconrec.2017.09.005

Potting, J., Hekkert, M. P., Worrell, E., & Hanemaaijer, A. (2017). *Circular economy: Measuring innovation in the product chain* (PBL-rapport nr. 2544). PBL Netherlands Environmental Assessment Agency. https://www.pbl.nl/en/publications/circular-economy-measuring-innovation-in-product-chains

Proske, M., Clemm, C., & Scheidt, L. (2018). Does the circular economy grow the pie? The case of rebound effects from smartphone reuse. *Frontiers in Energy Research*, *6*, artikkel 39. https://doi.org/10.3389/fenrg.2018.00039

Quinlan, J. R. (1986). Induction of decision trees. *Machine Learning*, *1*(1), 81–106. https://doi.org/10.1007/BF00116251

Rekdal, P. K., & Pettersen, B. I. A. (2026). *Kvantitative metoder i logistikk*. Høgskolen i Molde. Hentet 30. mai 2026 fra https://kml-site-production.up.railway.app/

Rogers, D. S., & Tibben-Lembke, R. S. (1999). *Going backwards: Reverse logistics trends and practices*. Reverse Logistics Executive Council.

Sokolova, M., & Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. *Information Processing & Management*, *45*(4), 427–437. https://doi.org/10.1016/j.ipm.2009.03.002

Stahel, W. R. (2016). The circular economy. *Nature*, *531*(7595), 435–438. https://doi.org/10.1038/531435a

Strobl, C., Boulesteix, A.-L., Zeileis, A., & Hothorn, T. (2007). Bias in random forest variable importance measures: Illustrations, sources and a solution. *BMC Bioinformatics*, *8*, artikkel 25. https://doi.org/10.1186/1471-2105-8-25

Teunter, R. H., & Flapper, S. D. P. (2011). Optimal core acquisition and remanufacturing policies under uncertain core quality fractions. *European Journal of Operational Research*, *210*(2), 241–248. https://doi.org/10.1016/j.ejor.2010.09.024

Turban, E., Sharda, R., & Delen, D. (2011). *Decision support and business intelligence systems* (9. utg.). Pearson.

Turkolmez, G. B., El Hathat, Z., Subramanian, N., Kuppusamy, S., & Sreedharan, V. R. (2024). Machine learning algorithms for pricing end-of-life remanufactured laptops. *Information Systems Frontiers*. Advance online publication. https://doi.org/10.1007/s10796-024-10515-9

Yin, R. K. (2018). *Case study research and applications: Design and methods* (6. utg.). Sage.

Zheng, A., & Casari, A. (2018). *Feature engineering for machine learning*. O'Reilly Media.

---

## Vedlegg

### Vedlegg A: Hovedpipeline (Python-kode)

Følgende kodeutdrag oppsummerer hovedstegene i analysepipelinen, fra innlasting til evaluering. Full kjørbar kode er tilgjengelig i prosjektets repository.

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. INNLASTING — CellDe (to regneark) og SAP, separate filer
cd24 = pd.read_excel(cellde_path, sheet_name='2024', dtype={'IMEI': str})
cd25 = pd.read_excel(cellde_path, sheet_name='2025', dtype={'IMEI': str})
cellde = pd.concat([cd24, cd25], ignore_index=True) \
            .drop_duplicates(subset='IMEI', keep='first')

sap = pd.read_excel(sap_path, sheet_name='Sheet1',
                    dtype={'imei': str, 'kunag': str, 'kunnr': str})

# 2. IN-MEMORY JOIN (filene lagres aldri sammenslått)
merged = sap.merge(cellde, left_on='imei', right_on='IMEI', how='left')

# 3. KLASSIFISERING — tre-trinns SAP-regel
traders = {'544127', '707086', '995702', '498232', '1533558', '1536986',
           '1550704', '715038', '1530444', '1530472', '1602135', '1602088'}

def classify(row):
    if row['kunnr'] == '1365865':           # Trinn 1: BER
        return 'C'
    if re.fullmatch(r'\d+', str(row['matnr'])):  # Trinn 2: 2nd-artikkel
        return 'A'
    if row['kunag'] in traders:             # Trinn 3: tredjepartshandler
        return 'B'
    return None  # Uklassifisert — ekskluderes

merged['klasse'] = merged.apply(classify, axis=1)
df = merged.dropna(subset=['klasse'])

# 4. FEATURE ENGINEERING — 15 features, alle fra CellDe-mottakstidspunkt
features = ['grade_num', 'device_value', 'model_encoded', 'color_group_enc',
            'Transaction Type_enc', 'Channel_enc', 'Device Category_enc',
            'har_feil', 'fault_count', 'storage_gb', 'inspect_month',
            'inspect_year', 'brand_enc', 'dealer_A_rate', 'dealer_B_rate']

X = df[features]
y = df['klasse']

# 5. STRATIFISERT 80/20-SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42)

# 6. MODELLER — baseline + primær
dt = DecisionTreeClassifier(class_weight='balanced', random_state=42)
dt.fit(X_train, y_train)

rf = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)

# 7. EVALUERING — testsett
print(classification_report(y_test, rf.predict(X_test)))
print(confusion_matrix(y_test, rf.predict(X_test)))

# 8. STRATIFISERT 5-FOLD KRYSSVALIDERING (kap. 7.3.1)
from sklearn.model_selection import cross_val_score, StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_acc = cross_val_score(rf, X_train, y_train, cv=skf, scoring='accuracy')
cv_f1  = cross_val_score(rf, X_train, y_train, cv=skf, scoring='f1_macro')
print(f"CV accuracy: {cv_acc.mean():.3f} ± {cv_acc.std():.3f}")
print(f"CV macro-F1: {cv_f1.mean():.3f} ± {cv_f1.std():.3f}")

# 9. TEMPORAL VALIDERING — tren på 2024, test på 2025 (kap. 7.4.1)
train_2024 = df[df['inspect_year'] == 2024]
test_2025  = df[df['inspect_year'] == 2025]

rf_temporal = RandomForestClassifier(
    n_estimators=100, class_weight='balanced',
    random_state=42, n_jobs=-1
)
rf_temporal.fit(train_2024[features], train_2024['klasse'])
y_pred_2025 = rf_temporal.predict(test_2025[features])
print(classification_report(test_2025['klasse'], y_pred_2025))

# 10. PERMUTATION IMPORTANCE — robust alternativ til Gini (kap. 9.2.2)
from sklearn.inspection import permutation_importance
perm = permutation_importance(rf, X_test, y_test,
                              n_repeats=10, random_state=42, n_jobs=-1)
perm_imp = pd.Series(perm.importances_mean, index=features) \
             .sort_values(ascending=False)
print(perm_imp)
```

### Vedlegg B: Full feature importance — Random Forest

**B.1: Gini-importance (innebygd i scikit-learn)**

| Rang | Feature | Viktighet | Kumulativ |
|---|---|---|---|
| 1 | `device_value` | 18,9 % | 18,9 % |
| 2 | `Device Category_enc` | 15,9 % | 34,8 % |
| 3 | `grade_num` | 13,8 % | 48,6 % |
| 4 | `model_encoded` | 9,2 % | 57,8 % |
| 5 | `inspect_month` | 6,9 % | 64,7 % |
| 6 | `color_group_enc` | 6,7 % | 71,4 % |
| 7 | `dealer_B_rate` | 5,7 % | 77,1 % |
| 8 | `dealer_A_rate` | 5,6 % | 82,7 % |
| 9 | `Transaction Type_enc` | 3,8 % | 86,5 % |
| 10 | `fault_count` | 3,6 % | 90,1 % |
| 11 | `storage_gb` | 2,5 % | 92,6 % |
| 12 | `Channel_enc` | 2,0 % | 94,6 % |
| 13 | `brand_enc` | 1,9 % | 96,5 % |
| 14 | `har_feil` | 1,7 % | 98,2 % |
| 15 | `inspect_year` | 1,7 % | 100,0 % |

**B.2: Permutation importance (mean decrease in accuracy, 5 repetisjoner)**

| Rang | Feature | Importance | Standardavvik |
|---|---|---|---|
| 1 | `Device Category_enc` | 10,96 % | ± 0,23 |
| 2 | `inspect_month` | 6,56 % | ± 0,21 |
| 3 | `model_encoded` | 6,11 % | ± 0,07 |
| 4 | `brand_enc` | 5,51 % | ± 0,08 |
| 5 | `inspect_year` | 3,99 % | ± 0,13 |
| 6 | `device_value` | 3,64 % | ± 0,24 |
| 7 | `grade_num` | 3,26 % | ± 0,08 |
| 8 | `Transaction Type_enc` | 2,51 % | ± 0,12 |
| 9 | `color_group_enc` | 1,04 % | ± 0,10 |
| 10 | `storage_gb` | 0,76 % | ± 0,11 |
| 11 | `har_feil` | 0,68 % | ± 0,10 |
| 12 | `fault_count` | 0,65 % | ± 0,09 |
| 13 | `Channel_enc` | −0,07 % | ± 0,05 |
| 14 | `dealer_B_rate` | **−0,21 %** | ± 0,11 |
| 15 | `dealer_A_rate` | **−0,34 %** | ± 0,09 |

*Negative permutation importance for `dealer_A_rate` og `dealer_B_rate` indikerer at modellen presterer marginalt bedre uten disse features — de er funksjonell støy og bør fjernes i produksjonsmodellen. Se diskusjon i kap. 9.2.2 og 9.4.8.*

### Vedlegg C: Full classification report — Random Forest (testsett, n = 18 713)

|  | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| A — Sluttkunde | 0,775 | 0,793 | 0,784 | 6 928 |
| B — Tredjepartshandler | 0,875 | 0,864 | 0,869 | 11 677 |
| C — Skrap/BER | 0,938 | 0,833 | 0,882 | 108 |
| **Accuracy** | | | **0,8376** | 18 713 |
| **Macro avg** | 0,863 | 0,830 | 0,845 | 18 713 |
| **Weighted avg** | 0,839 | 0,838 | 0,838 | 18 713 |

**Konfusjonsmatrise — Random Forest (testsett)**

| Faktisk \ Predikert | A | B | C |
|---|---|---|---|
| A (n = 6 928) | 5 497 | 1 428 | 3 |
| B (n = 11 677) | 1 587 | 10 087 | 3 |
| C (n = 108) | 7 | 11 | 90 |

**Decision Tree (baseline, testsett)**

|  | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| A — Sluttkunde | 0,729 | 0,736 | 0,732 | 6 928 |
| B — Tredjepartshandler | 0,842 | 0,837 | 0,840 | 11 677 |
| C — Skrap/BER | 0,714 | 0,787 | 0,749 | 108 |
| **Accuracy** | | | **0,7992** | 18 713 |
| **Macro avg** | 0,762 | 0,787 | 0,774 | 18 713 |

**Temporal validering — Random Forest trent på 2024, testet på 2025 (n = 52 252)**

|  | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| A — Sluttkunde | 0,626 | 0,581 | 0,603 | 20 115 |
| B — Tredjepartshandler | 0,747 | 0,783 | 0,765 | 31 898 |
| C — Skrap/BER | 0,925 | 0,565 | 0,701 | 239 |
| **Accuracy** | | | **0,7043** | 52 252 |
| **Macro avg** | 0,766 | 0,643 | 0,690 | 52 252 |

**Kontrolleksperiment 1: RF uten dealer-features (13 features, testsett n = 18 713)**

|  | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| A — Sluttkunde | 0,776 | 0,818 | 0,796 | 6 928 |
| B — Tredjepartshandler | 0,888 | 0,860 | 0,874 | 11 677 |
| C — Skrap/BER | 0,892 | 0,843 | 0,867 | 108 |
| **Accuracy** | | | **0,8442** | 18 713 |
| **Macro avg** | 0,852 | 0,840 | 0,846 | 18 713 |

Konfusjonsmatrise (13-feature RF):

| Faktisk \ Predikert | A | B | C |
|---|---|---|---|
| A (n = 6 928) | 5 667 | 1 253 | 8 |
| B (n = 11 677) | 1 634 | 10 040 | 3 |
| C (n = 108) | 5 | 12 | 91 |

**Kontrolleksperiment 2: Temporal split UTEN `inspect_year` (12 features, test 2025)**

|  | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| A — Sluttkunde | 0,629 | 0,579 | 0,603 | 20 115 |
| B — Tredjepartshandler | 0,747 | 0,787 | 0,766 | 31 898 |
| C — Skrap/BER | 0,929 | 0,603 | 0,731 | 239 |
| **Accuracy** | | | **0,7058** | 52 252 |

Forskjellen fra hovedmodellen med `inspect_year` (70,43 %) er +0,15 pp — driften er strukturell, ikke en feature-artefakt.

### Vedlegg D: Reproduserbarhet

Alle resultater er reproduserbare med:
- Python 3.x med `pandas`, `scikit-learn`, `openpyxl`
- `random_state=42` for alle stokastiske steg (train/test-split, Random Forest)
- Kildefiler `InspectedDeviceREport_cleaned_anon.xlsx` og `Z_BBTI_IMEI_TRACK_cleaned_anon.xlsx`
- Klassifiseringsregler og feature engineering som dokumentert i kapittel 5
