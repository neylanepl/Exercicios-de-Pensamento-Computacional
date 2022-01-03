## Jogo da Adivinhação Invertido

Vamos inverter os papéis daquele Jogo da Advinhação em que tínhamos que descobrir um número em que o computador escolhia aleatoriamente. Ou seja, vamos escolher um número e o computador terá que advinhar. Assim, escreva um programa que pede ao usuário para "pensar" em um número inteiro entre 0 e 10 e informar este número. O computador deverá sortear um número entre 0 e 10 até que ele acerte qual foi o número pensado pelo usuário. O programa deverá "ajudar o computador" da mesma forma que a versão "humana" do jogo, isto é, para cada tentativa errada, ajustar a nova escolha aléatória observando se o número pensado é menor ou maior que o informado pelo usuário. O programa deverá ficar em loop até que o computador acerte o número escolhido pelo usuário, mostrando no final quantos palpites foram necessários para acertar.

Para escolher um número aleatório entre 0 e 10, use a função random.randint(0, 10) depois de importar a biblioteca random.

#### Exemplo de entrada e saída:

```
Escolha um número entre 0 e 10, que o computador tentará adivinhar: 5
Palpite do computador: 8
Menor... Tente novamente.
Palpite do computador: 2
Maior... Tente novamente.
Palpite do computador: 7
Menor... Tente novamente.
Palpite do computador: 5
Acertou com 4 tentativas. Parabéns!
```

## Escada descendente e ascendente

Em uma questão passada resolvemos o problema #Escada que envolvia desenhar uma escada com loops e o módulo turtle. Desta vez vamos usar Python e desenhar uma escada descendente e uma outra ascendente. Assim, o programa deve solicitar ao usuário quantos degraus da escada descendente ele quer e quantos da ascendente para depois desenhar as escadas, como nas figuras abaixo:

    imagem
    

## Quadrados de Fibonacci
A sequencia de fibonacci é uma das mais famosas sequencias matemáticas, pois possui inumeras aplicações práticas. Os elementos desta sequencia são calculados através da equação abaixo:


    Fn= 0,se n=0
        1,se n=1
        Fn−1+Fn−2,caso contrario.


Na equação o elemento n da sequencia, Fn, é calculado com base nos dois elementos anteriores. Veja que n é obrigatóriamente um inteiro maior ou igual a 0. Usando esta fórmula escreva um programa que:

- Receba do usuário dois números inteiros n1 e n2, n1 < n2.
- Use loops para calcular os elementos dasequencia de fibonacci começando de Fn1 e terminando em Fn2
- Desenhe um quadrado com a largura e altura iguais a cada elemento do intervalo Fn1,Fn1+1 ..., Fn2−1, Fn2