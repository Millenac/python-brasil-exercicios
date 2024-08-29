while True:
    populacao_a = int(input("\nDigite a população do país A: "))
    populacao_b = int(input("Digite a população do país B: "))

    if populacao_a > populacao_b:
        print("\nA populão do país A precisa ser menor que a do país B")
        continue


    taxa_a = float(input("\nDigite a taxa de crescimento população do país A: "))
    taxa_b = float(input("Digite a taxa de crescimento da população do país A: "))

    anos = 0

    while populacao_a < populacao_b:
        populacao_a += populacao_a * (taxa_a/100)
        populacao_b += populacao_b * (taxa_b/100)
        anos += 1
    print(f"\nEm {anos} anos a população do país A ultrapará ou igualará a população do país B")