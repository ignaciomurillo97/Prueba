import turtle
import math

def elipse(angulo, radioMenor, altura):
    x = 2 * math.cos(angulo * 3.1415 / 180) * radioMenor
    y = math.sin(angulo * 3.1415 / 180) * radioMenor + altura
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

i = 0
turtle.ht()
while True:
    turtle.tracer(0, i)
    puntosCubo(100, i)
    puntosCubo(50, -i)
    turtle.update()
    turtle.clear()
    i+=0.25
turtle.done()
