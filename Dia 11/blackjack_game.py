import random  # Importa o módulo random para gerar números aleatórios.
from art import blackjack_logo  # Importa a arte ASCII do arquivo art.py


def deal_card():
    """Retorna uma carta aleatória do baralho."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(hand):
    """Calcula a pontuação de uma mão de cartas."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(player_score, dealer_score):
    """Compara as pontuações do jogador e do dealer para determinar o vencedor."""
    if player_score > 21:
        return "Você ultrapassou 21. Você perdeu."
    elif dealer_score > 21:
        return "Dealer ultrapassou 21. Você ganhou!"
    elif player_score == dealer_score:
        return "Empate."
    elif player_score == 0:
        return "Blackjack! Você ganhou!"
    elif dealer_score == 0:
        return "Dealer tem Blackjack! Você perdeu."
    elif player_score > dealer_score:
        return "Você ganhou!"
    else:
        return "Você perdeu."


def play_blackjack():
    """Função principal para executar o jogo de Blackjack."""

    print(blackjack_logo)
    print("Bem-vindo ao Blackjack!")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Suas cartas: {player_hand}, pontuação atual: {player_score}")
        print(f"Primeira carta do dealer: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Digite 's' para pegar outra carta, ou 'n' para passar: ").lower()
            if should_continue == 's':
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Sua mão final: {player_hand}, pontuação final: {player_score}")
    print(f"Mão final do dealer: {dealer_hand}, pontuação final: {dealer_score}")
    print(compare(player_score, dealer_score))


while True:
    play_game = input("Você quer jogar uma partida de Blackjack? Digite 'S' para sim ou 'N' para não: ").upper()

    if play_game == 'S':
        print("\n" * 20)
        play_blackjack()
    elif play_game == 'N':
        print("Obrigado por jogar! Até a próxima.")
        break
    else:
        print("Entrada inválida. Por favor, digite 'S' ou 'N'.")
