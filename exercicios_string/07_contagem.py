frase = input("Digite uma frase: ")
espacos = frase.count(" ")
vogais = sum(frase.lower().count(vogal) for vogal in "aeiou")

print(f"Quantidade de espaços em branco: {espacos}")
print(f"Quantidade de vogais: {vogais}")
