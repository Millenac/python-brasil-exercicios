import math

a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é de segundo grau. Programa encerrado!")
    exit()
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

delta = (-b**2) - (4*a*c)

raiz_quadrada = math.sqrt(delta)
x1 = (-b + raiz_quadrada) / (2*a)
x2 = (-b - raiz_quadrada) / (2*a)

if delta < 0:
    print("A equação não possui raízes reais. Programa encerrado!")
    exit()
elif delta == 0:
    print(f"A equação possui raízes iguais sendo elas {x1:.0f}.")
else:
    print(f"As raízes são {x1:.0f} e {x2:.0f}.")