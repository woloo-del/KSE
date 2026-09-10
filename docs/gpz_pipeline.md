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
