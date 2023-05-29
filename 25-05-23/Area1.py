def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"A área do terreno é {area_terreno} m².")

largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))

area(largura, comprimento)
