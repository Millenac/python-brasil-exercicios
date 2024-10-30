#%%
#Questão 1
str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

print(f'String 1: "{str1}"')
print(f'String 2: "{str2}"')
print(f'Tamanho de "{str1}": {len(str1)} caracteres')
print(f'Tamanho de "{str2}": {len(str2)} caracteres')

if len(str1) == len(str2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if str1 == str2:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")

#%%
#Questão 2
nome = input("Digite seu nome: ")
nome_invertido = nome[::-1].upper()
print(f"Nome ao contrário em maiúsculas: {nome_invertido}")

#%%
#Questão 3
nome = input("Digite seu nome: ")
for letra in nome:
    print(letra)

#%%
#Questão 4

nome = input("Digite seu nome: ")
for i in range(1, len(nome) + 1):
    print(nome[:i])

#%%
#Questão 5
nome = input("Digite seu nome: ")
for i in range(len(nome), 0, -1):
    print(nome[:i])

#%%
#Questão 6

data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes_extenso = meses[int(mes) - 1]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")

#%%
#Questão 7
frase = input("Digite uma frase: ")
espacos = frase.count(" ")
vogais = sum(frase.lower().count(vogal) for vogal in "aeiou")

print(f"Quantidade de espaços em branco: {espacos}")
print(f"Quantidade de vogais: {vogais}")

#%%
#Questão 8
texto = input("Digite uma sequência de caracteres: ")
texto_formatado = ''.join(c.lower() for c in texto if c.isalnum())
if texto_formatado == texto_formatado[::-1]:
    print("A sequência é um palíndromo.")
else:
    print("A sequência não é um palíndromo.")

#%%
#Questão 9

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"

cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")
if valida_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")


#%%
#Questão 10

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
