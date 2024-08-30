idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
    idades.append(idade)
    alturas.append(altura)

for i in range(4, -1, -1):
    print(f"Pessoa {i + 1} - Idade: {idades[i]}, Altura: {alturas[i]:.2f} m")