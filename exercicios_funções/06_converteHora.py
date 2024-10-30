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
