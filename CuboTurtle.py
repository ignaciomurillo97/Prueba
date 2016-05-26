import turtle
import math

def elipse(angulo, radioMenor, altura):
    x = 2 * math.cos(angulo * 3.1415 / 180) * radioMenor
    y = math.sin(angulo * 3.1415 / 180) * radioMenor + altura
    return (x, y)

def circulo(angulo, radio):
    x = math.cos(angulo * 3.1415 / 180) * radio
    y = math.sin(angulo * 3.1415 / 180) * radio
    return (x, y)

def conectar(pt1, pt2):
    turtle.penup()
    turtle.goto(pt1)
    turtle.pendown()
    turtle.goto(pt2)

def trasladar(pt):
    turtle.penup()
    turtle.goto(pt)
    turtle.pendown()

def puntosCubo (lado, angulo):
    pts = []
    for i in range(4):
        pts.append(elipse(angulo + 90 * i, lado, -lado))

    for i in range(len(pts)):
        conectar(pts[i], pts[(i+1)%4])

    pts2 = []
    for i in range(4):
        pts2.append(elipse(angulo + 90 * i, lado, lado))

    for i in range(len(pts2)):
        conectar(pts2[i], pts2[(i+1)%4])

    for i in range(len(pts2)):
        conectar(pts[i], pts2[i])

def rombo(radio, alto, angulo):
    pts = []
    for i in range(6):
        pts.append(elipse(angulo + 60 * i, radio, 0))

    for i in range(len(pts)):
        conectar(pts[i], pts[(i+1)%6])
        conectar(pts[i], (0, alto))
        conectar(pts[i], (0, -alto))

def diamante(radio, alto, angulo):
    pts = []
    for i in range(6):
        pts.append(elipse(angulo + 60 * i, radio, 0))

    pts2 = []
    for i in range(6):
        pts2.append(elipse(angulo + 60 * i, radio * 0.7, alto/3))

    for i in range(len(pts)):
        conectar(pts[i], pts[(i+1)%6])
        conectar(pts2[i], pts2[(i+1)%6])
        conectar(pts[i], pts2[i])
        conectar(pts[i], (0, -alto))

i = 0
turtle.ht()
turtle.bgcolor(0.1, 0.1, 0.1)
turtle.color(0.9, 0.9, 0.9)
while True:
    turtle.tracer(0, i)
    puntosCubo(100, i)
    diamante(50, 100, i)
    conectar((0, -250), (0, 250))
    turtle.update()
    turtle.clear()
    i+=0.25

turtle.done()
