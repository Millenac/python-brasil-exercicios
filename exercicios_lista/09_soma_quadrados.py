A = []

for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    A.append(numero)

soma_quadrados = 0
for numero in A:
    soma_quadrados += numero ** 2

print(f"A soma dos quadrados dos elementos do vetor é: {soma_quadrados}")
