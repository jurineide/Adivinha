import random

def jogar():
    explicacao_jogo()

    numero_secreto = random.randrange(1, 101)
    nivel = escolher_nivel()

    tentativas = 0

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    pontos = 1000
    acertou = False

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if chute == numero_secreto:
            acertou = True
            break
        elif chute > numero_secreto:
            print(f"VOCÊ ERROU. O NÚMERO SECRETO É MENOR QUE {chute}.")
            print("---------------x-----------------")
        else:
            print(f"VOCÊ ERROU. O NUMERO SECRETO É MAIOR QUE {chute}")
            print("---------------x-----------------")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

    if acertou:
        print(f"Você acertou e fez {pontos} pontos!")
        ganhou()
    else:
        perdeu(numero_secreto)

def explicacao_jogo():
    print("********************************")
    print("Bem-vindo ao jogo de adivinhação")
    print("********************************")
    print("*******************")
    print("***************")
    print("**********")
    print("******")
    print("***")
    print("Neste jogo, você precisa adivinhar um número secreto.")
    print("O número está entre 1 e 100, e você terá um número limitado de tentativas.")
    print("A quantidade de tentativas varia de acordo com o nível de dificuldade que você escolher.")
    print("E no final você terá a quantidade de pontos que você obteve.")
    print("Boa sorte!\n")    

def escolher_nivel():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (20 tentativas)")
    print("2 - Médio (10 tentativas)")
    print("3 - Difícil (5 tentativas)")

    while True:
        try:
            nivel = int(input("Digite o número correspondente ao nível desejado (1/2/3): "))
            if nivel in [1, 2, 3]:
                return nivel
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite um número válido.")

def ganhou():
    print("****** Parabéns!!! ******")
    print("Você é muito inteligente!!!")
    print("Ficamos felizes por sua vitória!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("*************************")

def perdeu(numero_secreto):
    print("***** Você perdeu!! *****")
    print(f"O número secreto era {numero_secreto}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == "__main__":
    jogar()
