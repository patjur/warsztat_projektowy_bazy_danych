### Stwórzmy główną aplikację. Będzie to program konsolowy pozwalający wysyłać i odczytywać wiadomości. Aplikacja powinna przyjmować od użytkownika następujące argumenty:

* -u, --username – nazwa użytkownika,
* -p, --password – hasło użytkownika,
* -t, --to – nazwa użytkownika, do którego ma zostać wysłana wiadomość,
* -s, --send – treść wiadomości,
* -l, --list – żądanie wylistowania wszystkich komunikatów użytkownika (flaga).

### Do parsowania argumentów użyj biblioteki argparse.

### Aplikacja powinna obsługiwać scenariusze opisane poniżej. Najprościej będzie, przygotować osobną funkcję na każdy, ze scenariuszy. W głównym kodzie programu wystarczy wtedy sprawdzić parametry instrukcję if – elif, a następnie wywołać odpowiednie funkcje.

## Listowanie wiadomości

### Jeśli podczas wywołania aplikacji, użytkownik poda parametry: username i password oraz ustawi flagę -l:

* sprawdź, czy użytkownik istnieje, jeśli nie wyświetl odpowiedni komunikat,
* sprawdź, czy hasło jest poprawne:
  1. jeśli nie, wyświetl odpowiedni komunikat,
  2. jeśli tak, wypisz wszystkie wiadomości wysłane do tego użytkownika.

### Każda z wiadomości powinna zawierać:

* adresata,
* datę wysłania wiadomości,
* treść wiadomości.

## Wysłanie wiadomości

### Jeśli podczas wywołania aplikacji, użytkownik poda parametry: username i password oraz dodatkowo ustawi parametr -t (--to) i -s (--send):

* sprawdź, czy użytkownik istnieje, jeśli nie wyświetl odpowiedni komunikat,
* sprawdź, czy hasło jest poprawne:
  1. jeśli nie, wyświetl odpowiedni komunikat,
  2. jeśli tak:
    * sprawdź, czy adresat wiadomości istnieje (--to), jeśli nie, poinformuj o tym użytkownika,
    * sprawdź, czy wiadomość jest krótsza, niż 255 znaków:
      1. jeśli nie, wyświetl odpowiedni komunikat,
      2. jeśli tak, utwórz wiadomość i zapisz ją do bazy danych.

## Pomoc

### Jeśli użytkownik poda inny zestaw parametrów, należy wyświetlić mu panel pomocy. Można to zrobić, wywołując: metodę print_help z obiektu parsera.

#### Przykład:

import argparse

parser = argparse.ArgumentParser()
parser.print_help()