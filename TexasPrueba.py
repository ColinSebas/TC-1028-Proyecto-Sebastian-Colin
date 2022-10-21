"""
====== Programa de Póquer, Texas Hold'Em ======

Simulador de una mano de Texas Hold'Em repartida a 
un sólo jugador. Genera cartas aleatorias que permiten
al usuario decicir o no quedarse en el juego. Al final
devuelve el mejor juego númerico (par, dos pares, tercia
o póquer) que se obtuvo. 
"""
#bilbliotecas
import math 
import random
from re import RegexFlag 
import time
 
"""
Lista de Cartas de una baraja inglesa estándar
"""

lista_de_cartas = [
  "2CR", "3CR","4CR", "5CR", "6CR", "7CR","8CR", "9CR", "10CR",
  "JCR", "QCR", "KCR", "ACR", "2DR", "3DR","4DR", "5DR", "6DR",
  "7DR","8DR", "9DR", "10DR", "JDR", "QDR", "KDR", "ADR", "2TN",
  "3TN","4TN", "5TN", "6TN", "7TN","8TN", "9TN", "10TN", "JTN", 
  "QTN", "KTN", "ATN", "2PN", "3PN","4PN", "5PN", "6PN", "7PN",
  "8PN", "9PN", "10PN", "JPN", "QPN", "KPN", "APN" ]

"""
==== Funciones creadas para el programa ====

"""

def cards(lista):
    """
    (uso de funciones)
    Recibe: lista de cartas de baraja inglesa completa (lista).
    Devuelve: carta al azar generada a partir de la lista.
    """
    carta = random.choice(lista)
    return carta

def elimina_cartas_de_lista(lista, carta):
    """
    (ciclos for, condicionales, funciones)
    Recibe: lista de cartas de baraja ingles completa (lista).
    Elimina la carta generada al azar en la función 'cards'.
    Devuelve: la lista sin la carta especificada. 
    """
    for item in lista[:]:
        if item == carta:
            lista.remove(item)
    return lista

def indices(lista):
    """
    (ciclos while, listas, condicionales, uso de operadores)
    Recibe: lista de las siete cartas que están en juego, dos 
    del jugador y cinco en la mesa.
    Genera una lista exclusiva de los índices de las cartas 
    (números). 
    Devuelve: la lista 'indices' con los valores numéricos de las
    cartas.
    """
    indices = []
    i = 0
    while i < len(lista):
        if lista[i][0] == '1':
            indices.append(10)
        elif lista[i][0] == 'J':
            indices.append(11)
        elif lista[i][0] == 'Q':
            indices.append(12)
        elif lista[i][0] == 'K':
            indices.append(13)
        elif lista[i][0] == 'A':
            indices.append(14)
        else:
            index = lista[i][0]
            index = int(index)
            indices.append(index)
        i += 1

    return indices 

def palos(lista):
    """
    (ciclos while, condicionales, uso de operadores)
    Recibe: lista de las siete cartas que están en juego, dos 
    del jugador y cinco en la mesa.
    Genera una lista exclusiva de los palos de las cartas 
    (corazones, picas, treboles, diamantes). 
    Devuelve: la lista 'palos' con los palos de las cartas.
    """
    palos = []
    i = 0
    while i < len(lista):
        if lista[i][0] == '1':
            palos.append(lista[i][2:4])
        else:
            palos.append(lista[i][1:3])
        i += 1
        
    return palos

def mayor_repeticion(cartas_full):
    """
    (ciclos for, condicionales, listas, diccionarios)
    Recibe: lista de las siete cartas que están en juego, dos 
    del jugador y cinco en la mesa.
    Genera un diccionario con en número de repeticiones de cada
    carta en juego. Y checha si hay dos valores máximos repetidos. 
    Devuelve: la carta con valor máximo y su número de repeticiones, 
    el diccionario con las cartas y en caso de que hayan dos valores 
    máximos, una lista con ambos. 
    """
    diccionario = {}

    for x in cartas_full:
        diccionario[x] = 0
    
    for x in cartas_full:
        diccionario[x] = diccionario[x] + 1
    
    max_val = cartas_full[0]
    max_repe = diccionario[max_val]

    for key in diccionario:
        if diccionario[key] > max_repe:
            max_repe = diccionario[key]
            max_val = key

    dos_val = []

    for key in diccionario:
        if diccionario[key] == max_repe:
            dos_val.append(key)

    
    return max_val, max_repe, diccionario, dos_val

def regresa_a_letra(indice):
    """
    (condicionales)
    Recibe: el indice de una carta > 10 
    y la convierte de regreso a una letra.
    Regresa: indice numérico convertido a 
    letra. 
    """
    if indice < 11:
        letra = indice
    elif indice == 11:
        letra = 'J'
    elif indice == 12:
        letra = 'Q'
    elif indice == 13:
        letra = 'K'
    elif indice == 14:
        letra = 'A'

    return letra 


"""
============== Estructura principal del programa ====================
"""

carta_1 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_1)

carta_2 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_2)

cartas_usuario = [carta_1, carta_2]

carta_main_1 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_1)

carta_main_2 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_2)

carta_main_3 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_3)

cartas_main_primeras_tres = [carta_main_1, carta_main_2, carta_main_3]

carta_main_4 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_4)

carta_main_5 = cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_5)

cartas_main_menos1 = [carta_main_1, carta_main_2, carta_main_3, carta_main_4]

cartas_main = [carta_main_1, carta_main_2, carta_main_3, carta_main_4,
carta_main_5]

cartas_total = [carta_main_1, carta_main_2, carta_main_3, carta_main_4, carta_main_5, 
carta_1, carta_2]

matriz_total = [[indices(cartas_total)], [palos(cartas_total)]]

cards_indexes = sorted(indices(cartas_total))
cards_suits = sorted(palos(cartas_total))
repeticion_max = mayor_repeticion(cards_indexes)

#Inicio de interacción con usuario
print("Guia de cartas: \n \n CR = Corazones Rojos, DR = Diamantes Rojos, \
TN = Treboles Negros, PN = Picas Negras")

time.sleep(3)

print("Estas son tus cartas: \n", cartas_usuario)

time.sleep(3)

print("Cartas principales: \n" ,cartas_main_primeras_tres)

time.sleep(3)

opcion = int(input("¿Deseas continuar el juego? \n \n 1 = si 0 = no \n"))

if opcion == 1:
    time.sleep(2)
    print("Siguiente carta: \n", cartas_main_menos1)
    time.sleep(2)
    elige_2 = int(input("¿Deseas continuar el juego? \n \n 1 = si 0 = no \n"))

    if elige_2 == 1:
        time.sleep(2)
        print("Ultima carta: \n", cartas_main)
        time.sleep(2)
        if len(repeticion_max[3]) == 1:
            if repeticion_max[1] == 2:
                print("Tuviste un par de: ", regresa_a_letra(repeticion_max[0]))
                puntos = repeticion_max[0] * 2
                time.sleep(1)
                print("Hiciste", puntos, "puntos")
            elif repeticion_max[1] == 3:
                print("Tuviste una tercia de: ", regresa_a_letra(repeticion_max[0]))
                puntos = repeticion_max[0] * 3
                time.sleep(1)
                print("Hiciste", puntos, "puntos")
            elif repeticion_max[1] == 4:
                print("Tuviste un póquer de: ", regresa_a_letra(repeticion_max[0]))
                puntos = repeticion_max[0] * 4
                print("Hiciste", puntos, "puntos")
        elif len(repeticion_max[3]) == 2: 
            print("Tuviste dos pares de: ", regresa_a_letra(repeticion_max[-1][0]),
            "y", regresa_a_letra(repeticion_max[-1][1]))
            puntos = (repeticion_max[-1][0] * 2) + (repeticion_max[-1][1] * 2)
            print("Hiciste", puntos, "puntos")
        else:
            print("Tuviste una carta alta: ", regresa_a_letra(max(repeticion_max[3])))
            puntos = max(repeticion_max[3])
            print("Hiciste", puntos, "puntos")
    elif elige_2 == 0:
        time.sleep(1)
        print("Te has doblado.")
    else:
        time.sleep(1)
        print("La opcion introducida es invalida")
elif opcion == 0:
    time.sleep(1)
    print("Te has doblado.")
else:
    time.sleep(1)
    print("La opción introducida es invalida")







