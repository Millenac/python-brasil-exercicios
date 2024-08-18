preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))


if kg_morango <= 5:
    valor_morango = kg_morango * preco_morango_ate_5kg
else:
    valor_morango = kg_morango * preco_morango_acima_5kg


if kg_maca <= 5:
    valor_maca = kg_maca * preco_maca_ate_5kg
else:
    valor_maca = kg_maca * preco_maca_acima_5kg

valor_total = valor_morango + valor_maca


if kg_morango + kg_maca > 8 or valor_total > 25.00:
    valor_total *= 0.90

print(f"Valor a ser pago: R$ {valor_total:.2f}")