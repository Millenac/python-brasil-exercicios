vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    valor = int(input(f"\nDigite um valor na {i+1} posição do primeiro vetor: "))
    vetor_1.append(valor)

for i in range(10):
    valor = int(input(f"\nDigite um valor na {i+1} posição do segundo vetor: "))
    vetor_2.append(valor)

for i in range(10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print("\n")
print(vetor_3)