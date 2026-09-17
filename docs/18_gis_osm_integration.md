# GIS i OpenStreetMap — wkład do oceny przyłączenia

Weryfikacja: 2026-09-17. Etap: audyt źródeł i próbka Radkowic. Warstwa OSM nie jest jeszcze włączona do mapy aplikacji ani do obliczeń dostępnej mocy.

## Co wnoszą oba rodzaje danych

| Dane | Przydatność | Granica interpretacji |
| --- | --- | --- |
| Prywatna kompilacja GIS deklarowana jako stan 2024 | Lokalizacja i nazwy stacji, historyczne grupy, wpisy o inwestycjach i odnośniki do publikacji | Rekord nie musi oznaczać unikalnego obiektu; grupa nie potwierdza połączenia elektrycznego. Licencja kompilacji pozostaje nieustalona — NEED-012. |
| Linie w kompilacji | Poszukiwanie planów i modernizacji | Warstwy inwestycyjne nie stanowią pełnej ewidencji istniejących linii. |
| OpenStreetMap | Geometrie, identyfikatory węzłów i odcinków, tagi napięcia, pola stacji i transformatory | Źródło społecznościowe klasy G; brak gwarancji kompletności, aktualnego układu pracy i parametrów elektrycznych. |
| Dokumenty operatorów | Potwierdzanie parametrów, inwestycji, punktów przyłączenia i zakresów | Dokument musi dotyczyć tego samego obiektu, zakresu i okresu. |

Szczegółowe wyniki kompilacji użytkownika pozostają w prywatnym raporcie. Ogólny Excel opisuje metodę i ograniczenia, bez importowania prywatnych rekordów.

## Mapa wskazana przez użytkownika

[Mapa ebin.josm.pl](https://ebin.josm.pl/electricity/) korzysta z danych OSM i kafli wektorowych. Sprawdzono HTML, map.js, locales.js oraz [TileJSON dla Polski](https://tiles.josm.pl/data/vector-power-poland.json). Warstwy metadanych: substation, substation_label, high_lines, minor_lines. Nie pobierano masowo kafli. Źródło katalogowe: EBIN_ELECTRICITY.

HTML deklarował aktualizację mapy 2026-02-26T15:27:19Z. Nie jest to data wszystkich danych OSM. [Obiekt Radkowice, way 199098055](https://www.openstreetmap.org/way/199098055), pobrany 2026-09-17, miał wersję 14 i datę edycji 2026-06-27T14:43:13Z. Data edycji nie oznacza odbioru ani uruchomienia urządzeń.

## Rzeczywista próbka Radkowic

Źródła OSM_RADK_STATION_OBJECT i OSM_RADK_STATION_AREA obejmują obiekt stacji oraz niewielki obszar wokół niego. Odpowiedź API zawiera pełne geometrie również poza prostokątem zapytania: 2679 elementów, z czego 754 z tagiem power. Nie są to liczby urządzeń stacji.

Audyt przestrzenny wybrał 69 rekordów: 1 obszar stacji, 26 portali, 39 obiektów liniowych przecinających obszar stacji i 3 punkty transformatorów wewnątrz obszaru. Dwa z tych transformatorów mają tagi strony pierwotnej 220 kV i wtórnej 110 kV. Brak znamionowej mocy MVA. Trzeci ma typ distribution bez napięcia. Liczba odcinków OSM nie jest liczbą niezależnych linii lub obwodów.

Wśród odcinków występują tagi pól 110 i 220 kV. Brak zmapowanych elementów power=switch w tej odpowiedzi nie dowodzi braku fizycznych łączników. Relacje obwodów pozostają w surowym XML, lecz audyt nie rozwiązuje ich do topologii elektrycznej. Tag PSE na całym obszarze stacji nie potwierdza własności części 110 kV ani granicy własności transformatorów.

Wartości tagów są REPORTED przez społeczność OSM, nie przez operatora. Konwersja napięć z V do kV i selekcja przestrzenna są CALCULATED. Połączenie elektryczne, własność wyposażenia, obciążenie i dostępna moc pozostają UNKNOWN. Nie uruchomiono power-flow ani punktacji na podstawie tej próbki.

## Dostęp i licencja

[OSM copyright](https://www.openstreetmap.org/copyright) określa licencję ODbL, obowiązek uznania autorstwa i warunki dalszego wykorzystania bazy. Osobno trzeba rozpatrywać warunki serwisu kafli i kodu mapy; ich dostępność nie jest zgodą na nieograniczone korzystanie z infrastruktury serwisu. Własny wynik OSM przechowujemy oddzielnie od prywatnej kompilacji.

Dwie ograniczone próby Overpass zwróciły HTTP 406; zapisano je w overpass_access_2026-09-17.json. To problem dostępu, nie dowód braku danych. Następnie wykonano dwa odczyty głównego API OSM dla rozpoznania próbki. [Polityka API](https://operations.osmfoundation.org/policies/api/) wskazuje jego przeznaczenie edycyjne; nie wybieramy go jako cyklicznego zaplecza aplikacji. Kolejny etap powinien wykorzystywać wyciąg PBF albo odpowiednio dobrany serwis Overpass, z cache, identyfikacją klienta i poszanowaniem limitów. [Zasady publicznego Overpass](https://dev.overpass-api.de/overpass-doc/en/preface/commons.html) również nie uzasadniają nieograniczonego ruchu aplikacji.

## Odtwarzanie i następny krok

Manifest probe_results_osm_radkowice_2026-09-17.json zawiera sześć plików wejściowych, URL, daty pobrania i SHA-256. Archiwum osm_radkowice_discovery_2026-09-17.zip jest lokalnym, ignorowanym przez Git dziewiątym archiwum źródeł; manifest jest wersjonowany. Audyt można odtworzyć bez ponownych zapytań:

```powershell
.venv/Scripts/python.exe scripts/audit_osm_radkowice.py --output data/reference/osm_radkowice_station_audit_replay.json
```

Plik wyjściowy musi być nowy. Referencja: data/reference/osm_radkowice_station_audit_2026-09-17_v2.json. Parser odrzuca brakujące węzły, niepoprawną geometrię, powtórzone identyfikatory i nieprawidłowe współrzędne. [Dokumentacja tagu voltage](https://wiki.openstreetmap.org/wiki/Key:voltage) stanowi podstawę konwersji jednostek, bez sumowania napięć rozdzielonych średnikiem.

Następny krok: regionalna warstwa geometrii OSM i jawni kandydaci połączeń, następnie porównanie z dokumentami operatorów. Przecięcie linii na mapie ani bliskość stacji nie utworzy automatycznie potwierdzonej krawędzi grafu. Pełne pokrycie polskiej sieci nie zostało potwierdzone.
