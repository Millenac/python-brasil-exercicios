area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

area_folga = area * 1.1

cobertura = 6  # metros quadrados por litro
litros_lata = 18
preco_lata = 80.00
litros_galao = 3.6
preco_galao = 25.00

litros_necessarios = area_folga / cobertura

# Apenas latas de 18 litros
latas = int(litros_necessarios / litros_lata)
if litros_necessarios % litros_lata > 0:
    latas += 1
preco_latas = latas * preco_lata

# Apenas galões de 3,6 litros
galoes = int(litros_necessarios / litros_galao)
if litros_necessarios % litros_galao > 0:
    galoes += 1
preco_galoes = galoes * preco_galao

# Mistura de latas e galões
latas_mista = int(litros_necessarios // litros_lata)
litros_restantes = litros_necessarios - (latas_mista * litros_lata)
galoes_mista = int(litros_restantes / litros_galao)
if litros_restantes % litros_galao > 0:
    galoes_mista += 1
preco_misto = (latas_mista * preco_lata) + (galoes_mista * preco_galao)

print(f"\nApenas latas de 18 litros: {latas} latas, R$ {preco_latas:.2f}")
print(f"Apenas galões de 3,6 litros: {galoes} galões, R$ {preco_galoes:.2f}")
print(f"Mistura: {latas_mista} latas e {galoes_mista} galões, R$ {preco_misto:.2f}")
