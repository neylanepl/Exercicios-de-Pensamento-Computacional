## Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#### Exemplo 1
```	
Valor da casa: R$ 200000
Salário do comprador: R$ 10000
Quantos anos de financiamento? 10
O valor máximo para prestação (margem de 30%) é R$3000.00
Para pagar uma casa de R$200000.00 em 10 anos a prestação será de R$1666.67
Empréstimo pode ser CONCEDIDO!
```

#### Exemplo 2
```
Valor da casa: R$ 200000
Salário do comprador: R$ 5000
Quantos anos de financiamento? 10
O valor máximo para prestação (margem de 30%) é R$1500.00
Para pagar uma casa de R$200000.00 em 10 anos a prestação será de R$1666.67
Empréstimo NEGADO!
```

## Contador de cédulas

Um caixa eletrônico de auto atendimento precisa de um programa para contar quantas cédulas ele precisará entregar a um usuário quando este solicitar um saque de um certo valor. O caixa possui cédulas de R$100, R$50, R$20, R$10 e R$5. Assim, o valor a ser sacado tem que ser entregue com estas cédulas de forma que não haja sobra ou fique faltando alguma parte do dinheiro.

Escreva um programa que peça ao usuário um valor possível de ser sacado e diga quantas cédulas de cada valor serão entregues neste saque.

#### Exemplo 1	
```
=-=-=-= Bem-vindo ao Caixa Eletrônico =-=-=-=
Tenho cédulas de R$100, R$50, R$20, R$10 e R$5
Qual valor deseja sacar: R$ 107
Não é possível sacar este valor!
Qual valor deseja sacar: R$ 110
Certo, lhe entregarei:
1 cédula(s) de R$100
1 cédula(s) de R$10
```

#### Exemplo 2
```
=-=-=-= Bem-vindo ao Caixa Eletrônico =-=-=-=
Tenho cédulas de R$100, R$50, R$20, R$10 e R$5
Qual valor deseja sacar: R$ 295
Certo, lhe entregarei:
2 cédula(s) de R$100
1 cédula(s) de R$50
2 cédula(s) de R$20
1 cédula(s) de R$5
```

## Calculadora de Palavras
Python é uma ótima linguagem para tratar palavras/textos. Existem muitas possibiliades do que pode ser feito, tanto que dá para criarmos uma calculadora de palavras.

Escreva um programa que leia do usuário uma opção e depois, com base nela realize as seguintes operações:

1. Caso opção seja 'add':

    1.1 Peça ao usuário 2 palavras, A e B.

    1.2 Calule a palavra A + B, colocando em uma varíavel C.
    1.3 Imprima a saída: "O valor de < A > add < B > é < C >"
2. Caso opção seja 'mul':

    2.1 Peça ao usuário uma palavra A e um número N.

    2.2 Calule a palavra A * N, colocando em uma varíavel C.
    2.3 Imprima a saída: "O valor de < A > mul < N > é < C >"
3. Caso opção seja 'in':

    3.1 Peça ao usuário 2 palavras, A e B.

    3.2 Calule o resultado da operação A in B, colocando em uma varíavel C.
    
    3.3 Imprima a saída: "O valor de < A > in < B > é < C >"


## Triângulo retângulo isósceles
Um triângulo é isósceles, se, e somente se, ele tem 2 lados iguais. Já um triângulo retângulo ele possui um dos ângulos em 90 graus. Entende-se, portanto, que o triângulo retângulo isósceles tem dois lados iguais e um ângulo reto, conforme mostrado na figura abaixo:

    imagem

Faça um programa que solicite o tamanho de x e desenhe o triângulo retângulo isósceles correspondente.

## Ponto no Semi-Circulo
A figura abaixo é definida pelo conjunto de pontos (x,y) que atendem os seguintes critérios: x>=0, y>=0 e x2+y2<=1. Ou seja, um semi-círculo de raio igual a 1.

    Semi Circulo

Escreva um programa para verificar se um dado ponto p, definido através de suas coordenadas (x,y), pertence ou não à região desenahda na figura. Seu programa deve inicialmente desenhar o semi circulo, os eixos e os textos da figura. Depois o programa deve ler do usuário os valores das coordenadas x e y de P e desenhá-lo. Caso P esteja dentro da figura, ele deve ser desenhando na cor verde, caso não esteja deve ser desenhado na cor vermelha.

Para confirmar visualmente que o ponto pertence ou não à região, desenhe a figura e os pontos em escala. Para fazer isso apenas multiplique todos os valores por algum número fixo. Por exemplo, se a escala é 10, desenhe o semi círuclo com raio 10, e multiplique as coordenadas dos pontos recebidos por 10 antes de desenhar! Veja que a escala é apenas uma questão relacionada ao desenho, não precisa mudar nada na equação.

Atente para os elementos do desenho uma vez que são a parte mais dificil da questão, não se prenda às cores (desde que o arco, as linhas, os pontos e as letras tenham cores diferentes, está ok!), mas tente desenhar todos os elementos!

Algumas dicas para o desenho:

- Use a função com seu parametro adicional, a função recebe dois parâmetros, no formato `circle(r, a)`, onde `r` é o raio e `a` é o grau do arco a ser desenhado.

- Use a função `write(texto, font=('Arial', 8, 'normal'))` . Mudando o tamanho da fonte para um tamanho que fique legível na figura. Lembre de mover a turtle para a posição desejada antes de desenhar.

- Use a função `turtle.dot(size=2)` para desenhar um ponto na posição em que a turtle estiver.

#### Exemplos de pontos que pertencem à regiao

```
x:  1
y:  1
não pertence

x:  0.2
y:  0.2
pertence

x:  -0.1
y:  0.3
não pertence

x:  1
y:  0
pertence
``` 

## Caixa envoltória
Muitos jogos digitais realizam testes de colisão entre elementos do jogos, tais como personagens, balas, muros, alvos, entre outros. Para simplicar os cálculos nos testes de colisão, vários jogos consideram a existência de uma caixa que envolve o personagem (daí o nome "caixa envoltória", do inglês bounding box). Se houver interseção entre as caixas de dois elementos do jogo, significa que um colidiu com o outro. A figura abaixo ilustra o caso de dois personagens, com suas respectivas caixas envoltórias, e a área de colisão em laranja. Mesmo que as imagens deles não se sobreponham, as caixas sim e, por isso, o jogo considera como uma colisão.

    caixas jogos

Desenvolva um teste de colisão simples, envolvendo apenas uma caixa envoltória e um ponto. Escreva um programa que lê inicialmente do usuário quatro valores. Os dois primeiros são as coordenadas do canto superior esquerdo da caixa envoltória (Xesquerda,Ytopo) e os dois seguintes são a largura e altura da caixa, respectivamente. Em seguida, leia do usuário mais dois valores correspondentes às coordenadas do ponto (x,y) que você quer testar.

Se o ponto (x,y) estiver dentro da caixa, informe que o ponto colide com a caixa, caso contrário que não colide. Para verificar visualmente se seu teste está correto, desenhe uma caixa e o ponto fornecidos pelo usuário, como exemplificado na figura abaixo.

    exemplo jogos

#### Exemplos de entrada e saída
```
esquerda: 0
topo: 50
largura: 150
altura: 50
x: 100
y: 40
=> Colide!

esquerda: 40
topo: 40
largura: 50
altura: 50
x: 10
y: 10
=> Não colide!

esquerda: -20
topo: 10
largura: 80
altura: 20
x: 0
y: 0
=> Colide!

esquerda: -50
topo: -30
largura: 10
altura: 10
x: -10
y: 20
=> Não colide!
```