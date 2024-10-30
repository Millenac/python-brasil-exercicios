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
