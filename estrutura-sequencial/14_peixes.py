peso = float(input("Digite o peso dos peixes: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso*4.0
    print(f"Seu excesso foi de {excesso} e sua multa é de R$", multa)
else:
    print("Você não excedeu o peso, logo não precisa pagar multa")
