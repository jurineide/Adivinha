import random
import sqlite3


def jogar():
    nome = obter_nome_jogador()  # Obtém o nome do jogador
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

        if chute < 1 or chute > 100:
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
        ponto=0

    if acertou:
        print(f"Você acertou e fez {pontos} pontos!")
        salvar_pontuacao(nome, pontos)  # Salva a pontuação no banco de dados
        ganhou()
    else:
        print(f"Você perdeu e fez {ponto} pontos!")
        perdeu(numero_secreto)

    mostrar_pontuacoes()  # Mostra as pontuações dos jogadores

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
    print("O número está entre 0 e 10, e você terá um número limitado de tentativas.")
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

# Função para obter o nome do jogador
def obter_nome_jogador():
    nome = input("Digite o seu nome abreviado: ")
    return nome

# Função para salvar a pontuação em um banco de dados
def salvar_pontuacao(nome, pontos):
    conn = sqlite3.connect("pontuacoes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pontuacoes (nome TEXT, pontos INT)")
    cursor.execute("INSERT INTO pontuacoes VALUES (?, ?)", (nome, pontos))
    conn.commit()
    conn.close()

# Função para mostrar as pontuações dos jogadores
def mostrar_pontuacoes():
    conn = sqlite3.connect("pontuacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, AVG(pontos) AS media FROM pontuacoes GROUP BY nome")
    resultados = cursor.fetchall()
    conn.close()

    print("Pontuações dos jogadores (média por jogador):")
    for nome, pontuacao_media in resultados:
        print(f"{nome}: Pontuação Média = {pontuacao_media:.2f}")

def mostrar_pontuacoes_individuais():
    conn = sqlite3.connect("pontuacoes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, pontos FROM pontuacoes ORDER BY pontos DESC")
    resultados = cursor.fetchall()
    conn.close()

    with open("pontuacoes_individuais.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Pontuações dos jogadores (em ordem decrescente):\n")
        for nome, pontos in resultados:
            arquivo.write(f"{nome}: Pontuação = {pontos}\n")

    arquivo.close()

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
    mostrar_pontuacoes_individuais()  # Mostra as pontuações individuais e escreve em um arquivo    
    jogar()
