while True:
    try:
        numero = int(input("Digite um número inteiro positivo menor que 16 (ou -1 para sair): "))
        if numero == -1:
            print("Programa finalizado.")
            break
        if numero < 0 or numero >= 16:
            print("Número inválido. Digite um número inteiro positivo menor que 16.")
            continue
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        print(f"O fatorial de {numero} é {fatorial}.")

    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
