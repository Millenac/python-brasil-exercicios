def verificar_numero(numero):

    if numero % 1 == 0:
        return f"O número {numero} é inteiro"
    else:
        return f"O numero {numero} é decimal"

num = float(input("Digite um número: "))
print(verificar_numero(num))