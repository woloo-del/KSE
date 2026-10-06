# Powierzchnia grup rejestrowych wokół stacji

Stan: 19.09.2026. Implementacja obliczeń: `gis/ownership_area.py`, metoda `registration_group_buffer_v1`. **Gotowy rdzeń obliczeniowy, brak rzeczywistego raportu 1 km dla stacji.** Dane źródłowe i zakres dostępności opisuje [rozpoznanie własności](25_land_ownership_discovery.md). Obliczenie powierzchni jest CALCULABLE po dostarczeniu właściwych wejść; interpretacja prawna publiczne/prywatne pozostaje niezatwierdzona.

## Wejście

Punkt odniesienia oraz wielokąty działek muszą być wcześniej jawnie przekształcone do EPSG:2180, kolejność x=easting, y=northing, jednostka metr. Moduł odrzuca inny deklarowany CRS. Nie wykonuje transformacji i nie potrafi wykryć każdego błędnego przypisania etykiety CRS. **GeoJSON próbki Grudziądza jest w EPSG:4326 i nie jest bezpośrednim wejściem tej funkcji.** Adapter opisany poniżej wykonuje transformację przed wywołaniem rdzenia; sam rdzeń nadal przyjmuje tylko EPSG:2180.

Każda działka ma ID, geometrię Polygon/MultiPolygon, oryginalną grupę 1–16 albo null, identyfikator źródła i datę źródłową (może być null). Punkt ma osobne źródło. Wymagana metryka źródeł: lokalizator dokumentu/URL, data pobrania i SHA-256. Importujący musi wcześniej sprawdzić hash oryginalnych bajtów; rdzeń sprawdza obecność metadanych i format hasha, nie pobiera plików. Odrzucane są powtórzone ID, nieprawidłowe geometrie, grupy poza zakresem oraz brak pochodzenia.

Przed użyciem punktu jako stacji trzeba potwierdzić jego tożsamość i pochodzenie. Moduł matematyczny nie potwierdza tożsamości stacji na podstawie współrzędnych. Promień domyślny 1000 m dotyczy punktu, nie granicy terenu stacji.

## Podział powierzchni

1. Tworzymy metryczny bufor B.
2. Przecinamy każdą działkę z B; działki poza nim i samo dotknięcie granicy nie wnoszą powierzchni.
3. Wykrywamy przecięcia działek o dodatniej powierzchni. Ich suma geometryczna tworzy obszar konfliktu O. Dotykające się granice nie są konfliktem.
4. Dla każdej grupy łączymy geometrie i odejmujemy O. Także nakładanie działek z tą samą grupą zostaje wyłączone do wyjaśnienia; moduł nie wybiera preferowanego rekordu.
5. Oddzielnie pokazujemy brak geometrii, obszar geometrii bez grupy (po odjęciu O) oraz O. Ich suma to powierzchnia nierozstrzygnięta.

Mianownik każdego udziału to **cały bufor B**, nie tylko powierzchnia otrzymanych działek. Wynik: m², ha i procent B. Suma grup 1–16 i powierzchni nierozstrzygniętej musi odpowiadać B. Kilka nakładających się działek nie powoduje wielokrotnego naliczenia konfliktu; pole `overlap_pairs` to diagnostyka par, której powierzchni nie należy sumować.

`geometric_coverage` opisuje część B przykrytą wejściowymi geometriami, także konfliktowymi. Nie dowodzi kompletności rejestru, aktualności danych ani dostępności gruntu do inwestycji. Nie stosujemy progu, po którym braki uznaje się za nieistotne.

## Dokładność i historia

Bufor przybliża koło 256 odcinkami (64 na ćwiartkę): przy promieniu 1000 m maksymalna różnica promienia względem koła planarnego jest mniejsza niż 0,076 m. Nie jest to dokładność geodezyjna danych ani korekta zniekształceń odwzorowania EPSG:2180. Wynik zależy od jakości punktu i granic działek.

Kontrola bilansu używa tolerancji numerycznej 1e-9 względnie / 1e-6 m² bezwzględnie. Te wartości służą jedynie kontroli arytmetyki, nie usuwaniu małych konfliktów. Geometrie nie są automatycznie naprawiane ani przyciągane do siatki.

Wynik zawiera wersję metody, CRS, promień, aproksymację bufora, punkt, źródła, daty obserwacji działek, wersje Shapely/GEOS oraz odcisk wejść. Kolejność wejściowych działek nie zmienia wyniku. Odtworzenie wymaga również zachowanych geometrii i źródłowych snapshotów; sam hash ich nie zastępuje.

## Zakres i dalsza praca

Testy `tests/test_ownership_area.py` używają wyłącznie syntetycznych geometrii: puste wejście, przycinanie, połowa koła, brak kategorii, styk granic, konflikty dwóch/trzech działek, otwory, obiekty poza buforem, nieprawidłowe wejścia i odtwarzalność.

Nie dodano endpointu ani wyniku w UI. Nie uproszczono grup do państwowe/prywatne. Następny krok: zweryfikowany import całego bufora z kontrolą paginacji, pokrycia, dat i praw do użycia. Adapter CRS i kontrola pojedynczej odpowiedzi są już dostępne (poniżej). Radkowice nadal wymagają danych wskazanych w NEED-021; próbka Grudziądza nie zastępuje tego wejścia.

## Adapter CRS i kontrola zakresu odpowiedzi — 19.09.2026

`gis/coordinates.py` wykorzystuje pyproj 3.7.2 / PROJ do jawnej transformacji EPSG:4326 → EPSG:2180. Wejście longitude/latitude, wyjście easting/northing (`always_xy=True`). Parser GML już zamienia źródłowe lat/lon na GeoJSON lon/lat; adapter nie zamienia ich ponownie. Kontrolujemy zakres zastosowania CRS z bazy PROJ, co wykrywa m.in. odwrócone osie polskich współrzędnych. Ten prostokąt nie jest dokładną granicą Polski. Niedopuszczone są transformacje ballpark, geometrie 3D i działanie z aktywnym pobieraniem siatek PROJ z sieci. Wynik zapisuje wersję biblioteki, PROJ, pipeline i deklarowaną dokładność transformacji — ta ostatnia nie określa dokładności działek.

Zależność dodano do `requirements-gis.txt`, ponieważ dotychczasowe Shapely nie wykonuje transformacji układów odniesienia. Oficjalna [dokumentacja Transformer](https://pyproj4.github.io/pyproj/stable/api/transformer.html) i [licencja pyproj 3.7.2](https://github.com/pyproj4/pyproj/blob/3.7.2/LICENSE), zweryfikowane 19.09.2026. Licencja pyproj dopuszcza użycie komercyjne z zachowaniem noty; nie nadaje praw do danych EGiB. Transytywne certifi przypięto w wersji 2026.7.22. Nie instalowano usługi sieciowej ani nowego silnika bazy danych.

`connectors/gis/ownership_snapshot.py` łączy sprawdzenie SHA-256 oryginalnej odpowiedzi, odczyt GML, transformację geometrii i rdzeń powierzchni. Przyjmuje tylko pojedynczą odpowiedź GetFeature WFS 2.0.0 z rozpoznanym CRS, typem działki, BBOX i początkiem od zera; dodatkowe filtry/nieznane parametry są odrzucane. Wynik pola `area_result` pozostaje null, gdy:

- prostokąt zapytania nie obejmuje całego obliczanego bufora;
- `numberMatched` jest nieznane albo różni się od liczby odczytanych rekordów;
- odpowiedź wskazuje następną stronę.

Odróżniamy braki zakresu zapytania od dziur w dostarczonych geometriach. Gdy odpowiedź przejdzie kontrolę, rdzeń nadal pokazuje dziury i konflikty. Status `SINGLE_RESPONSE_READY_FOR_REVIEW` oznacza gotowość pojedynczej odpowiedzi do przeglądu, **nie** kompletność rejestru, zatwierdzenie punktu jako stacji lub zgodę na publikację. Punkt wejściowy jest oznaczony `RESEARCH_POINT_NOT_VERIFIED_STATION`. Nie zaimplementowano pobierania kolejnych stron; taki wynik zatrzymuje analizę zamiast pomijać rekordy.

Odtworzenie kontroli rzeczywistej próbki: `.venv/Scripts/python.exe -X utf8 scripts/check_ownership_sample_readiness.py`. Wynik `data/reference/ownership_sample_readiness_2026-09-19.json`: dwie działki odczytane i przekształcone, liczba pasujących rekordów 2, ale **REQUEST_BBOX_DOES_NOT_COVER_BUFFER**, bez raportu powierzchni. Środek jest wyprowadzony z zachowanego prostokąta zapytania, nie z lokalizacji stacji. Używa istniejącego archiwum porównania; nie pobrano nowych działek.

Testy kontrolują południk centralny CRS, powrót do współrzędnych geograficznych, zamianę osi, pełną odpowiedź syntetyczną, zbyt mały BBOX, ucięcie, nieznaną liczbę, następną stronę, dodatkowy filtr, hash i rzeczywistą ograniczoną próbkę. Nie wygenerowano procentów dla stacji ani nie zmieniono publicznej aplikacji. Rejestry i dokumentacja zasilają kolejny raport; XLSX w tym kroku nie regenerowano.

## Paginacja i spójność migawki — 19.09.2026

Sprawdzono bezpośrednio [GetCapabilities zbiorczego WFS GUGiK](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities). Deklaracje źródłowe: `ImplementsResultPaging=TRUE`, `PagingIsTransactionSafe=FALSE`, `CountDefault=1000`. To deklaracje tego serwera, nie wniosek z ogólnej dokumentacji WFS. Gwarancji niezmienności danych pomiędzy stronami brak.

Dwie małe próby na wcześniej badanym prostokącie Grudziądza (`COUNT=1`, `STARTINDEX=0/1`) zwróciły kolejno **046201_1.0090.5/5** i **046201_1.0090.5/8**. Pierwsza odpowiedź podała `next`, druga nie. Obie podały `numberMatched=unknown`. Paginacja działa w tej próbce, ale nie potwierdzono kompletnej liczby rekordów ani transakcyjnego snapshotu. Bez sortowania i blokady wersji sam brak duplikatów nie wyklucza pominięcia podczas zmiany danych.

`connectors/gis/ownership_paging.py` sprawdza hashe wszystkich stron, pochodzenie, spójny endpoint i parametry zapytania, offsety od zera, limit COUNT, ciągłość odnośników, unikalność identyfikatorów działek oraz zgodność znanych liczników. Nie wykonuje automatycznej deduplikacji — powtórzona działka zatrzymuje import. Odnośnik do innego hosta/ścieżki, zmienionego filtra, zakresu lub wcześniejszej strony zostaje odrzucony przed kolejnym pobraniem.

Funkcja `fetch_page_chain` steruje pobieraniem przez przekazane funkcje transportu i archiwizacji. Domyślnie najwyżej 10 stron i budżet żądanych rekordów 10000; to zabezpieczenia lokalnego przebiegu, nie limity deklarowane przez operatora. Odpowiedź jest archiwizowana przed parsowaniem. Osiągnięcie limitu lub błąd przerywa przebieg, nie zwraca pozornego sukcesu. Transport musi mieć timeout, limit bajtów i zakaz niezweryfikowanych przekierowań; moduł nie instaluje globalnego klienta ani harmonogramu. Przetestowano go na kontrolowanym transporcie testowym, a rzeczywiste dwie strony pobrano w ograniczonym eksperymencie.

Odtworzenie rzeczywistej kontroli: `scripts/check_ownership_page_chain.py`. Wynik `data/reference/ownership_paging_audit_2026-09-19.json` odróżnia `server_sequence_exhausted=true` od gotowości do dalszej analizy. Zapisane blokady: **MATCHED_COUNT_UNKNOWN** i **TRANSACTIONAL_SNAPSHOT_NOT_GUARANTEED**. `area_result=null`. Nawet pozytywny wynik strukturalny wymaga nadal sprawdzenia całego bufora, pochodzenia lokalizacji stacji i praw do użycia. Nie połączono tej próby z raportem stacji.

Trzy surowe odpowiedzi zachowano w `data/archives/ownership_paging_2026-09-19.zip`, manifest `data/catalog/ownership_paging_archive_2026-09-19.json`. Archiwum wymaga prywatnej kopii zapasowej. Źródła, URL i daty są w `probe_results_ownership_paging_2026-09-19.json`. Testy obejmują również zmianę liczników, brak strony, dodatkową stronę po deklarowanym końcu, obcy host, pętlę i limit pobierania.

Kolejny kierunek: **datowany eksport albo wersjonowana usługa**. NEED-022 rejestruje brak takiego wejścia, oddzielnie od braku grup w Radkowicach (NEED-021). Rejestr zasilający raport jest zaktualizowany; XLSX nie był regenerowany w tym kroku.

## Paczka jako niezmienne wejście lokalne — 06.10.2026

Znaleziono oficjalny ZIP/GPKG Grudziądza; [szczegóły audytu](25_land_ownership_discovery.md). Jeden zachowany plik usuwa problem zmieniających się odpowiedzi podczas lokalnego przetwarzania, ale nie dowodzi jednej daty obowiązywania wszystkich danych EGiB. `connectors/gis/county_package.py` ponownie wykorzystuje istniejący dekoder GeoPackage; czyta tylko warstwę działek w trybie read-only, sprawdza CRS, unikalność ID, grupy oraz geometrie. Zwraca liczniki błędów, nie maskuje ich jako braków danych. `scripts/audit_county_export.py` sprawdza hash ZIP, rozmiar i nazwę członu oraz odmawia nadpisania odmiennego rozpakowanego pliku. Daty pozostają surowymi wartościami źródła.

Nie uruchomiono jeszcze bufora konkretnej stacji. Paczka obejmuje miasto Grudziądz (TERYT 0462), nie automatycznie sąsiedni powiat ani cały bufor stacji Grudziądz Węgrowo. Kolejny krok to zweryfikowana lokalizacja i wybór wszystkich potrzebnych paczek. Raport XLSX nie był regenerowany; rejestry zasilające go są zaktualizowane.

## Prywatna kontrola kandydata Węgrowo — 06.10.2026

Dodano `select_parcels` do istniejącego connectora paczki. Audyt całej warstwy poprzedza wybór działek przecinających bufor o dodatniej powierzchni; błędy paczki lub duplikaty blokują wynik. Adapter zwraca obiekty Parcel z grupą i pochodzeniem, używane przez istniejący rdzeń powierzchni. Nie dodano zależności.

`scripts/analyze_private_wegrowo_land.py` wybiera jawnie jeden punkt z przekazanego historycznego GIS (stan wskazany przez użytkownika: 2024). Zachowuje źródło i hash, używa x/y punktu, a następnie przekształca do EPSG:2180. Nie awansuje tego rekordu do potwierdzonej stacji. Wynik zapisuje wyłącznie w ignorowanym `data/private/reviews/wegrowo_land_2026-10-06/land_diagnostic.json`.

W tej diagnostyce **278 działek** paczki miasta przecina bufor; ich suma geometryczna pokrywa **około 52,76%** powierzchni bufora. Pozostała powierzchnia jest brakiem geometrii w zestawie wejściowym. Nie określono jej własności ani nie przypisano jej automatycznie do sąsiedniego powiatu — do tego potrzebna kontrola oficjalnej granicy. Wynik nie jest pełnym raportem stacji ani podziałem prawnym państwowe/prywatne.

Odczytane [obwieszczenie BIP z 03.02.2016](https://bip.grudziadz.pl/artykul/obwieszczenie-informacja-prezydenta-grudziadza-z-dnia-03-lutego-2016-r-o-wydaniu-decyzji-o-srod) potwierdza nazwę rozbudowy stacji 400/220/110 kV, ale nie podaje współrzędnych lub identyfikatorów działek. Próba OSM zakończyła się HTTP 406, a drugi serwer timeoutem. Próba odczytu odnośnika do sąsiedniej paczki przez WMS zakończyła się zerwaniem połączenia; paczki nie pozyskano w tym kroku. Te nieudane zapytania nie stanowią dowodu braku źródła.

Obwieszczenie zachowano w `data/archives/wegrowo_location_2026-10-06.zip`; manifest `data/catalog/wegrowo_location_archive_2026-10-06.json`. Prywatny GIS i diagnostyka wymagają oddzielnej prywatnej kopii; Git zawiera kod odtworzenia, dokumentację i metrykę publicznego źródła. NEED-022 doprecyzowano o sąsiednią paczkę i potwierdzenie punktu. Raport XLSX nie był regenerowany.


## 2026-10-06 — dwie paczki powiatowe dla Węgrowa

Oficjalny GetFeatureInfo usługi DanePowiatowe wskazał [paczkę 0406](https://opendata.geoportal.gov.pl/InneDane/latest_exports/eziudp_wfs/GPKG/0406.gpkg.zip), pobraną i zweryfikowaną 2026-10-06. Manifest: `data/catalog/probe_results_wegrowo_rural_2026-10-06.json`. Audyt: `data/reference/county_rural_export_audit_2026-10-06.json`. Paczka zawiera 43 791 działek, bez powtórzonych ID i błędów geometrii w kontroli; wszystkie mają grupę rejestrową. Zachowano surowe daty źródłowe, bez utożsamiania ich z datą obowiązywania prawnego. Pobranie nie rozstrzyga praw komercyjnego wykorzystania grup.

Powtórzenie: `.venv/Scripts/python.exe -X utf8 scripts/audit_county_export.py --county 0406`, następnie `.venv/Scripts/python.exe -X utf8 scripts/analyze_private_wegrowo_land.py --include-rural`. Wymaga również odtworzonej paczki miasta i prywatnego GIS użytkownika. Archiwum `data/archives/wegrowo_rural_2026-10-06.zip` zawiera odpowiedź usługi i ZIP; manifest w Git. Wymagana osobna prywatna kopia archiwum, której wykonania nie potwierdzono.

Wspólny bufor: 520 działek (278 miasta i 242 powiatu), pokrycie geometryczne około 100%. Zachowano 0,206 m² brakującej geometrii i 36,011 m² nakładania jako nierozstrzygnięte; nie zaokrąglono ich do zera w wyniku maszynowym. Nakładanie wyłączono ze wszystkich grup. To wartości obliczone w geometrii wejściowej, nie dokładność pomiaru terenowego. Brak grup: 0 m². Duplikaty identyfikatorów powodowałyby przerwanie obliczeń, a nie automatyczne scalenie.

Wynik zapisano osobno w prywatnym `land_diagnostic_two_counties.json`, pozostawiając wcześniejszy wynik miejski. Punkt stacji nadal HISTORYCZNY/NIEZWERYFIKOWANY (GIS użytkownika, stan deklarowany 2024). Nie publikujemy współrzędnych ani podziału Skarb Państwa/prywatne. Pełne pokrycie geometryczne nie dowodzi aktualności praw własności. Następne kroki: potwierdzenie punktu, interpretacja grup i warunki wykorzystania. Rejestr potrzeb nie prosi już o pobraną paczkę powiatu.


## 2026-10-06 — znaczenie grup i czytelny raport prywatny

Zweryfikowano [tekst jednolity EGiB 2024/219](https://eli.gov.pl/eli/DU/2024/219/ogl), §14 oraz załącznik 2 na stronie 27 PDF. Metadane ELI wskazują dwie nowelizacje: [2024/1954](https://eli.gov.pl/api/acts/DU/2024/1954/text.html) oraz [2026/1094](https://api.sejm.gov.pl/eli/acts/DU/2026/1094/text.pdf). Odczytane zmiany nie modyfikują §14 ani załącznika 2. Sprawdzono wizualnie stronę załącznika i pierwszą stronę nowelizacji 2026. Weryfikacja dotyczy znaczenia opublikowanych kategorii, nie poprawności każdego rekordu EGiB.

**Grupa rejestrowa nie jest pełną strukturą własności.** Uwzględnia również określone przypadki samoistnego posiadania. Przy wspólnych prawach o przypisaniu decyduje przeważająca suma udziałów, a przy remisie niższy numer grupy. Grupa 15 nie rozstrzyga kapitału spółki. Nie można więc przeliczyć hektarów grup na dokładne procenty praw SP/prywatnych. Użytkowanie wieczyste pozostaje odrębne. Zachowujemy wszystkie 16 klas i nierozstrzygnięte obszary.

Słownik skróconych etykiet z datą i źródłami: `data/reference/registration_group_labels.json`. Generator `scripts/describe_private_wegrowo_land.py` przygotowuje `data/private/reviews/wegrowo_land_2026-10-06/land_groups_review_v1.md`: powierzchnie, ograniczenia, hashe wyniku i słownika, proweniencja. Nie zmienia geometrii ani wyników obliczeń. Nie nadpisuje odmiennego raportu. Raport pozostaje prywatny, bez integracji publicznej i bez automatycznej kwalifikacji dostępności gruntów. Zaktualizowane rejestry zasilają raport projektu; XLSX nie odświeżono w tym kroku.

Dodatkowo odczytano [MPZP XXXIII/14/13 z 27.02.2013](https://bip.grudziadz.pl/pliki/grudziadz/zalaczniki/17200/mpzp_jaskolcza_rydygiera-podpisany.pdf). §22 na stronie 19 wskazuje stację 400/220/110 kV Grudziądz-Węgrowo w terenie 14E; rysunek na stronie 31 został obejrzany. Nie wykonano georeferencji ani kontroli późniejszych zmian planu. To historyczny dowód obszaru, nie potwierdzenie współrzędnych prywatnego GIS, statusu modernizacji lub własności. Pierwsza próba przekroczyła limit 15 MB; ponowiono z limitem 60 MB, plik ma 16 063 376 bajtów. Renderer zgłosił brak tablicy Fields, ale rysunek został poprawnie wyświetlony; dokumentu nie modyfikowano.

Siedem zachowanych odpowiedzi: `data/catalog/probe_results_land_interpretation_2026-10-06.json`; archiwum `data/archives/land_interpretation_2026-10-06.zip` i manifest w katalogu. Oddzielna kopia zapasowa archiwum nadal wymagana. Praw do redystrybucji powiatowych grup nie wywodzimy z dostępności dokumentów prawnych.
