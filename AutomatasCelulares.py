import pygame
import random
import time
from copy import deepcopy

## colores
backgroundColor = (70, 70, 70)
blanco = (255, 255, 255)
negro = (0, 0, 0) ## el negro en la funcion dibujarMatriz lo deja "transparente" (no lo dibuja)
sombraColor = (50, 50, 50)
ormiga = (170, 170, 255)

## inicializar la ventana de pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Automatas Celulares")


## Funcion que dibuja una matriz.
## Entradas:
##  - Matriz: matriz que sera dibujada, esta debe tener como elementos los indices del color que se
##    desea usar  de la matriz "colores", por ejemplo:
##  - ladoCuadrado: la medida de un cuadrado de la matriz
##  - Colores: lista de colores que se usaran, el ne

def dibujarMatriz (matriz, ladoCuadrado, colores, desplazamiento):
    desplazamientoX = screen.get_size()[0]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[0]
    desplazamientoY = screen.get_size()[1]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[1]
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if colores[matriz[y][x]] != negro:
                cuadrado = (x * ladoCuadrado + desplazamientoX, y * ladoCuadrado + desplazamientoY, ladoCuadrado, ladoCuadrado)
                screen.fill(colores[matriz[y][x]], rect=cuadrado)


## Funcion que dibuja un cuadrado de color "sombra" en cualquier lugar donde la matriz no sea cero
## debe dibujar antes que la matriz y dara un efecto de sombra en los cuadrados seleccionados
def dibujarSombra (matriz, ladoCuadrado, desplazamiento):
    desplazamientoX = screen.get_size()[0]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[0]
    desplazamientoY = screen.get_size()[1]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[1]
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if matriz[y][x] != 0:
                cuadrado = (x * ladoCuadrado + desplazamientoX, y * ladoCuadrado + desplazamientoY, ladoCuadrado, ladoCuadrado)
                screen.fill(sombraColor, rect=cuadrado)


## Funcion que crea una matriz con un porcentaje dado de 'unos'
def matrizRandom (lado, probabiliddad):
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
def celulasAdyacentes (x, y, matriz):
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


def celulasDiagonales (x, y, matriz):
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


## Automata Conway
def conway (matriz):
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

## moverOrmiga
def moverOrmiga(ormigaPos, ormigaOrientacion):
    if ormigaOrientacion == 0:
        ormigaPos[0] += 1
    elif ormigaOrientacion == 1:
        ormigaPos[1] += 1
    elif ormigaOrientacion == 2:
        ormigaPos[0] -= 1
    elif ormigaOrientacion == 3:
        ormigaPos[1] -= 1

    return ormigaPos

## Funcion Ormiga de langton
def hormigaLangton(matriz, ormigaPos, ormigaOrientacion):
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if [x, y] == ormigaPos: ## buscar el cuadrado en el que esta la ormiga
                if 0 < x < (len(matriz[0]) - 1) and 0 < y < (len(matriz) - 1):
                    if matriz[y][x] == 0: ## celula muerta
                        matriz[y][x] = 1 ## cambiar color del espacio donde esta la ormiga
                        ormigaOrientacion = (ormigaOrientacion-1)%4 ## giro derecha
                        ormigaPos = moverOrmiga(ormigaPos, ormigaOrientacion) ## avanzar un espacio
                        return matriz, ormigaPos, ormigaOrientacion

                    else: ## celula viva
                        matriz[y][x] = 0 ## cambiar color del espacio donde esta la ormiga
                        ormigaOrientacion = (ormigaOrientacion+1)%4 ## giro izquierda
                        ormigaPos = moverOrmiga(ormigaPos, ormigaOrientacion) ## avanzar un espacio
                        return matriz, ormigaPos, ormigaOrientacion

                else:
                    return matriz, ormigaPos, ormigaOrientacion




## Crear Matrices
m = matrizRandom(100, 50)
m1 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

def correrConway(m):
    siguienteCuadro = time.time() + 0.5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if time.time() > siguienteCuadro:
            screen.fill(backgroundColor)
            dibujarSombra(m, 5, (-4, 4))
            dibujarMatriz(m, 5, [negro, blanco], (0, 0))

            m = conway(m)

            pygame.display.update()
            siguienteCuadro = time.time() + 0.5

def correrHormiga(m, pos, orientacion, delay):
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
            dibujarMatriz(m1, 5, [negro, blanco, ormiga], (0, 0))

            m, pos, orientacion = hormigaLangton(m, pos, orientacion)

            pygame.display.update()
            siguienteCuadro = time.time() + delay

#correrHormiga(m, [49, 49], 0, 0)
correrConway(m)
