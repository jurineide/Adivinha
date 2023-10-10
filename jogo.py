import random
import sqlite3
import json

nome_jogador = ""


def jogar():
    obter_nome_jogador()
    explicacao_jogo()

    numero_secreto = random.randrange(0, 11)
    nivel = escolher_nivel()

    tentativas = 0

    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 5
    else:
        tentativas = 3

    pontos = 1000
    acertou = False

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute = int(input("Digite um número entre 0 e 10: "))

        if chute < 0 or chute > 10:
            print("Você deve digitar um número entre 0 e 10!")
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
        salvar_pontuacao(pontos)
        ganhou()
    else:
        print(f"Você perdeu e fez 0 pontos!")
        perdeu(numero_secreto)

    mostrar_pontuacoes_individuais_json()
    mostrar_pontuacoes_json()


def explicacao_jogo():
    print("********************************")
    print("*Bem-vindo ao jogo de adivinhação *")
    print("********************************")
    print("Neste jogo, você precisa adivinhar um número secreto.")
    print("O número está entre 0 e 10, e você terá um número limitado de tentativas.")
    print(
        "A quantidade de tentativas varia de acordo com o nível de dificuldade que você escolher."
    )
    print("E no final você terá a quantidade de pontos que você obteve.")
    print("Boa sorte!\n")


def escolher_nivel():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (20 tentativas)")
    print("2 - Médio (10 tentativas)")
    print("3 - Difícil (5 tentativas)")

    while True:
        try:
            nivel = int(
                input("Digite o número correspondente ao nível desejado (1/2/3): ")
            )
            if nivel in [1, 2, 3]:
                return nivel
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite um número válido.")


def obter_nome_jogador():
    global nome_jogador
    if not nome_jogador:
        nome_jogador = input("Digite o seu nome abreviado: ")


def salvar_pontuacao(pontos):
    conn = sqlite3.connect("pontuacoes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pontuacoes (nome TEXT, pontos INT)")
    cursor.execute("INSERT INTO pontuacoes VALUES (?, ?)", (nome_jogador, pontos))
    conn.commit()
    conn.close()


def mostrar_pontuacoes_json():
    conn = sqlite3.connect("pontuacoes.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nome, AVG(pontos) AS media FROM pontuacoes GROUP BY nome ORDER BY media DESC"
    )
    resultados = cursor.fetchall()
    conn.close()

    dados_json = []

    for nome, pontuacao_media in resultados:
        pontuacao_media_arredondada = round(pontuacao_media, 1)
        jogador = {"nome": nome, "pontuacao_media": pontuacao_media_arredondada}
        dados_json.append(jogador)

    with open("media_jogadores.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)


def mostrar_pontuacoes_individuais_json():
    conn = sqlite3.connect("pontuacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, pontos FROM pontuacoes ORDER BY pontos DESC")
    resultados = cursor.fetchall()
    conn.close()

    dados_json = {}

    for nome, pontos in resultados:
        if nome not in dados_json:
            dados_json[nome] = []
        dados_json[nome].append(pontos)

    with open("pontuacoes_individuais.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)


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
