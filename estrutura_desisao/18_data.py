data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

ano_bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

if mes < 1 or mes > 12:
    print("Data inválida: Mês inválido.")
elif dia < 1 or dia > 31:
    print("Data inválida: Dia inválido.")
elif mes in [4, 6, 9, 11] and dia > 30:
    print("Data inválida: O mês informado tem apenas 30 dias.")
elif mes == 2:
    if ano_bissexto and dia > 29:
        print("Data inválida: Fevereiro tem apenas 29 dias em ano bissexto.")
    elif not ano_bissexto and dia > 28:
        print("Data inválida: Fevereiro tem apenas 28 dias em ano não bissexto.")
else:
    print("Data válida!")