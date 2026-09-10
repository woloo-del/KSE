# Kierunek architektury po researchu

**10.09.2026 — propozycja do etapu 2, bez instalacji bazy i bez wyboru ostatecznego stosu.**

Na etapie 1 wystarczają lokalne pliki, katalog źródeł i zachowane próbki. Dla przyszłego MVP rekomendowanym punktem wyjścia jest PostgreSQL + PostGIS i relacyjne tabele węzłów, krawędzi, obserwacji oraz dowodów. Rekomendacja wynika z potrzeby historii, spójności danych i analizy przestrzennej; nie jest wynikiem benchmarku baz.

| Wariant | Korzyść dla projektu | Koszt / ograniczenie | Wstępna ocena |
|---|---|---|---|
| PostgreSQL + PostGIS | Jeden magazyn danych domenowych, źródeł, historii i geometrii; graf jako węzły/krawędzie | Złożone przejścia grafowe trzeba świadomie zaprojektować | Preferowany kandydat MVP |
| PostgreSQL + PostGIS + pgRouting | Algorytmy trasowania/analizy grafowej w tym samym środowisku | Kolejne rozszerzenie; koszt grafu nie jest modelem przepływu energii | Dodać tylko dla uzasadnionego zapytania lub warstwy trasowej |
| Neo4j | Naturalna reprezentacja węzłów i relacji z właściwościami | Wymaga oceny obsługi historii, GIS, edycji/licencji i utrzymania | Brak potrzeby wykazanej badaniem danych |
| PostgreSQL/PostGIS + Neo4j | Osobna projekcja do intensywnej eksploracji grafu | Synchronizacja dwóch magazynów, ryzyko niespójności i trudniejszy audyt | Odłożyć do czasu mierzalnej potrzeby |

Źródła techniczne sprawdzono 10.09.2026: [PostGIS — dokumentacja](https://postgis.net/documentation/getting_started/), [Neo4j — model grafowy](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/). Opis pgRouting znaleziono w [oficjalnej dokumentacji](https://docs.pgrouting.org/latest/en/), ale ponowny bezpośredni odczyt zwrócił 403; wersja i warunki konkretnego wdrożenia pozostają do sprawdzenia. Nie wykonano benchmarku ani przeglądu wszystkich warunków licencyjnych baz.

## Przepływ danych do zaprojektowania

```text
Źródło → niezmieniany RAW + manifest
       → parser operatora → STAGING + raport błędów
       → normalizacja jednostek i dat → walidacja
       → obserwacje historyczne + dowody + konflikty
       → rozwiązywanie tożsamości obiektów i relacji
       → graf referencyjny oraz analiza projektu
       → raport faktów, założeń, ryzyk i niewiadomych
```

Operatorowe `fetch/parse/normalize/validate/store` powinny pozostać w `connectors/`. Logika analizy nie pobiera stron. Warstwa GIS ocenia trasę i ograniczenia przestrzenne, a nie obciążenie sieci. Parametry projektu użytkownika nie nadpisują obserwacji operatora. Każdy wynik odwołuje się do snapshotu i wersji metody.

Python jest naturalnym kandydatem dla connectorów; API można później wystawić przez FastAPI. Nie ma jeszcze potrzeby Airflow, Kafki, Kubernetes ani dodatkowego solvera. Wybór biblioteki DataFrame i mapy należy oprzeć na rzeczywistych transformacjach i skali po pilotażu. Nie utworzono frontendowego dashboardu.
