n = int(input("Digite a quantidade de número: "))

lista = []
for i in range(n):
    while True:
        try:
            numero = int(input(f"Digite um número entre 0 e 1000: "))
            if  0 <= numero <= 1000:
                lista.append(numero)
                break
            else:
                print("Digite um número valido!")
        except ValueError:
            print("Digite uma entrada valida")


print(f"O menor número digitado é: {min(lista)}")
print(f"O maior número digitado é: {max(lista)}")
print(f"A soma dos números digitado é: {sum(lista)}")