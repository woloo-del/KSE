# Rejestr potrzebnych dokumentów i informacji

Aktualizacja: 2026-09-15. Rejestr edytowalny:
`data/project/information_requests.json`. Widok w Excelu: **Potrzebne informacje**.
Przegląd opiera się na dotychczasowej dokumentacji pilota i informacjach użytkownika;
nie jest nową weryfikacją dostępności serwisów operatorów.

Każda potrzeba ma stabilny ID, priorytet, status, potrzebny zakres, wyjaśnienie
zastosowania, następny krok, sposób pracy bez danych, możliwego pomocnika,
datę aktualizacji i podstawę wpisu. P0 dotyczy najbliższego kroku dokumentacyjnego,
P1 dalszej analizy, P2 zakresu bardziej zaawansowanego. Nie są to oceny sieci.

Statusy: Do sprawdzenia; W pozyskiwaniu; Niedostępne; Otrzymano — do oceny zakresu;
Zweryfikowano. Otrzymanie pliku nie zamyka analizy: trzeba jeszcze ocenić jego
wersję, daty, zakres i znaczenie poszczególnych tez. Statusy otrzymania i weryfikacji
wymagają zapisanego potwierdzenia. Nie ustalamy fikcyjnych terminów.

Najpilniejsze dla Radkowic są projekt techniczny mostu (NEED-001, w pozyskiwaniu)
oraz udokumentowane przypisania projektów do konkretnych miejsc (NEED-002).
Odrębne potrzeby obejmują granice PSE/PGE, statusy wniosków, obciążenia, stan
inwestycji sieciowych i parametry modelu elektrycznego. Nazwa stacji w wykazie
PSE nie wypełnia braku przypisań do mostu.

Ekspertyza wpływu (NEED-008) pozostaje niedostępna zgodnie z informacją użytkownika.
Nie ponawiamy prośby i nie blokujemy niezależnej pracy. Przekazane warunki
przyłączenia (NEED-009) są już otrzymane; nie prosimy o ponowne przesłanie.
Ich treść i ustalenia pochodne pozostają poza ogólnym raportem i Git.
NEED-010 dotyczy potwierdzenia niezależnej kopii archiwum, bez danych logowania.

Po otrzymaniu nowej informacji aktualizujemy właściwy ID, datę i status oraz
zachowujemy poprzedni stan w Git. Jeżeli dokument ma ograniczony zakres,
pozostały brak zostaje jawny albo otrzymuje osobny ID. Nie usuwamy pozycji
niedostępnych ani zamkniętych. Rejestr opisuje również informacje, które użytkownik
może znać bez posiadania dokumentu; takie twierdzenia nie zastępują dowodu operatora.

Generator czyta wyłącznie jawnie wskazany rejestr i waliduje ID, statusy, daty
oraz wymagane wyjaśnienia. Eksport jest kontrolowany pole po polu. Nie skanuje
prywatnych folderów. Do rejestru wpisujemy opis potrzeby i ogólny stan procesu,
bez parametrów z poufnych dokumentów, ich lokalnych ścieżek, danych osobowych
i sekretów. Sam walidator nie wykrywa automatycznie poufnych informacji w tekście.

Możesz odpowiadać numerem, np. „NEED-001: mam projekt, rewizja ...” albo
„NEED-004: nie uda się uzyskać”. Zaktualizuję rejestr i kolejny raport.
Zmiany wpisane bezpośrednio w Excel nie wracają automatycznie do rejestru.

16.09.2026: dodano NEED-011 — dwa publiczne dokumenty PGE, których bezpośrednie
pobranie ponownie zwraca HTML zamiast PDF. Dokładne linki są w końcowej sekcji
raportu badawczego. Pomoc polega na przekazaniu oryginalnych plików z datą i URL,
jeśli użytkownik może je zwyczajnie pobrać; nie wymaga przekazywania poświadczeń.
