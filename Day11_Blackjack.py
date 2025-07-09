import random

cards = [('2',2), ('3',3), ('4',4), ('5',5), ('6', 6), ('7',7), ('8',8), ('9',9), ('10',10), ('Q', 10), ('K',10), ('J',10), ('A', 1)]

def draw_card():
    return cards[random.randint(0, len(cards) - 1)]
    
def initial_draw(player_cards, dealer_cards):
    for i in range(0,2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())
        
def get_another_card(cards):
    player_cards.append(draw_card())
    
def print_cards(cards):
    return ' '.join(str(p[0]) for p in cards)

def print_cards_round(player_cards, dealer_cards, show_all_dealers):
    print(f'Your cards are [{print_cards(player_cards)}] and the total score is [{check_score(player_cards)}]')
    if show_all_dealers:
        print(f'Dealer cards are [{print_cards(dealer_cards)}] and the total score is [{check_score(dealer_cards)}]')
    else:
        print(f'Dealer cards are [{print_cards(dealer_cards)[0]}]')
    
def check_score(cards):
    return sum((p[1]) for p in cards)
    
def draw_new_card(player_cards, dealer_cards):
    stop_draw = False
    while not stop_draw:
        decision = input('Press h to hit another card or press n to hold: ')
        if (decision == 'n'):
            stop_draw = True
        elif (decision == 'h'):
            player_cards.append(draw_card())
            print_cards_round(player_cards, dealer_cards, False)
            if check_score(player_cards) > 21:
                print('Score exceeded 21. It is a BUST')
                stop_draw = True
                return True
        else:
            print("Enter correct option.")
            
def final_score_check(player_cards, dealer_cards):
    if check_score(dealer_cards) < 17:
        dealer_cards.append(draw_card())
     
    print_cards_round(player_cards, dealer_cards, True)    
    if check_score(dealer_cards) > check_score(player_cards):
        print('The House Won.')
    elif check_score(dealer_cards) < check_score(player_cards):
        print('You WON!!!!')
    elif check_score(dealer_cards) == check_score(player_cards):
        print('It is a draw.')
    
def main_game():
    player_cards = []
    dealer_cards = []
    start_game = input('Do you want to play Blackjack. Enter y for yes and n for no: ')
    if (start_game == 'y'):
        initial_draw(player_cards, dealer_cards)
        print_cards_round(player_cards, dealer_cards, False)
        bust = draw_new_card(player_cards, dealer_cards)
        if not bust:
            final_score_check(player_cards,dealer_cards)

main_game()