# Python 


## 1. Breve introdução 

O Python é uma linguagem, assim como C++, muito usada na Skyrats e em aplicações de tecnologia no geral.

A principal diferença entre Python e C++ é que os códigos em Python são **interpretados** e não *compilados* como em C++. Uma linguagem *compilada* passa por um processo de compilação, como se fosse uma verificação, antes que o código seja executado. Por outro lado, uma linguagem **interpretada** é "verificada" *durante* a execução do código. 

Então, se seu código tem um erro, em C++ esse erro vai ser identificado na compilação, antes de você poder executá-lo. Em Python, o erro seria identificado na prórpia execução, se ele estiver na última linha do código, por exemplo, todas as outras linhas seriam executadas e o código pararia por ter percebido o erro só na última linha.

Uma outra diferença entre as duas linguagens é que, diferente de C++ em que as linhas terminam com ```;``` e usamos parênteses e chaves em um monte de coisa, no Python o que diferencia as linhas e as funções é a **identação**, que é basicamente o espaço entre o começo da linha e o código que escrevemos nela, ou quantos ```TABS``` a gente dá pra começar a linha de código ~~se preparem pra ter muitos erros de identação na aventura Pythoniana de vocês :P~~ .

## 2. Comentários

Em Python, para comentar uma linha usamos o "#" e para comentar um bloco usamos ```"""``` ou ```'''```(tês aspas seguidas, podem ser aspas simples ```'``` ou duplas ```"``` ). 
É bom lembrar que quando comentamos um bloco, temos que fechar o comentário!

### Exemplo

```python
# Primeiro exemplo em Python do workshop

'''
Este workshop está sendo feito pelos membros mais legais da Skyrats!!
'''

def main():
# Comentário dentro da main hihihi

main()
```
##### Obs: A ```main()``` é uma função usualmente usada como a função principal de um código python, ou seja, é ela que possui os comandos principais. Mas veremos mais sobre funções mais pra frente!

## 3. Variáveis

No Python, não é necessário declarar o tipo da variável que vamos usar, basta colocar direto o que ela vai receber (sim, bem coxa, eu sei). O Python é espertinho e entende logo ~~às vezes não~~ de que tipo de dado estamos falando (viu como Python é mais legal que C++?).

Uma outra diferença quando comparamos Python com C++ é que não existe uma variável especificamente do tipo ```double``` em Python, porque o tipo ```float``` já tem uma precisão que corresponde à precisão de uma variável ```double``` em C++. Um float em Python pode ter um valor até 1.8e+308. 

Quando uma operação for realizada com a variável (uma soma, por exemplo), o resultado será de acordo com o tipo inerente dela. Se somarmos duas variáveis do tipo float, o resultado será float, e a mesma coisa acontece com inteiros e com strings. 

E podemos, ainda, somar variáveis de tipos diferentes em alguns casos, como somar um float e um inteiro, por exemplo. Mas não podemos somar uma string com um inteiro (imagina somar "oi" + 3). 

**Declaração de variáveis em Python:**
```python
def main():
    numeroInteiro = -15 # int
    dinheiro = 15.00 # float
    certo = True # bool - atenção na letra maiúscula 
    errado = False
    letra = "a" # caracter (é a mesma coisa que uma string)
    nome = "Sophzita" # string
    mol = 6.02e+23 # float

main()
```

### Transformações de variáveis

Uma operação importante que podemos fazer em Python é transformar variáveis. Se temos um dado do tipo float, por exemplo, mas queremos usá-lo como um inteiro, podemos simplesmente transformá-lo em inteiro com a função ```int()```. 

Se temos uma variável inteira e queremos, por exemplo, usá-la como string, também basta só transformá-la em string com a função ```str()```. 

#### Exemplo 1 
```python
def main():
    dinheiro_float = 13.95
    dinheiro_int = int(dinheiro_float) # corresponde à parte inteira da variável dinheiro_float

    ovos_int = 5
    ovos_string = str(ovos_int) # assim podemos usar o numero 5 em forma de string
main()
    
```
Mas é importante lembrar que não é qualquer transformação que podemos fazer! Assim como um politreco não pode ser transformado em um ser humano decente :P, não podemos, por exemplo, transformar uma string em um inteiro, a menos que os caracteres da string sejam algarismos. 

#### Exemplo 2
```python
def main():
    nome_string = "Sophzita"
    nome_int = int(nome) # vai dar erro!

    numero_string = "5"
    numero_int = int(numero) # vai devolver o inteiro 5
```

## 4. Impressão e leitura

A leitura de dados em Python é feita com a função ```input()``` e isso pode ser feito direto na declaração da variável que recebe o que será lido. Além disso, precisamos indicar que tipo de dado será lido. 

A impressão é feita com a função ```print```.

Podemos, também, imprimir coisas na própria função input (e aí, já provei que Python é mais legal que C++?). Se não quisermos escrever nada, seria só deixar a função input vazia ( ```input()```).

### Exemplo 1
```python
def main():
    minhaIdade = int(input("Digite a idade :"))
    print ("Minha idade é: ")
    print (minhaIdade)
main()
```

## 5. Operadores (aritméticos, booleanos e comparativos)
Os principais operadores do Python são iguais aos de C++. 

*Link pros operadores na parte de C++*


## 6. Condicionais
As funções condicionais em Python são relativamente intuitivas. Pra usá-las, é sempre importante prestar atenção na **identação**. 

### ```If```, ```else``` e ```elif```

Sintaxe:
```py
def main():
    if condição1:
        bloco_de_comandos1
    elif condição2:
        bloco_de_comandos2
    else:
        bloco_de_comandos3
```

O ```if``` é, como diz o próprio nome, a função que estabelece uma condição (ou mais) para que o bloco de comandos que está dentro dele seja executado. 

O ```elif``` é a mesma coisa que dizer "else, if". E só pode ser usado se já tiver um ```if``` logo acima dele ~~se não ele nem faz sentido né dããr~~. 

Já o ```else``` é literalmente um "senão". Ele, assim como o ```elif``` só pode ser usado se tiver um ```if``` antes dele. 

Na sintaxe de cima, o ```bloco_de_comandos1``` só é executado se a condição 1 for verdadeira, e, nesse caso, nenhum dos outos blocos seria executado. 

O ```bloco_de_comandos2``` só é executado se a condição1 for falsa e a condição2 for verdadeira e, nesse caso também, só esse bloco seria executado. 

Finalmente, o ```bloco_de_comandos3``` só seria executado se as condições de cima forem falsas e, novamente, só esse bloco seria executado. 

#### Exemplo 
```py
def main():
    idade = int(input("Quantos anos você tem? "))
    if idade >= 60:
        print("Idoso")
    elif idade >= 18:
        print("Adulto")
    else:
        print("Menor de idade")
main()
```
Se quisermos usar mais de uma condição no ```if``` ou no ```elif``` podemos usar os operadores ```and``` e ```or``` entre as condições. 

## 8. Laços de repetição
### ```while```
A famosa função "enquanto" . Um jeito comum de usar é com um *contador* e enquanto ele for menor que o número de vezes que queremos executar os comandos, eles serão executados, só não podemos esquecer de incrementar o valor dele a cada repetição. 
A sintaxe é assim:
```py
# Sem contador
while condição:
    bloco_de-comandos

# Com contador
contador = 0
while contador < numero_de_repeticoes:
    bloco_de_comandos
    contador = contador + 1 # ver Obs1
```
*Obs1: também podemos incrementar o contador escrevendo ```contador += 1```

Exemplo
```py
def main():
    print("Contagem de 1 a 10")
    contador = 1
    while contador <= 10: 
        print(contador, end=" ") # ver *Obs2
        contador += 1 
main()
```
*Obs2: aqui usamos o ```end=" "``` para que a próxima impressão não mude de linha. Por padrão, o ```end```, que é o final da impressão, é a quebra de linha, então nesse caso colocamos o final como um espaço. 

Também é comum usarmos o ```while``` com condições booleanas, ou seja, de verdadeiro ou falso. Então se queremos, por exemplo, contar até chegar no 10, podemos criar uma variável que fica verdadeira quando cheagamos no 10, para que o laço pare de ser executado:
```py
def main():
    print("Contagem de 1 a 10")
    chegouNo10 = False
    contador = 1
    while not chegouNo10: #Lê-se "enquanto não chegou no 10"
    if contador == 10:
            chegouNo10 = True #mudamos a variável que é responsável por parar o laço quando a contagem chega em 10
        print(contador, end=" ") # ver *Obs2
        contador += 1 
main()
```

### ```for```
A função ```for``` é usada, muitas vezes, em conjunto com a função ```range```. A sintaxe é assim:
```py
for variavel in range (inicio, fim, incremento):
    bloco_de_comandos
```
A função ```range``` usa uma variável local como controle do laço e ela tem, como padrão, o início no 0 e o incremento como 1, então podemos simplesmente não indicar essas coisas quando usamos o ```for```. Além disso, o valor que colocamos no fim não é contado, então se colocarmos o range de 0 a 5, a variável do ```for``` terá só os valores 0, 1, 2, 3 e 4. 

Exemplo 1
```py
def main(): 
    print("Contagem de 0 a 10 com for")
    for i in range(11):
        print(i, end=" ")
main()
```

## Funções

As funções no Python são relativamente simples e são parecidas com as funções da matemática. Elas podem receber ou não parâmetros, também chamados de argumentos, e também podem possuir ou não um retorno, que é basicamente a "resposta" das instruções que as funções realizam. Diferente de C++, não precisamos indicar o tipo de retorno da função quando a definimos. 

Exemplos claros de funções são as que já usamos até agora! O ```print()```, por exemplo, é a função que imprime na tela o prórpio argumento que ela recebe entre os parênteses. E uma função importante que usamos também é a tal da ```main() ```. Ela é convencionalmente a função principal de um código, onde as instruções principais são seguidas. 

Ok, mas como se define uma função?

Vamos supor que queremos um código que retorna dentre dois triângulos qual deles tem a maior área, a partir da base e da altura de cada um. 
### Exemplo
```py
def calculaArea(base, altura):  
    area = base * altura
    return area

# aqui, definimos que a função recebe a altura e a base do triângulo, calcula o produto entre elas e retorna a área

def maiorArea(area1, area2):
    if area1 > area2:
        return area1
    elif area2 > area1:
        return area2
    else:
        return "Áreas iguais"
# agora definimos a função que recebe duas areas e retorna a maior delas, ou, caso sejam iguais, retorna a mensagem de que elas são iguais

def main():
    base1 = int(input("Base do triângulo 1: "))
    altura1 = int(input("Altura do triângulo 1: "))
    area1 = calculaArea(base1, altura1) #chamamos a primeira função para calcular a área do triângulo
    print("A área 1 é: ", area1)
    base2 = int(input("Base do triângulo 2: "))
    altura2 = int(input("Altura do triângulo 2: "))
    area2 = calculaArea(base2, altura2)
    print("A área 2 é: ", area2)
    print("A maior área é: ")
    print(maiorArea(area1, area2)) # imprimimos o retorno da função
main()
```

## Listas

As listas são, de forma simplificada, estruturas de dados que têm itens organizados de forma linear, sendo que cada elemento da lista tem um índice relacionado, pelo qual esse elemento pode ser acessado. 

A lista é indicada com seus elementos dentro de colchetes ```[]``` e separados por vírgulas. Vale ressltar que a contagem dos índices começa no zero então o primeiro elemento da lista fica na posição zero. Existem algumas funções importantes associadas a listas:
- ```append(elemento)``` - serve para adicionar um elemento ao final da lista
- ```insert(elemento, índice)``` - adiciona o elemento especificado no índice especificado
- ```lista.index(elemento)``` - serve para retornar o índice (ou posição) do elemento dentro da lista em sua primeira ocorrência
- ```lista[índice]``` - retorna o elemento da lista que está localizado no índice especificado
- ```len(lista)``` - indica o tamanho da lista, ou seja, quantos elementos ela contém
- ```lista.remove(elemento)``` - exclui o elemento da lista em sua primeira ocorrência
- ```max(lista)``` - retorna o maior elemento (em valor ou tamanho)
- ```min(lista)```- retorna o menor elemento (em valor ou tamanho)

### Exemplos
Se queremos criar uma lista que tenha como elementos as compras de supermercado, podemos fazer da seguinte forma:
```py
def main():
    lista_de_compras = ["tomate", "cebola", "abacate", "morango"] # criamos a lista diretamente com os elementos
    lista_de_compras2 = [] # criamos uma lista vazia
    lista_de_compras2.append("tomate") # colocamos o primeiro elemento na lista
    lista_de_compras2.append("cebola") # colocamos o segundo elemento ao final (e assim por diante)
main()
```
E se quisermos modificar os elementos da lista?
```py
def main():
    lista_de_compras = ["tomate", "cebola", "abacate", "morango"] 
    lista_de_compras[1] = "cebola roxa" # modificamos o elemento da posição 1 (cebola)
    lista_de_compras.remove("tomate") # excluímos o elemento da lista
main()
```
Um aspecto importante das listas no Python é que elas podem conter elementos de tipos diferentes, basta adicioná-los. No caso dos exemplos acima, as listas criadas tinham elementos do tipo ```string```. 

```py
def main():
    listaVariada = []
    listaVariada.append(2) # adicionamos um inteiro à lista
    listaVariada.append("chocolate") # adicionamos uma string
    listaVariada.append(7.58) # adicionamos um float
    print(listaVariada)
main()
```
**Percorrendo uma lista**
```py
def main():
    lista = ["Python", "C", "C++", "Java", "R"]
    for elemento in lista:
        print(elemento)
main()
```
## Matrizes

As matrizes são, a princípio, listas feitas de listas e seu conceito é bem próximo ao das matrizes usadas na matemática. Elas têm, por isso, uma estrutura parecida e usam funções similares às usadas com listas. O que diferencia é que relacionamos os elementos da matrizes com **dois** índices: o da coluna e o da linha, na forma ```elemento[linha][coluna]```. Lembrando que a contagem dos índices começa no 0 (zero), então o índice da primeira coluna e o da primeira linha são ambos 0!

### Exemplo
Se queremos definir uma matriz com 3 linhas e 3 colunas em que os elementos são alternados, valendo 1 ou 0, podemos fazer o seguinte:

```py
def main():
    matriz = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    #criamos uma lista com três elementos
    #cada elemento é uma lista com outros 3 elementos
    matriz2 = []
    #podemos criar a matriz primeiro como uma lista
    linha1 = [0, 1, 0]
    linha2 = [1, 0, 1]
    linha3 = [0, 1, 0]
    #criamos separadamente as listas que correspondem a cada linha
    matriz2.append(linha1)
    #adicionamos a primeira linha com o append
    matriz2.append(linha2)
    #adicionamos a segunda linha ao final
    matriz2.append(linha3)
    #adicionamos a terceira linha
    print(matriz2)
main()
```
Para visualizarmos a matriz na forma como a conhecemos, pode-se fazer o seguinte:
```py
def mostraMatriz():
    matriz = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    for linha in matriz:
        print(linha)
main()
```
Mas como, então podemos acessar um elemento específico da matriz? Bom, fazemos isso usando os índices de linha e coluna! :P

```py
def main():
    matriz = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    matriz[2][2] = 3
    print(matriz)
    # mudamos o elemento da última linha e última coluna (0) para 3
    matriz[0][1] = 5
    # mudamos o elemento da primeira linha e da segunda coluna (1) para 5
    print(matriz)
main()
```
## Esqueleto de um programa em Python

```python
    def main():  #definição da função main do código

        anoIngresso = int(input("Insira seu ano de ingresso: ")) # declaração da variável com a função input, que recebe um valor int
        if anoIngresso < 2021:  # condição para definir o que será impresso
            print("Você é veterane")
        else:
            print("Você é bixe")

        return 0  # retorno da função main()

main()  
```
Obs: é importante lembrar de chamar a ```main()```!! ~~não esqueçam que nem eu quando fiz esse exemplo~~
## Importando arquivos

Existem duas formas comuns de usar códigos em Python. Podemos rodar um código de forma direta, ou seja, escrevemos o código, salvamos no arquivo ```.py``` e rodamos as funções e implementações desse arquivo diretamente. 

A outra forma é usando o código de um arquivo em outro, ou seja, fazendo um ```import```. Quando importamos um arquivo para outro, podemos usar as mesmas funções do arquivo importado no arquivo novo, o que permite uma certa organização de código. 
Mas nesse caso, se chamarmos uma função no arquivo que estamos importando, essa função rodará quando importarmos para outro arquivo também, o que nem sempre é o que queremos. Para que isso não ocorra, antes de chamar as funções, usamos a seguinte estrutura:
```py
if __name__ == "__main__":
    # chamadas de funções
    main()
``` 
### Exemplo
Vamos supor que temos o código usado no exemplo de funções: 
```py
# areas.py
def calculaArea(base, altura):  
    area = base * altura
    return area

def maiorArea(area1, area2):
    if area1 > area2:
        return area1
    elif area2 > area1:
        return area2
    else:
        return "Áreas iguais"

def main():
    base1 = int(input("Base do triângulo 1: "))
    altura1 = int(input("Altura do triângulo 1: "))
    area1 = calculaArea(base1, altura1) #chamamos a primeira função para calcular a área do triângulo
    print("A área 1 é: ", area1)
    base2 = int(input("Base do triângulo 2: "))
    altura2 = int(input("Altura do triângulo 2: "))
    area2 = calculaArea(base2, altura2)
    print("A área 2 é: ", area2)
    print("A maior área é: ")
    print(maiorArea(area1, area2))
main()
```
Supondo, também que salvamos esse código no arquivo ```areas.py```. Nesse código, temos uma função que calcula a área de um triângulo, outra que retorna a maior área e temos a função main que recebe valores de lados e alturas para fazer o cálculo de áreas usando as outras funções. 

Se quisermos usar a função ```calculaArea``` em um aquivo ```triangulo.py```, podemos importar o arquivo que a contém para podermos usá-la:
```py
# triangulo.py

import areas

def main():
    lado1 = 5
    lado2 = 6
    lado3 = 5
    altura_lado2 = 4
    area = areas.calculaArea(lado2, altura_lado2)
    print("O triângulo de lados %d, %d, %d tem área %d" %(5, 6, 5, area))
main()
```
##### Obs: a notação %d serve para referenciar variáveis numéricas que serão especificadas depois

É importante ressaltar que o arquivo ```areas.py``` deve estar na mesma pasta que o arquivo ```triangulo.py```. 

Se importarmos o arquivo dessa forma, quando rodarmos o ```triangulo.py``` a função ```main()``` do ```areas.py``` também será executada, quando nem sempre isso é o que queremos. Para que isso não aconteça, colocamos a sintaxe no arquivo ```areas.py```:
```py
# areas.py modificado
def calculaArea(base, altura):  
    area = base * altura
    return area

def main():
    base1 = int(input("Base do triângulo 1: "))
    altura1 = int(input("Altura do triângulo 1: "))
    area1 = calculaArea(base1, altura1)
    print("A área 1 é: ", area1)
    base2 = int(input("Base do triângulo 2: "))
    altura2 = int(input("Altura do triângulo 2: "))
    area2 = calculaArea(base2, altura2)
    print("A área 2 é: ", area2)

if __name__ == "__main__":
    main()
```
Assim, a função ```main()``` desse código só será executada quando rodarmos ele diretamente, e não mais quando importarmos esse arquivo para outro. 

## Consderações finais

Ok, agora sabemos mais ou menos como funciona programação em Python. Mas aí você me diz: "Tá, entendi, agora quero brincar de Python, como faz pra praticar?"

Pra praticar, você pode instalar o Python IDLE [aqui](https://www.python.org/downloads/). Ou pode instalar programas como o [Visual Studio Code](https://code.visualstudio.com) que possuem ambientes de desenvolvimento em Python! Que comecem as aventuras Pythonianas!
