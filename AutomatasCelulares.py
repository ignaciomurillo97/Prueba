import pygame
import random
import time
from copy import deepcopy

## colores
backgroundColor = (70, 70, 70)
blanco = (255, 255, 255)
negro = (0, 0, 0) ## el negro en la funcion dibujarMatriz lo deja "transparente" (no lo dibuja)
sombraColor = (50, 50, 50)
hormiga = (170, 170, 255)

screen = pygame.display.set_mode((0, 0))

## Funcion que dibuja una matriz.
## Entradas:
##  - Matriz: matriz que sera dibujada, esta debe tener como elementos los indices del color que se
##    desea usar  de la matriz "colores", por ejemplo:
##  - ladoCuadrado: la medida de un cuadrado de la matriz
##  - Colores: lista de tuplas de 3 valores que definen lo colores que se usaran, las posiciones de la matriz deberan ser los indices del color en esta lista
##  - desplazamiento: lista de dos elementos que define cuanto se dezplasara la matriz del centro
## Salidas:
##  - Una matriz dibujada en pygame, con los colores definidos por la lista colores
## Restricciones:
##  - La matriz solo puede contener ints
##  - los valores de la matriz deben corresponder a un indice de la lista "colores"
##  - el valor de ladoCuadrado debe ser un int o un float
##  - la lista colores solo puede contener tuplas de 3 floats con valores entre 0 y 255
##  - el desplazamiento debe ser una tupla o una lista de dos floats o ints
def dibujarMatriz (matriz, ladoCuadrado, colores, desplazamiento):

    if not esMatriz(matriz):
        print("la matriz no califica como matriz, revizar que cada lista tenga la misma cantodad de elementos y que todos los elementos sean ints")
        return
    if not isinstance(ladoCuadrado, (int, float)):
        print("la entrada 'lado cuadrado' debe ser un int o un float")
        return

    if not isinstance(colores, list) or any(not isinstance(fila, tuple) or len(fila) != 3 or any (not isinstance(x, int) for x in fila) for fila in colores):
        print("la entrada 'colores' debe ser una lista de tuplas con 3 ints con valor de 0 - 255.")
        return

    if not isinstance(desplazamiento, (list, tuple)) or len(desplazamiento) > 3:
        print("el valor desplazamiento debe ser una lista o tupla de 2 ints")
        return

    if not any(isinstance(x, int) for x in desplazamiento):
        print("los valores de desplazamiento solo pueden ser ints")
        return

    desplazamientoX = screen.get_size()[0]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[0]
    desplazamientoY = screen.get_size()[1]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[1]
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if colores[matriz[y][x]] != negro:
                cuadrado = (x * ladoCuadrado + desplazamientoX, y * ladoCuadrado + desplazamientoY, ladoCuadrado, ladoCuadrado)
                screen.fill(colores[matriz[y][x]], rect=cuadrado)

## funcion que reviza si la entrada es una matriz
## Entrada:
##  - elemento a ser revizado
## Salida:
##  - valor booleano (verdadero si es una matriz y falso si no lo es)
def esMatriz (matriz):
    if not isinstance(matriz, list):
        return False
    if not all(isinstance(x, list) for x in matriz):
        return False
    if not all (len(x) == len(matriz[0]) for x in matriz):
        return False
    if not all ( all(isinstance(x, int) for x in fila )for fila in matriz ):
        return False
    return True



## Funcion que dibuja un cuadrado de color "sombra" en cualquier lugar donde la matriz no sea cero
## debe dibujar antes que la matriz y dara un efecto de sombra en los cuadrados seleccionados
## Entrada:
##  - Matriz: lista de listas de ints, si el int es diferente de 0, no se dibujara sombra
##  - ladoCuadrado: float o int que representa el lado de cada cuadrado que se dibujara por cada elemento en la lista
##  - desplazamient: lista de 2 ints o floats que dara el desplazameinto de la matriz desde el centro en 'x' y 'y'
## Salida:
##  - se dibujara una matriz en pygame donde todos los elementos de la matriz entrada que no sean 0 se llenaran
## restricciones:
##  - la matriz debe contener ints o floats dentro de listas de igual tamaño entre si
##  - el lado cuadrado debe ser un int o un float
##  - el desplazamiento debe ser una lista de 2 ints o floats representando el desplazamiento de la matriz en x o en y
def dibujarSombra (matriz, ladoCuadrado, desplazamiento):

    if not esMatriz(matriz):
        print("la matriz no califica como matriz, revizar que cada lista tenga la misma cantodad de elementos y que todos los elementos sean ints")
        return
    if not isinstance(ladoCuadrado, (int, float)):
        print("la entrada 'lado cuadrado' debe ser un int o un float")
        return

    if not isinstance(desplazamiento, (list, tuple)) or len(desplazamiento) > 3:
        print("el valor desplazamiento debe ser una lista o tupla de 2 ints")
        return

    if not any(isinstance(x, int) for x in desplazamiento):
        print("los valores de desplazamiento solo pueden ser ints")
        return

    desplazamientoX = screen.get_size()[0]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[0]
    desplazamientoY = screen.get_size()[1]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[1]
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if matriz[y][x] != 0:
                cuadrado = (x * ladoCuadrado + desplazamientoX, y * ladoCuadrado + desplazamientoY, ladoCuadrado, ladoCuadrado)
                screen.fill(sombraColor, rect=cuadrado)


## Funcion que crea una matriz cuadrada con un porcentaje dado de 'unos'
## Entradas:
##  - lado: cantidad de filas y columnas que tentra la matriz resultante
##  - probabiliddad: probabidad que tiene cada valor de la matriz en ser 1
## Salidas:
##  - Una matriz cuadrada con un porcentaje de 'unos'
## Restricciones
##  - el lado debe ser un int
##  - la probabiliddad debe ser un int
##  - la probabiliddad debe estar entre 0 y 100
def matrizRandom (lado, probabiliddad):

    if not isinstance(lado, int):
        print("el lado de matriz random debe ser un int")
        return
    if not isinstance(probabiliddad, int):
        print("el lado de matriz random debe ser un int")
        return
    if 0 > probabiliddad > 100:
        print ("la probabiliddad debe estar entre 0 y 100")
        return

    matriz = []
    for y in range(lado):
        fila = []
        for x in range(lado):
            if random.randrange(100) < probabiliddad:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

## vecindades

## Funcion que reviza la cantidad de vecinos vivos en la vecinad de moore que tiene la celula en la posicion x, y
## Entrada:
##  - x: posicion en la columna en la que la cual la celula que se desea revizar esta situada
##  - x: posicion en la fila en la que la cual la celula que se desea revizar esta situada
##  - matriz: matriz en la cual la posicion sera revizada
## Salidas:
##  - float: la cantidad de vecinos vivos que tiene una celula
## Restricciones:
##  - x debe ser un int y estar en el rango de la matriz
##  - y debe ser un int y estar en el rango de la matriz
##  - la matriz debe calificar como matriz
## Nota:
##  - SI una celula esta en el borde o en una esqina tendra menos vecinos
def celulasAdyacentes (x, y, matriz):

    if not isinstance(x, int):
        print("celulasAdyacentes: el valor x debe ser un int")
        return
    if not isinstance(y, int):
        print("celulasAdyacentes: el valor y debe ser un int")
        return
    if 0 > x > len(matriz[0]):
        print("celulasAdyacentes: x esta fuera de los limites de la matriz")
        return
    if 0 > y > len(matriz):
        print("celulasAdyacentes: y esta fuera de los limites de la matriz")
        return

### NOTA!! esta funcion esa comentada por que se pega pygame cuando la matriz es muy grande (mayor que 25x25 se me pega), aun asi la funcion sirve
    #if not esMatriz(matriz):
    #    print("Celulas Adyacentes: la matriz no califica como matriz.")
    #    return

    vecinos = 0
    ancho = len(matriz[0])
    alto = len(matriz)

    if y != 0 and matriz[(y-1)][x] == 1:
        vecinos += 1
    if y != alto - 1 and matriz[(y+1)][x] == 1:
        vecinos += 1
    if x != 0 and matriz[y][(x-1)] == 1:
        vecinos += 1
    if x != ancho - 1 and matriz[y][(x+1)] == 1:
        vecinos += 1

    return vecinos

## Funcion que reviza la cantidad de vecinos vivos inmediatamente diagonales que tiene la celula en la posicion x, y
## Entrada:
##  - x: posicion en la columna en la que la cual la celula que se desea revizar esta situada
##  - x: posicion en la fila en la que la cual la celula que se desea revizar esta situada
##  - matriz: matriz en la cual la posicion sera revizada
## Salidas:
##  - float: la cantidad de vecinos vivos que tiene una celula
## Restricciones:
##  - x debe ser un int y estar en el rango de la matriz
##  - y debe ser un int y estar en el rango de la matriz
##  - la matriz debe calificar como matriz
def celulasDiagonales (x, y, matriz):
    if not isinstance(x, int):
        print("celulasAdyacentes: el valor x debe ser un int")
        return
    if not isinstance(y, int):
        print("celulasAdyacentes: el valor y debe ser un int")
        return
    if 0 > x > len(matriz[0]):
        print("celulasAdyacentes: x esta fuera de los limites de la matriz")
        return
    if 0 > y > len(matriz):
        print("celulasAdyacentes: y esta fuera de los limites de la matriz")
        return
### NOTA!! esta funcion esa comentada por que se pega pygame cuando la matriz es muy grande (mayor que 25x25 se me pega), aun asi la funcion sirve
    #if not esMatriz(matriz):
    #    print("Celulas Adyacentes: la matriz no califica como matriz.")
    #    return

    vecinos = 0
    ancho = len(matriz[0])
    alto = len(matriz)
    if x != 0 and y != 0 and matriz[(y-1)][(x-1)] == 1:
        vecinos += 1
    if x != ancho-1 and y != 0 and matriz[(y-1)][(x+1)] == 1:
        vecinos += 1
    if x != 0 and y != alto-1 and matriz[(y+1)][(x-1)] == 1:
        vecinos += 1
    if x != ancho-1 and y != alto-1 and matriz[(y+1)][(x+1)] == 1:
        vecinos += 1

    return vecinos


## Funcion que calcula el sigiente estado de la matriz segun las reglas del automata de Conway
## Entrads:
##  - Matriz:el estado actual de la matriz al que se le desea aplicar conway
## Salidas:
##  - la matriz resultante tras aplicarle las reglas del automata de Conway
## Restricciones:
##  - la matriz debe calificar como matriz
def conway (matriz):
    if not esMatriz(matriz):
        print("Conway: la matriz no esta correcta")
        return

    nuevaMatriz = [ [0 for i in range(len(matriz[0]))] for j in range(len(matriz)) ]
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            vecinos = celulasAdyacentes(x, y, matriz) + celulasDiagonales(x, y, matriz)
            #print(vecinos)

            if matriz[y][x] == 1:
                if vecinos < 2 or vecinos > 3:
                    nuevaMatriz[y][x] = 0
                else:
                    nuevaMatriz[y][x] = 1
            else:
                if vecinos == 3:
                    nuevaMatriz[y][x] = 1
                else:
                    nuevaMatriz[y][x] = 0
    return nuevaMatriz

## Funcion auxiliar para la Funcion hormiga langton, devuelve la posicion de la hormiga 1 cuadro en la direccion que esta orientada la hormiga
## Entradas:
##  - hormigaPos: tupla o lista con la posicion actual de la hormiga en la matriz
##  - hormigaOrientacion: recibe un int entre 0 y 4 con la hormigaOrientacion de la hormiga
## Salidas:
##  - tupla de dos ints con la nueva posicion de la hormiga
def moverOrmiga(hormigaPos, hormigaOrientacion):
    if hormigaOrientacion == 0:
        hormigaPos[0] += 1
    elif hormigaOrientacion == 1:
        hormigaPos[1] += 1
    elif hormigaOrientacion == 2:
        hormigaPos[0] -= 1
    elif hormigaOrientacion == 3:
        hormigaPos[1] -= 1

    return hormigaPos

## Funcion que calcula el siguiente estado de una matriz segun las reglas de hormiga de langton
## Entradas:
##  - Matriz: una matriz con los valores actuales del Automata
##  - hormigaPos: una lista con la posicion actual de la hormiga dentro de la matriz del Automata
##  - hormigaOrientacion: Direccion en la que esta orientada la hormiga
## Salidas:
##  - retorna el siguiente estado de la matriz segun las reglas del automata 'Hormiga de Langton'
## Restricciones:
##  - la matriz debe calificar como matriz
##  - la posicion de la hormiga debe ser una tupla de dos ints
##  - la orientacion de lo hormiga debe ser 0, 1, 2 o 3
def hormigaLangton(matriz, hormigaPos, hormigaOrientacion):

    if not esMatriz(matriz):
        print("La matriz no califica como matriz")
        return
    if not isinstance(hormigaPos, list) or len(hormigaPos) != 2:
        print("la posicion de la hormiga debe ser una lista de 2 eleentos")
        return
    if not all (isinstance(x, int) for x in hormigaPos):
        print("todos los elementos de hormiga pos deben ser ints")
        return
    if not isinstance(hormigaOrientacion, int) or 0 > hormigaOrientacion > 3:
        print("la orientacion de la ormiga debe ser 0, 1, 2 o 3")
        return

    x = hormigaPos[0]
    y = hormigaPos[1]
    if 0 < x < (len(matriz[0]) - 1) and 0 < y < (len(matriz) - 1):
        if matriz[y][x] == 0: ## celula muerta
            matriz[y][x] = 1 ## cambiar color del espacio donde esta la hormiga
            hormigaOrientacion = (hormigaOrientacion-1)%4 ## giro derecha
            hormigaPos = moverOrmiga(hormigaPos, hormigaOrientacion) ## avanzar un espacio
            return matriz, hormigaPos, hormigaOrientacion

        else: ## celula viva
            matriz[y][x] = 0 ## cambiar color del espacio donde esta la hormiga
            hormigaOrientacion = (hormigaOrientacion+1)%4 ## giro izquierda
            hormigaPos = moverOrmiga(hormigaPos, hormigaOrientacion) ## avanzar un espacio
            return matriz, hormigaPos, hormigaOrientacion

    else:
        return matriz, hormigaPos, hormigaOrientacion

## Crear Matrices

## procedimiento que corre connway en una ventana de pygame
## Entradas:
##  - tamañoMatriz: float que define el ancho y el alto de la matriz que se usara para el automata
## Restrucciones:
##  - tamañoMatriz debe ser un int
def correrConway(tamañoMatriz):
    if not isinstance(tamañoMatriz, int):
        print("el tamaño de la matriz debe ser un int")
        return

    m = matrizRandom(tamañoMatriz, 50)

    ## inicializar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((len(m) * 3 + 25, len(m) * 3 + 25))
    pygame.display.set_caption("Automatas Celulares")

    ## musica

    pygame.mixer.music.load("Backlash.mp3")
    pygame.mixer.music.play(-1, 0.02)
    siguienteCuadro = time.time() + 0.4
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if time.time() > siguienteCuadro:
            screen.fill(backgroundColor)
            dibujarSombra(m, 3, (-4, 4))
            dibujarMatriz(m, 3, [negro, blanco], (0, 0))

            m = conway(m)

            pygame.display.update()
            siguienteCuadro = time.time() + 0.5

## procedimiento que corre el automata celular 'la hormiga de langton'
## Entradas:
##  - tamañoMatriz: float que define el ancho y el alto de la matriz que se usara para el automata
## Restrucciones:
##  - tamañoMatriz debe ser un int
def correrHormiga(tamañoMatriz):

    if not isinstance(tamañoMatriz, int):
        print("el tamaño de la matriz debe ser un int")
        return

    parametros
    m = [[0 for x in range(tamañoMatriz)] for y in range(tamañoMatriz)]
    pos = [49, 49]
    orientacion = 0
    delay = 0


    siguienteCuadro = time.time() + delay

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if time.time() > siguienteCuadro:
            screen.fill(backgroundColor)
            dibujarSombra(m, 5, (-4, -4))

            m1 = deepcopy(m)
            m1[pos[1]][pos[0]] = 2
            dibujarMatriz(m1, 5, [negro, blanco, hormiga], (0, 0))

            m, pos, orientacion = hormigaLangton(m, pos, orientacion)

            pygame.display.update()
            siguienteCuadro = time.time() + delay

#correrHormiga(matrizHormiga, [49, 49], 0, 0)
correrConway(100)

## pruebas!!
