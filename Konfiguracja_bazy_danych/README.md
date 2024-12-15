# Napisz skrypt pythona: create_db.py, w którym:

## Utworzysz bazę danych. Jeśli baza już istnieje, skrypt ma poinformować o tym użytkownika, nie przerywając swojego działania (Podpowiedź: możesz przechwycić błąd: DuplicateDatabase).

## Stworzysz tabelę trzymającą dane użytkownika (users). Powinna posiadać następujące kolumny:

* id – klucz główny (najlepiej typu serial),
* username – ciąg znaków (varchar(255)),
* hashed_password – ciąg znaków (varchar(80)). Jeżeli istnieje już taka tabela, skrypt powinien poinformować o tym użytkownika, nie przerywając swojego działania (Podpowiedź: możesz przechwycić błąd: DuplicateTable).

## Stworzysz tabelę przechowującą komunikaty (messages). Powinna posiadać następujące kolumny:

* id – klucz główny (najlepiej typu serial),
* from_id – klucz obcy do tabeli users,
* to_id – klucz obcy do tabeli users,
* creation_date – timestamp, dodawany automatycznie,
* text – ciąg znaków (varchar(255)). Jeżeli istnieje już taka tabela, skrypt powinien poinformować o tym użytkownika, nie przerywając swojego działania (Podpowiedź: możesz przechwycić błąd: DuplicateTable).

### Pamiętaj o zamknięciu połączenia. Powinieneś też obsłużyć ewentualne błędy połączenia (OperationalError).