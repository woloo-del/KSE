# Lokalna aplikacja pilotażowa — Radkowice

Stan: 2026-09-16. Użytkownik zatwierdził rozpoczęcie aplikacji z oceną przesłanek i ryzyk; porównanie stacji pozostaje późniejszym etapem.

## Uruchomienie

W PowerShell, z folderu projektu:

```powershell
./scripts/start_local_app.ps1
```

Otwórz http://127.0.0.1:8787. Zatrzymanie: Ctrl+C w terminalu serwera. Skrypt wybiera Python z `.venv`, lokalnego środowiska Codex lub PATH; można wskazać `-PythonPath` i `-Port`. Aplikacja korzysta wyłącznie z biblioteki standardowej Pythona i lokalnych plików HTML/CSS/JS. Nie wymaga instalowania pakietów. Serwer nasłuchuje wyłącznie na 127.0.0.1. Nie należy udostępniać go jako serwera produkcyjnego.

## Zakres

- Przegląd Radkowic i formularz technologii, napięcia 110/220 kV, maksymalnych mocy importu/eksportu na PCC oraz pojemności BESS.
- Trzy zachowane wpisy PSE ze stanem na 31.07.2026, wyszukiwanie, statusy, daty i pochodzenie wartości.
- Graf dokumentacyjny 13 obiektów z relacjami i dowodami; nie jest schematem ruchowym ani mapą geograficzną.
- Wybrane źródła i 11 potrzeb informacyjnych z dalszym działaniem.
- Opinia z uzasadnieniem, osobnymi kierunkami przepływu oraz eksportem JSON.

## Interpretacja opinii

Metoda `documentary_screening_v1` jest jakościowym przeglądem dowodów. Dostępna moc, score i prawdopodobieństwo pozostają nieustalone. Zmiana zadanych MW nie uruchamia obliczeń rozpływowych. Technologia i MWh są zapisywane jako kontekst; nie mamy profili pracy ani modelu wykorzystującego pojemność do oceny ograniczeń. Dodatnia moc w każdym kierunku wymaga potwierdzenia operatora. Zero różni się od braku wartości.

Wpisy umów 220 kV stanowią punkt odniesienia, a nie dowód rezerwy dla nowego projektu. Ocena 110 kV nie przypisuje tych umów do części PGE. Brak wpisów operacyjnych/oczekujących w próbce nie jest zerową liczbą takich projektów. Sumy mocy są sumami wierszy zachowanej publikacji, nie obciążeniem stacji ani zajętością mostu.

## Dane, prywatność i odtwarzalność

Backend czyta jawną listę czterech plików: widok pipeline v1, graf v2, rejestr potrzeb i katalog źródeł. Nie udostępnia katalogów repozytorium, `_secrets` ani prywatnych warunków przyłączenia. Parametry formularza pozostają w pamięci sesji; odświeżenie usuwa je. Eksport zawiera parametry, datę UTC, wersję i hash metody oraz dokładny zestaw dowodów użytych podczas oceny z hashami plików wejściowych. Nie zawiera oryginalnych PDF/XLSX; ich odtworzenie wymaga zachowanego archiwum źródeł.

Zmiana formularza unieważnia poprzednią opinię. Źródła mają własne daty; uruchomienie aplikacji nie pobiera nowych danych operatorów. Linki zewnętrzne otwierają się dopiero po wybraniu przez użytkownika.

## Walidacja i dalszy rozwój

Testy `tests/test_local_app.py` sprawdzają niezależność kierunków, brak przenoszenia wniosków 220→110 kV, walidację formularza, wersjonowanie wyniku i brak dostępu do dowolnych plików. W przeglądarce sprawdzono formularz oraz zmianę poziomu napięcia. Automatyczne potwierdzenie zdarzenia pobrania JSON w przeglądarce Codex nie powiodło się; dostępny jest też tekst raportu do ręcznego zapisania.

To ograniczony pilot, nie zamknięcie zadania pełnego MVP. Następne kroki: uzupełnienie źródeł PGE, test użytkownika, lepsza prezentacja relacji, następnie mapa na zweryfikowanych współrzędnych. Docelowa architektura PostgreSQL/PostGIS i API pozostaje rekomendacją; obecny adapter można zastąpić bez przenoszenia metody analitycznej do UI.


### Uzupełnienie 17.09.2026

Ocena `documentary_screening_v2` korzysta także z piątego jawnie wskazanego snapshotu: przeglądu dat inwestycji PSE. Pokazuje rozbieżność roku lub zakresu wraz z dwoma źródłami, bez wyboru daty odbioru lub dodatkowej mocy. Eksport zapisuje przegląd i jego hash. Wcześniejsze wyniki v1 pozostają historyczne; nie są nadpisywane. Nie dodano prywatnych dokumentów do API.

Sprawdzono działającą aplikację w przeglądarce: scenariusz testowy BESS 50 MW eksportu i 20 MW importu pokazuje nową rozbieżność oraz oba źródła, zachowując niezależne kierunki i nieznaną rezerwę. Są to parametry testu interfejsu, nie nowy rekord inwestycji.


## 17.09.2026 — inwestycje sieciowe

Dodano zakładkę z dwoma zweryfikowanymi wpisami projektu PRSP po konsultacjach. Widok rozróżnia plan i realizację deklarowaną w dokumencie, pokazuje strony, identyfikatory, datę odczytu i hash. Zakończenie formalne/finansowe/techniczne nie jest datą załączenia; dostępne MW pozostają nieustalone. API i eksport oceny zachowują szósty snapshot `development_plan`. Metoda opinii documentary_screening_v2 nie zmienia reguł ani wag; nowy dokument jest dodatkowym materiałem do oceny użytkownika. Potwierdzono w przeglądarce oba horyzonty, oznaczenie projektu oraz rozwijany dowód i odnośnik. Test API sprawdza zawartość eksportu; nie testowano ponownie samego mechanizmu pobrania pliku przez przeglądarkę.

## 17.09.2026 — interaktywna koncepcja wizualna

Na prośbę użytkownika przygotowano `docs/prototypes/platform-concept.html`: jasna matowa paleta, mapa rzeczywistej geometrii OSM pilota, zakładki projektów, inwestycji i dowodów. To oddzielna koncepcja, nie zmiana działającej aplikacji ani metodologii. Parametry BESS są demonstracyjne; import/eksport niezależne. Widok jakościowej opinii reaguje na wejścia, ale nie oblicza mocy lub prawdopodobieństwa. Nie czyta prywatnych źródeł.

Odtworzenie danych osadzonych: `.venv/Scripts/python.exe scripts/build_platform_concept.py`. Potrzebne publiczne snapshoty OSM i pipeline. Hash OSM jest sprawdzany; hashe obu wejść zapisane w fragmencie. Projekcja D3 7.9.0, ODbL i atrybucja OSM. Przeglądarka wymaga dostępu do biblioteki D3 z CDN; dane nie są pobierane na żywo.

Sprawdzono podgląd przy 1024 i 360 px, przełączanie napięcia, zachowanie niezależnych mocy (import 75 MW / eksport 50 MW), scenariusz planów, tabelę projektów i wybór transformatora. Nie testowano hostowych wariantów palety Tweak; są opcjonalne. Koncepcja nie wdraża krajowej mapy ani automatycznego pozyskiwania danych.

## Rejestr dowodów — 18.09.2026

Siódma zakładka pozwala przeszukiwać publiczny rejestr i filtrować rodzaje wpisów. Szczegóły zawierają źródło, daty, lokalizator i zachowany rekord. `evidence_links` w API oraz eksporcie rozróżnia ten sam rekord publikacji od nierozstrzygniętej tożsamości; szczegóły w docs/20_station_data_aggregation.md. Backend po aktualizacji wymaga restartu.

## Etapy modernizacji w aplikacji — 18.09.2026

Zakładka Inwestycje sieciowe prezentuje oddzielnie dwa etapy opisane w portalu PSE i dwa zadania projektu PRSP. Brak mapowania do II.47 jest widoczny przed listą. Status portalu pozostaje raportowany, z nieznaną datą stanu i jawną datą pobrania; nie zastępuje statusu zadania PRSP. Nie liczymy tych czterech wpisów jako czterech inwestycji.

`investment_stages` jest ósmym jawnym wejściem API i częścią `evidence_snapshot` w eksporcie JSON. Lista źródeł zawiera PSE_RADK_STAGES. Historyczny rejestr 76 dowodów nie jest nadpisywany ani automatycznie rozszerzany. Test API sprawdza zachowanie statusów, brak ID zadania i daty stanu oraz obecność źródła w eksporcie. W przeglądarce potwierdzono wyświetlenie obu etapów, ograniczeń i harmonogramów.


## Przegląd profili PSE — 18.09.2026

Widok `/profiles` i API `/api/profiles` udostępniają 50 profili źródłowych obok pilota Radkowic. Używają trzech jawnych publicznych snapshotów; nie pobierają prywatnego GIS. Zgodność hashów między indeksami jest sprawdzana przed podaniem wyniku; niespójny zestaw zwraca błąd. Widok zachowuje niepotwierdzoną tożsamość i statusy projektów. Skrypty oraz style są osobnymi zasobami zgodnymi z dotychczasowym CSP. To aktualizacja lokalnej aplikacji; wcześniej opublikowany plik Sites pozostaje bez zmian.


## 07.10.2026 — notatka i karta przeglądu profilu

Widok `/profiles` udostępnia pole notatki, jawny zapis lokalny, podgląd karty i eksport Markdown/JSON. Notatki mają osobne klucze stabilnego ID profilu (w tym poziomu napięcia), nie indeksu listy. Szkice przechowywane w pamięci strony nie znikają przy zmianie wyboru. Zapis localStorage dotyczy konkretnej przeglądarki i origin (zmiana portu daje inny magazyn); nie jest kopią zapasową. Aplikacja sygnalizuje błąd odczytu/zapisu, nie twierdzi wtedy, że notatka została zapisana. Niezapisane szkice wywołują ostrzeżenie przy opuszczaniu strony, jeśli przeglądarka je obsługuje.

Eksport `profile_review_v1` zachowuje wybrany profil, statystyki wierszy wykazu, wszystkie powiązane nagłówki inwestycji, źródłowe daty i hashe wejść, niewiadome oraz osobno USER_INPUT_NOT_SOURCE_EVIDENCE. Nie eksportuje cudzych notatek ani prywatnego GIS. Raport nie jest pełną listą projektów: na tym etapie karta korzysta ze statystyk profilu. Brak projektów operacyjnych i oczekujących pozostaje UNKNOWN. Nie oblicza MW ani score. Własna notatka nigdy nie jest interpretacją operatora.

Testy: 10 testów Python kontraktu i API oraz 4 testy Node eksportu/notatek. W przeglądarce sprawdzono szkic po przełączeniu profilu, zapis i odtworzenie po reload, podgląd karty z notatką. Kliknięcie pobrania wywołuje komunikat, ale zdarzenia zapisu pliku narzędzie nie potwierdziło; nie uznajemy pełnego pobrania za zweryfikowane. Dostępny tekst podglądu do ręcznego skopiowania. Nie testowano ponownie wariantu mobilnego.

Uruchomiona sesja rozwojowa: http://127.0.0.1:8790/profiles. Standardowy launcher nadal pozwala wybrać port (`-Port 8790`). Strona Sites nie została zmieniona.


## Projekty i inwestorzy — 07.10.2026

Zakładka „Projekty i inwestorzy” pokazuje 282 wiersze zachowanego wykazu PSE przypisane do 50 profili źródłowych. Filtry rozdzielają wydane warunki, obowiązujące umowy, wnioski i odmowy; wyszukiwarka obejmuje nazwę podmiotu i obiektu. To dokumentacja źródłowa, nie 282 zweryfikowane unikalne inwestycje. Wnioskodawca/podmiot nie jest automatycznie właścicielem końcowym ani grupą. KRS/NIP i powiązania pozostają jawnie nieustalone (KSE-065, NEED-023).

Wartości wprowadzane i pobierane prezentowane są osobno, bez agregacji jako rezerwa lub konkurencja. Null nie jest zerem; dopiski pozostają w zapisie źródłowym i mają ostrzeżenia. Dostępne są przypisy wykazu, arkusz i numer wiersza. Raport `profile_review_v2` zawiera wszystkie wpisy profilu niezależnie od filtrów ekranu oraz opis pokrycia danych. Nie deklaruje pełnego pokrycia wniosków ani źródeł operacyjnych.

Odtworzenie szczegółów wymaga zachowanego XLSX z archiwum, `python scripts/benchmark_pipeline_scale.py`, a następnie `python scripts/build_profile_projects_manifest.py`. Drugi skrypt porównuje ponowny odczyt XLSX z importem i zapisuje niezmienny manifest. API sprawdza hash importu i powiązania rekordów z profilami, statusem, napięciem i źródłem. Brak lokalnego importu daje błąd dostępności zamiast wymyślonych szczegółów. Pełny import pozostaje ignorowany przez Git; manifest jest wersjonowany. Nie rozszerzono publicznego wdrożenia Sites ani praw redystrybucji danych PSE.
