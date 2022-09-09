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

def user_cards(lista):
    # Función para las cartas del usuario
    carta_1 = random.choice(lista)
    return carta_1

def main_cards(lista):
    # Función para las cinco cartas centrales
    carta_main = random.choice(lista)
    return carta_main

def elimina_cartas_de_lista(lista, carta):
    # Función para eliminar cartas de la lista y que no se repitan
    for item in lista[:]:
        if item == carta:
            lista.remove(item)
    return lista

def indices(lista):
    if lista[0][0] == '1':
        indices = ['10']
    else:
        indices = [lista[0][0]]
    i = 1
    while i < 7:
        if lista[i][0] == '1':
            indices.append('10')
        else:
            indices.append(lista[i][0])
        i += 1

    return indices

def palos(lista):
    palos = []
    i = 0
    while i < 7:
        if lista[i][0] == '1':
            palos.append(lista[i][2:4])
        else:
            palos.append(lista[i][1:3])
        i += 1
        
    return palos

def analiza_mejor_juego(cartas_completas):
    #analizará el mejor juego
    i = 0
    pass


carta_1 = user_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_1)

carta_2 = user_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_2)

cartas_usuario = [carta_1, carta_2]

carta_main_1 = main_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_1)

carta_main_2 = main_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_2)

carta_main_3 = main_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_3)

cartas_main_primeras_tres = [carta_main_1, carta_main_2, carta_main_3]

carta_main_4 = main_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_4)

carta_main_5 = main_cards(lista_de_cartas)

elimina_cartas_de_lista(lista_de_cartas, carta_main_5)

cartas_main_menos1 = [carta_main_1, carta_main_2, carta_main_3, carta_main_4]

cartas_main = [carta_main_1, carta_main_2, carta_main_3, carta_main_4, carta_main_5]

cartas_total = [carta_main_1, carta_main_2, carta_main_3, carta_main_4, carta_main_5, 
carta_1, carta_2]

""" ======== Zona de Pruebas de Print ==================

print(cartas_usuario, "\n\n" , cartas_main_primeras_tres, "\n\n", lista_de_cartas)

print(indices_de_cartas(carta_1), indices_de_cartas(carta_2), indices_de_cartas(carta_main_1))

print(cartas_main)

 """
    
print("Estas son tus cartas: \n", cartas_usuario)

time.sleep(3)

print("Cartas principales: \n" ,cartas_main_primeras_tres)

time.sleep(2)

opcion = int(input("¿Deseas continuar el juego? \n \n 1 = si 0 = no \n"))

if opcion == 1:
    time.sleep(2)
    print("Siguiente carta: \n", cartas_main_menos1)
elif opcion == 0:
    time.sleep(1)
    print("Te has doblado.")
else:
    time.sleep(1)
    print("La opción introducida es inválida")

time.sleep(2)
elige_2 = int(input("¿Deseas continuar el juego? \n \n 1 = si 0 = no \n"))

if elige_2 == 1:
    time.sleep(2)
    print("Última carta: \n", cartas_main)
elif opcion == 0:
    time.sleep(1)
    print("Te has doblado.")
else:
    time.sleep(1)
    print("La opción introducida es inválida")






