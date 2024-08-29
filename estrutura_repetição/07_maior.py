lista = []

for i in range(5):
    num = float(input(f"Digite o {i+1} número: "))
    lista.append(num)

print("O maior número da lista é:", max(lista))