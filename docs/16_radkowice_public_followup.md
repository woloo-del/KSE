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

## Pełna decyzja i rozróżnienie pól 8/6 — dalsza weryfikacja 15.09.2026

Pozyskano [pełną decyzję RDOŚ WOO-I.420.7.2025.PJ/PP.14](https://www.gov.pl/attachment/27ef7a8e-5094-4391-be1c-7e23cb1038b2)
z 04.12.2025, 8 stron. Strona 3, sprawdzona również na renderze PDF, opisuje
planowane zdjęcie przęsła od słupa 81 do pola 8 i budowę przęsła do pola 6.
Podana długość około 60 m dotyczy wyłącznie przebudowywanego odcinka, nie całej
linii Radkowice–Kielce Piaski. Klasyfikacja: REPORTED, jakość C, zakres FUTURE GRID.
Opis dotychczasowego układu jest stanem opisanym w dokumencie, a nie zweryfikowaną
topologią na 15.09.2026. Data wykonania i ostateczność decyzji pozostają UNKNOWN.

To konkretny dowód planowanej zmiany zakończenia linii. Nie łączymy go automatycznie
z mostem, przypisaniami inwestycji, zajętością pól ani dodatkowymi MW. NEED-006
w rejestrze raportowym wskazuje teraz potrzebę aktualnego schematu lub protokołu
potwierdzającego wykonanie tej zmiany. Nie zamykamy potrzeby całościowego statusu robót.

Źródło RDOS_RADK_PIASKI_DECISION_2025 pobrano bez konta, HTTP 200; ekstrakcja
tekstu jest możliwa. Nie ustalono API ani częstotliwości zmian tego załącznika.
Licencja i prawa do ewentualnych materiałów osób trzecich wymagają osobnej oceny;
nie wywodzimy nieograniczonej redystrybucji z samej dostępności PDF. Zachowano bajty,
SHA-256, manifest probe_results_radkowice_decision_2026-09-15.json i lokalny ZIP
 data/archives/radkowice_decision_2026-09-15.zip; kopia zewnętrzna niepotwierdzona.
Katalog po dodaniu dokumentu zawiera 64 źródła.

Sprawdzono również publiczny interfejs [postępowań PSE](https://przetargi.pse.pl/open-auctions.html)
i [wyników](https://przetargi.pse.pl/auction-result-publication.html), filtr nazwy
„Radkowice”. Pierwszy nie zwrócił rekordów; drugi pokazał dwa starsze opracowania
projektowe (AU-001312, AU-000861). To wynik konkretnego widoku i filtra, nie dowód
braku przetargu lub wykonawcy. Wynik nie jest snapshotem API i nie zasila modelu.
Trop TED 771822-2025 oraz informacje z agregatorów pozostają niezweryfikowane:
odczyt TED nie powiódł się. Nie przyjęto z nich numeru pola mostu ani przypisania BESS.


## 17.09.2026 — nierozstrzygnięty rok lub zakres wymiany transformatora

Nowy przegląd wskazuje różnicę 2023/2025 między raportem wpływu a portalem PSE; źródła i datę sprawdzenia zapisano w sekcji 17.09 w docs/01_data_research.md. Wcześniejsze odczyty portalu pozostają prawidłowymi zapisami jego treści, ale nie stanowią rozstrzygnięcia daty odbioru. Dane źródłowe: `data/reference/radkowice_investment_dates_2026-09-17_v1.json`.

Odtwarzanie: `python scripts/build_radkowice_investment_review.py --output NOWY_PLIK.json`. Skrypt kontroluje hashe, kontekst listy PDF oraz jedną dokładnie oznaczoną sekcję HTML. Błąd schematu zatrzymuje ekstrakcję. Testy obejmują brak roku, sąsiednią inwestycję, powtórzony nagłówek, przypis i rzeczywiste snapshoty. Nie jest to pełny parser raportów PSE. Obie wartości pozostają REPORTED, wybrany rok i dodatkowe MW są null.
