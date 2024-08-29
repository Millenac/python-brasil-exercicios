n = int(input("Digite um número: "))

lista = []
for i in range(n):
    numero = int(input(f"Digite o número {i+1}"))
    lista.append(numero)

print(f"O menor número digitado é: {min(lista)}")
print(f"O maior número digitado é: {max(lista)}")
print(f"A soma dos números digitado é: {sum(lista)}")