# %%
#Questão 1
def imprimeSequencia(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()


n = int(input("Digite o valor de n: "))
imprimeSequencia(n)

# %%
# Questão 2
def imprimeSequencia(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input("Digite o valor de n: "))
imprimeSequencia(n)
#%%
#Questão 3
def soma(num1, num2, num3):
    return num1 + num2 + num3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(soma(num1, num2, num3))
#%%
#Questão 4
def verifica(numero):
    if numero > 0:
        print("P")
    else:
        print("N")

num = int(input("Digite um número: "))
verifica(num)

#%%
#Questão 5
def somaImposto(taxaImposto, custo):
    return custo * (1 + taxaImposto / 100)

taxa = float(input("Digite a taxa de imposto (em %): "))
custo = float(input("Digite o custo do item: "))
custo_com_imposto = somaImposto(taxa, custo)
print(f"O custo do item com imposto é: R$ {custo_com_imposto:.2f}")

#%%
#Questão 6
def converteHora(horas, minutos):
    if horas >= 12:
        periodo = 'P'
        horas = horas - 12 if horas > 12 else 12
    else:
        periodo = 'A'
        horas = horas if horas > 0 else 12
    return horas, minutos, periodo

def exibe_hora(horas, minutos, periodo):
    sufixo = "A.M." if periodo == 'A' else "P.M."
    print(f"{horas}:{minutos:02d} {sufixo}")

while True:
    horas = int(input("Digite a hora (no formato de 24 horas): "))
    minutos = int(input("Digite os minutos: "))
    horas_12, minutos_12, periodo = converteHora(horas, minutos)
    exibe_hora(horas_12, minutos_12, periodo)

    repetir = input("Deseja converter outro horário? (s/n): ")
    if repetir.lower() != 's':
        break

#%%
#Questão 7
def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso > 0:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * dias_atraso
        return valor_prestacao + multa + juros
    else:
        return valor_prestacao

total_pago = 0
qnt_prestacoes = 0

while True:
    valor_prestacao = float(input("Digite o valor da prestação (0 para encerrar): "))
    if valor_prestacao == 0:
        break
    dias_atraso = int(input("Digite o número de dias em atraso: "))

    valor_final = valorPagamento(valor_prestacao, dias_atraso)
    print(f"Valor a ser pago: R$ {valor_final:.2f}")

    total_pago += valor_final
    qnt_prestacoes += 1

print("\nRelatório do dia")
print(f"Quantidade de prestações pagas: {qnt_prestacoes}")
print(f"Total pago: R$ {total_pago:.2f}")

#%%
#Questão 8
def quantidadeDigitos(numero):
    return len(str(abs(numero)))

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} possui {quantidadeDigitos(numero)} dígitos.")

#%%
#Questão 9
def reverso(numero):
    return int(str(abs(numero))[::-1]) * (-1 if numero < 0 else 1)

numero = int(input("Digite um número inteiro: "))
print(f"O reverso de {numero} é {reverso(numero)}.")

# %%
#Questão 10

import random

def rolar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogo_craps():
    print("Bem-vindo ao jogo de Craps!")
    ponto = rolar_dados()
    print(f"Primeira rolagem: {ponto}")

    if ponto in [7, 11]:
        print("Você tirou um 'natural'! Parabéns, você ganhou!")
        return
    elif ponto in [2, 3, 12]:
        print("Craps! Você perdeu!")
        return

    print(f"Seu Ponto é {ponto}. Continue jogando até tirar {ponto} novamente para ganhar.")

    while True:
        rolagem = rolar_dados()
        print(f"Você tirou {rolagem}")

        if rolagem == ponto:
            print("Parabéns! Você tirou o ponto e ganhou!")
            break
        elif rolagem == 7:
            print("Você tirou 7 antes de tirar o ponto. Você perdeu!")
            break

jogo_craps()

# %%
