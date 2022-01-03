import turtle

a = float(input("Qual o valor do primeiro termo?"))
r = float(input("Qual o valor da razão?"))

 
for i in range(5):
  for j in range(4):
    turtle.forward(a)
    turtle.left(90)
      
  a = a * r
