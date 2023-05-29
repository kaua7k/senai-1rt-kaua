while True:
    numero = int(input("Informe um número: "))
    div1 = numero % 2

    if div1 < 0:
        print("Encerrado.")
        break

    if div1 == 1:
        print(f"O valor de {numero} é ímpar.")
    else:
        print(f"O valor de {numero} é par.")
