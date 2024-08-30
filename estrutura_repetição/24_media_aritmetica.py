N = int(input("Digite o número de notas: "))

soma_notas = 0

for i in range(N):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota

media = soma_notas / N

print(f"A média aritmética das {N} notas é: {media:.2f}")
