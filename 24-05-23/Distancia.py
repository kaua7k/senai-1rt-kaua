km = int(input("Qual a distancia percorrida em km`s? "))

if km > 200:
    aumento = (km * 0.45)

else: 
    aumento = (km *0.50)


print(f"O valor total sera de {aumento}! ")
