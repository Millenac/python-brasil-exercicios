numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 == numero2 and numero1 == numero3:
    print("Os números são iguais.")
else:
    if numero1 > numero2 and numero1 > numero3:
        print(f"O número {numero1} é o maior número digitado.")
    elif numero2 > numero1 and numero2 > numero3:
        print(f"O número {numero2} é o maior número digitado.")
    else:
        print(f"O número {numero3} é o maior número digitado.")
