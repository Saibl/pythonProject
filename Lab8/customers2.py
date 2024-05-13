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

import os
import csv
from datetime import date
import random
import string

file_path = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\customer.csv'

if not os.path.exists('DATABASE'):
    os.makedirs('DATABASE')

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

def register_user():
    customer_file = 'DATABASE/customer.csv'

    name = input("Podaj imię i nazwisko nowego klienta: ")
    email = input("Podaj adres e-mail nowego klienta: ")
    phone = input("Podaj numer telefonu nowego klienta: ")
    country = input("Podaj Kraj zamieszkania: ")
    city = input("Podaj Miasto: ")
    street = input("Podaj nazwę ulicy: ")
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


def del_user_name():
    name = input("Podaj Imię i Nazwisko: ")     # Uzytkownik podaje imie, oraz nazwisko do usuniecia
    found = False

    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        line = list(reader)

    with open(file_path, mode='w', newline='') as plik:
        wpisz = csv.writer(plik)
        for wiersz in line:
            if wiersz[1] != str(name):
                wpisz.writerow(wiersz)
            else:
                print("Twoje dane zostały usunięte")
                found = True
        if not found:
            print("Podany użytkownik nie istnieje")

def del_user_ID():
    ID = input("Podaj ID: ")
    found = False

    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        line = list(reader)

    with open(file_path, mode='w', newline='') as plik:
        wpisz = csv.writer(plik)
        for wiersz in line:
            if wiersz[0] != str(ID):
                wpisz.writerow(wiersz)
            else:
                print("Twoje dane zostały usunięte")
                found = True
        if not found:
            print("Podany użytkownik nie istnieje")


def borrow_books(customer_id):
    # Wybór książek do wypożyczenia przez klienta
    books_to_borrow = input("Podaj tytuły książek do wypożyczenia (oddzielone przecinkami): ").split(',')

    # Aktualna data
    borrow_date = date.today()

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

    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='w', newline='') as books_file:
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
            customer_data.write(f"{book.strip()}, {borrow_date}\n")

    print("Książki zostały wypożyczone.")

def return_book(customer_id):
    # Wybór książki do zwrotu przez klienta
    book_to_return = input("Podaj tytuł książki do zwrotu: ")

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

    print("Książka została zwrócona.")

def control_panel():
    action = input("Wybierz opcję (rejestracja/usunięcie danych):")

    if action == "rejestracja":
        return register_user()
    elif action == "usunięcie danych":
        delt = input("Wybierz opcję: po(Imie nazwisko/ID):")
        if delt == "Imie nazwisko":
            return del_user_name()
        elif delt == "ID":
            return del_user_ID()
        else:
            print("Nieprawidłowa opcja wyboru")
            return None
    else:
        print("Nieprawidłowa opcja wyboru")
        return None

