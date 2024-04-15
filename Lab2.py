############ Typ danych (klasa) zbiór - Data type: set ###############
# my_list = [5, 1, 1, 2, 3]
# a = set(my_list)
# b = set([4, 5, 6, 7, 8])
# #### wybrane operacje na zbiorach (selected operation in sets)
# print(a & b)   #    & - ampersand
# print(a.intersection(b)) # operacja równoważna do powyższej
#
# print(a | b)  #
# print(a.union(b))   # operacja równoważna do powyższej
#
# print(a - b)
# print(a.difference(b))   # operacja równoważna do powyższej
#
# print(b - a)
# print(b.difference(a))   # operacja równoważna do powyższej

#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?

# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                 'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                 'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])

# print(set_gene1&set_gene2&set_gene3)
# print(set_gene1&set_gene3)
# print(set_gene1-set_gene2-set_gene3)

######### Operatory porównania lokalnego i globalne
####################Przykład
### Sprawdź wynik działania następujących operacji:
# l1 = [5,10]
# l2 = [5,11]
#
# print(l1,l2)
# print('l1 == l2 wynik:',l1 == l2)
# print('l1 is l2 wynik:',l1 is l2)
# print('l1 != l2 wynik: ',l1 != l2)
# print('l1 is not l2 wynik:',l1 is not l2)
# print('l1 >= l2 wynik:', l1 >= l2)

## x or y	jeżeli x == False, to y, w przeciwnym razie x
## w przybliżeniu alternatywa
## x and y	jeżeli x == False, to x, w przeciwnym razie y
## w przybliżeniu koniunkcja
## not x	negacja



####################Przykład
a = False
b = 2
c = True

# print(a or b)
# print(b or a)
# print(c or a)
# print(a or c)
# print(b and a)
# print(a and b)
# print(a and c)

###### Przykład
# list1 = [1,2,3,4,5,6,7,6,5,6,5]
# for element in list1:
#     print(element is 5)

# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
# ile1=lista_gene1.count('FGFR4')
# ile2=lista_gene1.count('FGERA4')
# if ile1>0:
#     jedn = lista_gene1.index('FGFR4')
#     print('Gen 1 znajduje się na liście na indexie:',jedn)
# else:
#     print('Nie ma takiego genu 1 w zbiorze')
# if ile2>0:
#     dwa = lista_gene1.index('FGERA4')
#     print('Gen 2 znajduje się na liście na indexie:',dwa)
# else:
#     print('Nie ma takiego genu 2 w zbiorze')

####################Łańcuchy znaków
## Zapoznaj się z wybranymi metodami dla typu string
## więcej metod znajdziesz tu: https://pl.python.org/docs/lib/string-methods.html
## s.endswith(przyrostek[, początek[, koniec]]) - sprawdzenia, czy napis jest zakończony napisem przyrostek
## s.index(napis[, początek[, koniec]]) - indeks wystąpienia napisu
## s.isalpha() - czy wszystkie znaki napisu są literami i napis składa się przynajmniej z jednego znaku.
# s.capitalize() - zmienia pierwszą literę na dużą\\
# s.center(długość) - Centruje napis w polu o podanej długości\\
# s.count(sub) - zlicza wystąpienie podciągu sub w napisie s\\
# s.encode(kodowanie) - zwraca zakodowaną wersję napisu ('utf-8', 'ascii', 'utf-16')\\
# s.isalnum() - sprawdza czy wszystkie znaki są znakami alfanumerycznymi\\
# s.isdigit() - sprawdza czy wszystkie znaki są cyframi\\
# s.islower() - sprawdza czy wszystkie litery są małe\\
# s.isspace() - sprawdza czy wszystkie znaki są białymi znakami\\
# s.isupper() - sprawdza czy wszystkie litery są duże\\
# s.join(t) - łączy wszystkie napisy na liście t używając s jako separatora\\
# s.lstrip() - usuwa początkowe białe znaki\\
# s.replace(old, new) - zastępuje stary podciąg nowym\\
# s.rstrip() - usuwa końcowe białe znaki\\
# s.split(separator) - dzieli napis używają podanego separatora\\
# s.strip() - usuwa początkowe i końcowe białe znaki\\
# s.upper() - Zwraca kopię napisu z wszystkimi literami zamienionymi na wielkie litery.

#### Przykład
# word = 'Python jest super, każdy to wie'
# print(word.capitalize())
# print(word.count('super'))
# print(word.endswith('per'))
# print(word.index('super'))
# print('-'.join(word))
# print(word.split(' '))
# print(word.upper())

#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) ile zdań jest w analizowanym tekście?

# tekst = 'Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki).'
# print(tekst.count('Emma'))
# print(tekst.upper())
# print(tekst.split(' '))
# print(tekst.count('.'))

######################################
#################Instrukcje sterujące tj. instrukcje warunkowe i pętle
 ################# 1. Instrukcja warunkowa "IF"#########struktura
# if warunek_1:
#     #lista instrukcji         # odstęp/wcięcie w programie 4 spacje lub 1 tablulacja
# elif warunek_2:
#     #lista instrukcji
# elif warunek_3:
#     #lista instrukcji
#     ...
# else:                          # każdy inny przypadek
#     #lista instrukcji

######################Przykład ########################
# liczba = int(input('Ile punktów dostałeś z wejściówki'))
# if liczba == 5:
#     print('Ocena 5')
# elif liczba == 4:
#     print('Ocena 4')
# elif liczba == 3:
#     print('Ocena 3')
# else:
#     print('Wejściówka do poprawy')


########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta
# liczb=int(input('Podaj liczbe: '))
# if liczb%2==0:
#      print(f'liczba {liczb} jest parzysta')
# else:
#     print(f'liczba {liczb} jest nieparzysta')
#################Instrukcje sterujące tj. instrukcje warunkowe i pętle  Teoria
################# 1. Instrukcja warunkowa "MATCH"#########struktura
# match zmienna:
#     case wartość zmiennej 1:
#         blok instrukcji
#     case wartość zmiennej 2:
#         blok instrukcji
# ....
#     case wartość zmiennej n:
#         blok instrukcji

## Przykład

# dane_osobowe = input('Wpisz "PESEL" albo "nazwisko"')
# match dane_osobowe:
#    case "PESEL":
#        print('781123242622')
#    case "nazwisko":
#        print('Kowalska')


########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)

# pkt = float((input('Wpisz ilosc punktow: ')))
# maks = 15
# procent = float((pkt / maks) * 100)
# #sprawdzenie
# print(f"Procentowa wartosc {procent:.2f}")
#
# match procent:
#    case procent if 50 <= procent <= 60:
#        print('3')
#    case procent if 61 <= procent <= 70 :
#        print('3.5')
#    case procent if 71 <= procent <= 80 :
#         print('4')
#    case procent if 81 <= procent <= 90 :
#         print('4.5')
#    case procent if 91 <= procent <= 100 :
#        print('5')

########### Pętla for  - jako wektor
# for i in wektor:  # wektor tworzymy korzystając z funkcji range(początek,koniec)
#     instrukcje
#
# print(list(range(0,5)))  # range(0,5) --> i przyjmuje wartości kolejno 0,1,2,3,4
##########Przykład
# for i in range(1, 6):
#     print('Python')

################# Pętla for - po kolekcji
## for x in kolekcja:      uwaga: elementy kolekcji moga być dowolnego typu,
##     instrukcje           #nie musi to być wektor liczb.

################Przykład #########################################
# for i in ['Ala','Ola','Tola']:
#     print(i)
#######################################################################################3

# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
### Write a program that calculates the sum of the sequence: 1+1/2+1/3+...+1/m using the for loop.
### The input variable m is arbitrary. The m-parameter is provided as input by the user (use input).
#
# suma = 0
# n=0
# m=int(input('Wprowadz gorna granice: '))
# for i in range(n+1, m):
#     print(i)
#     suma+=i
# print("Suma wynosi: ",suma)

################# Pętla while
# while warunek:  # pętla działa dopóki warunek jest prawdziwy
#     instrukcje
# while condition:  # the loop runs as long as the condition is true
#     instruction
############## Przykład ###########################################
# i = 0   # i to zmienna tzw iterator który w każdym kroku zwykle zmienia się o jakąś wartość np.  o 1
# while i < 5:
#    print('I like python')
#    i += 1      # equivalent to i = i + 1

###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while
# from math import sqrt
#
# num = 1
# while num <= 10:
#     print(round(sqrt(num), 2))
#     num += 1

### Jeśli masz problem z tłumaczeniem treści użyj https://www.deepl.com lub poproś o dodatkowe wyjaśnienie
###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0
# from math import sqrt
#
# a= int(input('Podaj wartosc a: '))
# b= int(input('Podaj wartosc b: '))
# c= int(input('Podaj wartosc c: '))
#
# delta= b*b - 4*a*c
# print(f'Delta: {delta}')
#
# if (delta > 0):
#     delta = sqrt(delta)
#     x1 = (-b - delta) / (2 * a)
#     x2 = (-b + delta) / (2 * a)
#     print(f'x1 = {x1}, x2 = {x2}')
#
# elif (delta == 0):
#     print(f'x0 = {-b / (2 * a)}')
#
# else:
#     print('Rownanie nie posiada pierwiastkow')
###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed
### in a comma-separated sequence on a single line.

# passed=[]
#
# for i in range(1, 1001):
#     numb = i
#     even = True
#     while numb>0:
#         a= numb % 10
#         if a%2==0:
#             numb=numb//10
#         else:
#             even = False
#             break
#     if even:
#         passed.append(i)
#
# print(passed)