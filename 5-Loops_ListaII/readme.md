## Primos em um intervalo
Escreva um programa que peça ao usuário dois números inteiros n1 e n2 (n2 > n1) e imprima quantos números primos existem no nintervalo [n1, n2]. Lembre que um número é primo se ele é divisivel apenas por 1 e por ele mesmo.
```
n1=2, n2=10
Existem 4 numeros primos entre 2 e 10
```
Dica: use dois loops, o primeiro conta os números e um loop interno testa se o número atual é primo ou não.

## Gerador Interativo de Jogos da Loteria
Vimos como usar fluxogramas para implementar problema com condicionais e loops com a linguagem de blocos, de forma similar podemos fazer isso com a linguagem textual. Dessa forma implemente o fluxograma abaixo:

    fluxograma

Dica: para gerar numeros aleatórios em python vc pode usar o snippet abaixo:
```
import random
n1 = random.randint(1,60)
```

Dica 2: em python é possível ler várias entradas de uma vez usando o mesmo comando raw_input. Para isso, vc pode usar split, que quebra a entrada em vários elementos, desde que sejam separados por espaço.

```
n1, n2, n3 = raw_input("digite os valores de n1 n2 e n3").split()
```

No exemplo acima se o usuário digitar 1 2 3 as variáveis n1, n2 e n3 terão os textos 1, 2, 3. Você ainda tem que convertê-los para numero se for usar como número!

## Desenho em Escala
Vimos na questão #Ponto no Semi-Circulo, que é útil desenhar em escala. Muitas vezes a escala é variável então é interessante sabermos como escalar alguns elementos básicos de desenho.

Escreva um programa que desenha um triângulo equilátero em 4 escalas, de 1 até 4x um do lado do outro. O programa deve pedir ao usuário o lado do triângulo e desenhar todos os triângulos de forma que não haja sobreposição, por exemplo, no formato abaixo:

    triangulos