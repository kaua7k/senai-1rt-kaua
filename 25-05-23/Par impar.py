#while True:
    #numero = int(input("Informe um numero! "))

#div1 = (numero % 2) 

 
#if div1 < 0:
  ## print("Encerrado. ")
#break



#if div1 == 1:
    #print(f"O valor de {numero} sera impar")

#else:
   # div1 == 0
 #   print(f"O valor de {numero} sera par")
    
#while True:

while True:
    numero = int(input("Informe um número: "))

    if numero < 0:
        print("Encerrado.")
        break

    div1 = numero % 2

    if div1 == 1:
        print(f"O valor de {numero} é ímpar.")
    elif div1 == 0:
        print(f"O valor de {numero} é par.")


