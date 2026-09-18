# Zbiorczy indeks inwestycji PSE

Wykonano 18.09.2026 na zachowanym tego dnia HTML [portalu inwestycji PSE](https://inwestycje.pse.pl/). Nie pobierano ponownie strony. Źródło jest już w katalogu jako PSE_RADK_STAGES; mimo historycznej nazwy identyfikatora snapshot obejmuje cały portal.

## Co uzyskaliśmy

| Miara | Wynik |
|---|---:|
| Niepuste wystąpienia nagłówków h4 | 267 |
| Różne teksty nagłówków | 258 |
| Profile PSE objęte porównaniem | 50 |
| Profile z co najmniej jedną wzmianką o nazwie | 40 |
| Różne nagłówki wskazane przez te profile | 105 |
| Potwierdzone kanoniczne tożsamości przez automat | 0 |

To indeks dowodów do przeglądu, nie 105 unikalnych inwestycji, 40 potwierdzonych stacji ani nowe relacje sieciowe. Kilka profili napięciowych może wskazywać te same nagłówki. Powtórzenia tekstu zachowano jako jeden wpis z wszystkimi pozycjami w HTML; nie traktujemy ich jako niezależnych potwierdzeń.

Wyszukiwanie zachowuje granice słów, polskie znaki, aliasy i kwalifikator „planowana”. Wzmianka o nazwie może dotyczyć linii, farmy lub stacji. Nie przypisujemy automatycznie napięcia zadania do profilu. Brak wzmianki nie oznacza braku inwestycji; portal nie jest kompletnym rejestrem stacji.

## Wynik merytoryczny dla wyjątków GIS

W zachowanym portalu jest nagłówek opisujący zakończoną budowę stacji 400/110 kV Gdańsk Przyjaźń wraz z wprowadzeniem toru linii. Potwierdza, że w publikacji operatora zakres tej inwestycji obejmował 110 kV; nie należy interpretować braku 110 kV w etykiecie GIS jako dowodu braku tego poziomu. W tym samym portalu inne zadania mają w nazwie stację Gdańsk Przyjaźń 400 kV. Różny zakres nazw nie jest automatycznie sprzecznością. Nie ustalono aktualnego schematu ani tożsamości konkretnego pola.

Portal opisuje też zadania dla Bydgoszczy Zachód i Choczewa. Nazwa „Baczyna” różni się od „Baczyna Systemowa”, a „Jarosław Systemowa” od „Jarosław (planowana)”; nie dodano automatycznych aliasów. Krajnik pozostaje do wyjaśnienia dla profilu 110 kV. Wszystkie szczegółowe nagłówki i lokalizatory są w indeksie JSON; status KSE-049 pozostaje „W toku”.

## Status i pochodzenie

Każdy nagłówek ma klasyfikację REPORTED i jakość źródła B. Powiązanie wzmianki z profilem jest INFERRED, a jej znaczenie dla napięcia i decyzji użytkownika pozostaje UNKNOWN. Nie nadajemy korzystnej oceny przez samą obecność inwestycji.

Status jest odczytywany tylko przy jednym rozpoznanym oznaczeniu na końcu nagłówka. Nagłówki łączące kilka etapów i statusów mają status null oraz flagę przeglądu. Zakończenie zadania nie stanowi daty uruchomienia stacji. Data publikacji treści pozostaje null; znany jest czas pobrania. Nie normalizujemy tu terminów ani opisów między nagłówkami, które mogą mieć niejednoznaczny zakres.

## Odtworzenie

`python scripts/build_pse_investment_index.py`

Wynik: `data/reference/pse_investment_heading_index_2026-09-18_v1.json`. Każdy lokalizator h4 należy interpretować razem z hashem snapshotu. Wynik zawiera hash wejściowych profili i obu modułów parsera. Źródło oraz jego archiwum mają wcześniejszy manifest `data/catalog/probe_results_radkowice_stages_2026-09-18.json`; należy zachować prywatną kopię archiwum zgodnie z docs/reproducibility.md. Skrypt odmawia nadpisania odmiennego wyniku.

Sprawdzono testami powtarzające się nagłówki, brak nagłówków, złożone statusy, granice nazw, brak automatycznej zamiany aliasów i brak promocji do kanonicznej tożsamości. Test rzeczywistego snapshotu obejmuje 50 profili i złożony nagłówek etapów Baczyny. Indeks nie jest jeszcze wystawiony w aplikacji; wymaga kontroli znaczenia relacji przed prezentacją przy stacji.

## Dostęp do słownika API

18.09.2026 anonimowe zapytanie do `specwezlow` z filtrem business_date równym 2026-09-17 i limitem 5 zwróciło HTTP 200 oraz pustą listę. Jest to obserwacja próby, nie zarchiwizowany snapshot słownika ani dowód braku węzłów. Następnego zapytania, o najnowszą datę, nie wykonano z powodu niedostępności kontroli uprawnień. Nie ustalono najnowszej dostępnej daty; brak aktualnego słownika pozostaje otwarty.
