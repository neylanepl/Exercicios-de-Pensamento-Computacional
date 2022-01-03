print("=-= CALCULADORA DE PALAVRAS =-=")
print("Operações:")
print("add - soma")
print("mul - multiplicação")
print("in - interseção")

op = input("Digite qual operação deseja realizar comforme as opções:")

if op == "add":
  A = input("Digite uma palavra:")
  B = input("Digite outra palavra:")
  C = A + B
  print("O valor de " + A + " add " + B + " é " + C) 
elif op == "mul":
  A = input("Digite uma palavra:")
  N = int(input("Digite um número:"))
  C = A * N
  print("O valor de " + A + " mul " + str(N) + " é " + C)
elif op == "in":
  A = input("Digite uma palavra:")
  B = input("Digite outra palavra:")
  C = A in B#se o valor de A esta em B
  print("O valor de " + A + " in " + B + " é " + str(C))