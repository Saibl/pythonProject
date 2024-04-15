def srednia_l(*args):
    lis = []
    for i in args:
        lis.append(i)
    summ = sum(lis)
    wynik = summ/len(lis)
    print("Srednia liczb wynosi: ", wynik)