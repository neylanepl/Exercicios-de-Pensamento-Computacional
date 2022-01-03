def primo(n):
  #for j in range(2,n):
    #if n%j == 0:
      #return false
      
    cont = 0
    for j in range(1,n+1):
      if n % j == 0:
        cont = cont + 1
    if cont == 2:
      return True
    else:
      return False

def par(x):
  if x % 2 == 0:
    return True
  else:
    return False

def multiplo(A,B):
  if A % B == 0:
    return True
  else:
    print(str(A) + " não é multiplo de " + str(B))

def principal():
  n1 = int(input("Informe o número:"))      
  
  if primo(n1) == True:
    print(str(n1) + " é Primo")
  else:
    print(str(n1) + " não é Primo")
    
  if par(n1) == True:
    print(str(n1) + " é Par")
  else:
    print(str(n1) + " é Ímpar")
  
  n2 = int(input("Informe outro número:"))
  
  if multiplo(n1,n2) == True:
    print(str(n1) + " é multiplo de " + str(n2))
   
principal()