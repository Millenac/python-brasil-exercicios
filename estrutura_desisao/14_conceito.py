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