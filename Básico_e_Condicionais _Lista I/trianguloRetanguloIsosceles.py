import turtle
import math

x = float(input("Digite x(base do triângulo retângulo isósceles):"))
t = turtle.Turtle()#só pra não ficar digitando turtle, só pra simplificar

t.forward(x)#Move x pixels para frente
t.left(135)#Gira à esquerda 135 graus, no caso o triangulo tem 45 graus pq 180-45=135

hipotenusa = math.sqrt((x**2) + (x**2))#teorema de pitagoras,"A soma dos quadrados de seus catetos corresponde ao quadrado de sua hipotenusa
t.forward(hipotenusa)
t.left(135)
t.forward(x)