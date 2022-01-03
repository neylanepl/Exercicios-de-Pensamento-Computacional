import turtle

valor = int(input("Digite o tamanho da linha:"))
print("1 - azul")
print("2 - vermelho")
print("3 - verde")
cor = int(input("Escollha uma cor:"))
t = turtle.Turtle()

if cor==1:
  t.color("blue")
elif cor==2:
  t.color("red")
elif cor==3:
  t.color("green")
  
t.pensize(10)
t.forward(valor)
