def main():
    matriz = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

    matriz2 = []
    #podemos criar a matriz primeiro como uma lista
    linha1 = [0, 1, 0]
    linha2 = [1, 0, 1]
    linha3 = [0, 1, 0]
    #criamos separadamente as listas que correspondem a cada linha
    matriz2.append(linha1)
    matriz2.append(linha2)
    matriz2.append(linha3)
    print(matriz2)

    for linha in matriz: # mostramos de uma forma visual
        print(linha)
main()
