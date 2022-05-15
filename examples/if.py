def main():
    idade = int(input("Quantos anos voce tem? "))
    if idade >= 60:
        print("Idoso")
    elif idade >= 18:
        print("Adulto")
    else:
        print("Menor de idade")
main()
