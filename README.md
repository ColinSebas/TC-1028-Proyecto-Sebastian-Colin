
# Proyecto TC 1028, Juego de Poker, Texas Hold Em

### Sebastian Colin de la Barreda
### A01710148

## Que es el Texas Hold'Em

El Texas Hold'Em es una variacion popular del Poquer. En esta, se reparten dos cartas a cada jugador.
Estas cartas son privadas, exclusivas a la vista de cada jugador. Por otro lado, se agregaran cinco
carta al centro. Primero tres juntas, luego una, y al final otra mas. 

La idea del juego es que el jugador busque realizar el mejor juego que pueda con las cartas que tiene
y con las cartas repartidas. Uno puede tomar la decision de retirarse del juego antes de que se revele
cada carta o set de cartas. En esta variacion de Poquer siempre se juega con apuesta, utilizando fichas
de apuesta mayor y apuesta menor que van siendo pasadas de jugador en jugador cada ronda subsecuente. 

Este programa pretende emular una mano aleatoria dada al usuario, seguida de una serie de carta al azar
repartidas al centro. El usuario podra decidir si continua el juego con la baraja que tiene, ademas de 
al final ser otorgado el nombre del mejor juego que pueda formar con sus cartas. Para fines practicos 
se le otorgaran nombres con siglas a las cartas con su respectivo palo y color. 

Corazones rojos = CR
Diamantes rojos = DR
Treboles negros = TN
Picas negras = PN 

## Algoritmo Principal

El juego tendra un deck standar de poquer, sin comodines y numeros del 2 al 10 ademas de un Jack, Queen, King y Ace. 

(EI) Preguntar al usuario si desea jugar Texas Hold'Em

    repartir dos cartas aleatorias al usuario [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

    revelar primeras tres cartas aleatoria [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

    preguntar al usuario se continua o se dobla 
    
        si continua == continua 
            seguir programa 
        sino
            detener programa 

     revelar cuarta carta aleatoria [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

     preguntar al usuario se continua o se dobla 
    
        si continua == continua 
            seguir programa 
        sino
            detener programa 

    revelar quinta y ultima carta aleatoria [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

        chechar combinaciones de cartas para devolver el valor del juego mas alto

(EO) Tu mejor juego es: (poquer, full, tercia, corrida, color, corrida color etc.)

    

    
    







