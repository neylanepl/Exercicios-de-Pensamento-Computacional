## Data com mês por extenso
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva um texto no formato D de mesPorExtenso de AAAA. Para cada data informada, valide a data e retorne "Data inválida!" caso a data não possa existir. Atenção para os anos bissextos em que há o dia 29 de fevereiro. Para que um determinado ano seja bissexto, ele precisa atender às seguintes condições:

- O ano é divisível por 4, mas não é divisível por 100; ou
- Caso o ano termine com 00 (dois zeros), ele é divisivel por 400.

Dica: para a entrada da data, use a função split('/') para separar o valor de dia, mês e ano do texto (string) informado pelo usuário. Exemplo:

```
dia, mes, ano = raw_input("Data no formato DD/MM/AAAA?").split('/')
```

#### Exemplo de entrada e saída:
```
Exemplo 1	
Data no formato DD/MM/AAAA? 29/02/2020
Retorno da função: 
29 de fevereiro de 2020
            
Exemplo 2

Data no formato DD/MM/AAAA? 31/11/2020
Retorno da função: 
Data inválida!
```

## Análise da função randint
Na questão do jogo da advinhação usamos a função randint que escolhe aleatoriamente um determinado número inteiro dentro de um intervalo informado como parâmetro. Vimos que é possível um número ser escolhido diversas vezes seguidas, como se a escolha estivesse "viciada". Para analisar se há vício ou não nesta função randint, devemos considerar uma quantidade relativamenet alta de escolhas dos números e contar quantas vezes cada número foi escolhido. Esta contagem por número escolhido (repetição) devem ser próximas umas das outras.

Assim, faça um programa que pede ao usuário um intervalo de valores e quantas escolhas aleatórias de números deste intervalo deseja fazer, dando como saída a quantidade em que cada número do intervalo foi escolhido. Exemplo:
```
Inteiro inicial do intervalo? 0
Inteiro final do intervalo? 1
Quantidade de escolhas? 100
Contagem de escolhas:
0 - 49
1 - 51
```

Dicas:

- Trabalhe com uma lista para guardar os números escolhidos para cada chamada da função `randint`, definindo-a com um valor inicial vazio `lista = []`, e depois vai adicionando os elementos nesta lista com `lista.append(elemento)`. Para checar o conteúdo de cada elemento da lista, basta informar o seu índice `lista[indice]`, onde `indice` inicia em 0 e vai até `len(lista) - 1`, onde a função `len()` retorna o tamanho da lista passada como argumento. Exemplo:
```
>>> lista = []
>>> lista.append(2)
>>> lista.append(1)
>>> lista.append(4)
>>> lista.append(0)
>>> print(len(lista))
4
>>> print(lista[3])
0
```

- Crie uma função que recebe como parâmetros a lista de números e o número a ser contado nesta lista, retornando a quantidade de vezes que este número aparece nesta lista.

## Desenho aleatório
Crie um programa que desenha uma quantidade n (informada pelo usuário) de círculos e quadrados escolhidos aleatoriamente. O desenho de cada objeto deve estar dentro da caixa de desenho cujo canto superior esquerdo é (-200, 200) e o canto inferior direito é (200, -200). O tamanho de cada objeto (raio do círculo ou lado do quadrado) deve variar entre 10 e 50. Os mesmos devem ser preenchidos com cores aleatórias. Utilize funções para o desenho de cada objeto. O programa deve ficar pedindo a quantidade n ao usuário e desenhando os objetos até que ele informe o valor 0 para encerrar o programa.