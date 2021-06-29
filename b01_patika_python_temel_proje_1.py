"""

Bir listeyi düzleştiren (flatten) fonksiyon:

"""


def flatten(liste):
    if len(liste) == 0:
        return liste
    if isinstance(liste[0], list):
        return flatten(liste[0]) + flatten(liste[1:])
    return liste[:1] + flatten(liste[1:])


print(flatten([[1,'a',['cat'],2],[[[[3]]],'dog'],4,5]))