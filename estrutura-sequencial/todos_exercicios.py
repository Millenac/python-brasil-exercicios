#%%
# Questão 1 #

print("Alo mundo")
# %%
# Questão 2 #

numero = float(input("Digite um número: "))
print("O número informado foi ", numero)

#%%
# Questão 3 #

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

print("A soma é:", num1+num2)
#%%
# Questão 4 #

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

print("A média é:", media)
#%%
#Questão 5 #

metros = int(input("Digite os metros: "))
centimetros = metros*100

print(f"A conversão de {metros} metros para centímetros é:", centimetros, "cm")
#%%
# Questão 6 #

raio = float(input("Digite o raio: "))
pi = 3.14
area = pi*raio**2

print(f"A área é: {area:.2f}")
#%%
# Questão 7 #

lado = float(input("Digite o lado do quadrado: "))
area = lado**2

print ("O dobro a área do quadrado é", area*2)
#%%
# Questão 8 #
hora = float(input("Digite quanto você ganha por hora: "))
trab = int(input("Digite a quantidade de horas que você trabalha por mês: "))

salario = (hora*trab)

print(f"Seu salário total no mês é R$ {salario:.2f}")
#%%
# Questão 9 #
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = 5*((fahrenheit-32)/9)
print(f"A conversão de {fahrenheit} para celsius é: {celsius:.0f} graus")
# %%
# Questão 10 #
celsius = int(input("Digite a temperatura em celsius: "))

fahrenheit = (1.8* celsius) + 32

print(f"A conversão de {celsius} celsius para fahrenheit é: {fahrenheit:.0f}")
# %%
# Questão 11 #

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print("O produto do dobro do primeiro com metade do segundo ", num1*num1(num2/2))
print("a soma do triplo do primeiro com o terceiro", (num1*3)+num3)
print(f"O {num3} elevado ao cubo é:", num3**3)
 #%%
 # Questão 12 #

altura = float(input("Digite sua altura: "))
peso_ideal = (72.7*altura) -58

print("Seu peso ideal é:", peso_ideal)
#%%
# Questão 13 #

altura = float(input("Digite sua altura: "))

ideal_woman = (62.1*altura) - 44.7
ideal_man = (72.7*altura) -58

print("Seu peso ideal caso você seja mulher é:", ideal_woman)
print("Seu peso ideal caso você seja homem é:", ideal_man)
# %%
#%%
# Questão 14 #

peso = float(input("Digite o peso dos peixes: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso*4.0
    print(f"Seu excesso foi de {excesso} e sua multa é de R$", multa)
else:
    print("Você não excedeu o peso, logo não precisa pagar multa")
#%%
# Questão 15 #

qnt = float(input("Quanto você ganha por hora: "))
horas = int(input("Digite quantas horas você trabalha por mês: "))

salario_bruto = qnt*horas
imposto = (11/100)*salario_bruto
inss = (8/100)*salario_bruto
sindicato = (5/100)*salario_bruto
descontos = imposto+inss+sindicato
salario_liquido = salario_bruto - descontos

print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%) : R$", imposto)
print("- INSS (8%) : R$", inss)
print("- Sindicato ( 5%) : R$", sindicato)
print("= Salário Liquido : R$", salario_liquido)
# %%
# Questão 16 #
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
#%%
#Questão 17 #

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

#%%
#Questão 18 #

tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade = float(input("Digite a velocidade do link de Internet (em Mbps): "))

velocidade_internet_MBps = velocidade/8
tempo_download_segundos = tamanho_arquivo/velocidade_internet_MBps
tempo_download_minutos = tempo_download_segundos/60

print(f"O tempo aproximado de download é de {tempo_download_minutos:.2f} minutos.")
