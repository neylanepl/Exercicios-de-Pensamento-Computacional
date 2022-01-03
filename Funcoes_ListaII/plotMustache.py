import matplotlib.pyplot as pyplot
import math

def principal():
  valores_de_x = [] #lista de valores de x
  valores_de_y = [] #lista de valores de y
  x = -2
  for i in range(80):
    x = x + 0.05
    valores_de_x.append(x) #adiciona valores de x na lista
  for x in valores_de_x:
    y = f(x)
    valores_de_y.append(y) #adiciona valores calculados de y na lista
  
  pyplot.plot(valores_de_x,valores_de_y) #plota valores
  pyplot.xlabel('X')
  pyplot.ylabel('Y')
  pyplot.show() #mostra o gráfico

def f(x):
  if -1.5 <= x and x <= 0:
    return (1/math.sqrt(2))* (math.cos(math.pi*x)-math.sin((math.pi*x)/2)+1)

  elif 0 < x and x <= 1.5:
    return (1/math.sqrt(2))* (math.cos(math.pi*x)+math.sin((math.pi*x)/2)+1)
  
  else:
    return 0
    
principal()