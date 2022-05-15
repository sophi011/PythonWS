def calculaArea(base, altura):  
    area = base * altura/2
    return area

def maiorArea(area1, area2):
    if area1 > area2:
        return area1
    elif area2 > area1:
        return area2
    else:
        return "Areas iguais"
        
def main():
    base1 = int(input("Base do triangulo 1: "))
    altura1 = int(input("Altura do triangulo 1: "))
    area1 = calculaArea(base1, altura1) #chamamos a primeira funcao para calcular a area do triangulo
    print("Area 1: ", area1)
    base2 = int(input("Base do triangulo 2: "))
    altura2 = int(input("Altura do triangulo 2: "))
    area2 = calculaArea(base2, altura2)
    print("Area 2: ", area2)
    print("A maior area e: ")
    print(maiorArea(area1, area2)) # imprimimos o retorno da funcao
main()
