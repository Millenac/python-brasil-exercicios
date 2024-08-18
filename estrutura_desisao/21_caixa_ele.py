valor = float(input("Digite a quantia que deseja sacar: "))

if valor < 10:
    print("O valor mínimo a se sacar é de 10 reais.")
elif valor > 600:
    print("O valor máximo a se sacar é de 600 reais.")
else:
    valor = int(valor)
    notas_100 = valor // 100
    valor %= 100

    notas_50 = valor // 50
    valor %= 50

    notas_10 = valor // 10
    valor %= 10

    notas_5 = valor // 5
    valor %= 5

    notas_1 = valor

    partes = []

    if notas_100 > 0:
        partes.append(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100")
    if notas_50 > 0:
        partes.append(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50")
    if notas_10 > 0:
        partes.append(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10")
    if notas_5 > 0:
        partes.append(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5")
    if notas_1 > 0:
        partes.append(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1")

    print(f"Para sacar a quantia de {sum([notas_100 * 100, notas_50 * 50, notas_10 * 10, notas_5 * 5, notas_1])} reais, o programa fornece {', '.join(partes[:-1])} e {partes[-1]}.")