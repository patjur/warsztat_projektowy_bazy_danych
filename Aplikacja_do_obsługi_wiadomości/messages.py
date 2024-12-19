import argparse

from psycopg2 import connect, OperationalError

from clcrypto import check_password
from models import User, Message

parser = argparse.ArgumentParser()                                        #Deklarujemy argumenty i sparujemy je z biblioteką
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-l", "--list", help="list all messages", action="store_true")
parser.add_argument("-t", "--to", help="to")
parser.add_argument("-s", "--send", help="text message to send")

args = parser.parse_args()


def print_user_messages(cur, user):
    messages = Message.load_all_messages(cur, user.id)            #Ładujemy wszystkie wiadomości z bazy dancch
    for message in messages:                                      #Przy użyciu pętli for wyświetlamy wiadomości z bazy danych
        from_ = User.load_user_by_id(cur, message.from_id)
        print(20 * "-")
        print(f"from: {from_.username}")
        print(f"data: {message.creation_date}")
        print(message.text)
        print(20 * "-")


def send_message(cur, from_id, recipient_name, text):
    if len(text) > 255:                                           #Sprawdzamy czy tekst nie jest za długi, jeżeli jest to wyświetlamy komunikat
        print("Message is too long!")
        return
    to = User.load_user_by_username(cur, recipient_name)          #Pobieramy obiekt adresata na podstawie jego nazwy
    if to:
        message = Message(from_id, to.id, text=text)              #Jeżeli adresat istnieje, możemy stworzyć wiadomość i zapisać ją do bazy danych
        message.save_to_db(cur)
        print("Message send")
    else:                                                         #Jeżeli adresat nie istnieje wyświetlamy komunikat
        print("Recipient does not exists.")


if __name__ == '__main__':
    try:
        cnx = connect(database="workshop", user="postgres", password="coderslab", host="127.0.0.1")   #Łączymy się z bazą danych przy użyciu wskazanych parametrów
        cnx.autocommit = True                                                      #Tryb automatycznego zatwierdzania transakcji na TRUE
        cursor = cnx.cursor()                                                      #Stworzenie obiektu kursora, który potrzebny jest do zapytań na bazioe danych
        if args.username and args.password:
            user = User.load_user_by_username(cursor, args.username)
            if check_password(args.password, user.hashed_password):                #Sprawdzamy czy dane logowania użytkownika są poprawne
                if args.list:
                    print_user_messages(cursor, user)
                elif args.to and args.send:
                    send_message(cursor, user.id, args.to, args.send)
                else:
                    parser.print_help()
            else:
                print("Incorrect password or User does not exists!")               #Jeżeli podane dane są niepoprawne to wyświetlamy komunikat
        else:
            print("username and password are required")
            parser.print_help()
        cnx.close()                                                                #Zamykamy połączenie
    except OperationalError as err:
        print("Connection Error: ", err)                                           #Jeśli wystąpił problem z połączeniem wyświetli się komunikat