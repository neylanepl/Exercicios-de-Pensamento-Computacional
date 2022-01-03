## Detector de Palíndromo
Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Essa mesma característica pode ser aplicada a frases, retirando os espaços entre as palavras. Exemplo de frases palíndromos:

- apos a sopa
- a sacada da casa
- a torre da derrota
- o lobo ama o bolo
- anotaram a data da maratona

Construa a função inverso(texto) que receba um texto qualquer como argumento e retorne esse texto em ordem inversa. Em seguida, use esta função para checar se um texto é palíndromo ou não.

Dica: em Python, assim como em outras linguagens, todo texto (ou string) é uma lista ou um vetor de caracteres. O acesso a cada caractere do texto é feito através do índice deste vetor, o qual inicia em 0 (zero) e vai até len(vetor) - 1:

```
>>> palavra = "osso"
>>> len(palavra)
4
>>> palavra[0] == palavra[3]
True
``` 

Exemplo de entrada e saída:

```
Exemplo 1
Digite o texto: anotaram a data da maratona
O inverso de 'anotaramadatadamaratona' é 'anotaramadatadamaratona'
Temos um palíndromo!
            
Exemplo 2
Digite o texto: abracadabra
O inverso de 'abracadabra' é 'arbadacarba'
NÃO temos um palíndromo!
```

## Caixas envoltórias
No problema Caixa Envoltoria, vimos como é possível identificar a colisão entre uma caixa e um ponto, porém, na prática o problema sempre envolve duas caixas. Como o exemplo abaixo mostra:

    caixas jogos

As caixas se colidem quando algum ponto (qualquer um dos 4) de uma caixa se encontrar dentro da outra caixa.

Assim, escreva uma função testaColisao, que recebe 8 parâmetros: xc1,yc1,lc1,ac1 e xc2,yc2,lc2,ac2 representando o canto superior esquerdo de cada caixa com sua respectiva largura e altura. Quando a caixa 1 colide com a caixa 2 a função deve imprimir "Colide", caso contrário "Não colide".

Escreva também uma função para desenhar as caixas, a função deve receber apenas 4 parâmetros: xc,yc,lc,ac e deve desenhar uma caixa com uma cor aleatória (use `turtle.color(randint(0,255), randint(0,255), randint(0,255))`).

Seu programa deve pedir ao usuário as coordenadas de cada caixa, desenhá-las e testar a colisão usando as funções feitas.

## Plot da função randint
Na questão análise da função randint, analisamos o quão aleatória são as escolhas da função randint para um determinado intervalo de valores, e quanto maior era o número de escolhas, melhor era essa distribuição dos números escolhidos.

Vimos também na questão plot mustache, o uso da biblioteca matplotlib para plotar um gráfico para um conjunto de valores X e Y.

Nesta questão, iremos plotar o percentual de variação das escolhas da função randint em relação à quantidade média ideal de escolhas de cada elemento dado o total de escolhas. Por exemplo, se temos 10 elementos (0 a 9, por exemplo), e fazemos 100 escolhas, a média ideal de escolhas por elemento para ficar totalmente balanceado é 100 / 10 = 10. Se um determinado elemento foi escolhido 14 vezes, então o percentual de variação deste elemento é: (14 - 10) / 10 = 0.4 = 40%. Já se um outro elemento foi escolhido apenas 7 vezes, o seu percentual de variação é: (7 - 10) / 10 = -0.3 = -30%.

Adapte o Trinket abaixo, aproveitando o seu código de análise da função randint de forma que a saída também tenha o gráfico de variação das escolhas da média ideal.

#### Exemplo de entrada e saída:
```
Entrada e saída textual	

Inteiro inicial do intervalo? 0
Inteiro final do intervalo? 9
Quantidade de escolhas? 100000
Contagem de escolhas:
0 - 9985
1 - 10060
2 - 9987
3 - 10022
4 - 10067
5 - 9942
6 - 9899
7 - 9969
8 - 9958
9 - 10111
```

Divida todo o código em várias funções, cada função com uma determinada funcionalidade:

- Código principal que pede um intervalo válido de inteiros e a quantidade de escolhas e mostra os resultados;
- Gera a lista contendo as escolhas aleatórias de cada elemento do intervalo;
- Gera a lista de contagem de escolhas de cada elemento do intervalo;
- Exibe a contagem (textual) de escolhas por elemento;
- Exibe o gráfico do percentual de variação desta contagem da média ideal de escolhas.