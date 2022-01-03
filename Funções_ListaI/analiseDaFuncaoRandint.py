import random

def principal():  
  inicio = int(input("Inteiro inicial do intervalo?"))
  fim = int(input("Inteiro final do intervalo?"))
  vezes = int(input("Quantidade de escolhas?"))
  
  lista = []
  #for i in range(vezes):
  cont = 0
  while cont <= vezes:
    n = random.randint(inicio,fim)
    lista.append(n)
    cont = cont + 1
    
  for j in range(inicio,fim+1):
    print(str(j) + " - " + pares(lista))

def pares(l):
  cont = 0
  for i in l:
    if i % 2 == 0:
      cont = cont + 1
  return cont
  
def quantidade(l,x):
  quant = l.count(x)
  return str(quant)


    
principal()