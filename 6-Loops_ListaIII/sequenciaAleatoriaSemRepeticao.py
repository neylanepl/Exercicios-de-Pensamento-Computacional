import random
def l(q,i1,i2):
  lista = []
  
  for i in range(q):
      n1 = random.randint(i1,i2)
      while n1 in lista:
          n1 = random.randint(i1,i2) 
      else:
          lista.append(n1)
  return lista
  
quant = int(input("Quantos números?"))
inter1, inter2 = raw_input("Qual o intervalo?").split()
inter1 = int(inter1)
inter2 = int(inter2)


if inter2 - inter1 < quant:
  print("Erro!")
  print("Não posso gerar " + str(quant) + " numeros não repetidos entre " + str(inter1) + " e " + str(inter2) + "!")

else:
  cont = 1 
  print("Seque sua sequencia:")
  for j in l(quant,inter1,inter2):
      print("Elemento " + str(cont) + " = " + str(j))
      cont = cont + 1