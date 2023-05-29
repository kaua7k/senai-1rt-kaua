nome = input("Informe o nome do candidato: ")


nota = float(input("Informe a nota do candidato: "))


if nota <= 50:
    print(f"Obrigado por participar da competicao {nome}, sua nota final foi de {nota}. ")


if nota >= 50:
    print(f"Estamos muitos honrados por recebe-lo como competidor {nome}, sua note final foi de {nota}. ")
else: nota < 60


if nota >= 60:
    print(f"Parabens, voce recebeu a medalha de bronze {nome}, sua nota final foi de {nota}. ")
else: nota < 70


if nota >= 70:
    print(f"Parabens, voce recebeu a medalha de prata {nome}, sua nota final foi de {nota}. ")
else: nota < 90


if nota >= 90:
    print(f"Parabens, voce recebeu a medalha de Ouro {nome}, sua nota final foi de {nota}. ")
