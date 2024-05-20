## 3. Moduł obsługi klienta zawierający funkcje:
## funkcja 1: rejestracja nowego klienta lub usuwanie danych klienta z bazy
## funkcja 2: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## Nowy klient podaje swoje dane (imie, nazwisko), nadawany jest w/w klientowi losowy numer ID złożony z 4 cyfr
## w folderze DATABASE tworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego będą zapisywane dane wypożyczonej przez klienta książki oraz
## data wypożyczenia a potem zwrotu książki
## funkcja 3: usuwanie danych klienta opcje: względem ID lub NAME
## Wypożyczanie książki/-ek przez użytkownika 2 funkcje:
## funkcja 4: wypożyczenie książki lub kilku książek przez klienta
## funkcja 5: zwrot 1 książki przez klienta

"""
System zarządzania biblioteką

Ten program jest systemem zarządzania biblioteką, który umożliwia rejestrację użytkowników,
usuwanie danych użytkowników, wypożyczanie książek i zwracanie książek. Wszystkie operacje
są zapisywane w plikach CSV, a dane o wypożyczeniach są przechowywane w osobnych plikach
tekstowych dla każdego użytkownika.

Pliki:
    - customer.csv: Przechowuje informacje o zarejestrowanych użytkownikach.
    - address.csv: Przechowuje adresy zarejestrowanych użytkowników.
    - book.csv: Przechowuje informacje o książkach dostępnych w bibliotece.
    - DATABASE/: Katalog przechowujący pliki tekstowe z danymi o wypożyczeniach dla każdego użytkownika.

Funkcje:
    - dec(func)
    - output2()
    - ensure_newline(file_path)
    - register_user(name, email, phone, country, city, street)
    - del_user_name(name)
    - del_user_ID(ID)
    - borrow_books(customer_id, **kwargs)
    - return_book(customer_id, book_to_return)
    - return_books(customer_id, book_to_return)
    - control_panel()
"""

import os
import csv
from datetime import date
import random
import string

file_path = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\customer.csv'

if not os.path.exists('DATABASE'):
    os.makedirs('DATABASE')


def dec(func):
    def wrapper(customer_id, **kwargs):
        # Wyciąganie tytułów książek z argumentów przekazanych przez kwargs
        books_to_return = kwargs.get('books_to_return', [])

        if not books_to_return:
            print("Nie podano żadnych książek do wypożyczenia.")
            return
        for book_to_return in books_to_return:
            book_to_return = book_to_return.strip()  # Usunięcie zbędnych spacji
            func(customer_id, book_to_return)

    return wrapper


def output2():
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)



def ensure_newline(file_path):
    with open(file_path, 'r+') as file:
        #przejście na ostatnia linijke
        file.seek(0, 2)
        file.seek(file.tell() - 1, 0)
        #wczytanie jednego znaku z ostatniej linijki
        last_char = file.read(1)
        if last_char != '\n':
            file.write('\n')




def register_user(name,email,phone,country,city,street):
    customer_file = 'DATABASE/customer.csv'
    ensure_newline(file_path)
    # Generowanie losowego ID klienta
    customer_id = ''.join(random.choices(string.digits, k=4))

    # Aktualna data
    created = date.today()
    updated = date.today()

    try:
        # Zapisanie danych klienta do pliku customer.csv
        with open(file_path, mode='a', newline='') as plik:
            writer = csv.writer(plik)
            writer.writerow([customer_id, name, email, phone, created, updated])
            print(f"Użytkownik został zarejestrowany: {customer_id}, {name}, {email}, {phone}, {created}, {updated}")

        #Zapisanie adresu klienta do adress.csv
        ensure_newline("C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\address.csv")
        with open("C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\address.csv", mode='a', newline='') as plik:
            writer = csv.writer(plik)
            writer.writerow([customer_id, street, city, country])
            print(customer_id, street, city, country)

        # Tworzenie pliku dla klienta do przechowywania danych wypożyczeń
        customer_data_file = f'DATABASE/{customer_id}.txt'
        if not os.path.exists(customer_data_file):
            open(customer_data_file, 'a').close()

    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")





def del_user_name(name):
    found = False
    customer_id = None

    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        line = list(reader)

    with open(file_path, mode='w', newline='') as plik:
        wpisz = csv.writer(plik)
        for wiersz in line:
            if wiersz[1] != name:
                wpisz.writerow(wiersz)
            else:
                customer_id = wiersz[0]
                print("Twoje dane zostały usunięte")
                found = True

    if found:
        # Usuń adres użytkownika
        address_file = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\address.csv'
        with open(address_file, mode='r') as plik:
            reader = csv.reader(plik)
            lines = list(reader)

        with open(address_file, mode='w', newline='') as plik:
            writer = csv.writer(plik)
            for row in lines:
                if row[0] != customer_id:
                    writer.writerow(row)

        # Usuń plik tekstowy użytkownika
        customer_data_file = f'DATABASE/{customer_id}.txt'
        if os.path.exists(customer_data_file):
            os.remove(customer_data_file)
            print(f"Plik {customer_data_file} został usunięty.")
        else:
            print(f"Plik {customer_data_file} nie istnieje.")
    else:
        print("Podany użytkownik nie istnieje")




def del_user_ID(ID):
    found = False

    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        line = list(reader)

    with open(file_path, mode='w', newline='') as plik:
        wpisz = csv.writer(plik)
        for wiersz in line:
            if wiersz[0] != ID:
                wpisz.writerow(wiersz)
            else:
                print("Twoje dane zostały usunięte")
                found = True

    if found:
        # Usuń adres użytkownika
        address_file = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\address.csv'
        with open(address_file, mode='r') as plik:
            reader = csv.reader(plik)
            lines = list(reader)

        with open(address_file, mode='w', newline='') as plik:
            writer = csv.writer(plik)
            for row in lines:
                if row[0] != ID:
                    writer.writerow(row)

        # Usuń plik tekstowy użytkownika
        customer_data_file = f'DATABASE/{ID}.txt'
        if os.path.exists(customer_data_file):
            os.remove(customer_data_file)
            print(f"Plik {customer_data_file} został usunięty.")
        else:
            print(f"Plik {customer_data_file} nie istnieje.")
    else:
        print("Podany użytkownik nie istnieje")


def borrow_books(customer_id, **kwargs):
    # Wyciąganie tytułów książek z argumentów przekazanych przez kwargs
    books_to_borrow = kwargs.get('books_to_borrow', [])

    if not books_to_borrow:
        print("Nie podano żadnych książek do wypożyczenia.")
        return

    # Aktualna data
    data = date.today()

    # Lista wypożyczonych książek
    borrowed_books = []

    # Sprawdzenie dostępności i aktualności książek w bazie danych CSV
    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='r') as books_file:
        reader = csv.DictReader(books_file)
        for row in reader:
            if row['TITLE'] in books_to_borrow:
                if row['STATUS'] == 'available':
                    borrowed_books.append(row['TITLE'])
                else:
                    print(f"Książka '{row['TITLE']}' nie jest dostępna do wypożyczenia.")
                    return

    # Aktualizacja statusu książek na "unavailable"
    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='r') as books_file:
        reader = csv.DictReader(books_file)
        books = list(reader)

    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='w',
              newline='') as books_file:
        fieldnames = ['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'STATUS']
        writer = csv.DictWriter(books_file, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            if book['TITLE'] in borrowed_books:
                book['STATUS'] = 'unavailable'
            writer.writerow(book)

    # Zapisanie danych wypożyczenia do pliku klienta
    customer_data_file = f'DATABASE/{customer_id}.txt'
    with open(customer_data_file, mode='a') as customer_data:
        for book in books_to_borrow:
            customer_data.write(f"{book.strip()}, {data}\n")

    print("Książki zostały wypożyczone.")


def return_book(customer_id, book_to_return):
    # Aktualizacja statusu książki na "available"
    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='r') as books_file:
        reader = csv.DictReader(books_file)
        books = list(reader)

    for book in books:
        if book['TITLE'] == book_to_return and book['STATUS'] == 'unavailable':
            book['STATUS'] = 'available'

    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='w', newline='') as books_file:
        fieldnames = ['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED', 'STATUS']
        writer = csv.DictWriter(books_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    # Usunięcie zwracanej książki z danych wypożyczeń klienta
    customer_data_file = f'DATABASE/{customer_id}.txt'
    with open(customer_data_file, mode='r') as customer_data:
        lines = customer_data.readlines()

    with open(customer_data_file, mode='w') as customer_data:
        for line in lines:
            if book_to_return.lower() not in line.lower():
                customer_data.write(line)

    print(f"Książka '{book_to_return}' została zwrócona.")


@dec
def return_books(customer_id, book_to_return):
    return_book(customer_id, book_to_return)


def control_panel():
    """
        Panel kontrolny do zarządzania biblioteką.

        Returns:
            None
        """
    while True:
        print("\nWybierz opcję:")
        print("1. Rejestracja użytkownika")
        print("2. Usunięcie użytkownika po imieniu")
        print("3. Usunięcie użytkownika po ID")
        print("4. Wypożyczenie książek")
        print("5. Zwrot książek")
        print("6. Wyświetl użytkowników")
        print("7. Wyjście")

        action = int(input("Wybierz opcję (1-7): "))

        if action==1:
            name = input("Imię-Nazwisko: ")
            email = input("Adres e-mail: ")
            while True:
                phone = input("Numer telefonu (9 cyfr): ")
                if len(phone) == 9 and phone.isdigit():
                    break
                else:
                    print("Numer telefonu musi składać się z dokładnie 9 cyfr. Spróbuj ponownie.")
            country = input("Aktualny Kraj: ")
            city = input("Miasto: ")
            street = input("Nazwa ulicy: ")
            register_user(name,email,phone,country,city,street)
        elif action==2:
            delt = int(input("Wybierz opcję usunięcia danych: po(Imie-Nazwisko(1)/ID(2)):"))
            if delt == 1:
                namee=input("Proszę wpisać Imie, oraz nazwisko użytkownika do usunięcia: ")
                del_user_name(namee)
            elif delt == 2:
                idd = input("Proszę wpisać ID użytkownika do usunięcia: ")
                del_user_ID(idd)
            else:
                print("Nieprawidłowa opcja wyboru")
                return None
        elif action == 3:
            customer_id = input("Proszę podać ID użytkownika: ")
            books = input("Proszę podać tytuły książek do wypożyczenia, oddzielone przecinkami: ").split(',')
            borrow_books(customer_id, books_to_borrow=[book.strip() for book in books])
        elif action == 4:
            customer_id = input("Proszę podać ID użytkownika: ")
            books = input("Proszę podać tytuły książek do oddania, oddzielone przecinkami: ").split(',')
            return_books(customer_id, books_to_return=[book.strip() for book in books])
        elif action == 5:
            print("Wyjście z programu.")
            break
        else:
            print("Nieprawidłowa opcja wyboru")


# borrow_books(8036, books_to_borrow=["The Object-Oriented Thought Process","The Art of Computer Programming"])
#return_books(8036, books_to_return=["The Object-Oriented Thought Process","The Art of Computer Programming"])