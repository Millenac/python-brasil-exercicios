def quantidadeDigitos(numero):
    return len(str(abs(numero)))

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} possui {quantidadeDigitos(numero)} dígitos.")