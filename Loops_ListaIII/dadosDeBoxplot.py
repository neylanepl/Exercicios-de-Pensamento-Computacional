N = int(input("Digite o tamanho da sequência:"))
v = 0

for i in range(1,(N+1)):
  anterior = v
  v = int(input("Digite valor " + str(i) + " da sequência:"))
  
  if i >= 2:
    if anterior >= v:
      print("Erro! Conjunto tem de estar em ordem crescente")
      break
    
  if i == 1:
    minimo = v
  elif i == N:
    maximo = v
    
  if i == round(N*1/4):
    quartil1 = v
  elif i == round(N*3/4):
    quartil3 = v
  
  if N % 2 == 0:
    if i == (N/2) + 1:
      mediana = (v + anterior) / 2
  else:
    if i == (N+1)/2:
      mediana = v
      
print("Menor elemento:" + str(minimo))
print("1° quartil:" + str(quartil1))
print("Mediana:" + str(mediana))
print("3° quartil:" + str(quartil3))
print("Maior elemento:" + str(maximo))