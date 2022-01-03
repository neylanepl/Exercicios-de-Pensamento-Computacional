import matplotlib.pyplot as plt 
import random

def principal():  
  i = int(input("Inteiro inicial do intervalo?"))
  f = int(input("Inteiro final do intervalo?"))
  v = int(input("Quantidade de escolhas?"))

  l = escolhasAleatorias(i,f,v)
  
  exibeContagem(i,f,l)
  exibeGrafico(i,f,v,l)


def escolhasAleatorias(inicio,fim,vezes):
  lst = []
  for i in range(vezes):
    n = random.randint(inicio,fim)
    lst.append(n)
  return lst


def exibeContagem(inicio,fim,lista):
  for j in range(inicio, fim + 1):
    print(str(j) + " - " + str(quantidade(lista,j)))


def quantidade(l,x): 
  quant = l.count(x)
  return quant


def porcentagem(inicio,fim,vezes,lista):
  porcent = []
  media = vezes / (fim - inicio+1)
  for k in range(inicio, fim+1):
    porcent.append((quantidade(lista,k)-media)/(fim-inicio+1))
  return porcent
  

def elementos(inicio,fim):
  e = []
  for j in range(inicio, fim + 1):
    e.append(j)
  return e
  
def exibeGrafico(inicio,fim,vezes,lista):
  plt.plot(elementos(inicio,fim), porcentagem(inicio,fim,vezes,lista), 'go-')
  plt.xlabel('Elemento do intervalo')
  plt.ylabel('%')
  plt.show()

principal()