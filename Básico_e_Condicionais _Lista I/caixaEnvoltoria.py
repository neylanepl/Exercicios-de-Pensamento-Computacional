import turtle

esquerda = float(input("esqueda:"))
topo = float(input("topo:"))
largura = float(input("largura:"))
altura = float(input("altura:"))
x = float(input("x:"))
y = float(input("y:"))

t = turtle.Turtle()

t.penup()
t.goto(esquerda,topo)
t.pendown()
t.forward(largura)
t.right(90)
t.forward(altura)
t.right(90)
t.forward(largura)
t.right(90)
t.forward(altura)
t.right(90)
t.penup()
t.goto(0,0)
t.pendown()

#se x do ponto maior que o x da esquerda e x menor que a oura lateral da caixa, então ele ta dentro
#se y do ponto  maior que o ponto debaixo da caixa e y menor que o topo, então ta dentro
if ((x >= esquerda) and (x <= (esquerda + largura))) and ((y >= (topo - altura)) and (y <= topo)):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(size=5)
    print("=> Colide!")
else:
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.dot(size=5)
  print("=> Não colide!")