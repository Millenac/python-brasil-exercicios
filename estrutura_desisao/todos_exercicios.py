#%%

# Questão 1 #
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if num1 > num2:
    print(num1)
else:
    print(num2)

#%%

#Questão 2 #
num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo")
else:
    print("O número é negativo")
#%%

# Questão 3 #

letra = input("Digite F ou M: ").upper()
if letra == 'F':
    print("Feminino")
elif letra == 'M':
    print("Masculino")
else:
    print("Sexo Invalido")
#%%

# Questão 4 #
letra = input("Digite uma letra: ").lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"A letra {letra} é uma vogal!")
else:
    print(f"A letra {letra} é uma consoante!")
#%%

# Questão 5 #
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if media >= 7:
    print("Aprovado")
elif media <= 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Digite valores validos")

#%%

# Questão 6 #

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 == numero2 and numero1 == numero3:
    print("Os números são iguais.")
else:
    if numero1 > numero2 and numero1 > numero3:
        print(f"O número {numero1} é o maior número digitado.")
    elif numero2 > numero1 and numero2 > numero3:
        print(f"O número {numero2} é o maior número digitado.")
    else:
        print(f"O número {numero3} é o maior número digitado.")

#%%

# Questão 7 #

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 == numero2 and numero1 == numero3:
    print("Os números são iguais.")
else:
    if numero1 > numero2 and numero1 > numero3:
        print(f"O número {numero1} é o maior número digitado.")
    elif (numero2 > numero3):
        print(f"O número {numero2} é o maior número digitado.")
    else:
       print(f"O número {numero3} é o maior número digitado.")
    if (numero1 < numero2) and (numero1 < numero3):
        print (f"O número {numero1} é o menor número digitado.")
    elif (numero2 < numero3):
        print (f"O número {numero2} é o menor número digitado.")
    else:
        print (f"O número {numero3} é o menor número digitado.")
#%%

# Questão 8 #

preco1 = float(input("Digite o preço: "))
preco2 = float(input("Digite o preço: "))
preco3 = float(input("Digite o preço: "))

if preco1 < preco2 and preco1 < preco3:
    print(preco1)
elif preco2 < preco1 and preco2 < preco3:
    print(preco2)
else:
    print(preco3)
#%%

# Questão 9 #

salario = float(input("Digite seu salario: "))

if salario < 280:
    aumento = (20/100)*salario
elif salario >= 280 and salario < 700:
    aumento = (15/100)*salario
elif salario > 700 and salario < 1500:
    aumento = (10/100)*salario
else:
    aumento = (5/100)*salario
print("Salario antigo: ", salario)
print("Valor aumentado: ", aumento)
print("Salario com aumento: ", aumento+salario)
# %%

#Questão 10

turno = input("Digite que turno você estuda. Digite M-Matutino ou V-Vespertino ou N-Noturno: ")

novo_turno = turno.upper()

if novo_turno == "M":
    print("Bom dia!")
elif novo_turno == "V":
    print("Boa tarde!")
elif novo_turno == "N":
    print("Boa noite!")
else:
    print("valor inválido!")

# %%

# Questão 11 #

salario_atual = float(input("Digite o valor do seu salario: "))

if salario_atual <= 280:
    salario_novo = salario_atual + (salario_atual*0.2)
elif salario_atual > 280 and salario_atual <= 700:
    salario_novo = salario_atual + (salario_atual*0.15)
elif salario_atual > 700 and salario_atual <= 1500:
    salario_novo = salario_atual + (salario_atual*0.1)
else:
    salario_novo = salario_atual + (salario_atual*0.05)

aumento = salario_novo - salario_atual
porcetagem = aumento/salario_atual *100

print(f"Seu salário antes do reajuste R$ {salario_atual:.2f} reais")
print(f"A porcetagem de aumento foi em {porcetagem:.0f} %")
print(f"Seu salário aumentou em R$ {aumento:.2f}")
print(f"Seu novo salário R$ {salario_novo:.2f} reais")

# %%

# Questão 12 #

valor_hora = float(input("Digite o valor da sua hora: "))
qnt_hora = float(input("Digite a quantidade de horas que você trabalha por mês: "))

salario_bruto = valor_hora * qnt_hora

if salario_bruto <= 900:
    desconto_ir = 0
    percentual_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    percentual_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    percentual_ir = 10
else:
    desconto_ir = salario_bruto * 0.20
    percentual_ir = 20

desconto_inss = salario_bruto * 0.03

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss

salario_liquido = salario_bruto - total_descontos

print("\nFolha de Pagamento:")
print(f"Salário Bruto: ({valor_hora:.2f}*{qnt_hora:.2f})    : R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%)                     : R$ {desconto_ir:.2f}")
print(f"(-) INSS ( 3%)                  : R$ {desconto_inss:.2f}")
print(f"FGTS (11%)                      : R$ {fgts:.2f}")
print(f"Total de descontos              : R$ {total_descontos:.2f}")
print(f"Salário Líquido                 : R$ {salario_liquido:.2f}")
#%%

# Questão 13 #
print("""1 - Domingo
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sabado\n""")

dia = int(input("Digite o número correspondente ao dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("Valor invalido!")
# %%

# Questão 13 # Usando match case
print("""1 - Domingo
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sabado\n""")

dia = int(input("Digite o número correspondente ao dia da semana: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print ("Valor invalido!")
# %%

# Questão 14 #
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = nota1+nota2/2

if 9 < media <= 10:
    print("APROVADO")
elif 7.5 < media <= 9:

    print("APROVADO")
elif 6 < media <= 7.5:
    print("APROVADO")
elif 4 <= media <= 6:
    print("REPROVADO")
elif 0 <= media < 4:
    print("REPROVADO")
else:
    print("Nota inválida")

print(f"A notas do aluno são {nota1} e {nota2}")
print(f"A média obtida pelo aluno é: {media}")
# %%

# Questão 15 #

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("É um triângulo.")
    if lado1 == lado2 and lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero: três lados iguais.")
    elif lado1 == lado2 or lado1 == lado2 or lado2 == lado3:
        print("Triângulo Isósceles: quaisquer dois lados iguais.")
    elif lado1 != lado2 and lado1 != lado2 and lado2 != lado3:
        print("Triângulo Escaleno: três lados diferentes.")
else:
    print("Não é um triângulo.")

# %%

# Questão 16 #
import math

a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é de segundo grau. Programa encerrado!")
    exit()
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

delta = (-b**2) - (4*a*c)

raiz_quadrada = math.sqrt(delta)
x1 = (-b + raiz_quadrada) / (2*a)
x2 = (-b - raiz_quadrada) / (2*a)

if delta < 0:
    print("A equação não possui raízes reais. Programa encerrado!")
    exit()
elif delta == 0:
    print(f"A equação possui raízes iguais sendo elas {x1:.0f}.")
else:
    print(f"As raízes são {x1:.0f} e {x2:.0f}.")

# %%

# Questão 17 #

ano = int(input("Digite um ano: "))

if ano % 4 == 00 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} tem 365 dias.")

# %%

# Questão 18 #

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

#%%

# Questão 19 #

def analisar_numero(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        partes.append(f"{centenas} centena" if centenas == 1 else f"{centenas} centenas")
    if dezenas > 0:
        partes.append(f"{dezenas} dezena" if dezenas == 1 else f"{dezenas} dezenas")
    if unidades > 0:
        partes.append(f"{unidades} unidade" if unidades == 1 else f"{unidades} unidades")

    print(f"{numero} = {', '.join(partes[:-1])} e {partes[-1]}" if len(partes) > 1 else f"{numero} = {partes[0]}")

numero = int(input("Digite um número inteiro menor que 1000: "))
analisar_numero(numero)

# %%

#Questãp 20 #
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1+nota2+nota3)/3

if media == 10:
    print(f"Aprovado com Distinção! Sua média é {media}")
elif media >= 7:
    print(f"Aprovado! Sua média é {media:.1f}")
else:
    print(f"Reprovado! Sua média é {media:.1f}")
# %%

#Questão 21#

valor = float(input("Digite a quantia que deseja sacar: "))

if valor < 10:
    print("O valor mínimo a se sacar é de 10 reais.")
elif valor > 600:
    print("O valor máximo a se sacar é de 600 reais.")
else:
    valor = int(valor)
    notas_100 = valor // 100
    valor %= 100

    notas_50 = valor // 50
    valor %= 50

    notas_10 = valor // 10
    valor %= 10

    notas_5 = valor // 5
    valor %= 5

    notas_1 = valor

    partes = []

    if notas_100 > 0:
        partes.append(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100")
    if notas_50 > 0:
        partes.append(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50")
    if notas_10 > 0:
        partes.append(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10")
    if notas_5 > 0:
        partes.append(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5")
    if notas_1 > 0:
        partes.append(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1")

    print(f"Para sacar a quantia de {sum([notas_100 * 100, notas_50 * 50, notas_10 * 10, notas_5 * 5, notas_1])} reais, o programa fornece {', '.join(partes[:-1])} e {partes[-1]}.")

#%%

# Questão 22 #
numero = int(input("Digite um número: "))

if numero < 0:
    print("Não é possivel verificar números negativos. ")
elif numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
# %%

#Questão 23#

def verificar_numero(numero):

    if numero % 1 == 0:
        return f"O número {numero} é inteiro"
    else:
        return f"O numero {numero} é decimal"

num = float(input("Digite um número: "))
print(verificar_numero(num))

#%%

#Questão 24 #

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja: ")

if operacao == 'soma' or operacao == '+':
    resultado = numero1+numero2
elif operacao == 'subtração' or operacao == '-':
    resultado = numero1 - numero2
elif operacao == 'multiplicação' or operacao == '*':
    resultado = numero1*numero2
elif operacao == 'divisão' or operacao == '/':
    resultado = numero1/numero2
else:
    print("Digite uma operação valida.")

if resultado % 2 == 0:
    print(f"O valor {resultado:.2f} é par")
else:
    print(f"O número {resultado:.2f} é ímpar")
if resultado > 0:
    print(f"O número {resultado:.2f} é positivo.")
else:
    print(f"O número {resultado:.2f} é negativo.")
if resultado % 1 == 0:
    print(f"O número {resultado:.2f} é inteiro")
else:
    print(f"O numero {resultado:.2f} é decimal")

# %%

# Questão 24 # Match case

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja: ")

match operacao:
    case 'soma' | '+':
        resultado = numero1+numero2
    case 'subtração' | '-':
        resultado = numero1 - numero2
    case 'multiplicação' | '*':
        resultado = numero1*numero2
    case 'divisão' | '/':
        resultado = numero1/numero2
    case _:
        print("Digite uma operação valida.")

if resultado % 2 == 0:
    print(f"O valor {resultado:.2f} é par")
else:
    print(f"O número {resultado:.2f} é ímpar")
if resultado > 0:
    print(f"O número {resultado:.2f} é positivo.")
else:
    print(f"O número {resultado:.2f} é negativo.")
if resultado % 1 == 0:
    print(f"O número {resultado:.2f} é inteiro")
else:
    print(f"O numero {resultado:.2f} é decimal")
# %%

# Questão 25 #

participacao = 0

telefone = input("Telefonou para vítima? (Responda com sim ou não.) ")
if telefone == 'sim':
    participacao +=1
local = input("Esteve no local do crime? (Responda com sim ou não.) ")
if local == 'sim':
    participacao +=1
mora = input("Mora perto da vítima? (Responda com sim ou não.) ")
if mora == 'sim':
    participacao +=1
devia = input("Devia para a vítima? (Responda com sim ou não.) ")
if devia == 'sim':
    participacao +=1
trabalhou = input("Já trabalhou com a  vítima? (Responda com sim ou não.) ")
if trabalhou == 'sim':
    participacao +=1

if participacao == 2:
    print("Suspeita!")
elif participacao > 2 and participacao <= 4:
    print("Cúmplice!")
elif participacao == 5:
    print("Assassino!")
else:
    print("Inocente!")

# %%

# Questão 26 #

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

#%%

# Questão 27 #

preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))


if kg_morango <= 5:
    valor_morango = kg_morango * preco_morango_ate_5kg
else:
    valor_morango = kg_morango * preco_morango_acima_5kg


if kg_maca <= 5:
    valor_maca = kg_maca * preco_maca_ate_5kg
else:
    valor_maca = kg_maca * preco_maca_acima_5kg

valor_total = valor_morango + valor_maca


if kg_morango + kg_maca > 8 or valor_total > 25.00:
    valor_total *= 0.90

print(f"Valor a ser pago: R$ {valor_total:.2f}")

#%%

# Questão 28 #

preco_file_duplo_ate_5kg = 4.90
preco_file_duplo_acima_5kg = 5.80

preco_alcatra_ate_5kg = 5.90
preco_alcatra_acima_5kg = 6.80

preco_picanha_ate_5kg = 6.90
preco_picanha_acima_5kg = 7.80


tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ").lower()
kg_carne = float(input("Digite a quantidade de carne (em Kg): "))
pagamento = input("Pagamento no cartão Tabajara? Digite S-sim ou N-não: ").lower()


if tipo_carne == "file duplo":
    preco_ate_5kg = preco_file_duplo_ate_5kg
    preco_acima_5kg = preco_file_duplo_acima_5kg
elif tipo_carne == "alcatra":
    preco_ate_5kg = preco_alcatra_ate_5kg
    preco_acima_5kg = preco_alcatra_acima_5kg
elif tipo_carne == "picanha":
    preco_ate_5kg = preco_picanha_ate_5kg
    preco_acima_5kg = preco_picanha_acima_5kg
else:
    print("Tipo de carne inválido.")
    exit()


if kg_carne <= 5:
    valor_total = kg_carne * preco_ate_5kg
else:
    valor_total = kg_carne * preco_acima_5kg


if pagamento == "s":
    desconto = valor_total * 0.05
    valor_total -= desconto
    tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    tipo_pagamento = "Dinheiro"


print("\n--Cupom Fiscal--\n")
print(f"Tipo de Carne: {tipo_carne.capitalize()}")
print(f"Quantidade: {kg_carne:.2f} Kg")
print(f"Preço Total: R$ {valor_total + desconto:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valor_total:.2f}")

# %%
