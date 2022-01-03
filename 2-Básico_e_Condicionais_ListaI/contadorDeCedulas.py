print("=-=-=-= Bem-vindo ao Caixa Eletrônico =-=-=-=")
print("Tenho cédulas de R$100, R$50, R$20, R$10 e R$5")

valor = 2#como era pra ficar repetindo, fiz um while, e dois é  pq ele entra no while
while (valor % 5) != 0:
  valor = int(input("Qual valor deseja sacar: R$"))
  if (valor % 5) != 0:#a condição foi feita para saber se o valor é multiplo de 5 pq o ultimo valor é 5, para poder pagar o valor
    print("Não é possível sacar este valor!")

#a ideia seguida foi que eu vou dividir o valor por 100 e pegar a parte inteira, depois multiplico o inteiro e diminuo do valor    

#Se antes queríamos sacar 256 reais, agora queremos somente 56, pois já demos os 200 reais.
#Vamos transformar nosso valor de 256 para 56

print("Certo, lhe entregarei:")
if valor >= 100:
    cont100 = int(valor/100)
    valor = valor - (cont100 * 100)
    print(str(cont100) + " cédula(s) de R$100")
if valor >= 50 and valor < 100:
    cont50 = int(valor/50)
    valor = valor - (cont50 * 50)
    print(str(cont50) + " cédula(s) de R$50")
if valor >= 20 and valor < 50 :
    cont20 = int(valor/20)
    valor = valor - (cont20 * 20)
    print(str(cont20) + " cédula(s) de R$20")
if valor >= 10 and valor < 20 :
    cont10 = int(valor/10)
    valor = valor - (cont10 * 20)
    print(str(cont10) + " cédula(s) de R$10")
if valor >= 5 and valor < 10 :
    cont5 = int(valor/5)
    valor = valor - (cont5 * 20)
    print(str(cont5) + " cédula(s) de R$5")