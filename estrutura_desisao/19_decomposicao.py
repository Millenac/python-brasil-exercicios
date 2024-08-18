def analisar_numero(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        partes.append(f"{centenas} centena" if centenas == 1 else f"{centenas} centenas")
    if dezenas > 0:
        partes.append(f"{dezenas} dezena" if dezenas == 1 else f"{dezenas} dezenas")
    if unidades > 0:
        partes.append(f"{unidades} unidade" if unidades == 1 else f"{unidades} unidades")

    print(f"{numero} = {', '.join(partes[:-1])} e {partes[-1]}" if len(partes) > 1 else f"{numero} = {partes[0]}")

numero = int(input("Digite um número inteiro menor que 1000: "))
analisar_numero(numero)