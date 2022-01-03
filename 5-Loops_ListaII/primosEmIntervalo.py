n1 = int(input("Digite n1:"))
n2 = int(input("Digite n2:"))


primos = 0
if n2 > n1:
  for i in range(n1,n2+1):
    cont = 0 #deve ser 0 em cada interação
    for j in range(1,n2+1):
      if i % j == 0:
        cont = cont + 1
    if cont == 2:
      primos = primos + 1
      
  print("Existem " + str(primos) + " numeros primos entre " + str(n1) + " e " + str(n2))