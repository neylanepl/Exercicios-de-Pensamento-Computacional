import turtle

n = int(input("Digite o lado do triângulo:"))

t = turtle.Turtle()

for i in range(1,5):
  for j in range(3):
    t.forward(n * i)
    t.left(120)
    
  t.penup()
  t.forward((n * i) / 2)
  t.right(90)
  t.forward(15)
  t.write( str(i) + "x", align='center', font=('Arial', 8, 'normal'))
  t.forward(-15)
  t.left(90)
  t.forward(((n * i / 2) +10))
  t.pendown()