from helper import decoreer


def print_aanbieding():
            
    #huiswerk 1 t/m 4
    prijzen_dictionary = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5

    } 
    aanbieding = (prijzen_dictionary["vanille"]  * 0.8)
    reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding} ")
    print(reclame_tekst)

    #huiswerk 5
    reclame_tekst2 = reclame_tekst[:62]
    print(reclame_tekst2)

    #huiswerk 6
    reclame_tekst3 = reclame_tekst2.upper()
    print(reclame_tekst3)

    #huiswerk 7
    reclame_tekst4 = reclame_tekst2.split()
    print(reclame_tekst4)

    #huiswerk 8
    for el in reclame_tekst4:
        print(el)

    #huiswerk 9
    for el in reclame_tekst4:
        print(el.lower()) 

    #huiswwerk 10
    for el in reclame_tekst4:
        if len(el) >=5 :
            print(el.upper())
        else:
            print(el.lower())

decoreer("aanbieding")
print_aanbieding()
print(print_aanbieding)


