import random

def rolar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogo_craps():
    print("Bem-vindo ao jogo de Craps!")
    ponto = rolar_dados()
    print(f"Primeira rolagem: {ponto}")

    if ponto in [7, 11]:
        print("Você tirou um 'natural'! Parabéns, você ganhou!")
        return
    elif ponto in [2, 3, 12]:
        print("Craps! Você perdeu!")
        return

    print(f"Seu Ponto é {ponto}. Continue jogando até tirar {ponto} novamente para ganhar.")

    while True:
        rolagem = rolar_dados()
        print(f"Você tirou {rolagem}")

        if rolagem == ponto:
            print("Parabéns! Você tirou o ponto e ganhou!")
            break
        elif rolagem == 7:
            print("Você tirou 7 antes de tirar o ponto. Você perdeu!")
            break

jogo_craps()