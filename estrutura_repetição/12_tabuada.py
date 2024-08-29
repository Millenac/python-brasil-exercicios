def tabuada(x):
    for i in range(1, 11):
        print (x," x ", i, "= ",x*i)

numero = int(input("Digite um número :"))
print("Tabuada de", numero, ":\n")
tabuada(numero)
