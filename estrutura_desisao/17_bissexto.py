ano = int(input("Digite um ano: "))

if ano % 4 == 00 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} tem 365 dias.")