## Tabuada

Faça um programa que imprima a tabuada de 6, 7 e 8, conforme exemplo, usando apenas 4 linhas de código.

#### Exemplo
```
=-=-=-= Tabuada de 6 =-=-=-=
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
=-=-=-= Tabuada de 7 =-=-=-=
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
=-=-=-= Tabuada de 8 =-=-=-=
8 x 1 = 6
8 x 2 = 16
...
8 x 10 = 80
```

## Elementos da sequência de Fibonacci
A sequencia de fibonacci é uma das mais famosas sequencias matemáticas, pois possui inumeras aplicações práticas. Os elementos desta sequencia são calculados através da equação abaixo:

    Fn= 0, se n=0
        1, se n=1
        Fn−1+Fn−2, caso contrario.

Na equação o elemento n da sequencia, Fn, é calculado com base nos dois elementos anteriores. Veja que n é obrigatóriamente um inteiro maior ou igual a 0. Usando esta fórmula escreva um programa que:

- Receba do usuário dois números inteiros n1 e n2, n1 < n2.
- Use loops para calcular e exibir os elementos da sequencia de fibonacci começando de Fn1 e terminando em Fn2

#### Exemplo de entrada e saída
```
Qual o valor de n1? 12
Qual o valor de n2? 16
Fibonacci(12) = 144
Fibonacci(13) = 233
Fibonacci(14) = 377
Fibonacci(15) = 610
Fibonacci(16) = 987
```
            
## Jogo da Adivinhação v2.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá informar ao usuário, para cada tentativa errada, se o número pensado é menor ou maior que o informado pelo usuário. O programa deverá ficar em loop até que o usuário acerte o número escolhido pelo computador, mostrando no final quantos palpites foram necessários para vencer.

Para escolher um número aleatório entre 0 e 10, use a função random.randint(0, 10) depois de importar a biblioteca random.

#### Exemplo de entrada e saída:

```
Vou pensar em um número entre 0 e 10. Tente adivinhar...
Em que número eu pensei? 8
Menos... Tente novamente.
Em que número eu pensei? 2
Menos... Tente novamente.
Em que número eu pensei? 1
Menos... Tente novamente.
Em que número eu pensei? 0
Acertou com 4 tentativas. Parabéns!
```