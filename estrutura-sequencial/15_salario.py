qnt = float(input("Quanto você ganha por hora: "))
horas = int(input("Digite quantas horas você trabalha por mês: "))

salario_bruto = qnt*horas
imposto = (11/100)*salario_bruto
inss = (8/100)*salario_bruto
sindicato = (5/100)*salario_bruto
descontos = imposto+inss+sindicato
salario_liquido = salario_bruto - descontos

print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%) : R$", imposto)
print("- INSS (8%) : R$", inss)
print("- Sindicato ( 5%) : R$", sindicato)
print("= Salário Liquido : R$", salario_liquido)