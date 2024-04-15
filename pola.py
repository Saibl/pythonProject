from pole_prostokata import Pp_prostokata
from pole_trojkata import Pp_trojkata
from globals import bok_kwadratu

def Pp_kwadrat(a=bok_kwadratu):
    return a ** 2

def pola_figur(globals):
    print(f'Pole prostokata: {Pp_prostokata(globals.bok_prostokata1, globals.bok_prostokata2)}')
    print(f'Pole trojkata: {Pp_trojkata(globals.podstawa_trojkata, globals.wysokosc_trojkata)}')
    print(f'Pole kwadratu: {Pp_kwadrat(globals.bok_kwadratu)}')