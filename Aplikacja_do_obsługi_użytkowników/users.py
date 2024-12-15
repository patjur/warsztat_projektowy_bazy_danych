import argparse

from psycopg2 import connect, OperationalError
from psycopg2.errors import UniqueViolation

from clcrypto import check_password
from models import User


parser = argparse.ArgumentParser()         #Deklarujemy argumenty i sparujemy je z biblioteką
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password (min 8 characters)")
parser.add_argument("-l", "--list", help="list all users", action="store_true")
parser.add_argument("-d", "--delete", help="delete user", action="store_true")
parser.add_argument("-e", "--edit", help="edit user", action="store_true")

args = parser.parse_args()


def edit_user(cur, username, password, new_pass):
    user = User.load_user_by_username(cur, username)          #Ładujemy użytkownika z bazy
    if not user:
        print("User does not exist!")                         #Sprawdzamy użytkownika czy istnieje, jeśli nie to wyświetlamy komunikat
    elif check_password(password, user.hashed_password):      #Sprawdzamy poprawność hasła, jeżeli nie to wyświetlamy komunikat
        if len(new_pass) < 8:                                 #Sprawdzamy długość hasła, jeśli jest krótsze niż 8 znaków to wyświetlamy komunikat
            print("Password is tho short. It should have minimum 8 characters.")
        else:
            user.hashed_password = new_pass
            user.save_to_db(cur)
            print("Password changed.")                        #Dodajemy nowe hasło i wyświetlamy komunikat
    else:
        print("Incorrect password")


def delete_user(cur, username, password):
    user = User.load_user_by_username(cur, username)
    if not user:
        print("User does not exist!")                         #Sprawdzamy czy dany użytkownik istnieje, jeżeli nie to wyświetlamy komunikat
    elif check_password(password, user.hashed_password):
        user.delete(cur)
        print("User deleted.")                                #Usuwamy użytkownika i wyświetlamy komunikat
    else:
        print("Incorrect password!")                          #Wyświetlamy kounikat o nieprawidłowym haśle


def create_user(cur, username, password):
    if len(password) < 8:
        print("Password is tho short. It should have minimum 8 characters.")   #Sprawdzamy długość hasła, jeżeli jest za krótkie to informujemy komunikatem że powinno mieeć min. 8 znaków
    else:
        try:
            user = User(username=username, password=password)
            user.save_to_db(cur)
            print("User created")                            #Tworzymy użytkownika i wyświetlamy komunikat
        except UniqueViolation as e:
            print("User already exists. ", e)                #Jeżeli taki użytkownik już istnieje wyświelamy komunikat


def list_users(cur):
    users = User.load_all_users(cur)
    for user in users:
        print(user.username)                                #Wyświetlamy wszystkich użytkowników


if __name__ == '__main__':
    try:
        cnx = connect(database="workshop", user="postgres", password="coderslab", host="127.0.0.1")   #Łączenie się z bazą danych wykorzystując podane parametry
        cnx.autocommit = True      #Tryb automatycznego zatwierdzania transakcji na TRUE
        cursor = cnx.cursor()      #Stworzenie obiektu kursora, który potrzebny jest do zapytań na bazioe danych
        if args.username and args.password and args.edit and args.new_pass:
            edit_user(cursor, args.username, args.password, args.new_pass)
        elif args.username and args.password and args.delete:
            delete_user(cursor, args.username, args.password)
        elif args.username and args.password:
            create_user(cursor, args.username, args.password)
        elif args.list:
            list_users(cursor)
        else:
            parser.print_help()             #Kiedy użytkownik poda inny zestaw parametrów, wyświeli mu się panel pomocy
        cnx.close()                         #Zamykamy połączenie
    except OperationalError as err:
        print("Connection Error: ", err)    #Jeśli wystąpił problem z połączeniem wyświetli się komunikat