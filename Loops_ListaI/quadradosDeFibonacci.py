import turtle

while True:
  n1 = int(input("Valor de n1?"))
  n2 = int(input("Valor de n2?"))
  
  if n1 >= 0:
    if n1 < n2:
      ultimo = 0
      penultimo = 0
      
      for i in range(n2+1):
        if i >= n1:
          turtle.color('#4169E1')
          turtle.begin_fill()
          if i != 0:
            for j in range(4):
              turtle.forward(ultimo*10)
              turtle.left(90)
          turtle.end_fill()
              
          turtle.penup()
          turtle.color('black')
          turtle.forward(ultimo*10 / 2)
          turtle.right(90)
          turtle.forward(15)
          turtle.write("F", align='center', font=('Arial', 8, 'normal'))
          turtle.left(90)
          turtle.forward(5)
          turtle.right(90)
          turtle.forward(2)
          turtle.write(str(i), align='center', font=('Arial', 5, 'normal'))
          turtle.forward(-2)
          turtle.left(90)
          turtle.forward(-5)
          turtle.right(90)
          turtle.forward(-15)
          turtle.left(90)
          turtle.forward(ultimo*10 / 2)
          turtle.forward(10)
          turtle.pendown()
          
          
        ultimo = ultimo + penultimo
        penultimo = ultimo - penultimo
        
        if ultimo == 0:
          ultimo = ultimo + 1
    else:
      print("Digite um valor em n2 que seja maior do que n1.")
  else:
    print("Digite um valor que seja maior ou igual a 0")
  
    
