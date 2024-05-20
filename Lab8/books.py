## 2. Moduł obsługi książek zawierający 2 funkcje:
## funkcja 1: dodanie nowej książki do bazy (book.csv)
## funkcja 2: usuwanie książki do bazy opcje: wględem ID lub tytułu (book.csv)
##

"""
Moduł Library

Ten moduł zawiera funkcje do zarządzania biblioteką książek. Zawiera funkcje dodawania,
usuwanie oraz wyświetlania książek.

Funkcje:
    - add_book: Dodaje nową książkę do biblioteki.
    - del_book_ID: Usuwa książkę z biblioteki na podstawie podanego ID.
    - del_book_name: Usuwa książkę z biblioteki na podstawie podanego tytułu.
    - output: Wyświetla zawartość biblioteki książek.
"""

import csv
from datetime import date


file_path = 'C:\\Users\\Admin\\PycharmProjects\\pythonProject\\Lab8\\Library\\book.csv'

def ensure_newline(file_path):
    with open(file_path, 'r+') as file:
        #przejście na ostatnia linijke
        file.seek(0, 2)
        file.seek(file.tell() - 1, 0)
        #wczytanie jednego znaku z ostatniej linijki
        last_char = file.read(1)
        if last_char != '\n':
            file.write('\n')

def add_book(ID,AUTHOR,TITLE,PAGES):
    """
        Dodaje nową książkę do pliku CSV, sprawdzając unikalność ID.

        Funkcja pyta użytkownika o dane nowej książki: ID, autora, tytuł i liczbę stron.
        Sprawdza, czy podane ID jest unikalne w pliku CSV przed dodaniem nowej książki.
        Po sprawdzeniu dodaje nową książkę do pliku CSV.

        Returns:
            None
    """
    CREATED = date.today()
    UPDATED = date.today()
    STATUS = "available"
    ensure_newline(file_path)
    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        for i, row in enumerate(reader):
            if i == 0:  # Pomijanie pierwszego wiersza (nagłówki kolumn)
                continue
            if int(row[0]) == ID:
                print("Takie ID juz istnieje, książka nie została dodana")
                return

    with open(file_path, mode='a', newline='') as plik:
        writer = csv.writer(plik)
        writer.writerow([ID, AUTHOR, TITLE, PAGES, CREATED, UPDATED, STATUS])
        print(f"Ksiazka wpisana: {ID}, {AUTHOR}, {TITLE}, {PAGES}, {CREATED}, {UPDATED}, {STATUS}")

def del_book_ID(ID):
    found = False  # Zmienna do śledzenia, czy znaleziono książkę o podanym ID

    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        line = list(reader)

    with open(file_path, mode='w', newline='') as plik:
        writer = csv.writer(plik)
        for wiersz in line:
            if wiersz[0] != str(ID):
                writer.writerow(wiersz)
            else:
                print("Ksiazka zostala usunieta")
                found = True  # Znaleziono książkę o podanym ID, ustawia found na True
        if not found:
            print("Podana ksiazka nie istnieje")

def del_book_name(tytul):
    found = False  # Zmienna do śledzenia, czy znaleziono książkę o podanym tytule

    with open(file_path, mode='r') as plik:
        reader = csv.reader(plik)
        line = list(reader)

    with open(file_path, mode='w', newline='') as plik:
        wpisz = csv.writer(plik)
        for wiersz in line:
            if wiersz[2] != str(tytul):     # Jeżeli tytul nie pasuje, zapisz ten wiersz
                wpisz.writerow(wiersz)
            else:
                print("Ksiazka zostala usunieta")
                found = True  # Znaleziono książkę o podanym tytule, ustawia found na True
        if not found:
            print("Podana ksiazka nie istnieje")

def output():
    with open('C:\\Users\Admin\PycharmProjects\pythonProject\Lab8\Library\\book.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)






