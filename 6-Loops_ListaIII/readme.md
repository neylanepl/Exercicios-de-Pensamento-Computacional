## Dados de um Boxplot
O boxplot é uma forma interessante de visualizar um conjunto de dados, pois mostra em um único gráfico informações estatísticas relevantes para um conjunto de números. Assim, um boxplot exibe graficamente os seguintes dados para um determinado conjunto de números:

- limite superior (maior valor)
- limite inferior (menor valor)
- 1º quartil (valor que se encontra na posição 1/4 do conjunto, considerando o conjunto em ordem crescente)
- 3º quartil (valor que se encontra na posição 3/4 do conjunto, considerando o conjunto em ordem crescente)
- mediana (valor que se encontra na metade do conjunto, considerando o conjunto em ordem crescente)

A figura abaixo mostra um exemplo de boxplot. Veja que apenas os valores no eixo Y são importantes. Os do eixo X não tem utilidade alguma aqui.

    boxplot.png

Escreva um programa para ler uma sequência de N valores ordenados. Esta leitura dos valores deve ser feita em um laço, considerando as seguintes observações:

- Em qualquer iteração do laço de leitura dos N valores, se o valor lido for menor que o anterior, exiba a mensagem: "Erro! Conjunto tem de estar em ordem crescente" e pare o programa.
- O 1º quartil é conhecido quando o laço estiver na i-ésima iteração, onde i == round(N * 1/4).
- O 3º quartil é conhecido quando o laço estiver na i-ésima iteração, onde i == round(N * 3/4).
- A mediana é conhecida quando o laço chegar na metade do total de iterações. Há, porém, dois casos para a "metade". Se N for ímpar, haverá um único "elemento do meio" (ex: em [1, 3, 5], 3 é central), mas se N for par haverá dois "elementos do meio" (ex: em [1, 3, 4, 6], 3 e 4 são centrais). No primeiro caso, a mediana é encontrada quando i == (N+1)/2. No segundo caso, precisamos calcular a média aritimética dos dois valores centrais. Ou seja, quando i == (N+1)/2, a mediana será a média do valor lido e seu anterior.
- Com um conjunto é ordenado, seus valores mínimos e máximos são o primeiro e último elementos.

Com esses valores em mãos, seu programa deve exibir: o menor elemento, o 1º quartil, a mediana, o 3º quartil e o maior elemento.

## Quadrados de uma PG
Uma progressão geométrica (PG) é uma sequência numérica an definida recursivamente por:

    an=an−1.r,n>1
    
onde o primeiro termo a1 e r são conhecidos. O número r é chamado de razão da progressão geométrica. Por exemplo, {8,16,32,64,128,...} é uma progressão geométrica em que o primeiro termo a1=8 e a razão r=2.

Desenvolva um programa que leia o primeiro termo e a razão de uma PG e desenhe os 5 primeiros quadrados dessa progressão, um dentro do outro, conforme exemplo abaixo.

## Sequencia aleatória sem repetição
Uma ferramenta muito útil nas linguagens de programação são as listas (ou vetores em algumas linguagens). Uma lista é uma variável que guarda vários valores ao invés de um só.
```
lista = [] #lista vazia
lista2 = [1, 2, 3, 4] #lista com 4 elementos
```

Muitas operações são possíveis com listas, uma bem simples é adicionar elementos no fim da lista, com a função append e testar se um elemento existe na lista com a função in.

```
lista = []
lista.append("banana") #lista agora é ["banana"]
lista.append("larajna") #lista agora é ["banana", "laranja"]
if "banana" in lista : #in retorna True se um valor está na lista
    print("banana está na lista")
```
Listas podem conter números, textos e valores de outras variáveis
```
lista_letras = ["a", "b"]
lista_numeros = [1, 2, 3]
lista_mista = [1, "a", 2, "b"]
var = "elemento da lista"
lista_mista.append(var) #adiciona o valor de var à lista
```
Para acessar os elementos em uma lista, classicamente usamos um laço for, o comando for ele in lista_letras intera em todos os elementos de lista_letras. A cada interação do loop, o valor de ele é atualizado com o próximo elemento da lista.
```
lista_letras = ["a", "b", "c", "d", "e"]
for ele in lista_letras :
    print(ele) #imprime a, b, c...
```
Usando listas implemente um programa que gera uma sequencia de números aleatórios não repetidos do tamanho informado pelo usuário. O programa deve perguntar ao usuário a quantidade de números desejados e o intervalo numérico desejado. A entrada/saída será no formato abaixo:
```
Ex1
Quantos números? 50
Qual o intervalo? 20 40
Erro!
Não posso gerar 50 numeros não repetidos entre 20 e 40!
Ex2
Quantos números? 10
Qual o intervalo? -20 40
Seque sua sequencia:
Elemento 1 = 1
Elemento 2 = -12
Elemento 3 = -3
Elemento 4 = 4
Elemento 5 = 5
Elemento 6 = 23
Elemento 7 = 17
Elemento 8 = 20
Elemento 9 = 11
Elemento 10 = 12
```

Dica: Use a função in para testar se um número sorteado pela função randint já está na lista, se o numero não estiver use a função push para inserir o numero; caso o numero esteja, sorteie novamente!

Dica 2: Para imprimir use um loop for e intere em todos os elementos da lista para imprimir no formato especificado.