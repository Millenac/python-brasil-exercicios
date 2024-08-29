while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <=10:
            break
    except ValueError:
        print("Digite uma entrada válida!")

print(f"\nA nota digitada foi {nota}")