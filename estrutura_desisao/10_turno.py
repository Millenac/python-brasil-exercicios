turno = input("Digite que turno você estuda. Digite M-Matutino ou V-Vespertino ou N-Noturno: ")

novo_turno = turno.upper()

if novo_turno == "M":
    print("Bom dia!")
elif novo_turno == "V":
    print("Boa tarde!")
elif novo_turno == "N":
    print("Boa noite!")
else:
    print("valor inválido!")