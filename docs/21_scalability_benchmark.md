# Test skalowania — zbiorczy import PSE

Wykonano 18.09.2026 na zachowanym wykazie PSE ze stanem 31.07.2026. To pierwszy test przetwarzania wielu punktów przyłączenia, nie walidacja krajowego katalogu stacji.

## Wynik

| Miara | Wynik |
|---|---:|
| Wpisy projektowe odczytane jednym importem | 892 |
| Grupy etykieta punktu + napięcie | 166 |
| Wpisy przypisane do grup źródłowych | 862 |
| Wpisy bez przypisania do grupy | 30 |
| Wpisy z co najmniej jednym ostrzeżeniem | 65 |
| Profile wybrane do próby | 50 |
| Potwierdzone tożsamości stacji między źródłami | 0 |

Przypisanie do grupy nie potwierdza fizycznej stacji. Nie utożsamiamy 166 grup ze 166 stacjami ani 892 wierszy z 892 unikalnymi inwestycjami. Nazwy z literówkami, skrótami i określeniem „planowana” pozostają oddzielne; poziomy napięcia również. 65 rekordów z ostrzeżeniami obejmuje 30 bez przypisania — tych liczb nie dodajemy. Pozostałe 35 przypisano do grup, lecz ich moce wymagają przeglądu. Brak flagi nie oznacza ręcznego potwierdzenia poprawności.

Zmierzony czas odczytu XLSX, walidacji i grupowania: 0,156 s w pierwszym przebiegu i 0,164 s w powtórzeniu na tym komputerze. Nie obejmuje pobrania, wstępnego hashowania, zapisu, badań źródeł ani pracy człowieka. Nie ekstrapolujemy go na koszty obsługi 2000 stacji. Wynik ponownego uruchomienia jest identyczny; zmienne czasy nie wchodzą do wersjonowanego wyniku danych.

## Wyjątki

- 28 wpisów z flagą wielu punktów; nie rozdzielamy automatycznie mocy pomiędzy stacje.
- 28 wpisów z napięciem wymagającym przeglądu, w tym wiersz 116 z 200 kV; nie zmieniamy go na 220 kV.
- 11 wpisów z etykietą wymagającą przeglądu (np. kilka nazw w komórce).
- 36 wartości eksportu i 4 importu z adnotacją lub niejednoznacznym zapisem; liczby nie są odzyskiwane przez usunięcie liter. Oryginalny zapis pozostaje zachowany.

Powody nakładają się. Dziesięć przypisów końcowych zachowano osobno, sześć pustych wierszy rozpoznano jako puste. Wszystkie 908 wierszy od piątego do ostatniego są rozliczone: 892 + 10 + 6. Ostrzeżenie biblioteki o rozszerzeniu walidacji Excela dotyczy funkcji zapisu; arkusz jest wyłącznie czytany i nie został zmieniony.

## Metoda i granice

Grupowanie korzysta wyłącznie z dokładnej etykiety po usunięciu skrajnych spacji, operatora PSE i pojedynczego napięcia 110/220/400 kV. Nie stosuje dopasowania przybliżonego ani automatycznego łączenia aliasów. ID grup jest zależne od źródła, etykiety i napięcia. ID wiersza jest lokalne dla snapshotu — przy historii należy stosować razem hash źródła i lokalizator, a nie sam numer wiersza.

Próba 50 grup jest wybierana naprzemiennie z poziomów 110, 220 i 400 kV, alfabetycznie wewnątrz poziomu. To deterministyczna próba techniczna, nie losowa próba reprezentatywna. Nie obejmuje kompletnego zbioru OSD. Rzeczywisty współczynnik błędnych dopasowań oraz minuty ręcznej pracy pozostają null, do ustalenia w osobnym audycie. Nie mierzyliśmy jeszcze przyspieszenia względem ręcznego researchu ani poprawności aliasów.

Moce eksportu i importu są odrębne, nie sumujemy ich ani nie szacujemy rezerwy. Status umowy nie oznacza uruchomienia; status wniosku jest zachowany dosłownie. Wszystkie wpisy są REPORTED. Przed regularnym pozyskiwaniem i redystrybucją trzeba rozstrzygnąć warunki wykorzystania źródła zapisane w katalogu.

## Odtworzenie

`python scripts/benchmark_pipeline_scale.py`

Źródło: [wykaz PSE na 31.07.2026](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx). Zachowany snapshot pobrano 2026-09-10T11:21:03.1201767Z; w tym teście nie odświeżano strony operatora. SHA-256: `21dff45875f6fe7d943fd3df98a2290c1e3f04e999389538bdc1c00fe54b86dc`.

Pełny import znajduje się w ignorowanym `data/processed/pse_bulk_pipeline_2026-07-31_v1.json`; powstaje ponownie z archiwum źródeł. Wersjonowany wynik próby i kolejka wyjątków: `data/reference/pse_scale_benchmark_2026-07-31_v1.json`. Kod odmawia nadpisania różnego wyniku. Testy kontrolują jednostkę MW, zmianę nagłówka/daty, zera i braki, wielopunktowość, 200 kV, adnotacje mocy, brak scalenia aliasów i zgodność trzech wierszy Radkowic z pilotem.

## Pięćdziesiąt profili źródłowych

Liczniki oznaczają wiersze publikacji. Tabela nie jest rankingiem stacji.

| Punkt według źródła | kV | Wpisy | Wpisy z ostrzeżeniem |
|---|---:|---:|---:|
| Adamów | 110 | 4 | 0 |
| Abramowice | 220 | 5 | 0 |
| Baczyna Systemowa | 400 | 21 | 0 |
| Baczyna Systemowa | 110 | 9 | 0 |
| Adamów | 220 | 4 | 0 |
| Byczyna | 400 | 1 | 0 |
| Baczyna Systemowa (planowana) | 110 | 4 | 0 |
| Blachownia | 220 | 7 | 0 |
| Bydgoszcz Zachód | 400 | 5 | 0 |
| CPKK | 110 | 4 | 2 |
| Boguszów | 220 | 2 | 0 |
| CPKK | 400 | 1 | 0 |
| Chmielów | 110 | 3 | 0 |
| Bujaków | 220 | 2 | 2 |
| Choczewo | 400 | 18 | 0 |
| Dobrzeń | 110 | 8 | 0 |
| Byczyna | 220 | 6 | 0 |
| Czarna | 400 | 13 | 0 |
| Dunowo | 110 | 2 | 1 |
| Chełm | 220 | 4 | 0 |
| Dobrzeń | 400 | 7 | 0 |
| Ełk Bis | 110 | 8 | 2 |
| Chełm Systemowa | 220 | 1 | 0 |
| Dunowo | 400 | 17 | 2 |
| Gdańsk Błonia | 110 | 4 | 0 |
| Chmielów | 220 | 2 | 0 |
| Ełk Bis | 400 | 14 | 0 |
| Gdańsk Przyjaźń | 110 | 2 | 0 |
| Cieplice | 220 | 3 | 0 |
| Gdańsk Błonia | 400 | 5 | 0 |
| Gorzów | 110 | 1 | 1 |
| Dunowo | 220 | 1 | 0 |
| Gdańsk Przyjaźń | 400 | 2 | 0 |
| Jarosław (planowana) | 110 | 8 | 0 |
| Glinki | 220 | 1 | 0 |
| Grudziądz Węgrowo | 400 | 11 | 0 |
| Konin | 110 | 4 | 0 |
| Groszowice | 220 | 3 | 0 |
| Jarosław (planowana) | 400 | 5 | 0 |
| Kopanina | 110 | 2 | 0 |
| Grudziądz Węgrowo | 220 | 5 | 0 |
| Kozienice | 400 | 8 | 0 |
| Krajnik | 110 | 1 | 0 |
| Janów | 220 | 2 | 0 |
| Krajnik | 400 | 5 | 0 |
| Kromolice | 110 | 12 | 0 |
| Joachimów | 220 | 8 | 0 |
| Kromolice | 400 | 5 | 0 |
| Krosno Iskrzynia | 110 | 4 | 0 |
| Kielce | 220 | 8 | 0 |

## Następna bramka

1. Zweryfikować tożsamości 50 grup wobec niezależnego słownika, zachowując rozdział stacji planowanych i istniejących; mierzyć błędy i czas rozstrzygnięć.
2. Uruchomić drugi zbiorczy import dla OSD; dopiero wtedy ocenić przenośność metody między operatorami.
3. Udostępnić wybór wielu stacji w aplikacji po ustaleniu jawnych identyfikatorów i zakresu pokrycia. Dokumentacja szczegółowa Radkowic pozostaje osobnym poziomem analizy na żądanie.

## Drugi operator — TAURON, próba z 18.09.2026

Przetworzono zachowany 99-stronicowy PDF: 98 stron tabeli i stronę legendy. Data wydrukowana w nagłówku: 30.06.2026; plik pobrano 10.09.2026. Nie odświeżano danych operatora. Obejrzano render pierwszej i ostatniej strony tabeli. Parser rozlicza ciąg numerów 1–10955; nie jest to ręczny audyt wszystkich komórek.

| Miara | Wynik |
|---|---:|
| Wiersze tabeli | 10 955 |
| Grupy kod + poziom napięcia | 624 |
| Wiersze przypisane do grup | 8 571 |
| Wiersze bez przypisania | 2 384 |
| Wiersze z flagą weryfikacji tożsamości | 2 389 |
| Unikalne wartości ID obiektu w źródle | 9 926 |
| Wartości ID występujące więcej niż raz | 847 |
| Wiersze z powtarzającymi się ID | 1 876 |
| Wiersze o statusie obiekt przyłączony | 342 |
| Znormalizowane wartości mocy | 0 |

624 grupy nie są 624 potwierdzonymi GPZ. ID obiektu nie jest liczbą projektów: powtórzenia mogą dotyczyć części instalacji lub wielu punktów i pozostają zachowane. Zdarzają się opisy „Stacja obca”, brak określonego miejsca oraz kody, które wymagają słownika. Automatycznie grupujemy tylko pojedynczą etykietę w formie trzech wielkich liter ASCII i cyfry 3/4, przy fladze NIE; jest to rozpoznanie formy kodu, nie interpretacja jego znaczenia. Inne oznaczenia trafiają do przeglądu. Numer kodu nie wyznacza napięcia — poziom odczytujemy z osobnej kolumny.

Wiersze z powtarzanym ID i pojedynczym kodem mogą zachować grupę źródłową, ale nadal mają flagę weryfikacji. Flagi nakładają się: 638 etykiet poza pojedynczym kodem, 1873 wiersze z wieloma miejscami, 1876 z powtórzonym ID. Nie sumujemy tych liczb jako liczby błędów.

Eksport tekstu PDF usuwa puste komórki, więc kolejne liczby w linii nie określają bezpiecznie kolumn eksport/import. Dlatego adapter normalizuje punkt, poziom, status, typ, ID i lokalizator; moce mają null oraz NOT_EXTRACTED_FROM_FLATTENED_PDF, a oryginalna linia jest zachowana. To świadomie węższy zakres niż PSE. Liczniki wyjątków PSE i TAURON nie mierzą identycznych kryteriów. Do mocy potrzebna jest osobna ekstrakcja geometryczna tabeli i kontrola nagłówków oraz próbek — nie zgadywanie pozycji liczb.

Odczyt tekstu 99 stron: 65,04 s. Przebieg z zapisanym tekstem, parsowaniem i zapisem wyników: około 0,53 s. Cache związano z hashem PDF i tekstu. Są to dwa różne zakresy pomiaru. Nie uwzględniają czasu researchu i ręcznej weryfikacji. Test potwierdza możliwość przetwarzania całych publikacji, nie potwierdza jakości identyfikacji wszystkich stacji.

Odtworzenie: `python scripts/benchmark_tauron_scale.py`. Brak cache powoduje ponowny odczyt PDF. Wynik śledzony: `data/reference/tauron_scale_benchmark_2026-09-10_v1.json`; pełne 10955 rekordów w ignorowanym `data/processed/tauron_bulk_pipeline_2026-09-10_v1.json`. Cache oraz surowy PDF pozostają lokalne. Adapter zatrzymuje się przy zmianie formatu wiersza, nieznanym statusie, braku/sporze daty lub nieciągłej numeracji. Nie deduplikuje po ID obiektu i nie sumuje mocy.

Źródło: [TAURON — wykaz obiektów i odmów](https://www.tauron-dystrybucja.pl/-/media/offer-documents/dystrybucja/przylaczenie/dostepne-moce/informacja-o-przylaczanych-obiektach-i-wydanych-odmowach.ashx). SHA-256 zachowanej wersji: `ce11455a2575454588fef46f711700b476ead67f4cd0b9a829b96e6698bc83b8`. Licencja i warunki regularnego użycia pozostają zgodne z nierozstrzygniętymi ograniczeniami katalogu; ten test nie ustanawia prawa redystrybucji.

Wspólne dla obu operatorów są kontrola snapshotu, provenance, rozdział statusów, jawne braki i kolejka wyjątków. Odczyt tabeli i znaczenie identyfikatorów pozostają specyficzne dla operatora. Następna bramka to NEED-019 (słownik kodów) i KSE-049 (niezależny audyt tożsamości), nie rozszerzanie ręcznej analizy każdego GPZ.
