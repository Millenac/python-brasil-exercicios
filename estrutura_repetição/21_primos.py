entrada = int(input("\nDigite um número: "))
primos = []

for valor in range(1, 1001):
    if entrada % valor == 0:
        primos.append(valor)

#print("\nDivisores de", entrada, "são:", primos)

if len(primos) == 2:
    print(f"\n{entrada} é um número primo.")
else:
    print(f"\n{entrada} não é um número primo.")
