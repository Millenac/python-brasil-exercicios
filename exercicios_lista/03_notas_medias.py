lista = []

for i in range(4):
    nota = float(input(f"Digite a nota {i +1}:"))
    lista.append(nota)

media = sum(lista)/len(lista)
print(media)