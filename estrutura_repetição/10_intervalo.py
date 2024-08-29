num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

for i in range(num1, num2):
    if i > num1: #Esse if foi feito porque o start é inclusivo e a questão não queria ele incluso
        print(i)