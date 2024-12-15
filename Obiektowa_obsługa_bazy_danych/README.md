## Utwórz osobny moduł (np. models.py). W nim umieść kod z klasami, obsługującymi poszczególne tabele.

# Klasa użytkownika

### Stwórz klasę, obsługującą użytkownika. Powinna ona posiadać następujące atrybuty:

* _id – ustawione podczas tworzenia na -1,
* usename – nazwa użytkownika,
* _hashed_password – zahaszowane hasło użytkownika.

### Udostępnij _id i _hashed_password do odczytu na zewnątrz.

### Dodaj metodę, która pozwoli, na ustawienie nowego hasła (Podpowiedź: możesz użyć settera).

### Dodaj metody do obsługi bazy: save_to_db – zapis do bazy danych lub aktualizacja obiektu w bazie, load_user_by_username – wczytanie użytkownika z bazy danych na podstawie jego nazwy, load_user_by_id – wczytanie użytkownika z bazy danych na podstawie jego id, load_all_users – wczytanie wszystkich użytkowników z bazy danych, delete – usunięcie użytkownika z bazy i nastawienie jego _id na -1.

## Podpowiedzi:

* Wszystkie powyższe metody, powinny przyjmować kursor do obsługi bazy danych.
* Możesz wykorzystać kod, który omówiliśmy w artykule poświęconym wzorcowi projektowemu Active Record. Wystarczy, że dodasz do niego metodę, wczytującą użytkownika z bazy na podstawie jego imienia.

# Klasa wiadomości

### Utwórz teraz klasę, która będzie obsługiwała nasze wiadomości. Powinna ona posiadać następujące atrybuty:

* _id – ustawione podczas tworzenia na -1,
* from_id – id nadawcy, ustawiane podczas tworzenia obiektu,
* to_id – id odbiorcy, ustawiane podczas tworzenia obiektu,
* text – tekst do przesłania,
* creation_data – data utworzenia wiadomości. Podczas tworzenia przypisz do niej None. Ustawisz ją w momencie zapisu do bazy danych.

### Udostępnij _id na zewnątrz.

### Dodaj metody do obsługi bazy:

* save_to_db – zapis do bazy danych lub aktualizacja obiektu w bazie,
* load_all_messages – wczytanie wszystkich wiadomości.

## Podpowiedzi:

Usuwanie wiadomości, nie będzie nam potrzebne.
Metody, będą bardzo podobne do tych z klasy użytkownika. Wystarczy, że lekko je zmodyfikujesz.
Pamiętaj, żeby przetestować, czy biblioteka działa. Możesz wykorzystać scenariusze testowe, opisane w artykule omawiającym Active Record.