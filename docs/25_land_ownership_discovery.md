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
