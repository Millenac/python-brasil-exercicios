numero = int(input("Digite um número: "))

if numero < 0:
    print("Não é possivel verificar números negativos. ")
elif numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")