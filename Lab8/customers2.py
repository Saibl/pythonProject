
'''
NAME
    customers2

DESCRIPTION
    This module allows the user to manage a library system, including registering users,
    deleting users, borrowing books, and returning books.

    This tool uses CSV files to store data about users, addresses, and books.

    This script requires the `os`, `csv`, `datetime`, `random`, `string`, `tkinter`,
    and `tkinter.messagebox` packages to be installed within the Python environment
    you are running this script in.

FUNCTIONS
    This module contains the following functions:
    * register_user(name, email, phone, city, street) - registers a user with the given details
      and saves the information in customer.csv and address.csv files.

    * del_user_name(name) - deletes a user by their name from the customer.csv file and
      corresponding data from address.csv and the user's data file.

    * del_user_ID(ID) - deletes a user by their ID from the customer.csv file and corresponding
      data from address.csv and the user's data file.

    * borrow_books(customer_id, **kwargs) - borrows books for a user by their customer ID,
      updating the status of books in book.csv and recording the borrowed books in the user's data file.

    * return_book(customer_id, book_to_return) - returns a book for a user by their customer ID,
      updating the status of the book in book.csv and removing the book from the user's data file.

    * output2() - prints the content of the customer.csv file.

    * ensure_newline(file_path) - ensures there is a newline at the end of the specified file.

    * register_user_gui() - opens a GUI for user registration.

    * del_user_gui() - opens a GUI for user deletion.

    * borrow_books_gui() - opens a GUI for borrowing books.

    * return_book_gui() - opens a GUI for returning books.

    * add_book_gui() - opens a GUI for adding books to the library.

    * del_book_gui() - opens a GUI for deleting books from the library.

    * call() - starts the main application GUI with options to register users, delete users,
      borrow books, return books, add books, and delete books.

EXAMPLES
    register_user("John Doe", "john@example.com", "123456789", "Warsaw", "Main St.")
    del_user_name("John Doe")
    del_user_ID("1234")
    borrow_books("1234", books_to_borrow=["Book Title 1", "Book Title 2"])
    return_book("1234", book_to_return="Book Title 1")
    output2()
'''

import os
import csv
from datetime import date
import random
import string
import tkinter as tk
from tkinter import messagebox
from books import add_book,del_book_ID,del_book_name

file_path = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\customer.csv'

if not os.path.exists('DATABASE'):
    os.makedirs('DATABASE')


def dec(func):
    def wrapper(customer_id, **kwargs):
        # Wyciąganie tytułów książek z argumentów przekazanych przez kwargs
        books_to_return = kwargs.get('books_to_return', [])

        if not books_to_return:
            print("Nie podano żadnych książek do zwrotu.")
            return

        for book_to_return in books_to_return:
            book_to_return = book_to_return.strip()
            # Sprawdzenie czy książka istnieje w bazie danych
            with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv',
                      mode='r') as books_file:
                reader = csv.DictReader(books_file)
                existing_books = {row['TITLE'] for row in reader}

            if book_to_return not in existing_books:
                print(f"Książka '{book_to_return}' nie istnieje w bazie danych.")
                continue
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




def register_user(name,email,phone,city,street):
    customer_file = 'DATABASE/customer.csv'
    ensure_newline(file_path)

    # Generowanie losowego ID klienta
    customer_id = ''.join(random.choices(string.digits, k=4))

    # Aktualna data
    country = "Polska"
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
    # Sprawdzenie czy ID użytkownika istnieje
    if not os.path.exists(f'DATABASE/{customer_id}.txt'):
        print(f"Użytkownik o ID {customer_id} nie istnieje.")
        return

    # Wyciąganie tytułów książek z argumentów przekazanych przez kwargs
    books_to_borrow = kwargs.get('books_to_borrow', [])

    if not books_to_borrow:
        print("Nie podano żadnych książek do wypożyczenia.")
        return

    non_existing_books = []
    with open('C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv', mode='r') as books_file:
        reader = csv.DictReader(books_file)
        existing_books = {row['TITLE'] for row in reader}
        non_existing_books = [book for book in books_to_borrow if book not in existing_books]

    if non_existing_books:
        print(f"Następujące książki nie istnieją w bazie danych: {', '.join(non_existing_books)}")
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


@dec
def return_book(customer_id, book_to_return):
    # Sprawdzenie czy ID użytkownika istnieje
    if not os.path.exists(f'DATABASE/{customer_id}.txt'):
        print(f"Użytkownik o ID {customer_id} nie istnieje.")
        return

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


# borrow_books(8036, books_to_borrow=["The Object-Oriented Thought Process","The Art of Computer Programming"])
#return_books(8036, books_to_return=["The Object-Oriented Thought Process","The Art of Computer Programming"])

def register_user_gui():
    def register():
        name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        city = entry_city.get()
        street = entry_street.get()

        if len(phone) != 9 or not phone.isdigit():
            messagebox.showerror("Błąd", "Numer telefonu musi mieć 9 cyfr")
            return

        if "@" not in email:
            messagebox.showerror("Błąd", "Adres e-mail powinien zawierać znak @")
            return

        try:
            register_user(name, email, phone, city, street)
            messagebox.showinfo("Rejestracja użytkownika", "Użytkownik został zarejestrowany.")
        except ValueError as e:
            messagebox.showerror("Błąd walidacji", str(e))
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił nieoczekiwany błąd: {e}")

    window = tk.Toplevel()
    window.title("Rejestracja użytkownika")

    tk.Label(window, text="Imię i nazwisko").grid(row=0, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1)

    tk.Label(window, text="Email").grid(row=1, column=0)
    entry_email = tk.Entry(window)
    entry_email.grid(row=1, column=1)

    tk.Label(window, text="Telefon").grid(row=2, column=0)
    entry_phone = tk.Entry(window)
    entry_phone.grid(row=2, column=1)

    tk.Label(window, text="Miasto").grid(row=3, column=0)
    entry_city = tk.Entry(window)
    entry_city.grid(row=3, column=1)

    tk.Label(window, text="Ulica").grid(row=4, column=0)
    entry_street = tk.Entry(window)
    entry_street.grid(row=4, column=1)

    tk.Button(window, text="Zarejestruj", command=register).grid(row=5, columnspan=2)

def del_user_gui():
    def del_user():
        if var.get() == 1:
            name = entry_del.get()
            del_user_name(name)
        elif var.get() == 2:
            user_id = entry_del.get()
            del_user_ID(user_id)

    window = tk.Toplevel()
    window.title("Usunięcie użytkownika")

    var = tk.IntVar()

    tk.Radiobutton(window, text="Imię i nazwisko", variable=var, value=1).grid(row=0, column=0)
    tk.Radiobutton(window, text="ID", variable=var, value=2).grid(row=0, column=1)

    entry_del = tk.Entry(window)
    entry_del.grid(row=1, columnspan=2)

    tk.Button(window, text="Usuń", command=del_user).grid(row=2, columnspan=2)

def borrow_books_gui():
    def borrow():
        customer_id = entry_customer_id.get()
        books = entry_books.get().split(',')
        borrow_books(customer_id, books_to_borrow=[book.strip() for book in books])

    window = tk.Toplevel()
    window.title("Wypożyczenie książek")

    tk.Label(window, text="ID użytkownika").grid(row=0, column=0)
    entry_customer_id = tk.Entry(window)
    entry_customer_id.grid(row=0, column=1)

    tk.Label(window, text="Książki (oddzielone przecinkami)").grid(row=1, column=0)
    entry_books = tk.Entry(window)
    entry_books.grid(row=1, column=1)

    tk.Button(window, text="Wypożycz", command=borrow).grid(row=2, columnspan=2)

def return_book_gui():
    def return_books_action():
        customer_id = entry_customer_id.get()
        books = entry_books.get().split(',')
        return_book(customer_id, books_to_return=[book.strip() for book in books])

    window = tk.Toplevel()
    window.title("Zwrot książek")

    tk.Label(window, text="ID użytkownika").grid(row=0, column=0)
    entry_customer_id = tk.Entry(window)
    entry_customer_id.grid(row=0, column=1)

    tk.Label(window, text="Książki (oddzielone przecinkami)").grid(row=1, column=0)
    entry_books = tk.Entry(window)
    entry_books.grid(row=1, column=1)

    tk.Button(window, text="Zwróć", command=return_books_action).grid(row=2, columnspan=2)

def add_book_gui():
    def add():
        book_id = entry_id.get()
        author = entry_author.get()
        title = entry_title.get()
        pages = entry_pages.get()

        if not book_id.isdigit():
            messagebox.showerror("Błąd", "ID musi być liczbą")
            return

        if not pages.isdigit():
            messagebox.showerror("Błąd", "Liczba stron musi być liczbą")
            return

        try:
            add_book(int(book_id), author, title, int(pages))
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił nieoczekiwany błąd: {e}")

    window = tk.Toplevel()
    window.title("Dodawanie książki")

    tk.Label(window, text="ID").grid(row=0, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=0, column=1)

    tk.Label(window, text="Autor").grid(row=1, column=0)
    entry_author = tk.Entry(window)
    entry_author.grid(row=1, column=1)

    tk.Label(window, text="Tytuł").grid(row=2, column=0)
    entry_title = tk.Entry(window)
    entry_title.grid(row=2, column=1)

    tk.Label(window, text="Liczba stron").grid(row=3, column=0)
    entry_pages = tk.Entry(window)
    entry_pages.grid(row=3, column=1)

    tk.Button(window, text="Dodaj", command=add).grid(row=4, columnspan=2)


def del_book_gui():
    def del_book():
        if var.get() == 1:
            title = entry_del.get()
            del_book_name(title)
        elif var.get() == 2:
            book_id = entry_del.get()
            if not book_id.isdigit():
                messagebox.showerror("Błąd", "ID musi być liczbą")
                return
            del_book_ID(int(book_id))

    window = tk.Toplevel()
    window.title("Usunięcie książki")

    var = tk.IntVar()

    tk.Radiobutton(window, text="Tytuł", variable=var, value=1).grid(row=0, column=0)
    tk.Radiobutton(window, text="ID", variable=var, value=2).grid(row=0, column=1)

    entry_del = tk.Entry(window)
    entry_del.grid(row=1, columnspan=2)

    tk.Button(window, text="Usuń", command=del_book).grid(row=2, columnspan=2)

def call():
    root = tk.Tk()
    root.title("Biblioteka")

    width = 400
    height = 300
    root.geometry(f"{width}x{height}")

    tk.Button(root, text="Rejestracja użytkownika", command=register_user_gui).pack(fill='x')
    tk.Button(root, text="Usunięcie użytkownika", command=del_user_gui).pack(fill='x')
    tk.Button(root, text="Dodawanie książki", command=add_book_gui).pack(fill='x')
    tk.Button(root, text="Usunięcie książki", command=del_book_gui).pack(fill='x')
    tk.Button(root, text="Wypożyczenie książek", command=borrow_books_gui).pack(fill='x')
    tk.Button(root, text="Zwrot książek", command=return_book_gui).pack(fill='x')

    root.mainloop()