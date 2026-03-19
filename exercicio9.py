import random


def nome_opcao(numero):

    if numero == 1:
        return "Pedra"

    elif numero == 2:
        return "Papel"

    elif numero == 3:
        return "Tesoura"

    elif numero == 4:
        return "Lagarto"

    elif numero == 5:
        return "Spock"


def jogar(jogador, computador):

    nome_jogador = nome_opcao(jogador)
    nome_computador = nome_opcao(computador)

    print(f"voce: {nome_jogador}")
    print(f"computador: {nome_computador}")

    if jogador == computador:
        print("empate")
        return

    ganhou = 0

    if jogador == 1:
        if computador == 3:
            print("pedra quebra tesoura - voce ganhou")
            ganhou = 1
        elif computador == 4:
            print("pedra esmaga lagarto - voce ganhou")
            ganhou = 1

    elif jogador == 2:
        if computador == 1:
            print("papel cobre pedra - voce ganhou")
            ganhou = 1
        elif computador == 5:
            print("papel refuta spock - voce ganhou")
            ganhou = 1

    elif jogador == 3:
        if computador == 2:
            print("tesoura corta papel - voce ganhou")
            ganhou = 1
        elif computador == 4:
            print("tesoura decapita lagarto - voce ganhou")
            ganhou = 1

    elif jogador == 4:
        if computador == 2:
            print("lagarto come papel - voce ganhou")
            ganhou = 1
        elif computador == 5:
            print("lagarto envenena spock - voce ganhou")
            ganhou = 1

    elif jogador == 5:
        if computador == 1:
            print("spock vaporiza pedra - voce ganhou")
            ganhou = 1
        elif computador == 3:
            print("spock derrete tesoura - voce ganhou")
            ganhou = 1

    if ganhou == 0:
        print("computador ganhou")


print("1 - pedra")
print("2 - papel")
print("3 - tesoura")
print("4 - lagarto")
print("5 - spock")

jogador = int(input("escolha: "))

if jogador < 1 or jogador > 5:
    print("opcao invalida")

else:
    computador = random.randint(1, 5)
    jogar(jogador, computador)
