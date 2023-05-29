string_numeros = input("Digite três números separados por espaços: ")
numeros = [int(num) for num in string_numeros.split()]

if len(numeros) != 3:
    print("Por favor, digite exatamente três números.")
else:
    maior = max(numeros)
    menor = min(numeros)
    print("O maior número é:", maior)
    print("O menor número é:", menor)
