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

import csv
import random
import os
import string
from datetime import datetime
import books

file_path = 'customer.csv'
if not os.path.exists('DATABASE'):
    os.makedirs('DATABASE')


def output2():
    with open('customer.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)


def register_new_customer(books):
    customer_file = 'DATABASE/customer.csv'

    name = input("Podaj imię i nazwisko nowego klienta: ")
    email = input("Podaj adres e-mail nowego klienta: ")
    phone = input("Podaj numer telefonu nowego klienta: ")

    # Generowanie losowego ID klienta
    customer_id = ''.join(random.choices(string.digits, k=4))

    # Aktualna data
    created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated = created
    try:
        # Zapisanie danych klienta do pliku customer.csv
        with open(file_path, mode='a', newline='') as customer_csv:
            writer = csv.writer(customer_csv)
            writer.writerow([customer_id, name, email, phone, created, updated])

        # Tworzenie pliku dla klienta do przechowywania danych wypożyczeń
        customer_data_file = f'DATABASE/{customer_id}.txt'
        if not os.path.exists(customer_data_file):
            open(customer_data_file, 'a').close()

        print("Nowy klient został zarejestrowany.")

    except IOError as e:
        print(f"Błąd wejścia/wyjścia: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


def delete_customer_data():
    customer_file = 'DATABASE/customer.csv'

    customer_id = input("Podaj ID klienta do usunięcia: ")

    # Usuwanie danych klienta z pliku customer.csv
    temp_customer_file = 'DATABASE/temp_customer.csv'
    with open(file_path, mode='r', newline='') as old_file, \
         open(temp_customer_file, mode='w', newline='') as new_file:

        reader = csv.reader(old_file)
        writer = csv.writer(new_file)

        for row in reader:
            if row[0] != customer_id:
                writer.writerow(row)

    os.remove(customer_file)
    os.rename(temp_customer_file, customer_file)

    # Usuwanie pliku danych klienta
    customer_data_file = f'DATABASE/{customer_id}.txt'
    if os.path.exists(customer_data_file):
        os.remove(customer_data_file)

    print("Dane klienta zostały usunięte.")


def manage_customer_data():
    action = input("Wybierz akcję (register/delete): ")

    if action == 'register':
        register_new_customer()
    elif action == 'delete':
        delete_customer_data()
    else:
        print("Niepoprawna akcja. Dostępne akcje to 'register' lub 'delete'.")


def borrow_books(customer_id):
    # Wybór książek do wypożyczenia przez klienta
    books_to_borrow = input("Podaj tytuły książek do wypożyczenia (oddzielone przecinkami): ").split(',')

    # Aktualna data
    borrow_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Zapisanie danych wypożyczenia do pliku klienta
    customer_data_file = f'DATABASE/{customer_id}.txt'
    with open(customer_data_file, mode='a') as customer_data:
        for book in books_to_borrow:
            customer_data.write(f"{book.strip()}, {borrow_date}\n")

    print("Książki zostały wypożyczone.")


def return_book(customer_id):
    # Wybór książki do zwrotu przez klienta
    book_to_return = input("Podaj tytuł książki do zwrotu: ")

    # Odczytanie danych wypożyczeń klienta
    customer_data_file = f'DATABASE/{customer_id}.txt'
    with open(customer_data_file, mode='r') as customer_data:
        lines = customer_data.readlines()

    # Usunięcie zwracanej książki z danych wypożyczeń klienta
    with open(customer_data_file, mode='w') as customer_data:
        for line in lines:
            if book_to_return.lower() not in line.lower():
                customer_data.write(line)

    print("Książka została zwrócona.")


def manage_borrow_return(customer_id):
    action = input("Wybierz akcję (borrow/return): ")

    if action == 'borrow':
        borrow_books(customer_id)
    elif action == 'return':
        return_book(customer_id)
    else:
        print("Niepoprawna akcja. Dostępne akcje to 'borrow' lub 'return'.")

