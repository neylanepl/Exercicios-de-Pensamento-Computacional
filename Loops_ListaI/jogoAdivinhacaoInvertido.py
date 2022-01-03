import random

n = int(input('Escolha um número entre 0 e 10, que o computador tentará adivinhar:'))
sorteio = random.randint(0, 10)#sorteao um numero aleatorio entre 0 e 10

cont = 0
max = 10
min = 0

while True:
  
  print("Palpite do computador: " + str(sorteio))
  if n < sorteio:
    cont = cont + 1
    print('Menor... Tente novamente.')
    max = sorteio - 1
    sorteio = random.randint(min, max)
  elif n > sorteio:
    cont = cont + 1
    print('Maior... Tente novamente.')
    min = sorteio + 1
    sorteio = random.randint(min, max)
  elif n == sorteio:
    cont = cont + 1
    print("Acertou com " + str(cont) + " tentativas. Parabéns!")
    break