# Agregacja dowodów stacji — Radkowice

Stan 17.09.2026. Metoda `radkowice_evidence_aggregation_v1` łączy cztery wcześniej zweryfikowane publiczne snapshoty. Nie wykonuje nowych zapytań i nie oznacza odświeżenia danych operatora.

## Wynik

| Rodzaj wpisu | Liczba | Co oznacza |
| --- | --- | --- |
| Publikacja projektu PSE | 3 | Wiersze z wykazu na 31.07.2026; nie potwierdzają fizycznego przyłączenia |
| Zadanie projektu PRSP | 2 | Udokumentowane zadania stacji i linii, ze statusem w publikacji |
| Rekord przestrzenny OSM | 69 | Selekcja względem obszaru stacji; bez potwierdzenia połączenia elektrycznego |
| Deklaracja daty inwestycji | 2 | Zachowane wskazania 2023/2025; tożsamość zakresów nierozstrzygnięta |

Łącznie 76 rekordów dowodowych. To nie jest liczba projektów, urządzeń ani unikalnych inwestycji. Nie sumowano mocy i nie przypisano automatycznie pozytywnego lub negatywnego wpływu. Interpretacja ma status NOT_ASSESSED; liczby unikalnych projektów i urządzeń pozostają null.

Każdy rekord ma stabilny identyfikator dowodu zależny od źródła i identyfikatora źródłowego, oryginalną treść, URL, datę pobrania, hash snapshotu, lokalizator (wiersz, strona lub OSM ID), klasę źródła i jawny rodzaj powiązania ze stacją. Nazwa nie jest kluczem scalania. Dwa źródła o tym samym urządzeniu pozostają dwoma dowodami do późniejszego powiązania.

Źródła OSM klasy G zachowują odrębny rodzaj i atrybucję ODbL. Publiczne publikacje operatora nie są mieszane z dokumentami prywatnymi ani bazą EMP o niewyjaśnionej licencji. Edycja OSM nie staje się datą obserwacji lub odbioru. Rozbieżność dat inwestycji jest zachowana.

## Odtwarzanie

```powershell
.venv/Scripts/python.exe scripts/build_station_evidence.py --output data/reference/radkowice_aggregated_evidence_2026-09-17_v1.json
```

Ten sam wynik jest idempotentny. Inne bajty pod istniejącą nazwą powodują błąd; trzeba wybrać nową wersję. Wynik zawiera hashe czterech plików wejściowych i modułu metody. Listę wejść utrzymuje skrypt; nie przeszukuje prywatnych folderów. Adapter obsługuje wyłącznie sprawdzone schematy pilota Radkowic, nie dowolną stację.

Backend dodaje `aggregated_evidence` do `/api/station` oraz snapshotu eksportowanej oceny. To siódme jawne wejście API; wejścia źródłowe agregacji są identyfikowane dodatkowo wewnętrznymi hashami. Istniejąca opinia nie wykorzystuje liczby 76 jako przesłanki. Nie dodano nowej zakładki frontendowej. Uruchomiony wcześniej proces serwera wymaga restartu, aby załadować zmieniony kod.

## Kontrole i następny krok

Testy obejmują powtarzalność, zachowanie kategorii i rozbieżności, brak mutacji danych, odrzucenie duplikatów źródłowych, braków provenance i zmienionego schematu. Następny krok to przegląd relacji pomiędzy dowodami i obiektami oraz przypisanie kontekstowych przesłanek. Nie powstaje score, rezerwa MW ani werdykt możliwości przyłączenia.
