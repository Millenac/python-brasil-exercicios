def somaImposto(taxaImposto, custo):
    return custo * (1 + taxaImposto / 100)

taxa = float(input("Digite a taxa de imposto (em %): "))
custo = float(input("Digite o custo do item: "))
custo_com_imposto = somaImposto(taxa, custo)
print(f"O custo do item com imposto é: R$ {custo_com_imposto:.2f}")