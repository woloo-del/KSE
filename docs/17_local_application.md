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
