lista_media = []

for i in range(2):
    nota1 = float(input(f"\nDigite a nota 1: "))
    nota2 = float(input(f"Digite a nota 2: "))
    nota3 = float(input(f"Digite a nota 3: "))
    nota4 = float(input(f"Digite a nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4)/ 4
    lista_media.append(media)

aluno = 0
for i in lista_media:
    if i >= 7:
        aluno +=1

print(f"\nA quantidade de alunos que tem a média igual ou maior que 7 é de {aluno} alunos.")
