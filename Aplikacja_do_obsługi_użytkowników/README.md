## Utwórzmy aplikację, obsługującą naszych użytkowników. Będzie to aplikacja konsolowa, przyjmująca argumenty wprowadzone przez użytkownika. Wykorzystaj do tego bibliotekę argparse. Aplikacja powinna obsługiwać następujące parametry: * -u, --username – nazwa użytkownika, * -p, --password – hasło użytkownika, * -n, --new_pass – nowe hasło, * -l, --list – listowanie użytkowników, * -d, --delete – usuwanie użytkownika, * -e, --edit – edycja użytkownika.

## Aplikacja powinna obsługiwać scenariusze opisane poniżej. Najprościej będzie, przygotować osobną funkcję na każdy, ze scenariuszy. W głównym kodzie programu wystarczy wtedy sprawdzić parametry instrukcję if – elif, a następnie wywołać odpowiednie funkcje.

# Tworzenie użytkownika

## Jeśli podczas wywołania aplikacji, użytkownik poda tylko parametry: username i password:

* jeśli użytkownik o podanej nazwie istnieje – zgłaszamy błąd (Podpowiedź: możesz przechwycić błąd: UniqueViolation),
* jeśli nie ma takiego użytkownika:
 1. jeśli hasło ma co najmniej 8 znaków, należy go utworzyć, korzystając z podanych danych (pamiętaj, o zapisaniu obiektu do bazy danych),
 2. jeśli hasło jest za krótkie, należy wyświetlić odpowiedni komunikat.

# Edycja hasła użytkownika

## Jeśli podczas wywołania aplikacji, użytkownik poda parametry:

* username,
* password,
* edit,
* new_pass, powinniśmy:
* sprawdzić, czy użytkownik istnieje
* sprawdzić, czy hasło jest poprawne:
 1. jeśli tak, sprawdzamy, czy nowe hasło (new_pass) ma wymaganą długość:
   - jeśli jest krótsze niż 8 znaków, zgłaszamy to odpowiednim komunikatem,
   - jeśli jest wystarczającej długości, ustawiamy nowe hasło,
 2. jeśli hasło jest niepoprawne, zgłaszamy to odpowiednim komunikatem.

Podpowiedź: Do sprawdzenia hasła, możesz wykorzystać funkcję check_password z biblioteki clcrypto.

# Usuwanie użytkownika

## Jeśli podczas wywołania aplikacji, użytkownik poda parametry:

* username,
* password,
* delete, należy:
* sprawdzić poprawność hasła:
 1. jeśli jest poprawne – usunąć użytkownika z bazy danych,
 2. jeśli jest niepoprawne – poinformować o tym użytkownika odpowiednim komunikatem np. "Incorrect Password!.

# Listowanie użytkowników:

## Jeśli podczas wywołania aplikacji, użytkownik poda parametr -l (--list), należy wypisać listę wszystkich użytkowników.

# Pomoc

## Jeśli użytkownik poda inny zestaw parametrów, należy wyświetlić mu panel pomocy. Można to zrobić, wywołując: metodę print_help z obiektu parsera.

Przykład:

import argparse

parser = argparse.ArgumentParser()
parser.print_help()