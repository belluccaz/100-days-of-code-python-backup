from random import randint
from art import guess_logo

# O programa deve pedir ao usuário para adivinhar um número de 0 a 100.
# O programa deve ceder 10 tentativas no modo "easy" e 5 tentativas no modo "hard".
# O programa deve dar as seguintes dicas: caso o palpite do usuário seja menor que a resposta "muito baixo" ou "muito alto" para o inverso.
# Checar a resposta.

CHANCES_EASY_LEVEL = 10
CHANCES_HARD_LEVEL = 5




def checar_resposta(p_user, r_atual, turns):
    """Função para checar a resposta do usuário. Retornando o número de tentativas restantes."""
    if p_user > r_atual:
        print("Muito alto.")
        return turns - 1
    elif p_user < r_atual:
        print("Muito baixo.")
        return turns - 1
    else:
        print(f"Você acertou! A resposta era {r_atual}")


def selecionar_dificuldade():
    level = input("Escolha a dificuldade. Digite 'easy' ou 'hard': ")
    if level == "easy":
        return CHANCES_EASY_LEVEL
    else:
        return CHANCES_HARD_LEVEL



def game():
    print(guess_logo)
    print("Bem-vindo ao Jogo de Adivinhação!")
    # Escolhendo um número aleatório entre 1 e 100.
    print("Estou pensando em um numero entre 1 e 100.")
    resposta = randint(1, 100)
    print(f"Psssssiu, a resposta correta é {resposta}")


    turns = selecionar_dificuldade()
    palpite = 0

    while palpite != resposta:
        print(f"Você tem {turns} tentativas restantes para adivinhar o número.")
        # Palpite do usuário.
        palpite = int(input("Faça um palpite: "))

        turns = checar_resposta(palpite, resposta, turns)
        if turns == 0:
            print("Você utilizou todas as tentativas. Você perdeu.")
            return
        elif palpite != resposta:
            print("Tente de novo.")




game()