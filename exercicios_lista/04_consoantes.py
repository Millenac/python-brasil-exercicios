lista = []

for i in range(10):
    letra = input("Digite um caractere: ").lower()
    lista.append(letra)

vogais = 'aeiou'

consoantes = [letra for letra in lista if letra.isalpha() and letra not in vogais]

quantidade_consoantes = len(consoantes)

print(f"Número de consoantes lidas: {quantidade_consoantes}")
print(f"Consoantes: {', '.join(consoantes)}")
