
# Proyecto TC-1028, Juego de Póquer, Texas Hold Em

### Sebastián Colín de la Barreda
### A01710148

## ¿Qué es el Texas Hold'Em?

El Texas Hold'Em es una variación popular del Póquer. En esta, se reparten dos cartas a cada jugador.
Estas cartas son privadas, exclusivas a la vista de cada jugador. Por otro lado, se agregaran cinco
cartas al centro. Primero tres juntas, luego una, y al final otra más. 

La idea del juego es que el jugador busque realizar la mejor mano que pueda con las cartas que tiene
y con las cartas repartidas. Uno puede tomar la decisión de retirarse del juego antes de que se revele
cada carta o set de cartas. En esta variación de Póquer siempre se juega con apuesta, utilizando fichas
de apuesta mayor y apuesta menor que van siendo pasadas de jugador en jugador ronda tras ronda.

Este programa pretende emular una mano aleatoria dada al usuario, seguida de una serie de cartas al azar
repartidas al centro. El usuario podrá decidir si continua el juego con la baraja que tiene; además de 
al final ser otorgado el nombre del mejor juego que pueda formar con sus cartas. Para fines prácticos 
se le otorgaran nombres con siglas a las cartas con su respectivo palo y color. 

Corazones rojos = CR
Diamantes rojos = DR
Treboles negros = TN
Picas negras = PN 

## Algorítmo Principal

El juego tendra un deck standar de Póquer, sin comodines y numeros del 2 al 10; adems de un Jack, Queen, King y Ace. 

(EI) Preguntar al usuario si desea jugar Texas Hold'Em

    repartir dos cartas aleatorias al usuario [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

    revelar primeras tres cartas aleatorias [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

    preguntar al usuario se continúa o se dobla 
    
        si continúa == continúa 
            seguir programa 
        sino
            detener programa 

     revelar cuarta carta aleatoria [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

     preguntar al usuario se continúa o se dobla 
    
        si continúa == continúa 
            seguir programa 
        sino
            detener programa 

    revelar quinta y última carta aleatoria [1CR - 10CR, 1DR - 10DR, 1TN - 10TN, 1PN - 10PN, Jack, Queen, King, Ace]

        chechar combinaciones de cartas para devolver el valor del juego mas alto

(EO) Tu mejor juego es: (póquer, full, tercia, corrida, color, corrida color etc.)

    

    
    







