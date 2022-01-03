import turtle
t = turtle.Turtle()#só pra não ficar digitando turtle, só pra simplificar

#desenhando o semi circulo
t.penup()#Levanta a caneta (os deslocamentos não "riscam")
t.goto(0,-60)#dece para baixo
t.circle(60,90)#o primeiro argumento é o raio e o segundo a extencão dele, se for 180 é um semicirculo
t.pendown()#abaixa a caneta
t.color(211,211,211)#cor no formato rgb
t.begin_fill()#Informa que os próximos desenhos serão preenchidos
t.circle(60,90)
t.goto(0,0)
t.right(180)#Gira à direita de 180 graus
t.end_fill()#Encerra o preenchimento dos desenhos

#desenhando o eixo X
t.color("black")
t.forward(100)#Move x pixels para frente
t.penup()
t.right(90)
t.forward(15)
t.write("X", align='left', font=('Arial', 10, 'normal'))
    #arg - info, que deve ser escrito no TurtleScreen
    #alinhar (opcional) - uma das strings "esquerda", "centro" ou direita "
    #fonte (opcional) - um triplo (nome da fonte, tamanho da fonte, tipo de fonte)
t.forward(-15)
t.left(90)
t.pendown()
t.forward(-120)#volta 120 pq foi 100 e passa 20 pra trás
t.forward(20)

#desenhando o eixo Y
t.left(90)
t.forward(100)
t.penup()
t.left(90)
t.forward(15)
t.write("Y", align='left', font=('Arial', 10, 'normal'))
t.forward(-15)
t.right(90)
t.pendown()
t.forward(-120)
t.forward(20)
t.right(90)

x = float(input("Digite x:"))
y = float(input("Digite y:"))

a =  x * 60#multipliquei por questoes de escala
b = y * 60


if (x >= 0) and (y >= 0) and ((x**2) + (y**2)) <= 1:
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.color("green")
    t.dot(size=5)
    t.penup()
    t.color("black")
    t.goto((a-10),(b+5))#para o ponto ficar um pouco a esquerda e para cima
    t.write("P", align='left', font=('Arial', 10, 'normal'))
    t.goto(0,0)
    t.pendown()
    print("pertence")
else:
  t.penup()
  t.goto(a,b)
  t.pendown()
  t.color("red")
  t.dot(size=5)#tamanho do ponto e posso colocar cor no 2°argumento
  t.color("black")
  t.goto((a-5),(b+10))
  t.write("P", align='left', font=('Arial', 10, 'normal'))
  t.goto(0,0)
  t.pendown()
  print("não pertence")