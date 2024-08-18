numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja: ")

if operacao == 'soma' or operacao == '+':
    resultado = numero1+numero2
elif operacao == 'subtração' or operacao == '-':
    resultado = numero1 - numero2
elif operacao == 'multiplicação' or operacao == '*':
    resultado = numero1*numero2
elif operacao == 'divisão' or operacao == '/':
    resultado = numero1/numero2
else:
    print("Digite uma operação valida.")

if resultado % 2 == 0:
    print(f"O valor {resultado:.2f} é par")
else:
    print(f"O número {resultado:.2f} é ímpar")
if resultado > 0:
    print(f"O número {resultado:.2f} é positivo.")
else:
    print(f"O número {resultado:.2f} é negativo.")
if resultado % 1 == 0:
    print(f"O número {resultado:.2f} é inteiro")
else:
    print(f"O numero {resultado:.2f} é decimal")