num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
num3 = int(input("Insira o terceiro numero: "))

print(num1, num2, num3)

numeros = num1, num2, num3 

maior = max(numeros)
menor = min(numeros)

print (f"O maior numero e {maior}: ")
print (f"O menor numero e {menor}: ")