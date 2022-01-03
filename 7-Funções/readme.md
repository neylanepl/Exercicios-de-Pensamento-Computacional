## Primo, par/ímpar, múltiplo/divisor
Em diversos dos nossos programas tivemos a necessidade de responder a essas questões:

- Dado um número N ele primo ou não?
- Dado um número N ele é par ou ímpar?
- Dado dois números A e B, A é múltiplo de B; A é divisor de B?

Para não ter que ficar reescrevendo toda vez, podemos escrever funções que possam ser reusadas em outros programas e que resolvam esses problemas para nós. Assim escreva as funções:

1. primo: recebe um número e retorna True se ele for primo e False se ele não for
2. par: recebe um número e retorna True se ele for par, False se ele for ímpar
3. multiplo: recebe dois números A e B e retorna True se A é multiplo de B

Escreva também um programa que, usando as funções imprima as saídas com base nas entradas abaixo:

```
Ex1:
Informe o número: 3
3 é Primo
3 é Ímpar
Informe outro número: 4
3 não é multiplo de 4.

Ex2:
Informe o número: 10
10 não é Primo
10 é Par
Informe outro número: 2
10 é multiplo de 2.
```

## Main e outras funções
Uma função muito recorrente nas linguagens de programação é a função main. Usualmente, a função main é o ponto de partida dos programas, o que ocorre de forma diferente na linguagem Python, em que não precisamos escrever função alguma para começar a programar.

No entanto, o uso da função main tem suas vantagens, especialmente quando queremos controlar o escopo das variáveis do programa. O programa abaixo é uma implementação em python de um programa parecido com o exercício Desenho Maluco!, ele contem 2 funcionalidades básicas: desenhar um retângulo e desenhar um semi-círculo em locais aleatórios da tela. Reescreva o programa usando 3 funções: uma função main, uma funçao para desenhar o retangulo e outra para desenhar o círculo. As três funções devem ter as seguintes características:

- main: função principal, não recebe parâmetros e nem retorna nada. Deve chamar as demais funções do programa e implementar o comportamento de repetição e leitura da entrada do usuário
- semi_circulo: recebe como parametros uma posição x, y e um raio. Deve desenhar um semi-círculo na posição especificada com uma cor aleatória.
- retangulo: recebe como parmetros uma posição x,y e uma largura e altura do retangulo. Deve desenhar um retangulo com cor aleatória na posição especificada usando os parâmetros recebidos.

Veja que na sua versão reescrita o programa precisa funcionar exatamente como o programa abaixo, logo dentro do main vc deve colocar o while True garantindo que o programa se repete indefinidamente.

```
import random
import turtle

while True:
  vezes = int(input('Quantas vezes quer fazer?'))

  if vezes >= 0 :
    for i in range (vezes):
      figura = random.randint(0,1)
      turtle.speed(10)
      if figura == 0: #retangulo
        turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        l = random.randint(20,50)
        a = random.randint(20,50)
        turtle.penup()
        turtle.goto(random.randint(-200, 200),random.randint(-200, 200))
        turtle.pendown()
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(a)
        turtle.penup()
      if figura == 1: #círculo
        r = random.randint(20,50)
        g = random.randint(0,360)
        turtle.penup()
        turtle.goto(random.randint(-200, 200),random.randint(-200, 200))
        turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        turtle.pendown()
        turtle.circle(r,g)
        turtle.penup()
  else:
    break
```

## Draw Triangle
Com o módulo turtle, podemos fazer alguns desenhos básicos como ponto e círculo. No entanto, muitas aplicaçãoes de desenho nos obrigam a implementar o desenho de várias outras formas. Uma forma básica e não suportada é o triângulo.

Para desenhar um triângulo precisamos de 3 pontos apenas, desde que eles não sejam colineares, eles formarão um triângulo. Usando funções escreva um programa que realize as seguintes operações:

1. Pergunte ao usuário quantos triângulos ele quer desenhar
    1.1 se o número for maior que 0

    - sorteie 3 coordenadas x,y
    - sorteie uma cor
    - desenhe um trângulo na tela com as coordenadas e cor sorteadas (caso seja um triângulo)
    - repita o passo anterior até que o número desejado de triângulos tenha sido desenhado, depois volte ao inicio do program.
2. se o número informado for menor ou igual a 0, encerre o programa.