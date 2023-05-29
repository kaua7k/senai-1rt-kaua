num1 = float( input("Insira o primeiro Numeral: "))
num2 = float( input("Insira o segundo Numeral: "))
num3 = float( input("Insira o terceiro Numeral: "))

total = (num1 + num2 + num3 )
media = (total /3)

valor = round(media, 2)



if media >= 6:
   print(f"Voce foi aprovado! sua media final foi {valor}!")

else:
    if media >=5:
        print("recuperacao")
    else:
      print(f"Voce foi reprovado! Sua media final foi {valor}!")   

