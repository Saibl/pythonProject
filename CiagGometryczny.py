def ciaggometryczny(n,a1=1,q=2):
    el_enty= a1 * (q ** (n - 1))
    if q==1:
        sum_g = a1 * n
    else:
        sum_g = a1 * ((1 - q ** n) / (1 - q))
    print("N-ty wyraz ciagu wynosi: ", el_enty)
    print("Suma ciagu wynosi: ", sum_g)

ciaggometryczny(4,3,3)