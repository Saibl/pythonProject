################## Dokumentacja  (docstrings) ########################################
################################################################################
#
# Dla zachowania czytelności i jednolitości kodu stosuj określoną gramatykę kodu, w pythonie
# najczęściej stosuje się konwencję opisaną w dokumencie PEP 258
# Wykonaj dokumentację kodu (dla funkcji, modułu)
# Stosuj obsługę wyjątków

# #################### Przykład 1 - dokumentacja funkcji (Google style)
# def divide(x: int,y: int) -> float:
#   """
#   Funkcja dzieli liczbę x przez liczbę y
#
#   Args:
#     x (int): dzielna
#     y (int): dzielnik
#
#   Returns:
#     wynik dzielenia x/y
#
#   """
#   result = x/y
#   return(result)
#
# print(divide(2,3))
# print(divide(x = 1, y = 2))
# help(divide)
# print(divide.__doc__)
################################################################################
################################################################################
######## Function: break() and continue()
################################################################################
## Funkcja break() jest używana często do zakończenia programu/pętli (for, while)
## podczas gdy funkcja continue() pozwala opuścić blok instrukcji
## i wrócić do początku pętli.

################### Example 1: the program only prints the numbers 0 1 2 3 4
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# licz = 0
# while licz in list_1:
#     print(list_1[licz]),
#     licz += 1  # licz = licz + 1
#     if licz >= 5:
#         break

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)

################################################################################
## Function with multiple arguments: args, kwargs
################################################################################

################################## Example 1:  sum of a sequence of numbers
# def suma(*args):
#     if not args:                        # case: no input parameters
#         return('no parameters')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


############# Example 2: Sum of arithmetic sequence
## functional requirements:
##  minimum number of input parameters: 1

# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

############  Example 3:   Sum the first four elements of arithmetic sequence
## functional requirements:
##  minimum number of input parameters: 4

# def sum2(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#
#     print(sumaLiczb)
#     return(None)
#
# sum2(1,2,3,4,5,6,7,8,9,10)
# sum2()

############  Example 3:   Sum the three elements
## functional requirements:
## minimum number of input parameters: 3
## user enter the name of input parameters

# def dict1(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# dict1(a=1, b=2, c=3)

############  Example 4: Say hello to a friend
## functional requirements:
## minimum number of input parameters: unknown
## name of input parameters: unknown

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# hello(firstname="John", secondname='Smith')
# hello(user="John")

############  Example 5: unpack list

# list_arg = [1, 3, 5]
#
# def unpack1(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# unpack1(*list_arg)
#####################################################
################################################################################
################################################################################


########################## Zadania do wykonania
# # ################################ Task 0
# '''
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation
#
# '''

# def numbers(x: int, y: int) -> int:
#     """
#         Funkcja sprawdza dla kazdej liczby z zakresu od x do y czy jest podzielna przez 7, oraz czy nie jest wielokrotnoscia 5,
#         wypisujac tylko liczby spelniajace oba warunki w formie listy.
#
#         Args:
#           x (int): Poczatek zakresu
#           y (int): koniec zakresu
#
#         Returns:
#           lista liczb podzielnych przez 7, ale nie podzielnych przez 5
#     """
#     wynik = []
#     for liczba in range(x,y):
#         if liczba %7 == 0 and liczba %5 != 0:
#             wynik.append(liczba)
#         else:
#             continue
#     print(wynik)
#
# x = 1000
# y = 2101
# numbers(x,y)
# help(numbers)
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#

# ''
# # ################################ Task 1
## A website requires the users to input username and password to register.
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file

# def password_check(password: str):
#     """
#         Funkcja sprawdza poprawnosc hasla uzytkownika.
#
#         Kryteria sprawdzania hasla:
#             1. Przynajmniej 1 litera z zakresu [a-z]
#             2. Przynajmniej 1 cyfra z zakresu [0-9]
#             3. Przynajmniej 1 litera z zakresu [A-Z]
#             4. Dlugosc hasla musi byc od 4 do 8 znakow.
#
#         Args:
#             password (str): Haslo do sprawdzenia.
#
#         Returns:
#             Zapisuje nazwe uzytkownika oraz haslo do pliku wypisujac odpowiedni komunikat
#         """
#     if len(password) < 4 or len(password) > 8:
#         return "Error, haslo powinno zawierac od 4 do 8 znakow"
#     lowercase = False
#     uppercase = False
#     digit = False
#     passed = False
#     for symbol in password:
#         if symbol.islower():
#             lowercase = True
#         if symbol.isupper():
#             uppercase = True
#         if symbol.isdigit():
#             digit = True
#         if lowercase and uppercase and digit:
#             passed = True
#             break
#     if passed:
#         print("Haslo jest poprawne, oraz zostalo zapisane")
#         return password
#     else:
#         return "Haslo jest nie poprawne, powinno zawierac co najmniej 1 mala litere, 1 duze litere, oraz 1 liczbe"
#
#
# username = input("Wprowadz nazwe uzytkownika: ")
# password = input("Wprowadz haslo: ")
# Final = password_check(password)
# with open("hasla_lab5.txt", "w") as file:
#     file.write(username)
#     file.write("\n")
#     file.write(Final)
# help(password_check)

################ Task 2
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line.
## You should to document your code by using python docstrings
## (dokumentacja kodu styl google)
## Don't forget to handle exceptions (obsłudze wyjątków)
## Save result to *.pkl file use picle package
# '''
# import pickle
# def numbers(x: int, y: int) -> int:
#     """
#         Funkcja sprawdza dla kazdej liczby z zakresu od x do y czy jest podzielna przez 7, oraz czy nie jest wielokrotnoscia 5,
#         wypisujac tylko liczby spelniajace oba warunki w formie listy. Jesli x jest wieksze od y program wypisuje blad.
#
#         Args:
#           x (int): Poczatek zakresu
#           y (int): koniec zakresu
#
#         Returns:
#           lista liczb podzielnych przez 7, ale nie podzielnych przez 5
#     """
#
#     wynik = []
#     for liczba in range(x,y):
#         if liczba %7 == 0 and liczba %5 != 0:
#             wynik.append(liczba)
#         else:
#             continue
#     print(wynik)
#
# x = 1000
# y = 1200
# if x >= y:
#     raise ValueError("Poczatek zakresu (x) musi byc mniejszy niz koniec zakresu (y)")
# wynik = numbers(x,y)
#
# with open("wynik.pkl", "wb") as file:
#     pickle.dump(wynik, file)

# help(numbers)
##### do testów możesz użyć:
# x = 1000
# y = 2101
# my_list = list(range(x,y,1))
# print(my_list)

# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#

################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Name of input parameters:
## You should to document your code by using python docstrings (google)
###############

# def power(*args):
#     """
#     Funkcja przyjmuje sekwencje liczb oddzielonych przecinkami z konsoli i zwraca ich potegi.
#
#     Args:
#         *args: Argumenty do obliczenia potegi. Może być dowolna liczba argumentów, ale nie wiecej niż 99.
#
#     Returns:
#         list: Lista zawierająca potegi kolejnych argumentów. Potega i-tego argumentu to i-ta potęga tego argumentu.
#
#     Raises:
#         ValueError: Jeśli liczba argumentów przekracza 99.
#     """
#     if len(args) > 99:
#         raise ValueError("Maksymalna liczba argumentów wynosi 99.")
#
#     powers = []
#     for i, arg in enumerate(args, start=1):
#         powers.append(arg ** arg)
#
#     return powers
#
# numbers = input("Podaj liczby oddzielone przecinkami: ").split(',')
# numbers = [int(num) for num in numbers]
# results = power(*numbers)
# print(results)
# help(power)


################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Don't forget to handle exceptions (obsłudze wyjątków)
###############

# def power(*args):
#     """
#     Funkcja przyjmuje sekwencje liczb oddzielonych przecinkami z konsoli i zwraca ich potegi.
#
#     Args:
#         *args: Argumenty do obliczenia potegi. Może być dowolna liczba argumentów, ale nie wiecej niż 99.
#
#     Returns:
#         list: Lista zawierająca potegi kolejnych argumentów. Potega i-tego argumentu to i-ta potęga tego argumentu.
#
#     Raises:
#         ValueError: Jeśli liczba argumentów przekracza 99.
#     """
#     if len(args) > 99:
#         raise ValueError("Maksymalna liczba argumentów wynosi 99.")
#
#     powers = []
#     for i, arg in enumerate(args, start=1):
#         var_name = 'x' + str(i)
#         locals()[var_name] = arg
#         exec(f"{var_name} = {arg}")  # Przypisz wartość argumentu do zmiennej lokalnej
#         exec(f"{var_name}_power = {var_name} ** {var_name}")  # Oblicz potęgę argumentu i przypisz do zmiennej lokalnej
#         powers.append(locals()[f"{var_name}_power"])  # Dodaj wynik do listy powers
#
#     return powers
#
#     return powers
#
# numbers = input("Podaj liczby oddzielone przecinkami: ").split(',')
# numbers = [int(num) for num in numbers]
# results = power(*numbers)
# print(results)


########################## Task 5 ########################
## The first step,
## generate test data: create folder. Create 5 text files to this folder,
## each file contains more than 5 sentences.
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file
## contain words with more than 3 letters
## Next step: decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename
## b) if the file has 0 in the filename then the function counts words in the text of the file
## c) if the filename contains 'EF.txt', then the function copy this file to
## 'DocumentLab5copy' directory

import os
import shutil
# os.makedirs('C:\\Users\Admin\PycharmProjects\pythonProject\lab5zad5') ##utworzenie folderu lab5zad5

def dec(func):
    def wrapper(folder):
        folder_content = os.listdir(folder)
        num_zero_files = 0
        num_words = 0
        for file in folder_content:
            if '0' in file:
                num_zero_files += 1
                with open(file, 'r') as file:
                    text = file.read()
                    words = text.split()
                    for word in words:
                        num_words += 1
        if 'EF.txt' in file:
            destination_folder = os.path.join(folder, 'DocumentLab5copy')
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.copy(file, destination_folder)
        result = func(folder)
        result += f"\nLiczba plików z 0 w nazwie: {num_zero_files}"
        result += f"\nLiczba wyrazów w plikach z 0 w nazwie: {num_words}"
        return result
    return wrapper

@dec
def fun(folder):
    folder_content = os.listdir()
    print(folder_content)
    abc = [plik for plik in folder_content if plik.endswith('ABC.txt')]
    for filee in abc:
        with open(filee, 'r') as file:
            num_words = 0
            textt = file.read()
            words = textt.split()
            for word in words:
                if len(word) >= 3:
                    num_words += 1
    return "Liczba wyrazow zlozonych z conajmniej 3 liter w plikach ABC wynosi: " + str(num_words)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ut erat nibh. Mauris blandit diam nec ex congue, sed posuere sem ornare. Morbi sollicitudin justo nibh, et pulvinar orci malesuada efficitur. Mauris id ex quis magna auctor cursus. Proin eu gravida eros. Sed pretium tellus faucibus enim sagittis vulputate. Phasellus placerat magna diam."
os.chdir('C:\\Users\Admin\PycharmProjects\pythonProject\lab5zad5')
current_folder = os.getcwd()
files = []
files.append(open('Tekst1ID_ABC.txt', 'w', encoding='utf-8'))
files.append(open('Tekst2ID_405.txt', 'w', encoding='utf-8'))
files.append(open('Tekst3ID_607.txt', 'w', encoding='utf-8'))
files.append(open('Tekst4ID_ABC.txt', 'w', encoding='utf-8'))
files.append(open('Tekst5ID_DEF.txt', 'w', encoding='utf-8'))

for file in files:
    file.write(text)

for file in files:
    file.close()

print(fun(current_folder))