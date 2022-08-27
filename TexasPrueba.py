
#bibliotecas
import math 
import time 
import random

# Simplificación de Programa de Texas Hold'Em para entrega de 
# operaciones con operadores 

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Utilizando de momento sólo números y asociando del 11 - 14 como J, Q, K y A

def random_cards(lista):
    carta = random.choice(lista)
    return carta

def eliminar_de_lista(lista_elim, carta):
    for item in lista_elim[:]:
        if item == carta:
            lista_elim.remove(item)
    return lista_elim

carta_1 = random_cards(deck)

eliminar_de_lista(deck, carta_1)

carta_2 = random_cards(deck)

eliminar_de_lista(deck, carta_2)

carta_3 = random_cards(deck)

eliminar_de_lista(deck, carta_3)

promedio = (carta_1 + carta_2 + carta_3) / 3
suma = (carta_1 + carta_2 + carta_3)

print("Tus cartas son: ", "\n", carta_1, "\n", carta_2, "\n", carta_3)
print("El promedio de las cartas dadas es: ", promedio)
print("La suma de las cartas dadas es: ", suma)

if carta_1 > carta_2 and carta_3:
    print("La carta más alta es: ", carta_1)
elif carta_2 > carta_1 and carta_3:
    print("La carta más alta es: ", carta_2)
else:
    print("La carta más alta es: ", carta_3)
