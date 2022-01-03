import turtle

D = int(input('Quantos degraus descendentes deve ter?'))
A = int(input('Quantos degraus ascendentes deve ter?'))


for i in range(D):
  
  turtle.begin_fill()
  for j in range(2):
    turtle.color('#1B4F8F')
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.color('#4169E1')
  turtle.end_fill()
  
  turtle.penup()
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.pendown()
  
turtle.penup()
turtle.forward(30)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.pendown()

for i in range(A):
  
  turtle.begin_fill()
  for j in range(2):
    turtle.color('#1B4F8F')
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
  turtle.color('#FF0000') 
  turtle.end_fill()
  
  turtle.penup()
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(20)
  turtle.right(90)
  turtle.pendown()