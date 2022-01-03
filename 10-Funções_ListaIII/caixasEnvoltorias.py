import turtle
import random

def principal():
  lc1 = float(input("Informe largura1:"))
  ac1 = float(input("Informe altura1:"))
  xc1 = float(input("Informe x1(canto superior esquerdo):"))
  yc1 = float(input("Informe y1(canto superior esquerdo):"))
  
  lc2 = float(input("Informe largura2:"))
  ac2 = float(input("Informe altura2:"))
  xc2 = float(input("Informe x2(canto superior esquerdo):"))
  yc2 = float(input("Imforme y2(canto superior esquerdo):"))
  
  desenhaCaixa(xc1,yc1,lc1,ac1)
  desenhaCaixa(xc2,yc2,lc2,ac2)
  print(testaColisao(xc1,yc1,lc1,ac1,xc2,yc2,lc2,ac2))
  
def testaColisao(x1,y1,l1,a1,x2,y2,l2,a2):
  if (x1 <= x2 and (x1+l1) >= x2) or (x2 <= x1 and (x2+l2) >= x1):
    if (y1 <= y2 and y1 >= (y2-a2)) or ( y2 <= y1 and y2 >= (y1-a1)):
        return("Colide!")
  
  return("Não colide!")
    
    
def desenhaCaixa(xc,yc,lc,ac):
  t = turtle.Turtle()
  t.penup()
  t.goto(xc,yc)
  t.pendown()
  t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
  for i in range(2):
    t.forward(lc)
    t.right(90)
    t.forward(ac)
    t.right(90)
    
principal()