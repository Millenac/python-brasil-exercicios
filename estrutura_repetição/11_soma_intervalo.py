num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

lista = []
for i in range(num1, num2):
    if i > num1: #Esse if foi feito porque o start é inclusivo e a questão não queria ele incluso
        lista.append(i)

print("A soma do valores dentro do intervalo é de:", sum(lista))