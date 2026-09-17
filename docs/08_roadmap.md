# Kierunek rozwoju aplikacji

Aktualizacja: 2026-09-17. Plan oparty na wynikach projektu; opisuje także funkcje jeszcze niewdrożone. Zastępuje rekomendację z 10.09.2026 zachowaną w Git. Radkowice są pilotem, lokalna aplikacja dokumentacyjna działa, a użytkownik wybrał ocenę przesłanek i ryzyk przed porównywaniem stacji.

## Cel produktu

Aplikacja ma być warsztatem oceny lokalizacji inwestycji. Użytkownik wskazuje lokalizację, parametry i termin projektu, a otrzymuje kartę potencjalnego punktu przyłączenia: infrastrukturę, znane projekty, inwestycje sieciowe, przesłanki, ryzyka i brakujące dowody. Każdy wniosek prowadzi do źródła z datą i zakresem.

Rezultat: użytkownik rozumie, które warianty warto dalej badać oraz jakie informacje mogą zmienić ocenę. Obecne dane nie uzasadniają liczbowego prawdopodobieństwa otrzymania WP ani automatycznej rezerwy MW.

## Dostępna podstawa i wartość dla użytkownika

| Podstawa | Kierunek rozwoju | Granica |
| --- | --- | --- |
| Kompilacja GIS deklarowana jako stan 2024 | Wyszukiwanie stacji, nazwy i aliasy, historia oraz kolejka inwestycji do weryfikacji | Dane historyczne; prawa kompilacji nadal NEED-012; prywatne rekordy pozostają odseparowane |
| Zachowana próbka OSM Radkowic | Mapa infrastruktury, pola, transformatory i kandydaci relacji | Źródło społecznościowe; brak potwierdzonego układu pracy i kompletności |
| Pipeline i dokumenty PSE | Karta znanych projektów przy stacji | Niepełne pokrycie; wiersz dokumentu nie zawsze jest unikalnym projektem |
| Plany inwestycji operatora | Oś czasu i wariant przyszłej sieci | Plan nie jest odbiorem, a termin nie gwarantuje dodatkowych MW |
| Dokumentacja przyłączeniowa użytkownika | Dokładniejsza analiza konkretnego punktu i wspólnej infrastruktury | Osobny tryb prywatny, konieczność rozstrzygnięcia rewizji i sprzeczności |
| Źródła, historia i rejestr potrzeb | Audytowalna opinia oraz lista następnych działań | Ocena jakościowa bez niezweryfikowanych wag i procentów |

## Przebieg pracy użytkownika

1. Wskazanie lokalizacji, technologii, napięcia, eksportu i importu na PCC, MWh oraz terminu.
2. Wybór stacji lub przegląd kandydatów. Odległość geometryczna jest opisana wprost; nie jest długością dopuszczalnej trasy kabla.
3. Karta stacji z rozdziałem napięć i dowodów. Wnioski z części 220 kV Radkowic nie przechodzą automatycznie na część 110 kV.
4. Znane projekty: operacyjne, planowane z określonym statusem, oczekujące wnioski tylko przy dowodzie złożenia i aktualnego stanu. Osobno status nieustalony i pokrycie źródeł. Brak wpisu nie oznacza braku projektu.
5. Scenariusz bieżący lub planowany. Dla BESS osobno ładowanie i rozładowanie; dla hybryd limity PCC zamiast sumowania mocy urządzeń.
6. Opinia: fakty, przesłanki korzystne, ryzyka, sprzeczności i niewiadome. Każde stwierdzenie wskazuje podstawę, znaczenie dla projektu i dowód, który może zmienić ocenę.
7. Eksport z parametrami, wersją metody, snapshotami i listą dokumentów do pozyskania.

## Kolejność rozwoju

| Przyrost | Rezultat | Kryterium ukończenia | Zadania |
| --- | --- | --- | --- |
| 1. Geometria pilota | Mapa Radkowic z elementami OSM i źródłami | ID, CRS, wersje, daty i atrybucja; geometria oddzielona od relacji elektrycznej; przecięcia nie tworzą automatycznie połączeń | KSE-020, KSE-024 |
| 2. Relacje i karta stacji | Obiekty mapy powiązane z dokumentami i znanymi projektami | Stabilne ID i przegląd niejednoznacznych dopasowań; projekty pobliskie oddzielone od przypisanych do stacji | KSE-017, KSE-018, KSE-021 |
| 3. Ocena konkretnego projektu | Wyjaśnione przesłanki dla importu, eksportu i terminu | Wniosek ograniczony do napięcia, daty i zakresu dowodów; bez sztucznego score | KSE-022, KSE-023 |
| 4. Historia i przyszła sieć | Co się zmieniło i które inwestycje mogą mieć znaczenie | Zachowane wersje, wykrywanie zmian i usunięć, jawne statusy planu i odbioru; bez automatycznego przyrostu MW | KSE-025, KSE-027 |
| 5. Porównanie stacji | Zestawienie wariantów z widocznymi brakami | Wspólne definicje, okresy i napięcia; brak danych nie daje przewagi w rankingu | KSE-026, KSE-028 |

Najbliższy zakres to geometria Radkowic. Najpierw wykorzystać zachowaną próbkę do normalizacji geometrii i identyfikatorów, następnie zwiększać obszar przez odpowiednie źródło wyciągów. Nie stosować cyklicznie głównego API OSM ani masowego pobierania kafli mapy. Nie wprowadzać nowej bazy lub frameworka tylko dla pokazania próbki.

## Realistyczne możliwości

| Funkcja | Wykonalność |
| --- | --- |
| Zachowana geometria OSM | AVAILABLE_DIRECTLY w zakresie próbki; widok wymaga implementacji |
| Odległość w linii prostej | CALCULABLE po walidacji współrzędnych i jednostek; nie dowodzi wykonalności trasy |
| Znane projekty z publikacji pilota | AVAILABLE_DIRECTLY w zakresie źródeł; pełna lista konkurencji niedostępna |
| Kandydaci powiązań sieci | ESTIMABLE jako jawne INFERRED po analizie topologii; potwierdzenie wymaga dowodów |
| Zakres planowanej inwestycji | AVAILABLE_DIRECTLY gdy udokumentowany; przyrost MW NOT_CURRENTLY_AVAILABLE |
| Aktualne obciążenie linii i transformatorów | NOT_CURRENTLY_AVAILABLE |
| Wiarygodna rezerwa importu/eksportu i prawdopodobieństwo WP | NOT_CURRENTLY_AVAILABLE na podstawie obecnej próbki |

Dla SN można rozwijać rozpoznanie stacji i otoczenia; relacja feeder–projekt nadal wymaga źródeł. Dla 110 kV geometria wspiera analizę kandydatów powiązań i inwestycji, lecz nie dowodzi wspólnego ograniczenia. Dla 220/400 kV publikacje PSE wspierają analizę dokumentacyjną, ale nie zastępują stanu pracy KSE ani studium przyłączenia.

## Co może dostarczyć użytkownik

Rejestr potrzeb `data/project/information_requests.json` pozostaje źródłem prawdy. Przydatne są aktualny schemat z oznaczeniami pól i granicami własności, jednoznaczna rewizja dokumentacji mostu, potwierdzenia odbioru inwestycji i aktualne publikacje PGE. Nie ponawiamy oczekiwania na niedostępną analizę wpływu. Braki nie blokują mapy dowodów, ale ograniczają wnioski techniczne.

Podstawa: [audyt GIS i OSM](18_gis_osm_integration.md), [działająca aplikacja](17_local_application.md), [wykonalność](02_feasibility_matrix.md), [pipeline GPZ](gpz_pipeline.md). Dokument nie zmienia metodologii scoringu i nie deklaruje wdrożenia nowych funkcji. Jest wejściem kolejnej wersji automatycznego raportu Excel; wcześniejszy Excel pozostaje historycznym snapshotem.
