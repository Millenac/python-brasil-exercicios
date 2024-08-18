valor_hora = float(input("Digite o valor da sua hora: "))
qnt_hora = float(input("Digite a quantidade de horas que você trabalha por mês: "))

salario_bruto = valor_hora * qnt_hora

if salario_bruto <= 900:
    desconto_ir = 0
    percentual_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    percentual_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    percentual_ir = 10
else:
    desconto_ir = salario_bruto * 0.20
    percentual_ir = 20

desconto_inss = salario_bruto * 0.03

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss

salario_liquido = salario_bruto - total_descontos

print("\nFolha de Pagamento:")
print(f"Salário Bruto: ({valor_hora:.2f}*{qnt_hora:.2f})    : R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%)                     : R$ {desconto_ir:.2f}")
print(f"(-) INSS ( 3%)                  : R$ {desconto_inss:.2f}")
print(f"FGTS (11%)                      : R$ {fgts:.2f}")
print(f"Total de descontos              : R$ {total_descontos:.2f}")
print(f"Salário Líquido                 : R$ {salario_liquido:.2f}")
