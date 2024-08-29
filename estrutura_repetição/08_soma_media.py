lista = []

for i in range(5):
    num = float(input(f"Digite o {i+1} número: "))
    lista.append(num)

print("A soma é:", sum(lista))
print("A média é:", sum(lista)/len(lista))