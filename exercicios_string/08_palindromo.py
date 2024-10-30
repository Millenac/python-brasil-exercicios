texto = input("Digite uma sequência de caracteres: ")
texto_formatado = ''.join(c.lower() for c in texto if c.isalnum())
if texto_formatado == texto_formatado[::-1]:
    print("A sequência é um palíndromo.")
else:
    print("A sequência não é um palíndromo.")
