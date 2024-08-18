preco_file_duplo_ate_5kg = 4.90
preco_file_duplo_acima_5kg = 5.80

preco_alcatra_ate_5kg = 5.90
preco_alcatra_acima_5kg = 6.80

preco_picanha_ate_5kg = 6.90
preco_picanha_acima_5kg = 7.80


tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ").lower()
kg_carne = float(input("Digite a quantidade de carne (em Kg): "))
pagamento = input("Pagamento no cartão Tabajara? Digite S-sim ou N-não: ").lower()


if tipo_carne == "file duplo":
    preco_ate_5kg = preco_file_duplo_ate_5kg
    preco_acima_5kg = preco_file_duplo_acima_5kg
elif tipo_carne == "alcatra":
    preco_ate_5kg = preco_alcatra_ate_5kg
    preco_acima_5kg = preco_alcatra_acima_5kg
elif tipo_carne == "picanha":
    preco_ate_5kg = preco_picanha_ate_5kg
    preco_acima_5kg = preco_picanha_acima_5kg
else:
    print("Tipo de carne inválido.")
    exit()


if kg_carne <= 5:
    valor_total = kg_carne * preco_ate_5kg
else:
    valor_total = kg_carne * preco_acima_5kg


if pagamento == "s":
    desconto = valor_total * 0.05
    valor_total -= desconto
    tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    tipo_pagamento = "Dinheiro"


print("\n--Cupom Fiscal--\n")
print(f"Tipo de Carne: {tipo_carne.capitalize()}")
print(f"Quantidade: {kg_carne:.2f} Kg")
print(f"Preço Total: R$ {valor_total + desconto:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valor_total:.2f}")
