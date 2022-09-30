"""
====== Programa de Póquer, Texas Hold'Em ======
"""
#Bilbliotecas
import math 
import random 
import time
 

# Lista de todas las cartas del deck

lista_de_cartas = ["2CR", "3CR","4CR", "5CR", "6CR", "7CR","8CR", "9CR", "10CR"
, "JCR", "QCR", "KCR", "ACR", "2DR", "3DR","4DR", "5DR", "6DR", "7DR","8DR", "9DR", "10DR"
, "JDR", "QDR", "KDR", "ADR", "2TN", "3TN","4TN", "5TN", "6TN", "7TN","8TN", "9TN", "10TN"
, "JTN", "QTN", "KTN", "ATN", "2PN", "3PN","4PN", "5PN", "6PN", "7PN","8PN", "9PN", "10PN"
, "JPN", "QPN", "KPN", "APN" ]

"""
==== Funciones creadas para el programa ====

"""

def cards(lista):
    # Función para repartir cartas al azar
    carta = random.choice(lista)
    return carta

def elimina_cartas_de_lista(lista, carta):
    # Función para eliminar cartas de la lista y que no se repitan
    for item in lista[:]:
        if item == carta:
            lista.remove(item)
    return lista

def indices(lista):
    # Lista de enteros dadas las 7 cartas totales
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
    # Lista de palos de las 7 cartas totales
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
    # Busca el número más repetido en la lista de cartas
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

cartas_main = [carta_main_1, carta_main_2, carta_main_3, carta_main_4, carta_main_5]

cartas_total = [carta_main_1, carta_main_2, carta_main_3, carta_main_4, carta_main_5, 
carta_1, carta_2]

cards_indexes = sorted(indices(cartas_total))
cards_suits = sorted(palos(cartas_total))
repeticion_max = mayor_repeticion(cards_indexes)

print("Estas son tus cartas: \n", cartas_usuario)

time.sleep(3)

print("Cartas principales: \n" ,cartas_main_primeras_tres)

time.sleep(2)

opcion = int(input("¿Deseas continuar el juego? \n \n 1 = si 0 = no \n"))

if opcion == 1:
    time.sleep(2)
    print("Siguiente carta: \n", cartas_main_menos1)
    time.sleep(2)
    elige_2 = int(input("¿Deseas continuar el juego? \n \n 1 = si 0 = no \n"))

    if elige_2 == 1:
        time.sleep(2)
        print("Última carta: \n", cartas_main)
        time.sleep(2)
        print(cards_indexes)
        time.sleep(2)
        print(repeticion_max)
        time.sleep(1)

        if len(repeticion_max[3]) == 1:
            if repeticion_max[1] == 2:
                print("Tuviste un par de:", repeticion_max[0])
            elif repeticion_max[1] == 3:
                print("Tuviste una tercia de:", repeticion_max[0])
            elif repeticion_max[1] == 4:
                print("Tuviste un póquer de:", repeticion_max[0])
        else: 
            print("Tuviste dos pares de:", repeticion_max[-1][0], "y", repeticion_max[-1][1])
    elif elige_2 == 0:
        time.sleep(1)
        print("Te has doblado.")
    else:
        time.sleep(1)
        print("La opción introducida es inválida")
elif opcion == 0:
    time.sleep(1)
    print("Te has doblado.")
else:
    time.sleep(1)
    print("La opción introducida es inválida")







