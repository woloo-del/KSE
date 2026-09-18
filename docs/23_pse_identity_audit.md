# Weryfikacja profili PSE — lista kandydatów GIS

18.09.2026. Etap częściowy KSE-049. Nie zakończono niezależnej walidacji tożsamości stacji.

## Wynik zbiorczego porównania

Porównano 50 profili z zachowanego wykazu PSE (31.07.2026) z 124 rekordami przekazanej przez użytkownika warstwy stacji NN/WN. Rok 2024 jest deklaracją użytkownika o kompilacji; nie ustalono daty obowiązywania każdego rekordu. Pochodzenie kompilacji nie dowodzi niezależności od publikacji PSE ani prawa do jej redystrybucji.

| Wynik | Profile |
|---|---:|
| Jeden kandydat o zgodnej nazwie i wymienionym napięciu | 36 |
| Brak dokładnej nazwy | 12 |
| Zgodna nazwa, napięcia profilu nie wymieniono w etykiecie GIS | 2 |
| Potwierdzone tożsamości na podstawie tego porównania | 0 |

36 kandydatów nie oznacza 36 zweryfikowanych stacji. Kilka profili napięciowych może wskazywać ten sam rekord. Pozostałe 14 profili wymaga poszerzonego rozpoznania, ale wszystkie 50 wymaga kontroli przed nadaniem kanonicznej tożsamości. Brak nazwy nie dowodzi braku stacji. Niewymienienie napięcia nie jest dowodem nieistnienia rozdzielni: etykieta historycznej warstwy może mieć węższy zakres niż punkt przyłączenia w wykazie.

## Metoda

Wykorzystano istniejący czytnik GeoPackage, z kontrolą geometrii i CRS. Dopasowanie usuwa skrajne i powtarzające się odstępy, ignoruje wielkość liter oraz oddziela tylko końcowy, jawny zapis napięć z jednostką kV. Nie usuwa słów „Systemowa”, „SE” ani „planowana”, nie transliteruje polskich liter i nie stosuje podobieństwa nazw. Powtarzające się nazwy trafiają do niejednoznacznych niezależnie od napięcia; powtarzające się lokalizatory lub ID profili zatrzymują przetwarzanie.

Wynik jest INFERRED i zawsze ma `canonical_station_id = null`. Lokalizator kandydata obejmuje tabelę, fid i hash całego źródła. Zachowano hash profili PSE i kodu metody. Nie pobierano mocy z historycznych komórek, nie tworzono relacji elektrycznych ani wniosków o możliwości przyłączenia. Geometria nie bierze udziału w dopasowaniu, ponieważ profile źródłowe PSE nie dostarczają współrzędnych do takiej kontroli.

## Odtworzenie i prywatność

Uruchomienie: `python scripts/audit_pse_gis_candidates.py`.

Pełna kolejka: `data/private/analysis/pse_gis_candidates_2026-09-18_v2.json`. Dane szczegółowe pozostają prywatne i nie trafiają do API ani ogólnego raportu. W raporcie można przedstawić niniejsze zagregowane wyniki i ograniczenia. Skrypt nie nadpisze odmiennego wyniku; odtworzenie wymaga prywatnej kopii oryginalnego GPKG. Wersja v1 była przebiegiem roboczym; v2 stosuje precyzyjne określenie „napięcie niewymienione”, zamiast sugerować sprzeczność.

Źródło profili: [wykaz PSE, stan 31.07.2026](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx), snapshot z 10.09.2026; szczegóły w docs/21_scalability_benchmark.md. Źródło porównawcze: prywatnie przekazany plik `Stacje NN_WN.gpkg`, bez potwierdzonego publicznego URL pierwotnego zbioru. Nie odświeżano tych źródeł przez internet w tym porównaniu.

## Następna bramka

Uzupełnienie z 18.09.2026: [zbiorczy indeks nagłówków portalu PSE](24_pse_bulk_investment_index.md) dostarcza tropów dla 40 profili. Opis budowy Gdańsk Przyjaźń 400/110 kV wyjaśnia, dlaczego brak napięcia w etykiecie GIS wymaga sprawdzenia zakresu, a nie automatycznego odrzucenia. Nie zmienia to statusu kandydatów na potwierdzony.

Dla kandydatów potrzebne jest pierwotne źródło potwierdzające stację, poziom napięcia i zakres czasowy. Dla wyjątków dodatkowo kontrola aliasów, skrótów i planowanego statusu. Nie należy usuwać słowa „planowana” tylko w celu zwiększenia liczby dopasowań. Miernik błędnych tożsamości i czas ręcznej pracy pozostają null — automatyczne wyszukanie kandydatów nie stanowi ręcznego audytu ani próby reprezentatywnej.
