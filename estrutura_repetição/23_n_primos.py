N = int(input("Digite um número inteiro N: "))

primos = []

divisoes = 0

for num in range(1, N + 1):
    # Contador de divisores do número atual
    contador_divisores = 0
    for i in range(1, num + 1):
        divisoes += 1  # Incrementa o contador de divisões
        if num % i == 0:
            contador_divisores += 1
    if contador_divisores == 2:
        primos.append(num)

print(f"\nNúmeros primos entre 1 e {N}: {primos}")

print(f"\nTotal de divisões realizadas: {divisoes}")
