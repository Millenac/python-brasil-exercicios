import math

area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

cobertura_por_litro = 3
litros_por_lata = 18
lata = 80.00

litros_necessarios = area/cobertura_por_litro
latas_necessarias = math.ceil(litros_necessarios/litros_por_lata)
custo_total = latas_necessarias * lata

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R$ {custo_total:.2f}")