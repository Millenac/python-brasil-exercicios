def reverso(numero):
    return int(str(abs(numero))[::-1]) * (-1 if numero < 0 else 1)

numero = int(input("Digite um número inteiro: "))
print(f"O reverso de {numero} é {reverso(numero)}.")