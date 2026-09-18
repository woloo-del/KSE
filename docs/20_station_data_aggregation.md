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

Backend dodaje `aggregated_evidence` do `/api/station` oraz snapshotu eksportowanej oceny. To siódme jawne wejście API; wejścia źródłowe agregacji są identyfikowane dodatkowo wewnętrznymi hashami. Istniejąca opinia nie wykorzystuje liczby 76 jako przesłanki. Od 18.09.2026 dostępna jest zakładka Rejestr dowodów. Uruchomiony wcześniej proces serwera wymaga restartu, aby załadować zmieniony kod.

## Kontrole i następny krok

Testy obejmują powtarzalność, zachowanie kategorii i rozbieżności, brak mutacji danych, odrzucenie duplikatów źródłowych, braków provenance i zmienionego schematu. Następny krok to przegląd relacji pomiędzy dowodami i obiektami oraz przypisanie kontekstowych przesłanek. Nie powstaje score, rezerwa MW ani werdykt możliwości przyłączenia.

## Powiązania i przeglądarka dowodów — 18.09.2026

Metoda `exact_evidence_record_link_v1` rozpoznaje ten sam wpis projektu wyłącznie przy zgodności ID rekordu, source_id oraz SHA-256 źródła. Trzy wiersze PSE mają odpowiedniki w grafie; to ponowne użycie tej samej publikacji, nie niezależne potwierdzenie. Pozostałe 73 wpisy pozostają UNLINKED. Nie oznacza to nieobecności urządzeń ani nieistnienia relacji. Nie powstają nowe połączenia elektryczne.

API i eksport zawierają `evidence_links`, wersję metody i hash jej kodu. Interfejs udostępnia wyszukiwanie po nazwie, ID i źródle, filtr rodzaju wpisu oraz rozwijane źródło, lokalizator, daty, hash i oryginalną treść. Liczniki wynikają z danych.

Weryfikacja: 18 testów modułów powiązań, agregacji i API; przeglądarka: 76 wpisów, filtr projektów 3, wyszukanie Chęcin 1, rozwinięcie źródła z wierszem 847 i hashem. Nadal potrzebna jest osobna weryfikacja tożsamości obiektów między różnymi źródłami.

## Kolejka weryfikacji — 18.09.2026

`evidence_review_queue_v1` grupuje 73 nierozstrzygnięte wpisy: 69 przestrzennych OSM (NEED-018), dwa zadania PRSP (NEED-017) i dwie deklaracje daty (NEED-014). To grupy pracy, nie liczby unikalnych urządzeń ani ocena ryzyka sieciowego. Powtórzenia tej samej publikacji nie trafiają do kolejki. Konflikt wersji trafia do wewnętrznego przeglądu bez automatycznej prośby do użytkownika.

Kolejka w API i eksporcie zachowuje ID dowodów i wersję kodu. UI pokazuje powiązane potrzeby obok wpisu. Brak wskazanego NEED powoduje błąd walidacji. Samo oznaczenie dokumentu jako otrzymanego lub zweryfikowanego nie zamyka rozstrzygnięcia tożsamości. Potrzeby są częścią istniejącego rejestru czytanego przez generator Excel; historyczne pliki Excel nie aktualizują się automatycznie.
