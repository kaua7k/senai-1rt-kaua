num1 = float(input("Informe o primeiro numero: "))

num2 = float(input("Informe o segundo numero: "))

operacao = input("Escolha a operacao: ")

if operacao == "+":
    print( num1 + num2)

else:
    if operacao == "-":
        print( num1 - num2)
    else:

        if operacao == "x":
            print( num1 * num2 )

        else: 
            if operacao == "/":
                print( num1 / num2 )
