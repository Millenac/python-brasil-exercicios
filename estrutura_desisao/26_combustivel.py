litros = float(input("Digite o número de litros comprados: "))
tipo = input("Digite o tipo de combustível: A-álcool ou G-gasolina.").upper()

gasolina_litro = 2.50
alcool_litro = 1.90

if tipo == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_sem_desconto = litros * alcool_litro
    valor_desconto = preco_sem_desconto * desconto
    valor_total = preco_sem_desconto - valor_desconto

elif tipo == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_sem_desconto = litros * gasolina_litro
    valor_desconto = preco_sem_desconto * desconto
    valor_total = preco_sem_desconto - valor_desconto

print(f"Valor a ser pago: R$ {valor_total:.2f}")