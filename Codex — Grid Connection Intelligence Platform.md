# PROJECT: Grid Connection Intelligence Platform for Renewable Energy & BESS

Chcę wspólnie z Tobą zaprojektować i zbudować lokalnie aplikację do analizy możliwości przyłączenia projektów energetycznych do sieci elektroenergetycznej.

Aplikacja ma przede wszystkim analizować polski system elektroenergetyczny, ale architektura powinna umożliwiać późniejsze rozszerzenie na inne kraje europejskie.

Masz dostęp do folderu projektu na moim komputerze. Możesz tworzyć w nim kod, strukturę projektu, bazę danych, dokumentację, skrypty ETL, aplikację frontend/backend, testy oraz pliki pomocnicze.

Nie zaczynaj jednak od budowania aplikacji.

Projekt ma być realizowany etapowo:

**RESEARCH → DATA DISCOVERY → FEASIBILITY ANALYSIS → DATA MODEL → SYSTEM ARCHITECTURE → MVP → VALIDATION → ITERATIVE DEVELOPMENT**

---

# 1. CEL BIZNESOWY

Chcę stworzyć narzędzie typu:

**Grid Connection Intelligence / Grid Capacity Intelligence Platform**

które pomoże ocenić możliwość przyłączenia nowej inwestycji energetycznej do sieci.

Użytkownik będzie podawał parametry projektu, np.:

- lokalizacja,
- współrzędne geograficzne,
- typ projektu,
- planowany punkt przyłączenia,
- GPZ / stacja elektroenergetyczna,
- linia SN/WN/NN,
- napięcie przyłączenia,
- moc oddawana do sieci,
- moc pobierana z sieci,
- pojemność magazynu energii,
- profil generacji / poboru,
- technologia,
- ewentualnie preferowany OSD/OSP.

Obsługiwane technologie:

- PV,
- BESS,
- elektrownie wiatrowe,
- PV + BESS,
- Wind + BESS,
- PV + Wind + BESS,
- inne hybrydowe źródła energii.

Dla wskazanej lokalizacji aplikacja powinna zebrać wszystkie możliwe informacje dotyczące infrastruktury sieciowej i odpowiedzieć między innymi na pytania:

**1. Do jakiego elementu sieci projekt może potencjalnie zostać przyłączony?**

Np.:

- linia SN,
- GPZ,
- stacja 110 kV,
- stacja 220 kV,
- stacja 400 kV,
- transformator,
- sekcja szyn,
- konkretny węzeł sieciowy.

**2. Jakie inne projekty są już związane z tym elementem sieci?**

W miarę dostępności danych określ:

- istniejące źródła,
- istniejące BESS,
- projekty w budowie,
- projekty posiadające warunki przyłączenia,
- projekty posiadające umowę przyłączeniową,
- projekty planowane,
- duże odbiory energii,
- data center,
- zakłady przemysłowe,
- elektrolizery / hydrogen,
- cable pooling / instalacje hybrydowe.

Dla każdego projektu próbuj ustalić:

- inwestora,
- SPV,
- technologię,
- moc generacji,
- moc poboru,
- lokalizację,
- punkt przyłączenia,
- GPZ / stację,
- linię,
- status,
- datę publikacji informacji,
- źródło informacji,
- confidence score.

**3. Jak bardzo obciążony jest dany element sieci?**

Jeżeli dostępne są dane, analizuj:

- obciążenie transformatorów,
- obciążenie linii,
- przepływy mocy,
- generację,
- pobór,
- ograniczenia napięciowe,
- przeciążenia,
- redispatching,
- curtailment,
- ograniczenia generacji,
- congestion,
- dostępne moce,
- historyczne maksima/minima obciążenia,
- kierunek przepływu energii.

Jeżeli operator nie publikuje bezpośrednio informacji o wykorzystaniu elementu sieci, sprawdź, czy możliwe jest jego **oszacowanie pośrednie**.

Wyraźnie rozróżniaj:

**measured**
**reported**
**calculated**
**estimated**
**inferred**

Nie przedstawiaj estymacji jako danych operatora.

---

# 2. NAJWAŻNIEJSZY OUTPUT APLIKACJI

Docelowo użytkownik powinien otrzymać raport dla wskazanego projektu.

Przykład:

PROJECT:
BESS 50 MW / 200 MWh

LOCATION:
X / Y

PROPOSED CONNECTION:
GPZ / SE XXXXX

GRID NODE:
110 kV

EXISTING GENERATION:
72 MW

KNOWN CONNECTION CONDITIONS:
135 MW

KNOWN NEW DEMAND:
20 MW

BESS PIPELINE:
80 MW

KNOWN TOTAL PIPELINE:
235 MW

TRANSFORMER CAPACITY:
2 × 63 MVA

ESTIMATED AVAILABLE CAPACITY:
20–40 MW

GRID CONGESTION:
HIGH

DATA CONFIDENCE:
76%

GRID CONNECTION SCORE:
42 / 100

ESTIMATED CONNECTION PROBABILITY:
LOW / MEDIUM

MAIN CONSTRAINT:
110/15 kV transformer capacity

POSSIBLE ALTERNATIVE:
SE XXXXX 110 kV – approximately 9 km

SUGGESTED NEXT ACTION:
analyse 110 kV connection instead of GPZ connection.

Oczywiście jest to tylko przykład.

Model scoringowy musi zostać opracowany na podstawie rzeczywiście dostępnych danych.

---

# 3. RESEARCH — ETAP OBOWIĄZKOWY

Zanim napiszesz kod aplikacji, wykonaj szeroki research źródeł danych.

Nie ograniczaj się do listy, którą podaję poniżej.

Szukaj również:

- open data,
- GIS,
- WMS,
- WFS,
- WMTS,
- REST API,
- public API,
- CSV,
- XLSX,
- JSON,
- XML,
- HTML,
- PDF,
- BIP,
- publicznych rejestrów,
- map infrastruktury,
- raportów operatorów,
- planów rozwoju sieci,
- dokumentów inwestycyjnych,
- danych przestrzennych,
- repozytoriów GitHub,
- istniejących bibliotek Python,
- istniejących projektów open-source.

W Polsce przeanalizuj co najmniej:

PSE S.A.

oraz wszystkich głównych OSD:

- PGE Dystrybucja,
- ENEA Operator,
- TAURON Dystrybucja,
- Energa-Operator,
- Stoen Operator.

Sprawdź również innych operatorów i operatorów lokalnych, jeśli publikują wartościowe dane.

Przeanalizuj między innymi:

- mapy sieci,
- wykazy stacji,
- wykazy GPZ,
- dane o liniach,
- napięcia,
- moce transformatorów,
- plany rozwoju,
- inwestycje sieciowe,
- dostępne moce przyłączeniowe,
- informacje o odmowach przyłączenia,
- warunki przyłączenia publikowane publicznie,
- listy projektów,
- dane o ograniczeniach generacji,
- redysponowanie,
- dane rynku energii,
- dane operacyjne systemu.

---

# 4. ŹRÓDŁA EUROPEJSKIE

Sprawdź również, czy przydatne będą źródła paneuropejskie, np.:

- ENTSO-E Transparency Platform,
- ENTSO-E Grid Map,
- OpenStreetMap / OpenInfraMap,
- Ember,
- Energy Charts,
- JRC,
- Copernicus,
- Open Power System Data,
- PyPSA,
- pandapower,
- GridCal,
- MATPOWER,
- PowerModels,
- inne istniejące open-source grid models.

Nie zakładaj, że którekolwiek z powyższych źródeł jest odpowiednie.

Zweryfikuj:

- aktualność,
- licencję,
- dokładność,
- zakres geograficzny,
- możliwość automatycznego pobierania danych,
- częstotliwość aktualizacji,
- ograniczenia API,
- możliwość komercyjnego wykorzystania.

---

# 5. DANE NIEENERGETYCZNE

Aplikacja powinna również móc integrować dane przestrzenne przydatne przy wyborze punktu przyłączenia.

Przeanalizuj dostępność między innymi:

- działek ewidencyjnych,
- EGIB,
- BDOT10k,
- ortofotomapy,
- NMT/DEM,
- MPZP,
- studiów / planów ogólnych,
- form ochrony przyrody,
- Natura 2000,
- lasów,
- terenów zalewowych,
- dróg,
- kolei,
- infrastruktury technicznej.

Docelowo może to pozwolić na ocenę:

**czy alternatywny punkt przyłączenia jest technicznie i przestrzennie osiągalny.**

---

# 6. DISCOVERY DANYCH

Dla każdego znalezionego źródła utwórz rejestr danych.

Minimum:

SOURCE_ID  
Operator  
Source name  
URL  
Data owner  
Country  
Data category  
Grid voltage  
Geographical scope  
Data format  
API available  
GIS service available  
Update frequency  
Historical data available  
Authentication required  
License  
Commercial use  
Reliability  
Machine readable  
Scraping required  
Key fields  
Potential application  
Known limitations  
Data quality score  
Priority

Zapisz rejestr w repozytorium projektu.

Preferowany format:

`/docs/data_sources.md`

oraz w formacie strukturalnym:

`/data/catalog/data_sources.csv`

lub:

`data_sources.json`.

---

# 7. FEASIBILITY MATRIX

Po researchu przygotuj:

`/docs/feasibility_matrix.md`

Dla każdego planowanego modułu określ:

**AVAILABLE DIRECTLY**

jeżeli istnieją wiarygodne dane źródłowe,

**CALCULABLE**

jeżeli wartość można wyliczyć,

**ESTIMABLE**

jeżeli można stworzyć uzasadniony model estymacyjny,

**NOT CURRENTLY AVAILABLE**

jeżeli brak wystarczających danych.

Przykładowe moduły:

- liczba projektów na GPZ,
- moc projektów na GPZ,
- moc istniejących źródeł,
- pipeline projektów,
- wolna moc GPZ,
- moc transformatorów,
- rzeczywiste obciążenie transformatora,
- obciążenie linii 110 kV,
- congestion,
- zdolność eksportowa,
- zdolność importowa,
- możliwość przyłączenia BESS,
- prawdopodobieństwo otrzymania WP.

To ma zapobiec budowaniu funkcjonalności bazujących na danych, których w rzeczywistości nie można pozyskać.

---

# 8. MODEL SIECIOWY

Chcę, żeby aplikacja docelowo zbudowała graf sieci.

Rozważ model:

NODE:
substation / GPZ / switching station

EDGE:
transmission / distribution line

TRANSFORMER:
connection between voltage levels

PROJECT:
generation / storage / demand

Przykład:

SE 400/220 kV
↓
220 kV
↓
SE 220/110 kV
↓
110 kV line
↓
GPZ 110/15 kV
↓
15 kV feeder
↓
PV/BESS

Każdy element powinien posiadać własne parametry techniczne i odniesienie do źródła danych.

Przeanalizuj zastosowanie grafowej bazy danych, ale nie wybieraj jej automatycznie.

Porównaj np.:

PostgreSQL + PostGIS

vs

PostgreSQL + pgRouting

vs

Neo4j

vs rozwiązanie hybrydowe.

Preferuj rozwiązanie możliwie proste operacyjnie dla MVP.

---

# 9. GRID CAPACITY ENGINE

Kluczowym modułem aplikacji będzie silnik oceniający możliwość przyłączenia.

Nie chcę prostego:

installed capacity < transformer capacity

Model powinien w przyszłości uwzględniać co najmniej:

- napięcie,
- poziom sieci,
- transformację,
- thermal capacity,
- generation,
- demand,
- simultaneous generation,
- BESS charging,
- BESS discharging,
- project pipeline,
- connection conditions,
- contracted capacity,
- N-1,
- reverse power flow,
- congestion,
- planned grid reinforcements,
- curtailment,
- redispatching,
- historical loading,
- topology.

Jeżeli danych jest za mało do dokładnego power-flow, przygotuj model heurystyczny.

Każdy wynik powinien posiadać:

`confidence score`

oraz informację:

**dlaczego model doszedł do takiego wyniku.**

---

# 10. BESS

Magazyny energii traktuj osobno od źródeł generacyjnych.

BESS posiada dwa niezależne parametry:

`P_export`

oraz

`P_import`.

Przykład:

BESS:

50 MW export  
50 MW import  
200 MWh

Nie można automatycznie zakładać, że wpływ BESS na sieć odpowiada elektrowni PV 50 MW.

Model powinien analizować dwa scenariusze:

**DISCHARGE / GENERATION**

oraz

**CHARGE / DEMAND**

i odpowiednio oceniać dostępność sieci.

---

# 11. HYBRID / CABLE POOLING

Architektura musi umożliwiać modelowanie:

PV + BESS

Wind + BESS

PV + Wind + BESS

oraz cable pooling.

Rozróżnij:

installed capacity

od:

maximum power at PCC.

Przykład:

PV 30 MW  
BESS 30 MW  
PCC limit 30 MW

nie powinien automatycznie oznaczać:

60 MW injection.

---

# 12. PLANOWANE INWESTYCJE SIECIOWE

Jest to bardzo ważny moduł.

Aplikacja powinna zbierać inwestycje operatorów, takie jak:

- nowe GPZ,
- nowe stacje,
- nowe transformatory,
- modernizacje,
- zwiększenie mocy transformacji,
- przebudowa linii,
- nowe linie 110 kV,
- 220 kV,
- 400 kV.

Dzięki temu aplikacja powinna pokazywać:

CURRENT GRID CAPACITY

oraz potencjalnie:

FUTURE GRID CAPACITY

np.:

2026  
2028  
2030  
2035.

---

# 13. HISTORIA DANYCH

Nigdy nie nadpisuj bezpowrotnie danych operatora.

Buduj model historyczny.

Powinniśmy móc odpowiedzieć:

„Jak wyglądała sytuacja na tej stacji trzy miesiące temu?”

Przechowuj minimum:

`source_date`

`retrieval_date`

`valid_from`

`valid_to`

`source_version`

jeżeli są dostępne.

---

# 14. ETL / DATA PIPELINE

Każdy operator może publikować dane inaczej.

Zaprojektuj modularną warstwę:

`connectors`

np.:

connectors/
    pse/
    pge/
    enea/
    tauron/
    energa/
    stoen/
    entsoe/
    gis/

Każdy connector powinien mieć:

fetch  
parse  
normalize  
validate  
store

Nie mieszaj kodu odpowiedzialnego za pobieranie danych z logiką biznesową aplikacji.

---

# 15. DATA PROVENANCE

Każda istotna wartość prezentowana użytkownikowi powinna posiadać źródło.

Przykład:

Transformer capacity: 63 MVA

Source:
PGE Dystrybucja

Document:
Plan Rozwoju 2026–2031

Page:
72

Retrieved:
2026-09-10

Jeżeli wartość jest wyliczona:

Calculated value

Inputs:
A
B
C

Formula:
...

Jeżeli estymowana:

Estimated value

Method:
...

Confidence:
...

---

# 16. MAPA

Centralnym elementem UI powinna być mapa.

Powinna docelowo prezentować:

- sieć elektroenergetyczną,
- GPZ,
- stacje PSE,
- linie SN,
- linie WN,
- linie NN,
- transformatory,
- projekty PV,
- BESS,
- Wind,
- odbiorców,
- pipeline projektów,
- planowane inwestycje operatorów.

Użytkownik powinien móc kliknąć GPZ i zobaczyć:

technical parameters

connected assets

known projects

known connection conditions

estimated loading

available capacity

planned upgrades

grid connection score.

---

# 17. PROPONOWANA ARCHITEKTURA

Nie traktuj tego jako narzuconej technologii.

Po researchu zaproponuj najlepszy stack.

Preferowane technologie do rozważenia:

Backend:
Python

API:
FastAPI

Data processing:
Pandas / Polars / GeoPandas

Database:
PostgreSQL + PostGIS

Grid calculation:
pandapower / PyPSA / inne

Frontend:
React / Next.js

Maps:
MapLibre / Leaflet

ETL:
Python

Containerisation:
Docker

Ale możesz zaproponować inne technologie, jeśli będą lepsze.

---

# 18. ARCHITEKTURA MODUŁOWA

Preferuję strukturę umożliwiającą dalszy rozwój, np.:

/app
/backend
/frontend
/connectors
/data
/database
/grid_engine
/scoring
/gis
/tests
/docs
/scripts
/config

Nie twórz monolitycznego skryptu.

---

# 19. AUTOMATYCZNA AKTUALIZACJA

Docelowo system powinien regularnie sprawdzać:

PSE  
OSD  
BIP  
API  
GIS  
plany rozwoju  
inne źródła.

Zmiany danych powinny być wykrywane automatycznie.

Przykład:

NEW PROJECT DETECTED

BESS

50 MW

GPZ XXXXX

Investor:
XXXXX

Source:
BIP

Publication date:
XXXXX

Impact:
Potential reduction of available export capacity.

Nie implementuj wszystkiego na początku, ale architektura musi umożliwiać taki rozwój.

---

# 20. DATA QUALITY

Dane pochodzące z różnych źródeł mogą być sprzeczne.

Zaprojektuj system oceny jakości danych.

Przykładowe poziomy:

A — operator / official API

B — official public document

C — official BIP / administrative document

D — company publication

E — media

F — inferred / estimated

Każdy rekord może posiadać:

`source_quality`

`confidence`

`last_verified`.

---

# 21. ENTITY RESOLUTION

Ten sam obiekt może mieć różne nazwy.

Przykład:

GPZ Radkowice

SE Radkowice

Stacja Radkowice 110 kV

RADKOWICE

System musi rozpoznawać, że może chodzić o ten sam obiekt.

Zaprojektuj system:

canonical ID

aliases

operator ID

geographical matching

fuzzy matching.

To samo dotyczy:

projektów,

SPV,

inwestorów,

linii,

stacji.

---

# 22. TESTOWANIE

Każdy parser danych powinien posiadać testy.

Nie chcę sytuacji, w której zmiana strony operatora powoduje zapis błędnych danych bez ostrzeżenia.

Wprowadź:

schema validation

range validation

unit validation

duplicate detection

geographical validation

historical consistency checks.

---

# 23. WAŻNA ZASADA

Nie buduj „ładnego dashboardu” na niezweryfikowanych danych.

Priorytety projektu są następujące:

DATA QUALITY  
↓  
GRID MODEL  
↓  
ANALYTICS  
↓  
SCORING  
↓  
UI

---

# 24. ETAP 1 — TWOJE PIERWSZE ZADANIE

Nie twórz jeszcze produkcyjnej aplikacji.

Najpierw wykonaj dokładny research i przygotuj dokument:

`/docs/01_data_research.md`

Dokument powinien odpowiedzieć:

1. Jakie dane są publicznie dostępne?
2. Którzy operatorzy publikują najlepsze dane?
3. Jak można je automatycznie pobierać?
4. Jakie istnieją API?
5. Jakie istnieją WMS/WFS/REST GIS?
6. Jakie dane trzeba pobierać z dokumentów PDF/XLSX?
7. Jakie dane wymagają web scrapingu?
8. Jakie istnieją open-source grid datasets?
9. Czy istnieje możliwy do wykorzystania model topologii polskiej sieci?
10. Czy możliwe jest odtworzenie relacji:
   project → feeder → GPZ → 110 kV → SE PSE?
11. Czy można określić obciążenie poszczególnych elementów?
12. Czy można estymować wolną moc?
13. Jak dokładnie można robić to dla:
   - SN,
   - 110 kV,
   - 220 kV,
   - 400 kV?
14. Jakie są największe braki danych?
15. Które dane można uzupełnić metodami inferencyjnymi?
16. Jakie biblioteki i projekty open-source mogą być wykorzystane?
17. Jakie ograniczenia licencyjne występują?
18. Jak często dane mogą być aktualizowane?

Każde źródło musi posiadać link i datę weryfikacji.

---

# 25. ETAP 2 — FEASIBILITY

Następnie utwórz:

`/docs/02_feasibility_matrix.md`

oraz:

`/docs/03_system_architecture.md`

Przedstaw również rekomendację:

**MVP**

**V1**

**V2**

**LONG-TERM**

Nie zakładaj, że wszystkie funkcjonalności są możliwe.

Powiedz wprost, czego nie da się wiarygodnie zrobić na podstawie dostępnych danych.

---

# 26. ETAP 3 — PROOF OF CONCEPT

Dopiero po wykonaniu researchu wybierz jeden obszar Polski i spróbuj stworzyć pierwszy rzeczywisty model.

Preferowany test:

jedna stacja / GPZ

+

sieć 110 kV wokół niej

+

znane źródła

+

znane projekty

+

planowane inwestycje.

Spróbuj zbudować:

NODE → LINE → SUBSTATION → PROJECT

oraz policzyć pierwszy uproszczony:

GRID CAPACITY SCORE.

---

# 27. GRID CONNECTION SCORE

Docelowo chcę stworzyć autorski wskaźnik:

**Grid Connection Score 0–100**

Nie definiuj jeszcze arbitralnie jego wag.

Podczas researchu określ, jakie zmienne rzeczywiście możemy pozyskać.

Potencjalne czynniki:

available capacity

known pipeline

transformer utilisation

line utilisation

generation concentration

demand

network topology

planned reinforcements

voltage level

distance to connection point

BESS flexibility

curtailment

redispatching

connection refusals

connection conditions

operator investment plans

data confidence.

Wynik zawsze musi być explainable.

---

# 28. SCENARIUSZE

Dla projektu analizuj co najmniej:

BASE CASE

CURRENT GRID

FUTURE GRID

CONSERVATIVE

OPTIMISTIC.

Dla BESS dodatkowo:

CHARGING

DISCHARGING.

---

# 29. NIEPEWNOŚĆ

To bardzo ważne.

Nigdy nie przedstawiaj szacunkowej dostępnej mocy jako pewnej informacji.

Przykład:

Estimated available connection capacity:

35–60 MW

Confidence:

MEDIUM — 67%

Reasons:

transformer capacity known

existing generation known

connection pipeline partially known

real-time transformer loading unavailable.

---

# 30. DOKUMENTACJA

Prowadź dokumentację projektu równolegle z kodem.

Minimum:

README.md

/docs/01_data_research.md

/docs/02_feasibility_matrix.md

/docs/03_system_architecture.md

/docs/04_data_model.md

/docs/05_grid_capacity_methodology.md

/docs/06_scoring_methodology.md

/docs/07_data_quality.md

/docs/08_roadmap.md

---

# 31. CHANGELOG / DECISION LOG

Twórz:

`/docs/decision_log.md`

Każda ważna decyzja technologiczna powinna zawierać:

Decision

Options considered

Selected option

Reason

Trade-offs

Date.

---

# 32. ZASADY WSPÓŁPRACY

Pracujemy iteracyjnie.

Możesz samodzielnie:

- analizować repozytorium,
- tworzyć pliki,
- tworzyć kod,
- wykonywać skrypty,
- instalować zależności projektowe,
- uruchamiać testy,
- refaktoryzować kod.

Nie zmieniaj jednak fundamentalnych założeń biznesowych bez ich udokumentowania.

Jeżeli napotkasz problem, najpierw spróbuj go samodzielnie rozwiązać.

Nie pytaj mnie o decyzje dotyczące drobnych kwestii implementacyjnych.

Pytaj mnie przede wszystkim wtedy, kiedy decyzja wpływa na:

- zakres produktu,
- logikę biznesową,
- interpretację danych energetycznych,
- Grid Connection Score,
- architekturę mającą istotne konsekwencje dla dalszego rozwoju.

---

# 33. KRYTERIUM SUKCESU

Końcowym celem nie jest aplikacja pokazująca mapę sieci.

Końcowym celem jest system, który dla lokalizacji i parametrów projektu energetycznego potrafi powiedzieć:

**„Jak wygląda sytuacja sieciowa w tym miejscu, jakie projekty konkurują o tę samą infrastrukturę, jakie są potencjalne ograniczenia i jak duże jest prawdopodobieństwo uzyskania możliwości przyłączenia?”**

Odpowiedź musi być oparta na danych, transparentna, audytowalna i posiadać określony poziom niepewności.

---

# START

Rozpocznij od ETAPU 1.

Najpierw:

1. przejrzyj strukturę folderu projektu,
2. przygotuj strukturę repozytorium,
3. rozpocznij research dostępnych źródeł danych,
4. nie buduj jeszcze frontendowej aplikacji,
5. nie twórz fikcyjnych danych,
6. zapisuj link do każdego źródła,
7. zapisuj datę jego weryfikacji,
8. rozróżniaj dane oficjalne, obliczone i estymowane,
9. zweryfikuj możliwość legalnej i technicznej automatyzacji pobierania danych,
10. po zakończeniu researchu przedstaw mi executive summary.

Na końcu pierwszego etapu chcę otrzymać przede wszystkim odpowiedź:

**Czy da się zbudować wiarygodny Grid Connection Intelligence System dla Polski na podstawie obecnie dostępnych danych i jaki poziom dokładności możemy realistycznie osiągnąć dla SN, 110 kV oraz sieci PSE 220/400 kV?**

Dopiero na podstawie tej odpowiedzi zdecydujemy o implementacji MVP.