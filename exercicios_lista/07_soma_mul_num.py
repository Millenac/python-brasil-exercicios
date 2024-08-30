import math
lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)

soma = sum(lista)
mul = math.prod(lista)

print("A soma é:", soma)
print("A multiplicação é:", mul)
print("A lista de números digitadas", lista)