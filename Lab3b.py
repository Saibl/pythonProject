'''
###################################################################################################################
Dziś zajęcia dotyczą tworzenia funkcji ze zmienną liczbą argumentów wejściowych.
Przed realizacją zadań koniecznie zapoznaj się ze slajdami prezentacji do Wykładu 3

Dodatkowe linki do filmów, które ułatwią Ci zrozumienie materiału z laboratorium:
"Co oznacza zapis *args oraz **kwargs w funkcjach?"   -  https://www.youtube.com/watch?v=7nwXBWzkqNU
####################################################################################################################

'''
##################################### Zadanie 0   na rozgrzewkę ##################
## Utwórz funkcję o nazwie "Rozprawka.py", która będzie wyświetlała,
## na ekranie napis "to poprostu jest wspaniałe i niesamowite, musisz to zobaczyć",
## następnie używając w/w funkcji napisz tekst reklamujący, opisujący jeden z 7 Cudów świata gdzie
## wywołasz tą funkcję w tekście minimum 3 krotnie
######################################################################################################################

# import Rozprawka
#
# def cud_swiata():
#     print("Kolos Rodyjski – olbrzymich rozmiarów posąg Heliosa, greckiego bóstwa słońca, wybudowany na wyspie Rodos przez Charesa z Lindos w latach 294–282 p.n.e.")
#     Rozprawka.rozprawka()
#     print("Wykonano go z brązu i ustawiono u wejścia do portu Rodos dla upamiętnienia niepowodzenia Demetriusza Poliorketesa, który w latach 305–304 p.n.e. oblegał miasto.")
#     print("Posąg miał 30–32 metry wysokości, stał na 10-metrowym piedestale.")
#     Rozprawka.rozprawka()
#     print("Posąg został zniszczony w 227/226 p.n.e., w wyniku trzęsienia ziemi. Jest to jeden z siedmiu cudów świata starożytnego.")
#     Rozprawka.rozprawka()
#
# cud_swiata()

############################### Teoria: Funkcja z dowolną liczbą argumentów wejściowych (*args)  #########################
### def nazwa_funkcji(*args):
###    instrukcje
##     return obiekt                 *args - krotka argumentów pozycyjnych

###### Wyrażenie “args” bierze się z od słowa “arguments” czyli argumenty i jest to zazwyczaj zmienna,
###### która zawiera tuple argumentów pozycyjnych. Wyrażenia z jedną gwiazdką (*) używamy gdy do funkcji
### chcemy przekazać dowolną liczbę argumentów pozycyjnych (czyli takich dla których
### przy wywołaniu funkcji nie podajemy ich nazwy, a przypisanie wartości bazuje na kolejności argumentów dlatego
### args - argumenty umieszczane są w krotce/tupli po której możemy iterować args[0], args[1] itd.
## używamy *args gdy nie są istotne dla nas nazwy zmiennych
### Pamiętaj aby parametr *args umieszczać na końcu listy parametrów w definicji funkcji!


################################## Przykład 1  suma dowolnego ciągu cyfr
# def suma(*args):
#     if not args:                        # wkazane jest kontrolowanie przypadku braku argumentów
#         return('brak argumentów')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


################################### Przykład 2:  suma dowolnego ciągu cyfr plus wartość stałej
# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

#################################### Przykład 3:  suma pierwszych 4 cyfr dowolnego ciągu cyfr
# def suma3(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#
#     print(sumaLiczb)
#     return(None)
#
# suma3(1,2,3,4,5,6,7,8,9,10)
# suma3()

#########################################################################################################
#############funkcje z dowolną liczbą argumentów kluczowych (**kwargs) ############
### ** kwargs pozwala przekazywać zmienną długość argumentów ze słowami kluczowymi do funkcji.
### W przypadku gdy do naszej funkcji chcemy przekazywać argumenty, które wyróżniają
### się nazwą możemy użyć parametru z dwoma gwiazdkami (**).
### Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika.
### Jego pary klucz-wartość stanowią nazwa i wartość przekazanego argumentu.
### używamy **kwargs gdy istotna dla nas jest nazwa zmiennych

# def nazwa_funkcji(**kwargs):
#     instrukcje
#     return obiekt                 # kwargs - słownik argumentów kluczowe

######## wstaw jako argument funkcji:  *kwargs  ########################################

## “kwargs” z j.ang. “keyword arguments” czyli argumenty nazwane
## i zmienna taka zawiera pary nazwa-wartość argumentu.

## Przykład
# def slownik(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# slownik(a=1, b=2, c=3)

# def witaj(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# witaj(name="yasoob")

########################################## Zapamiętaj:
#### 1. “args” i “kwargs” możesz zastąpić dowolnymi innymi nazwami zmiennych
#### 2. Pamiętaj umieszczając w definicji funkcji wyrażenie z jedną lub dwoma gwiazdkami
### pozwalamy na przekazywanie do niej argumentów w dowolniej liczbie i nazwie.
### bez konieczności konkretnego określenia tych parametrów.
### 3. Pamiętaj o kolejności – wyrażenie z dwoma gwiazdkami
### musi być na końcu, z jedną gwiazdką wcześniej, a pozostałe zdefiniowane argumenty na początku.


#### Gwiazdek możesz również używać w wywołaniu funkcji.
#### Jest to tak zwane rozpakowywanie list i słowników z argumentami.
#### Jeżeli funkcja przyjmuje kilka argumentów i posiadasz listę,
#### która zawiera argumenty, które chcesz przekazać do tej funkcji
#### wystarczy poprzedzić nazwę listy gwiazdką zamiast podawać kolejne argumenty ręcznie.

# list_arg = [1, 3, 5]
#
# def rozpakowywanie(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# rozpakowywanie(*list_arg)     # odpowiednik dużo dłuższego kodu:   rozpakowywanie(list_arg[0], list_arg[1], list_arg[2])
############################################################################################################################################

################################   Zadania do realizacji
## Zadanie 1
# Utwórz 1 funkcje wielu-zmiennych wejściowych, która obliczy wartość wyrażenia
## dla dowolnego jednego argumentu wejściowego, x^x
## dla dowolnych dwóch argumentów wejściowych  x^x,
## dla pozostałych przypadków wyświetli komunikat, że jest błąd.

# def power(*args):
#     if len(args)==1:
#         x=args[0]
#         return x**x
#     elif len(args)==2:
#         x,y=args
#         return x**y
#     else:
#         return "Blad podaj 1 lub 2 argumenty"
# print(power(2))


######### Zadanie 2
## Wczytaj poniższy fragment tekstu opisujący komputer
## Napisz funkcję która ustali liczbę występujących w tym tekście wyrazów wskazanych przez użytkownika
## ciąg nazw i liczba wyszukiwanych wyrazów podanych przez użytkownika jest dowolna,
## niemniej w tekście są wyrazy o nazwach kluczowych i potencjalnie zawsze ważnych
### dla innych użytkowników np. komputera, skaner, uwzględnij je w wyszukiwaniu.

# def il_liczb(txt,c_words):
#     num=0
#     for slowo in c_words:
#         num+=txt.lower().count(slowo)
#     return num
#
# text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
#        'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
#        'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
#        'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
#        'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
#        'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
#        'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
#        'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
#        'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
#        'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'
#
# words_to_find= ['komputer', 'skaner']
# wyr=input("Wpisz wyraz/y: ")
# words_to_find.extend(wyr.split())
# print(il_liczb(text,words_to_find))
# print(words_to_find)


############ Zadanie 3 #################
## Utwórz funkcję o nazwie "SredniaLiczb.py", która wczyta N dowolnych liczb
## i obliczy średnią z w/w liczb, podane przez użytkownika liczby przypisz do listy

# import SredniaLiczb
# SredniaLiczb.srednia_l(5,5,2,8,9)

############ Zadanie 4##################
## Utwórz funkcję o nazwie "ZdanieRozdziel.py", która wczyta od użytkownika pewien dowolny tekst,'
## a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
## funkcja w zależności od ustawionych kolejnych parametrów wejściowych funkcji
## (ustaw domyślnie argumenty wejściowe: True),
## może ale nie musi wyświetlić następujące informacje:
## ile w każdym zdaniu jest fragmentów rozdzielonych przez określony znak np. ',', ';'
## (domyślnie argument wejściowy to przecinek: ',')
## ile w każdym zdaniu jest wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)
## użyj odpowiednich metod dla zmiennych typu string np. split do rozdzielenia elementów: x = ‘blue,red,green’,   x.split(“,”)

# def ZdanieRozdziel(txt, symb=',' , frags=True, words=True  ):
#     doc=txt.split(".")
#     for zdanie in doc:
#         part=zdanie.split(symb)
#         wor=zdanie.split(" ")
#         if frags:
#             print(f'Liczba fragmentów w zdaniu wynosi: {len(part)}')
#         if words:
#             print(f'Liczba slow w zdaniu wynosi: {len(wor)}')
#
# print(ZdanieRozdziel("Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"))


########### Zadanie 5 ########################
## Zdefiniuj funkcję "CiagGometryczny.py", która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2)
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego
## b) sumę elementów ciągu geometrycznego

# import CiagGometryczny
# CiagGometryczny.ciaggometryczny(3,1,2)

############Przykład
### Mamy 2 sklepy  z różnymi produktami
# def test_kwargs(id_sklep = 0, liczba_pracownikow = 5, **kwargs):
#     print(id_sklep)
#     print(liczba_pracownikow)
#     print(kwargs)
#
# test_kwargs(1, mleko=100, woda=500)
# print('#################')
# test_kwargs(2, liczba_pracownikow = 15, drabina=500, cement=200)

# ########################## Zadanie 6
## Zaprojektuj program służący do obsługi prostej bazy danych dla sklepu z
## dowolnej branży o różnej liczbie pracowników. Program zapisuje do kolejnych list
## liczby produktów dostarczonych w danym dniu (nazwa listy odpowiada nazwie towaru)
## liczba towarów powinna być zapamiętana

# Przetestuj swój program dla różnych przypadków dostawy towaru
# Pamiętaj że asortyment sprzedawanego towaru ulega zmianie
# Użyj kwargs



# ########################## Zadanie 7
## W module pole_prostokata.py
## Zdefiniuj funkcję która obliczy pole powierzchni prostokąta
## W module pole_trojkata.py
## Zdefiniuj funkcję która obliczy pole powierzchni trójkąta
# W module pola.py
## Korzystając z modułów pole_prostokata i pole_trojkata
## napisz funkcję która ma możliwość obliczenia pola prostokąta, trójkąta i kwadratu
## Użyj zmiennych globals, utwórz moduł globals.py w którym będą przechowywane
## domyślne wartości dla boków prostokąta, trójkąta, kwadratu (równe 1)

# import globals
# from pola import pola_figur
#
# globals.bok_kwadratu = 3
# globals.bok_prostokata1 = 5
# globals.bok_prostokata2 = 8
# globals.podstawa_trojkata = 6
# globals.wysokosc_trojkata = 7
#
# pola_figur(globals)

# ########################## Zadanie 8
## Zdefiniuj funkcję wyższego rzędu która ma możliwość obliczenia
## pole powierzchni prostokąta i pola powierzchni trójkąta
## Nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj możliwość
## obliczenia pola kwadratu

# def pole_prostokata(a, b):
#     return a * b
#
# def pole_trojkata(a, h):
#     return (a * h)/2
#
# def oblicz(fun, *args):
#     return fun(*args)
#
# def dec(fun):
#     def pole_kwadratu(a, b):
#         if b != 0:
#             b=a
#             return fun(a, b)
#         else:
#             return a**2
#
#     return pole_kwadratu
#
# print("Pole prostokata wynosi:", oblicz(pole_prostokata, 8, 2))
# print("Pole trojkata wynosi:", oblicz(pole_trojkata, 5, 3))
#
# @dec
# def pole_prostokata(a, b):
#     return a * b
#
# print("Pole kwadratu wynosi:", pole_prostokata(5,0))

# ########################## Zadanie 9
## Utwórz funkcję która umożliwia logowanie na serwer
## Ma dwa argumenty wejściowe:
## user i password (domyślne wartości odpowiednio: 'edek2003', 'Wsx123')
## a) nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj dodatkowe
## pola tj. host, port
## b) nie modyfikując zawartości w/w funkcji, użyj dekoratora i  daj możliwość
## wprowadzania dodatkowych innch pól użytkownikowi (wprowadzane jako słownik
##  np. {'data_base': 'https://pl.wikipedia.org'})

# def dec(func,**kwargs):
#     def edit(user,password,**kwargs):
#         func_connect = func(user,password)
#         func_connect.update(kwargs)
#         print(func_connect)
#     return edit
#
# @dec
# def log(user = 'edek2003',password = 'Wsx123'):
#     a={'User': user, 'Password': password}
#     return a
#
# log('Daniello2115', "gjnkd", host='localhost', port=7643, data_base="https://pl.wikipedia.org")

# ########################## Zadanie 10
## Zdefiniuj funkcję ciag_gometryczny, która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2)
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego
## Następnie korzystając z dekoratora udoskonal swoją funkcję,
## dodaj możliwość obliczenia sumy elementów ciągu geometrycznego
# def dec(func):
#     def edit(n,a1=1,q=2):
#         if q == 1:
#             sum_g = a1 * n
#         else:
#             sum_g = a1 * ((1 - q ** n) / (1 - q))
#         func_connect = func(n, a1=a1, q=q)
#         print(func_connect)
#         print("Suma ciagu wynosi: ", sum_g)
#     return edit
# @dec
# def ciag_gometryczny(n,a1=1,q=2):
#     el_enty= a1 * (q ** (n - 1))
#     return f"N-ty wyraz ciagu wynosi: {el_enty}"
# ciag_gometryczny(4,3,3)







