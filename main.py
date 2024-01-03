import random
from replit import clear
from art import logo

def random_card():
    """Return a card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return 'You went over 21. You lose :('
    if player_score == computer_score:
        return "It's a Draw"
    elif computer_score == 0:
        return "The player loose :("
    elif player_score == 0:
        return "The player win ! :)"
    elif player_score > 21:
        return "Your score is over 21. Bad luck"
    elif computer_score > 21:
        return "The computer is over 21. You win"
    elif player_score > computer_score:
        return "You win :)"
    else:
        return "You lose :("

def play_blackjack():

    print(logo)
    
    is_game_over = False
    player = []
    computer = []

    for _ in range(2):
        player.append(random_card())
        computer.append(random_card())

    while not is_game_over:

        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        print(f"    Your cards: {player} and current score: {player_score}")
        print(f"    Computer's first card: {computer[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            pick_another_card = input("Do you want another card? Type 'y' or 'no'")
            if pick_another_card == 'y':
                player.append(random_card())
            else:
                is_game_over = True

        '''If the computer score > 17 and not a blackjack (0)'''
    while computer_score != 0 and computer_score < 17:
        computer.append(random_card())
        computer_score = calculate_score(computer)

    print(f"    Your final hand: {player}, final score: {player_score}")
    print(f"    Computer final hand: {computer}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_blackjack()