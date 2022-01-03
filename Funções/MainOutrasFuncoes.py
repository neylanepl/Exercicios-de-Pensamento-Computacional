import random
import turtle


def semi_circulo(x,y,r):
  turtle.penup()
  turtle.goto(x,y)
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  turtle.pendown()
  turtle.circle(r,360)
  turtle.penup()

def retangulo(x,y,l,a):
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(a)
  turtle.right(90)
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(a)
  turtle.penup()


def main():
  while True:
    vezes = int(input('Quantas vezes quer fazer?'))
    
    
    if vezes >= 0 :
      for i in range (vezes):
        figura = random.randint(0,1)
        turtle.speed(10)
        
        if figura == 0: #retangulo
          xr = 
          yr = input("Digite a posição do retângulo(x y):").split()
          lr = random.randint(20,50)
          ar = random.randint(20,50)
          retangulo(xr,yr,lr,ar)
          
        if figura == 1: #círculo
          xc, yc = input("Digite a posição do círculo(x y):").split()
          rc = random.randint(10,50)
          semi_circulo(xc,yc,rc)
          
    else:
      break
main()
