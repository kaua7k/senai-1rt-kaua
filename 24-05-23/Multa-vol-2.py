km = float(input("informe a velocidade do carro: "))

if km >= 80:
   multa = (km - 80)
   total = (multa * 7.00)


print(f"Voce foi multado por passar na velocidade de {km} p/ hora, o valor sera de {total}")