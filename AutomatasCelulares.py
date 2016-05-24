import pygame
import random
import time

## colores
backgroundColor = (70, 70, 70)
blanco = (255, 255, 255)
negro = (0, 0, 0)
sombraColor = (50, 50, 50)

## inicializar la ventana
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Automatas Celulares")


## Funcion que dibuja una matriz
def dibujarMatriz (matriz, ladoCuadrado, color, desplazamiento):
    desplazamientoX = screen.get_size()[0]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[0]
    desplazamientoY = screen.get_size()[1]/2 - ladoCuadrado * len(matriz) / 2 + desplazamiento[1]
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if matriz[y][x] == 1:
                cuadrado = (x * ladoCuadrado + desplazamientoX, y * ladoCuadrado + desplazamientoY, ladoCuadrado, ladoCuadrado)
                screen.fill(color, rect=cuadrado)

## Matriz
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
            

## conway
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

m = matrizRandom(50, 40)

m1 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]


siguienteCuadro = time.time() + 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if time.time() > siguienteCuadro:
        screen.fill(backgroundColor)
        dibujarMatriz(m, 10, sombraColor, (-4, 4))
        dibujarMatriz(m, 10, blanco, (0, 0))
        m = conway(m)
        pygame.display.update()
        siguienteCuadro = time.time() + 0.5