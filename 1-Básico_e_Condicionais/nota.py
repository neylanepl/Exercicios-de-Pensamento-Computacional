import turtle

submetidas = int(input("Digite quantas atividades foram submeditas ao todo:"))
completas = int(input("Quantas dessas atividades foram completas(corretas e dentro do prazo):"))
incompletas = submetidas - completas

valorCompletas = (4/60)*completas
valorIncompletas = ((4/60)/2)*incompletas
total = valorCompletas + valorIncompletas

print("A nota obtida foi:" + str(total))

t = turtle.Turtle()
t.pensize(50)
t.color("orange")
t.forward(submetidas)
t.goto(0,0)
t.color("green")
t.forward(completas) 




