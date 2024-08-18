salario_atual = float(input("Digite o valor do seu salario: "))

if salario_atual <= 280:
    salario_novo = salario_atual + (salario_atual*0.2)
elif salario_atual > 280 and salario_atual <= 700:
    salario_novo = salario_atual + (salario_atual*0.15)
elif salario_atual > 700 and salario_atual <= 1500:
    salario_novo = salario_atual + (salario_atual*0.1)
else:
    salario_novo = salario_atual + (salario_atual*0.05)

aumento = salario_novo - salario_atual
porcetagem = aumento/salario_atual *100

print(f"Seu salário antes do reajuste R$ {salario_atual:.2f} reais")
print(f"A porcetagem de aumento foi em {porcetagem:.0f} %")
print(f"Seu salário aumentou em R$ {aumento:.2f}")
print(f"Seu novo salário R$ {salario_novo:.2f} reais")