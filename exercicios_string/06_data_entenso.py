data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes_extenso = meses[int(mes) - 1]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
