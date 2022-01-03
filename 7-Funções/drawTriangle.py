import random
import turtle


  
def determinante(x1,y1,x2,y2,x3,y3):  
  determinante = ((x1*y2*1)+(y1*1*x3)+(1*x2*y3))-((1*y2*x3)+(x1*1*y3)+(y1*x2*1))
  return determinante
  
def cor():
  turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def triangulo(x1,y1,x2,y2,x3,y3):
  turtle.penup()
  turtle.goto(x1,y1)
  turtle.pendown()
  turtle.goto(x2,y2)
  turtle.goto(x3,y3)
  turtle.goto(x1,y1)

def main():
  while True:
    vezes = int(input("Quantos triângulos quer desenhar:"))
  
    if vezes >= 0 :
      for i in range (vezes):
        turtle.speed(10)
        xp1 = random.randint(-200, 200) 
        yp1 = random.randint(-200, 200)
        xp2 = random.randint(-200, 200)
        yp2 = random.randint(-200, 200)
        xp3 = random.randint(-200, 200)
        yp3 = random.randint(-200, 200)
        
        
        if determinante(xp1,yp1,xp2,yp2,xp3,yp3) != 0:
            cor()
            triangulo(xp1,yp1,xp2,yp2,xp3,yp3)
        else:
          print("Colineares")
    else:
      break
    
main()