# Własność gruntów w otoczeniu stacji — rozpoznanie

Zgłoszenie użytkownika: 18.09.2026. Cel: udział gruntów Skarbu Państwa i prywatnych w promieniu 1 km od stacji. Moduł dotyczy struktury własności, nie pokrycia terenu (las, zabudowa itd.) ani oceny możliwości przyłączenia.

## Źródła i stan weryfikacji — 18.09.2026

- [GUGiK — Mapa własności, grupy rejestrowe](https://www.gov.pl/web/gugik/nowa-usluga-mapa-wlasnosci---grupy-rejestrowe-dostepna-w-modulach-geoportal-krajowy-i-geodezja-i-kartografia-w-serwisie-wwwgeoportalgovpl): znaleziony oficjalny komunikat. Wyszukiwarka wskazuje przeglądanie działek według grup rejestrowych; pełne otwarcie strony zakończyło się timeoutem. Nie zweryfikowano endpointu, schematu atrybutów, zasięgu, licencji ani automatycznego pobierania. DISCOVERED, nie gotowy connector.
- [Geoportal — EGiB](https://www.geoportal.gov.pl/pl/dane/ewidencja-gruntow-i-budynkow-egib/): odczytano oficjalną dokumentację geometrii działek, usług WMS/WFS i plików wektorowych. Sam dostęp do geometrii nie potwierdza dostępności kategorii własności dla każdej działki. Dokumentacja wskazuje rozproszony, powiatowy charakter danych. CONTENT_REVIEWED.

## Proponowany wynik i warunki

Mapa działek oraz hektary i procent powierzchni bufora w kategoriach: Skarb Państwa, samorządy/inne podmioty publiczne, prywatne, nierozstrzygnięte/brak danych. To propozycja klasyfikacji do weryfikacji ze schematem źródła, nie zatwierdzone mapowanie grup rejestrowych. Nie klasyfikować pozostałych grup automatycznie jako prywatne. Uwzględnić współwłasność oraz rozdział właściciela i użytkownika wieczystego; sama dominująca grupa może nie rozstrzygać wszystkich udziałów.

Promień 1000 m od jawnie wskazanego, zweryfikowanego punktu stacji; bufor od granicy terenu stacji jest inną metodą i musi być oznaczony oddzielnie. Nie używać przesuniętych znaczników mapy TAURON. Obliczenia w metrycznym CRS odpowiednim dla Polski (np. EPSG:2180), z przecięciem geometrii działek i bufora. Mianownikiem udziałów jest cała powierzchnia analizowanego bufora; luki pozostają nieznane. Nie sumować pełnych powierzchni działek przecinających bufor, nie liczyć pikseli kolorowego WMS jako dokładnych danych powierzchniowych. Kontrolować duplikaty, nakładanie geometrii, braki, daty i dokładność lokalizacji stacji.

Wynik musi zawierać daty, źródła kategorii i geometrii, pokrycie danymi i metodę. Nie potrzebujemy nazwisk właścicieli. Publiczny charakter gruntu nie dowodzi jego dostępności inwestycyjnej ani łatwiejszego pozyskania.

## Wykonalność

Geometria i obliczenie bufora: CALCULABLE po pozyskaniu prawidłowych wejść. Wiarygodny podział własności w skali kraju: NIEZWERYFIKOWANY, zależny od atrybutów i ich znaczenia. Nie opublikowano procentów ani danych przykładowych. Następny krok: sprawdzić interfejs mapy grup rejestrowych i próbkę działek dla jednej stacji oraz zasady ponownego wykorzystania. Dopiero następnie decyzja o connectorze i module obliczeniowym.

## Aktualizacja 19.09.2026 — interfejs istnieje, lokalne wartości są puste

Odczytano i zachowano [pełny komunikat GUGiK](https://www.geoportal.gov.pl/aktualnosci/nowa-usluga-mapa-wlasnosci-grupy-rejestrowe-dostepna-w-modulach-geoportal-krajowy-i-geodezja-i-kartografia-w-serwisie-www-geoportal-gov-pl/) opublikowany 24.10.2025. Mapa korzysta z powiatowych WFS, prezentuje 16 klas i statystyki kompletności na poziomie kraju, województw i powiatów. Statystyk powiatowych nie wolno przenosić na bufor stacji.

Sprawdzono DescribeFeatureType obu adresów powiatowych: [wfs.php](https://geoportal.powiat.kielce.pl/map/geoportal/wfs.php) oraz [wfse.php](https://geoportal.powiat.kielce.pl/map/geoportal/wfse.php). Schematy działek nie deklarują grupy rejestrowej; zawierają identyfikatory, nazwy obrębu i gminy, datę oraz geometrię. WFS 2.0.0 deklaruje m.in. CRS EPSG:2178, 2180 i 4326. Nie pobierano działek z tych interfejsów. [Strona powiatu](https://geoportal.powiat.kielce.pl/) zawiera ograniczenia kopiowania i publikowania, jednocześnie wskazując bezpłatną usługę geometrii; zakres praw wymaga wyjaśnienia przed regularnym wykorzystaniem.

Schemat [zbiorczego WFS GUGiK](https://mapy.geoportal.gov.pl/wss/service/PZGIK/EGIB/WFS/UslugaZbiorcza) deklaruje opcjonalne pole `GRUPA_REJESTROWA`. Dwa zapytania GetFeature z COUNT=3 zwróciły:

| Próba | Zwrócone działki | Wypełniona grupa | Pusta grupa |
|---|---:|---:|---:|
| Szerszy prostokąt otoczenia, zwrócone obiekty z obrębu Brzeziny | 3 | 0 | 3 |
| Mały prostokąt przy punkcie stacji, obręb Radkowice | 1 | 0 | 1 |

W drugiej próbce zwrócono identyfikator 260403_5.0011.425/7; to odpowiedź na okno przestrzenne, nie potwierdzenie własności stacji ani pełnej granicy jej terenu. Pole DATA również puste. Kontrola granic odpowiedzi wykazała współrzędne w oczekiwanym otoczeniu; nie wykonano pełnej walidacji geometrii ani obliczeń powierzchni. Te cztery rekordy nie są losową próbą ani inwentaryzacją bufora. Nie można stwierdzić na ich podstawie, że cały powiat nie ma danych. Brak wartości nie oznacza gruntu prywatnego.

Wynik dostępności zapisano w `data/reference/land_ownership_probe_2026-09-19.json`, a daty pobrania, URL i hashe w dwóch manifestach `probe_results_land_ownership_2026-09-18.json` i `probe_results_land_ownership_2026-09-19.json`. Archiwum dziewięciu surowych plików: `data/archives/land_ownership_discovery_2026-09-19.zip`; manifest `data/catalog/land_ownership_archive_2026-09-19.json`. Archiwum wymaga osobnej prywatnej kopii zapasowej. Testowany inspektor odróżnia pole nieobecne od pustego i nie przypisuje kategorii własności.

Potrzeba NEED-021 trafia do rejestru zasilającego raport: eksport działka–grupa rejestrowa–data, bez danych osobowych. Moduł pozostaje w rozpoznaniu; nie podano powierzchni ani procentów. Nadal do sprawdzenia: interfejs samej mapy własności, inne źródła dla braków, znaczenie kategorii i zasady wykorzystania.

## Bezpośrednia Mapa własności — weryfikacja 19.09.2026

Odczytano oficjalny [WMS GetCapabilities](https://mapy.geoportal.gov.pl/wss/ext/MapaWlasnosci?SERVICE=WMS&REQUEST=GetCapabilities). Usługa WMS 1.3.0 udostępnia `dzialki_polygon` (maksymalny mianownik skali 26000) i `dzialki_stats_pow_polygon`. GetFeatureInfo w HTML zwraca atrybuty, natomiast text/plain w tej próbie zwrócił wyłącznie oznaczenie obiektu. Zadeklarowany GetMap application/json sprawdzono w małym prostokącie: wynik to siatka UTFGrid z pustym `data`, nie GeoJSON ani eksport geometrii. Nie wykorzystujemy jej do liczenia powierzchni. Pozostałych formatów wektorowych nie zweryfikowano.

Zapytanie punktowe przy 50.78798, 20.52238 zwróciło działkę **260403_5.0011.425/7**, grupę **0 = brak danych**, czas pozyskania z WFS **2026-09-17 00:07:28.008347** (bez strefy czasowej w źródle). To czas pobrania przez usługę, nie data zmiany własności. Skrypty odpowiedzi potraktowano jako tekst; nie wykonano ich.

Statystyka **2604 — powiat kielecki** podaje **264634 działki**, **264634 bez grupy**, **0 duplikatów**, po **0** w grupach 1–16. Wskazana data **17.09.2026 00:07** dotyczy pobrania ostatniego podzbioru. Są to REPORTED liczby w konkretnej migawce usługi; nie dowodzą braku kategorii w źródłowej EGiB ani pełnej kompletności geometrii. Nie są procentami powierzchni bufora 1 km. Wynik jest mocniejszy od wcześniejszych czterech próbek: obecna mapa nie dostarczy brakujących grup w tym powiecie.

Odpowiedź zawiera opisy 16 grup. Grupy 1/2 rozróżniają SP bez/z użytkowaniem wieczystym; 3 dotyczy podmiotów państwowych; 7 osób fizycznych; 15 spółek prawa handlowego. **Grupy 15 nie klasyfikujemy automatycznie jako prywatnej** — sam rodzaj podmiotu nie określa struktury jego kapitału. Zachowujemy surową grupę i rozdział własności od użytkowania; docelowe uproszczenie wymaga weryfikacji znaczenia kategorii.

Technicznie wykonano sześć małych zapytań łącznie z capabilities, bez uwierzytelniania. `Fees=NONE` i `AccessConstraints=NONE` to metadane usługi, nie pełna analiza praw do komercyjnego importu i redystrybucji. Częstotliwość i limity nieustalone. Nie uruchomiono cyklicznego pobierania.

Odtwarzalność: `scripts/build_ownership_map_probe.py` sprawdza hash HTML i odtwarza `data/reference/ownership_map_probe_2026-09-19.json`. Inspektor kontroluje identyfikator powiatu, obecność 16 grup i zgodność sum; nie wykonuje JavaScript. Surowe sześć odpowiedzi zapisano w `data/archives/ownership_map_discovery_2026-09-19.zip`, manifest w `data/catalog/ownership_map_archive_2026-09-19.json`. Archiwum wymaga osobnej prywatnej kopii zapasowej.

Dalszy kierunek KSE-054: kontrola kompletności powiatu przed pobieraniem działek, następnie lokalna kontrola pokrycia bufora. Powiat z choćby częściowo wypełnionymi grupami może posłużyć do testu metody; nie przeniesiemy jego danych do Radkowic. NEED-021 doprecyzowano jako eksport z EGiB z kategorią, datą i zasadami użycia, bez danych osobowych. Rejestry zasilą następny raport Excel; pliku XLSX w tym kroku nie regenerowano.
