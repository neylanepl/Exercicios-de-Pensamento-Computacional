import random

while True:
  op = int(input("Escolha o tipo de jogo:\n1 - 6 dezenas\n2 - 7 dezenas\n3 - 8 dezenas\n4 - sair\n:"))
  if op == 4:
    print("Saindo...")
    break
  else:
    modo = int(input("Jogo aleatório (1) ou manual (2)?"))
    if op == 1:
      if modo == 1:
        a = ""
        for i in range(6):
          a = a + str(random.randint(1,60)) + " "
        print("Jogo {}".format(a))
        
      elif modo == 2:
        n1, n2, n3, n4, n5, n6 = raw_input("Digite os valores de n1 n2 n3 n4 n5 n6:").split()
    
    if op == 2:
      if modo == 1:
        a = ""
        for i in range(7):
          a += str(random.randint(1,60)) + " "
        print("Jogo {}".format(a))
    
      elif modo == 2:
        n1, n2, n3, n4, n5, n6, n7 = raw_input("Digite os valores de n1 n2 n3 n4 n5 n6 n7:").split()
    
    if op == 3:
      if modo == 1:
        a = ""
        for i in range(8):
          a += str(random.randint(1,60)) + " "
        print("Jogo {}".format(a))
    
      elif modo == 2:
        n1, n2, n3, n4, n5, n6, n7, n8 = raw_input("Digite os valores de n1 n2 n3 n4 n5 n6 n7 n8:").split()
    
    print("Jogo comfirmado!")
  
  