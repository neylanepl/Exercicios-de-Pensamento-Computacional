import turtle

def main():
        turtle.speed(10)
        xp1 = int(input("Digite x1:"))
        yp1 = int(input("Digite y1:"))
        
        xp2 = int(input("Digite x2:"))
        yp2 = int(input("Digite y2:"))
        
        xp3 = int(input("Digite x3:"))
        yp3 = int(input("Digite y3:"))
        
        t = int(input("Escolha uma das opcões: 1-Translação, 2-Escala: ")) 
        
        turtle.color("blue")
        triangulo(xp1,yp1,xp2,yp2,xp3,yp3)
        
        if t == 1:
          xt = int(input("Digite xt:"))
          yt = int(input("Digite yt:"))
          turtle.color("red")
          translacao(xp1,yp1,xp2,yp2,xp3,yp3,xt,yt)
          
        elif t == 2:
          alfa = int(input("Digite alfa:"))
          turtle.color("red")
          escala(xp1,yp1,xp2,yp2,xp3,yp3,alfa)
          
def triangulo(x1,y1,x2,y2,x3,y3):
  turtle.penup()
  turtle.goto(x1,y1)
  turtle.pendown()
  turtle.goto(x2,y2)
  turtle.goto(x3,y3)
  turtle.goto(x1,y1)

def translacao(x1,y1,x2,y2,x3,y3,xt_,yt_):
  P1x = x1 + xt_
  P1y = y1 + yt_
  P2x = x2 + xt_
  P2y = y2 + yt_
  P3x = x3 + xt_
  P3y = y3 + yt_
  
  triangulo(P1x,P1y,P2x,P2y,P3x,P3y)
  
def escala(x1,y1,x2,y2,x3,y3,alfa_):
  P1x = x1 * alfa_
  P1y = y1 * alfa_
  P2x = x2 * alfa_
  P2y = y2 * alfa_
  P3x = x3 * alfa_
  P3y = y3 * alfa_
  
  triangulo(P1x,P1y,P2x,P2y,P3x,P3y)


main()