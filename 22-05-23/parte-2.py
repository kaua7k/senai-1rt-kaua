nome = input("Digite o nome do aluno: ")
dia = input("digite o dia em que voce nasceu: ")
mes = input("digite o mes em que voce nasceu: ")
ano = input("digite o ano em que voce nasceu: ")

mensagem = ("Ola {}, voce nasceu no dia {} de {} de {}").format(nome, dia, mes, ano)
print(mensagem)