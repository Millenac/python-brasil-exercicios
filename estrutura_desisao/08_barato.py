preco1 = float(input("Digite o preço: "))
preco2 = float(input("Digite o preço: "))
preco3 = float(input("Digite o preço: "))

if preco1 < preco2 and preco1 < preco3:
    print(preco1)
elif preco2 < preco1 and preco2 < preco3:
    print(preco2)
else:
    print(preco3)