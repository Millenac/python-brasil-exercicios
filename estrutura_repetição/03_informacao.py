while True:
    nome = input("Digite seu nome: ")
    tamanho = len(nome)
    if tamanho <= 3:
        print("Seu nome possui menos de 3 caracteres.")
        continue
    idade = int(input("Digite sua idade: "))
    if idade > 150 or idade < 0:
        print("Sua idade precisa está entre 0 a 150 anos.")
        continue
    salario = float(input("Digite seu salario"))
    if salario < 0:
        print("Digite um salario valido.")
        continue
    sexo = input("Digite f ou m para seu sexo")
    if sexo != 'f' and sexo != 'm':
        print("Você digitou o sexo errado.")
        continue
    estado = input("Digite a inicial do seu Estado Civil")
    if estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
        print("Digite a incial corretamente.")
        continue
    else:
        break