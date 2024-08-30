idades = []

num_pessoas = int(input("\nDigite o número total de pessoas: "))

for i in range(num_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    idades.append(idade)

media_idade = sum(idades) / num_pessoas

print(f"A média das idades é: {media_idade:.2f}")

if media_idade >= 0 and media_idade <= 25:
    classificacao = "jovem"
elif media_idade >= 26 and media_idade <= 60:
    classificacao = "adulta"
else:
    classificacao = "idosa"

print(f"A turma é {classificacao}.")