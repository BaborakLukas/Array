def discount(price, percent):
    """
    Funkce má dvě vstupní hodnoty - cena produktu a slevu v procentech. Vypočítejte,
    jaká bude cena produktu po slevě.
    
    >>> discount(1500, 50)
    750.0
    """
    procent = price / 100
    var = percent * procent
    return (price - var)

print(discount(1500, 50))

def dps(damage, attacks, time, timespan):
    """
    Napište funkci na výpočet dps (damage per second). Na vstupu budou čtyři hodnoty -
    výše dmg za jeden útok, počet útoků za sekundu, časová jednotka a délka času.

    >>> dps(40, 5, 'second', 3)
    600
    >>> dps(100, 1, 'minute', 15)
    90000
    >>> dps(2, 100, 'hour', 1)
    720000
    """


    x = damage * attacks 
    if(timespan == "second"):
        timespan = timespan
    
    if(time == "minute"):
        timespan = timespan * 60
    
    if(time == "hour"):
        timespan = timespan * 3600
    
    y = x * timespan 
    return (y)

print(dps(2, 100, "hour", 1))






def color_invert(Red, Green, Blue):
    """
    Napište funkci color_invert, které bude invertovat barvy zapsané
    ve formátu RGB. Tyto barvy se zapisují stylem (255, 255, 255), 
    kde první hodnota značí hodnotu červené barvy, druhá hodnota značí
    hodnotu zelené barvy a třetí hodnota značí hodnotu modré barvy.
    každá barva má hodnotu od 0 do 255.

    >>> color_invert(255,255,255)
    (0, 0, 0)
    >>> color_invert(165,170,221)
    (90, 85, 34)
    """
    
    
    x = Red
    y = Green
    z = Blue

    a = 255 - x , 255 - y , 255 - z




    return (a)

print(color_invert(165,170,221))

def distance(xa, ya, xb, yb):
    """
    Funkce vypočítá vzdálenost dvou bodů A a B v rovině.
    Body jsou zadané dvojicí souřadnic A(xa, ya), B(xb, yb)

    >>> distance(0, 0, 3, 4)
    5.0
    """







    return ()









# def list_swap(list, old_num, new_num):
#     """
#     Funkce vymění hodnoty old_num za hodnotu new_num v zadaném listu.

#     >>> list_swap([1,5,3,6,5], 5, 0)
#     [1, 0, 3, 6, 0]
#     """

#     return ()




if __name__ == '__main__':
    import doctest
    doctest.testmod()


            

































































