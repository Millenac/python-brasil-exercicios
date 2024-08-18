lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É um triângulo.")
    if lado1 == lado2 and lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero: três lados iguais.")
    elif lado1 == lado2 or lado1 == lado2 or lado2 == lado3:
        print("Triângulo Isósceles: quaisquer dois lados iguais.")
    elif lado1 != lado2 and lado1 != lado2 and lado2 != lado3:
        print("Triângulo Escaleno: três lados diferentes.")
else:
    print("Não é um triângulo.")