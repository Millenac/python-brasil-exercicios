numero = int(input("Digite um número até 99: "))
unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
teens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

if numero < 10:
    print(unidades[numero])
elif 10 <= numero < 20:
    print(teens[numero - 10])
else:
    dezena = dezenas[numero // 10]
    unidade = unidades[numero % 10]
    print(f"{dezena} e {unidade}".strip(" e "))
