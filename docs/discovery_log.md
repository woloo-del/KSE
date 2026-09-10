# Zakres odkrywania interfejsów — 10.09.2026

Uzupełnienie [raportu](01_data_research.md) i [katalogu](data_sources.md). To macierz wyników pierwszego badania, nie certyfikat nieistnienia nieodnalezionego interfejsu.

Badano następujące rodziny: API/REST, pliki JSON/CSV/XLSX/XML/GeoJSON, WMS/WFS/WMTS/ArcGIS REST, HTML/PDF/BIP oraz GitHub. `Nie potwierdzono` oznacza wynik przeglądu oficjalnych stron i wyszukiwania interfejsów w tym etapie. Nie przeprowadzono pełnej inspekcji ruchu wszystkich aplikacji mapowych.

| Rodzina | API / dane strukturalne | GIS | Dokumenty / pozostałe | Dowód w katalogu |
|---|---|---|---|---|
| PSE | Działa API JSON, pobrano OpenAPI i XLSX | Nie potwierdzono publicznego operacyjnego WFS/ArcGIS ani pełnej topologii API | PDF mocy i planów; dokumentacja strukturalna B2B to odrębny zakres | PSE_API, PSE_PIPELINE, PSE_CAPACITY, PSE_STRUCT_B2B |
| PGE | Brak potwierdzenia; odczyt blokowany | Nie potwierdzono | Wskazania PDF; treść niepotwierdzona | PGE_LANDING, PGE_EXPORT_DISCOVERY, PGE_PLAN_DISCOVERY |
| ENEA | Nie potwierdzono publicznego API; Power BI w HTML | Viewer; nie potwierdzono WFS/WMS/GeoJSON do pobierania infrastruktury | Wykazy, kryteria SN, plan | ENEA_MAP, ENEA_PIPELINE, ENEA_PLAN |
| TAURON | Nie potwierdzono publicznego API portalu | Viewer dostępności; brak potwierdzonego eksportu topologii | Pobrany PDF wykazu, indeks planu | TAURON_PIPELINE, TAURON_MAP, TAURON_PLAN |
| Energa | Nie potwierdzono publicznego API badanych wykazów | Nie potwierdzono operacyjnej topologii GIS | Pobrane osobne PDF eksport/import/pipeline; plan | ENERGA_* |
| Stoen | Nie potwierdzono publicznego API | Nie potwierdzono operacyjnej topologii GIS | PDF kierunkowych mocy; linki rejestrów i planu | STOEN_* |
| KGHM OSDn | Linki do arkuszy; nie zwalidowano załączników | Nie potwierdzono | Publiczne informacje OSD i rejestry | KGHM_OSD |
| GUGiK | Pliki i GeoParquet; dokumentowane usługi | Potwierdzony WFS GetCapabilities EGiB; dokumentacja WMS/WMTS/WCS pozostałych produktów | Dane katastralne/topograficzne/terenowe, integracja MPZP | GUGIK_* |
| GDOŚ | OGC XML | Potwierdzony WFS GetCapabilities, opis WMS | Ochrona przyrody; akty prawne osobno | GDOS_GIS |
| Wody Polskie / BDL | Zależnie od produktu | Opis WMS i WFS/WMTS BDL, adresy usług ArcGIS; brak testu całego pobierania | Procedury udostępniania | WODY_SIGW, BDL_GIS |
| ENTSO-E | REST/XML z tokenem, nie wykonano zapytania | Mapa PDF nie jest API topologii | Warunki ponownego wykorzystania według datasetu | ENTSOE_TP, ENTSOE_MAP |
| OSM/OpenInfraMap | Regionalny PBF; Overpass jako wskazany kanał małych ekstraktów | Geometria społecznościowa, nie potwierdzone relacje operatora | ODbL; OpenInfraMap nie jest drugim źródłem | OSM_LICENSE, GEOFABRIK_PL, OPENINFRAMAP |
| Modele otwarte | Repozytoria GitHub i formaty modeli | Geometria i parametry mogą być inferowane | PyPSA-Eur i historyczny MATPOWER nie są aktualnym operacyjnym KSE | PYPSA_EUR, MATPOWER_POLAND |
| URE / BIP / KRS | Rejestry, punkt wejścia OpenAPI KRS; brak pełnego krajowego pipeline API | Nie potwierdzono kompletnego połączenia z GPZ | HTML/PDF, rozproszone postępowania; Ekoportal wymaga wyjaśnienia dostępności | URE_REGISTERS, BIP_ENV_DISCOVERY, KRS_API_DOCS |

## Otwarte działania po badaniu

- Sprawdzić prawa i warunki dla wybranych konkretnych zbiorów; brak pełnego przeglądu robots.txt i umów dostępu nie pozwala uznać wszystkich scraperów za gotowe do wdrożenia.
- Wyjaśnić datę pipeline Energi; ponownie sprawdzić zwykły dostęp do PGE.
- Zweryfikować możliwość oficjalnego eksportu ENEA/TAURON bez uzależniania connectora od prywatnych mechanizmów interfejsu.
- W wybranym regionie przejść z ogólnych indeksów BIP do aktualnych rejestrów konkretnych organów i prawdziwych dokumentów projektowych.
- Testować GetFeature i schematy wybranych warstw GIS na małym obszarze, a następnie sprawdzić CRS, geometrię, limity i licencję.

Nie traktować powyższej listy jako zaległej implementacji w etapie 1: są to ujawnione warunki wejścia do dalszych etapów. Źródła o niepotwierdzonej treści pozostają oznaczone jako niepotwierdzone.
