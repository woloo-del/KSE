# Radkowice — uzupełnienie publicznych dowodów, 15.09.2026

## Nowy punkt odniesienia dla projektu mostu

[Ogłoszenie PSE 205815-2025](https://www.pse.pl/documents/20182/5928746423/OKRESOWE_OGLOSZENIE_ROBOTY_BUDOWLANE.pdf/883a7669-eb9a-4650-84f4-cd67502fd545?safeargs=76657273696f6e3d312e31),
publikacja 31.03.2025 (PDF s.37), na s.29 wymienia rozbudowę Radkowic o pole
220 kV i most szynowy. Treść strony sprawdzono również wizualnie.

To REPORTED — planowany zakres zamówienia. Ogłoszenie dotyczy prognozowanych
postępowań od kwietnia 2025 do I kwartału 2026, z możliwością zmian i późniejszym
udostępnieniem wiążącej dokumentacji. Nie potwierdza wykonawcy, rozpoczęcia,
odbioru, geometrii, liczby miejsc ani dostępnych MW. Adres Warszawska 165 jest
wskazany na potrzeby ogłoszenia, nie jako geolokalizacja stacji. Nie wolno
geokodować po nim Radkowic.

NEED-001 pozostaje „W pozyskiwaniu”. Numer ogłoszenia i dokładny zakres pomagają
szukać projektu i dokumentacji postępowania. Nie utożsamiamy automatycznie tego
zamówienia z konkretną rewizją prywatnego projektu ani z wszystkimi etapami stacji.

## Linia Radkowice–Kielce Piaski

[Obwieszczenie RDOŚ Kielce](https://www.gov.pl/web/rdos-kielce/obwieszczenie-regionalnego-dyrektora-ochrony-srodowiska-w-kielcach-z-dnia-04122025-r-znak-woo-i42072025pjpp16)
z 04.12.2025, opublikowane 09.12.2025, informuje o wydaniu decyzji środowiskowej
WOO-I.420.7.2025.PJ/PP.14 dla przebudowy linii 220 kV Radkowice–Kielce Piaski
w ramach zadania stacji, planowanego przez PSE. To REPORTED — informacja o
etapie administracyjnym, nie dowód realizacji lub prawomocności. Zachowano HTML.

NEED-006 uzupełniono o ten trop. Nie połączono automatycznie robót na linii
z zakresem mostu ani przebudową linii 110 kV Radkowice–Wolica.

## Ponowny odczyt portalu PSE

[Portal inwestycji PSE](https://inwestycje.pse.pl/) nadal opisuje etap I rozbudowy
Radkowic jako „w budowie”, etap II jako „w przygotowaniu”, wymianę transformatora
jako zakończoną w 2025 i wcześniejszą rozbudowę jako zakończoną w 2020.
Zakres tych opisów jest zgodny z przeglądem 11.09.2026. Nie ma dowodu, że konkretna
część wspólnego przyłącza została uruchomiona, ani znamionowej mocy wymienionego
urządzenia. Snapshot z 15.09 nie wyznacza początku obowiązywania statusu.

## Automatyzacja i odtwarzanie

Trzy zasoby pobrano bez konta (HTTP 200), zachowano oryginalne bajty i SHA-256.
PDF zawiera tekst, HTML wymaga rozpoznania właściwej sekcji. Nie ustalono API,
GIS, limitów wywołań ani gwarantowanego cyklu dla tych konkretnych publikacji.
To jednorazowy odczyt, bez cyklicznego scrapera. Katalog zawiera obecnie 63 źródła;
aktualizacja dotyczy tych trzech pozycji, nie ponownej weryfikacji całego katalogu.

[Zasady Gov.pl](https://www.gov.pl/web/gov/prawa-autorskie), sprawdzone 15.09.2026,
wskazują CC BY-SA 4.0 dla tekstów oraz zastrzeżenia dotyczące materiałów osób
trzecich. Załączniki i komercyjną integrację trzeba oceniać odrębnie. Dla dokumentu
PSE nie potwierdzono otwartej licencji. Nie deklarujemy nieograniczonej redystrybucji.

Manifest pobrań: `data/catalog/probe_results_radkowice_followup_2026-09-15.json`.
Archiwum lokalne: `data/archives/radkowice_followup_2026-09-15.zip`.
Jego manifest: `data/catalog/radkowice_followup_archive_2026-09-15.json`.
Sprawdzono hashe wszystkich trzech elementów po odczycie z ZIP. Kopia poza
komputerem pozostaje niepotwierdzona. Nie zmieniono wcześniejszych snapshotów.

Tropy niezaliczone do dowodów modelu: prognoza postępowań z innym plikiem PSE
(odczyt web zwrócił błąd), projekt PRSP 2027–2036 i projekt planu PGE 2026–2031
(w tym przyroście tylko wyniki wyszukiwania). Daty z ich snippetów nie zasilają modelu.

Nie uzupełniono fikcyjnie parametrów v2 ani przypisań miejsc. Najbliższy krok to
poszukiwanie dokumentacji konkretnego postępowania i aktualnych dowodów realizacji.
Rejestr potrzeb został uaktualniony; poprzedni Excel pozostaje snapshotem sprzed
tego uzupełnienia, a nowe wpisy trafią do następnego odświeżenia.

Kontrola katalogu obejmuje obecnie wszystkie datowane foldery `data/raw/research`
i dodatkowe manifesty pilota. Identyfikator źródła może wystąpić ponownie przy
nowym pobraniu; unikalna musi być tożsamość snapshotu (źródło, czas, ścieżka).
663 kontrole katalogu przeszły; zachowano cztery wcześniejsze ostrzeżenia źródłowe.
