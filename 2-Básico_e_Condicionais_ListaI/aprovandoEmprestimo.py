#Defini variaveis e transformei input para float
valorCasa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))

meses = 12 * anos#multipliquei por 12 para ficar em meses os anos que foram informados
prestacao = valorCasa / meses #de quanto vai ser a prestacao por mes
prestacao = round(prestacao,2) #aredonda e pega apenas duas casas decimais depois da virgula
porcentagemSalario = salario * (30/100)#calcula o valor que é 30% do salario

# %.2f tbm aredonda, usei dois diferentes só para teste
print("O valor máximo para prestação (margem de 30%) é R$" + "%.2f" % porcentagemSalario)
print("Para pagar uma casa de R$" + "%.2f" % valorCasa + " em " + str(anos) + " anos a prestação será de R$" + str(prestacao))

if prestacao > porcentagemSalario:
  print("Empréstimo NEGADO!")
  
else:
  print("Empréstimo pode ser CONCEDIDO!")