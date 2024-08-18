salario = float(input("Digite seu salario: "))

if salario < 280:
    aumento = (20/100)*salario
elif salario >= 280 and salario < 700:
    aumento = (15/100)*salario
elif salario > 700 and salario < 1500:
    aumento = (10/100)*salario
else:
    aumento = (5/100)*salario
print("Salario antigo: ", salario)
print("Valor aumentado: ", aumento)
print("Salario com aumento: ", aumento+salario)