import random

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
sorteio = random.randint(0, 10)

cont = 0
while True:
  n = int(input('Em que número eu pensei? '))
  if n < sorteio:
    cont = cont + 1
    print('Maior... Tente novamente.')
  elif n > sorteio:
    cont = cont + 1
    print('Menor... Tente novamente.')
  elif n == sorteio:
    cont = cont + 1
    print("Acertou com " + str(cont) + " tentativas. Parabéns!")
    break