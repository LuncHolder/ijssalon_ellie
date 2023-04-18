
from algemene_functies import mijn_functie_2


def aanbieding(smaak, prijs,korting):
    korting = prijs - prijs * korting
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    return uitvoer

print(aanbieding("aardbei", 4 ,0.1))


#huiswerk 6

def inkomsten_totaal(inkomsten):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    return totaal

inkomsten =[220,430,125,160,205,90,345]
print(inkomsten_totaal(inkomsten))


# huiswerk 7

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    btw = totaal * 0.09
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer

btw = 0.09
inkomsten =[220,430,125,160,205,90,345]


print(inkomsten_totaal(inkomsten,btw))


# huiswerk 8

def laag_en_hoog(mijn_lijst):
    uitvoer1 = max(mijn_lijst)
    uitvoer2 = min(mijn_lijst)
    return uitvoer1,uitvoer2


mijn_lijst = [220,430,125,160,205,90,345]

print(laag_en_hoog(mijn_lijst))


# huiswerk 9

def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    gemiddelde = som / lengte
    return gemiddelde

mijn_lijst = [220,430,125,160,205,90,345]
lengte = len(mijn_lijst)

print(gemiddelde(mijn_lijst))


# huiswerk 10

def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    gemiddelde = som / lengte
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return uitvoer

mijn_lijst = [220,430,125,160,205,90,345]
lengte = len(mijn_lijst)

print(gemiddelde(mijn_lijst))



# huiswerk 11
def meervoudig(invoer_lijst):
   uitvoer = laag_en_hoog(invoer_lijst)
   return uitvoer

invoer_lijst = [10,5,3,2,1,2,9]
print(meervoudig(invoer_lijst))


#huiswerk 12
# Er bestaat geen bestand aanbieding.py, heb de import op dit blad toegepast in regel 1
# Ik snap de opdracht niet.

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    mijn_functie_2 = korte_lijst
    return mijn_functie_2

invoer_lijst_2 = invoer_lijst
print(combinatie(invoer_lijst_2))