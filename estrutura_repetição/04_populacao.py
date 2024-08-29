populacao_a = 8000
populacao_b = 20000

taxa_a = 3 / 100
taxa_b = 1.5 / 100

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f"Em {anos} anos a população do país A ultrapará ou igualará a população do país B")
