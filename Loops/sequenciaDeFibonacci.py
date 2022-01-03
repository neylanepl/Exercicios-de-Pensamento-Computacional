n1 = int(input("Qual o valor de n1?"))
n2 = int(input("Qual o valor de n2?"))

if n1 < n2:
  ultimo = 0
  penultimo = 0
  cont = True
  while cont:
    for i in range(n2+1):
      if i >= n1:
        print('Fibonacci(' + str(i) + ') = ' + str(ultimo))
        
      ultimo = ultimo + penultimo
      penultimo = ultimo - penultimo
      
      if ultimo == 0:
        ultimo = ultimo + 1
        
    cont = False
    
else:
  print("Digite um valor em n2 que seja maior do que n1.")