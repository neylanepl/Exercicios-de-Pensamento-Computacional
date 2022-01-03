## Número por extenso
A escrita dos números por extenso é algo que aprendemos no ensino fundamental. Por exemplo as palavras cem, duzentos, duzentos e treze, são todos exemplos de escritas por extenso de números conhecidos. Devido à variedade de possibilidades programas que calculam o texto que representa um número por extenso são muito grandes, por isso usamos funções para facilitar o entendimento.

Escreva um programa que receba do usuário um número entre 0 e 999 e escreva na saída o número por extenso. O programa deve usar a função principal abaixo, obrigatoriamente, para imprimir o número por extenso:

```
def principal():
    num = int(input('Forneça um número entre 0 e 999'))
    if num < 0 or num > 999:
        print('Não sei o valor por extenso')
    else:
        print('Número por extenso é ' + extenso(num))
```

Veja que a função extenso precisa retornar um texto que deve ser a representação do número por extenso. Divida seu programa em funções para tratar a dezena, centena e unidade de forma separada.

## plot mustache
Nos exercícios com blocos, vimos a implementação da função mustache. Que é definida de acordo com a equação abaixo:

    mustache(x)= 1/√2 ∗ (cos(πx)−sin(πx/2)+1)  se −1.5≤ x ≤0
                 1/√2 ∗ (cos(πx)+sin(πx/2)+1)  se 0< x ≤ 1.5 
                 0 para outros casos 

No exercício fizemos apenas a implementação da função, não nos preocupamos em fazer um plot da mesma. Usando uma biblioteca da linguagem python é possível fazer plot de funções usando listas de forma simples por exemplo o código abaixo, plota a função f(x) = sin(x).

```
import matplotlib.pyplot as pyplot
import math

def principal():
  valores_de_x = [] #lista de valores de x
  valores_de_y = [] #lista de valores de y
  x = 0
  for i in range(100):
    x = x + 0.1
    valores_de_x.append(x) #adiciona valores de x na lista
  for x in valores_de_x:
    y = f(x)
    valores_de_y.append(y) #adiciona valores calculados de y na lista
  pyplot.plot(valores_de_x,valores_de_y) #plota valores
  pyplot.xlabel('X')
  pyplot.ylabel('Y')
  pyplot.show() #mostra o gráfico

def f(x):
  return math.sin(x)


principal()

``` 

Usando como base o código abaixo, escreva um programa que plote a função mustache(x), com x entre -2 e 2, com variação de 0.05. Para mais informações sobre plots no trinket, veja a documentação na seção sobre a matplotlib.


## Transformações 2D - Translação e Escala
Quando desenhamos em um espaço 2D é comum queremos transformar figuras ao invés de ficar pensando sempre em suas coordenadas finais. Por exemplo, podemos usar um quadrado com lado igual 1, em qualquer coordenada inicial (x0,y0) e transformá-lo de diversas formas para movê-lo ou deformá-lo.

Existem muitas transformações possíveis, mas todas são baseadas em funções matemáticas que são aplicadas em todos os vértices da figura que queremos transformar para gerar um novo conjunto de pontos. Abaixo você conhece duas transformações. Seja F uma figura em 2D com seus pontos denotados por P1, P2, ... PN:

- Translação: a translação tra(F,xt,yt) é dada pela seguinte equação:

    translada(F,xt,yt)={ P′nx=Pnx+xt ∀Pn∈F
                         P′ny=Pny+yt ∀Pn∈F

- Escala: a escala de uma figura F, denodata pela função scale(F, α ) é dada pela equação abaixo:

    escala(F,α)={ P′nx=Pnx∗α ∀Pn∈F
                  P′ny=Pny∗α ∀Pn∈F

Assim, escreva um programa que aplique as transformações em um triângulo, T. O programa deve funcionar da seguinte maneira:

1. Inicialmente o programa deve pedir ao usuário os parâmetros do triângulo, através dos 3 pares x, y que formam cada um dos vértices. Para simplificar, considere que os pontos sempre irão definir um triângulo(não precisa testar se os pontos são colineares!).

2. O programa deve apresentar ao usuário uma lista com duas opções: 1-Translação, 2-Escala. Dependendo da opção escolhida o programa deve pedir o valor de α, no caso de escala ou pedir os valores de xt e yt no caso de translação.

3. Depois de recebidos os parâmetros o programa deve chamar funções que implementem a escala e/ou translação no triângulo T. O programa também deve desenhar dois triângulos: o original, sem transformação alguma e o final após as transformações. Use cores diferentes para diferenciar as duas figuras.

Dica: Escreva uma função para desenhar um triângulo genérico, dados os seus 3 pontos, e depois escreva as funções para desenhar o mesmo triangulo após a translação ou escala.

