lista = []
for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)

par = [num for num in lista if num%2 ==0]
impar = [num for num in lista if num%2 != 0]

print("Seu vetor geral" , lista)
print("Seu vator de números pares" , par)
print("Seu vetor de número ímpares", impar)