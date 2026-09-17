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
