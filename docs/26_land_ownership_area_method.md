# Powierzchnia grup rejestrowych wokół stacji

Stan: 19.09.2026. Implementacja obliczeń: `gis/ownership_area.py`, metoda `registration_group_buffer_v1`. **Gotowy rdzeń obliczeniowy, brak rzeczywistego raportu 1 km dla stacji.** Dane źródłowe i zakres dostępności opisuje [rozpoznanie własności](25_land_ownership_discovery.md). Obliczenie powierzchni jest CALCULABLE po dostarczeniu właściwych wejść; interpretacja prawna publiczne/prywatne pozostaje niezatwierdzona.

## Wejście

Punkt odniesienia oraz wielokąty działek muszą być wcześniej jawnie przekształcone do EPSG:2180, kolejność x=easting, y=northing, jednostka metr. Moduł odrzuca inny deklarowany CRS. Nie wykonuje transformacji i nie potrafi wykryć każdego błędnego przypisania etykiety CRS. **GeoJSON próbki Grudziądza jest w EPSG:4326 i nie jest bezpośrednim wejściem tej funkcji.** Adapter transformacji pozostaje do wykonania wraz z pozyskaniem kompletnego zestawu.

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

Nie dodano endpointu ani wyniku w UI. Nie uproszczono grup do państwowe/prywatne. Następny krok: adapter CRS i zweryfikowany import całego bufora z kontrolą paginacji, pokrycia, dat i praw do użycia. Radkowice nadal wymagają danych wskazanych w NEED-021; próbka Grudziądza nie zastępuje tego wejścia.
