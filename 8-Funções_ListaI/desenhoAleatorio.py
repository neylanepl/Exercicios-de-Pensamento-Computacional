import random
import turtle

def main():
  while True:
    vezes = int(input('Quantas vezes quer fazer?'))
    
    if vezes >= 1: 
      for i in range (vezes):
        figura = random.randint(0,1)
        turtle.speed(10)
        
        if figura == 0: #quadrado
          xq = random.randint(-200, 200)
          yq = random.randint(-200, 200)
          lq = random.randint(10,50)
          quadrado(xq,yq,lq)
          
        if figura == 1: #círculo
          xc = random.randint(-200, 200)
          yc = random.randint(-200, 200)
          rc = random.randint(10,50)
          circulo(xc,yc,rc)
          
    elif vezes == 0:
      break

def circulo(x,y,r):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
  turtle.circle(r)
  turtle.end_fill()
  
def quadrado(x,y,l):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
  for i in range(4):
    turtle.forward(l)
    turtle.right(90)
  turtle.end_fill()

main()