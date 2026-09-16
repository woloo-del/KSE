# Widok GPZ — projekty istniejące i pipeline

Wymaganie użytkownika z 10.09.2026. Status: specyfikacja do pilota, bez wdrożonego interfejsu i bez wprowadzania danych projektowych.

Po wybraniu GPZ użytkownik powinien zobaczyć projekty w trzech grupach, z datą stanu źródeł i możliwością obejrzenia dowodów:

| Grupa | Warunek zakwalifikowania | Szczegóły widoczne dla użytkownika |
|---|---|---|
| A. Przyłączone | Źródło potwierdza wykonane przyłączenie do tej stacji | Data przyłączenia, status eksploatacji, jeśli osobno znany; sama umowa lub WP nie wystarcza |
| B. Planowane do przyłączenia | Udokumentowane planowane przyłączenie, bez potwierdzenia wykonania | Osobno: plan wstępny, wydane WP, umowa, budowa; plan bez wniosku nie jest rezerwacją mocy |
| C. Wnioski oczekujące na odpowiedź | Źródło wprost potwierdza oczekiwanie na rozstrzygnięcie dla danego wniosku i wskazuje GPZ | Data złożenia, data aktualizacji statusu i źródło; nie utożsamiać pustej daty WP z potwierdzonym brakiem odpowiedzi |

Jeżeli wiadomo tylko, że złożono wniosek, a dalszego przebiegu nie znamy, rekord otrzymuje **„Wniosek złożony — dalszy status nieznany”**. Jest pokazywany obok grupy C, ale poza liczbą potwierdzonych oczekujących. Brak informacji o odpowiedzi w publicznym źródle nie dowodzi, że operator nie odpowiedział.

Odmowy, wycofania, wygaśnięcia i anulowania pozostają w historii i osobnym filtrze, poza aktywnym pipeline. Przeczące sobie lub nieporównywalne czasowo źródła powodują oznaczenie konfliktu zamiast wymuszonego przypisania do jednej grupy. Grupy dotyczą wybranego momentu wiedzy; nie obiecują bieżącego statusu niezależnego od dat publikacji.

## Powiązanie projektu ze stacją

Podstawowy widok i sumy obejmują projekty z potwierdzonym w źródle wskazaniem danego GPZ. Dla planowanego projektu jest to potwierdzone **wskazanie planowanego punktu**, a nie fizycznie istniejące połączenie. Powiązania prawdopodobne lub inferowane można pokazać osobno z uzasadnieniem; nie należy ich po cichu dodawać do pewnego zestawienia.

Wniosek bez określonego miejsca przyłączenia pozostaje nieprzypisany. Sama bliskość geograficzna nie uzasadnia umieszczenia go w pipeline danego GPZ. Projekty z alternatywnymi punktami przyłączenia wymagają osobnych wariantów i nie mogą być wielokrotnie liczone w zestawieniach zbiorczych.

## Informacje i podsumowania

Każdy wiersz: projekt, inwestor/SPV jeśli jawny, technologia, napięcie/punkt przyłączenia, moc eksportu i importu, limity PCC, MWh jeśli podane, status źródłowy i znormalizowany, daty oraz link do dokumentu i miejsca w nim. Puste wartości pozostają nieznane; nie zastępujemy ich zerem.

Dla każdej grupy podajemy liczbę unikalnych znanych projektów i odrębne sumy eksportu/importu z jawną definicją agregowanej mocy. Zainstalowane MW nie są zamienne z mocą przyłączeniową lub limitem PCC. Pokazujemy także liczbę rekordów z brakującą mocą. BESS i hybrydy zachowują oba kierunki i ograniczenia PCC.

Jedna inwestycja może mieć wiele wniosków, wersji i etapów. Model musi rozróżniać `project_id` i `connection_application_id`. Szczegóły wniosków mogą być widoczne, ale suma projektów nie może wielokrotnie dodawać tej samej inwestycji. Przy równoległych nierozstrzygniętych wariantach moc projektu pozostaje niejednoznaczna zamiast wyboru wygodnej wartości.

Nagłówek raportu: **„Znane projekty na podstawie wskazanych źródeł”**, z datą i zakresem pokrycia. Brak pozycji oznacza „brak znalezionych danych”, dopóki źródło nie potwierdza kompletnej listy i zera projektów. Sumy pipeline nie są obciążeniem GPZ ani liczbą MW, którą można automatycznie odjąć od dostępności publikowanej przez operatora.

## Warunki gotowości pilota

1. Wybrana stacja ma jednoznaczny identyfikator, aliasy i operatora.
2. Parser zachowuje daty, statusy źródłowe i dowody powiązania ze stacją.
3. Odróżnia wykonane przyłączenie od WP/umowy oraz potwierdzone oczekiwanie od nieznanego statusu.
4. Deduplikacja działa dla kolejnych etapów i wielu wniosków tego samego projektu.
5. Sumy nie mieszają importu/eksportu, mocy zainstalowanej i limitów PCC.
6. Testy na rzeczywistych dopuszczonych próbkach sprawdzają wszystkie dostępne kategorie; brakujące przypadki nie są przedstawiane jako dane produkcyjne.

Źródła kandydackie i ich ograniczenia są już opisane w [katalogu](data_sources.md) oraz [macierzy wykonalności](02_feasibility_matrix.md). Specyfikacja nie potwierdza kompletności takich list dla wszystkich GPZ w Polsce.

## Działający widok badawczy Radkowic — 16.09.2026

Skrypt `scripts/build_radkowice_pipeline.py` ponownie odczytuje zachowany XLSX PSE,
sprawdza hash i nagłówki przez istniejący ekstraktor, a następnie generuje
`data/reference/radkowice_pipeline_view_2026-07-31_v1.json`.
Stan dokumentu: **31.07.2026**, nie aktualny stan na dzień uruchomienia.

| Wpis PSE | Eksport przyłączeniowy MW | Import przyłączeniowy MW | Wiersz |
|---|---|---|---|
| MEE Chałupki | 96,96 | 98,8992 | 787 |
| MEE Radkowice | 50 | 50 | 843 |
| MEE Chęciny | 100 | 102 | 847 |

Wszystkie trzy mają źródłowy status „UMOWA O PRZYŁĄCZENIE obowiązująca” i wskazanie
Radkowice 220 kV; kwalifikujemy je do B — planowane, bez dowodu wykonania.
Suma **wierszy tej próbki**: eksport 246,96 MW, import 250,8992 MW (CALCULATED).
To dokładne dodawanie wartości dokumentu, nie taka precyzja oceny sieci. Nie jest
to bilans przepływów, dostępna moc, suma zarezerwowana na moście ani pełna,
zdeduplikowana liczba inwestycji. Identyfikatory zachowują tożsamość wiersza,
nie udają kanonicznych identyfikatorów projektów między źródłami.

Źródło: [PSE — wykaz na 31.07.2026](https://www.pse.pl/documents/20182/51490/Informacje_publikowane_zgodnie_z_Art_7_ust_8l_ustawy_PE_stan_na_31_07_2026.xlsx),
arkusz „Wykaz wspólny”, kolumny I/J (kierunki MW), Q (status), E/F (punkt/napięcie).
Pobrano 10.09.2026; lokalny odczyt i zgodność SHA-256 sprawdzono 16.09.2026.
Nie pobierano nowego pliku ani nie potwierdzano aktualności strony operatora.

Dla A i C brak potwierdzających rekordów w tym widoku. Liczba projektów całej
stacji i sumy bez żadnych znanych mocy pozostają null. Nieznany status trafia do
UNKNOWN; przeszła data planowanego rozpoczęcia dostaw nie tworzy przyłączenia.
Brakująca moc pozostaje odrębna od zera. Nie przypisujemy wpisów do miejsc mostu.

Każdy wiersz zachowuje proweniencję; każda suma wskazuje użyte rekordy i formułę.
Wynik zawiera wersję metody i hashe dwóch skryptów. Ponowienie z tymi samymi
wejściami zachowuje identyczny plik; inna treść pod istniejącą nazwą jest odrzucana.
Nie jest to uniwersalny parser statusów PSE, pełny connector ani realizacja KSE-021.
Nadal potrzebne są rozstrzygnięcia tożsamości, dane PGE i kompletność źródeł.
