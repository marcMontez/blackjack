from random import shuffle

values = [_ for _ in range(2, 11)] + ['J', 'Q', 'K', 'A']
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

def get_deck():
    return [[value, suit] for value in values for suit in suits]

deck = get_deck()
shuffle(deck)

player_in = True
dealer_in = True

player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

def card_value(card):
    value = card[0]
    if value in values[0:-4]:
        return int(value)
    elif value == "A":
        return 11
    else:
        return 10

def hand_value(hand):
    temp_value = sum(card_value(_) for _ in hand)
    for card in hand:
        if card[0] == 'A':
            if temp_value > 21:
                temp_value -= 10
    return temp_value


input("Ready to play Blackjack? (enter 1 to continue) ")

print("The deck has been shuffled and the cards have been delt.")
while player_in:
    current_score_string = f"You are currently at {hand_value(player_hand)} with {player_hand}\nand the dealer is showing{dealer_hand[0]}"
    print(current_score_string)
    if hand_value(player_hand) == 21:
        if len(player_hand) < 3:
            print("Blackjack!!!")
        break
    elif hand_value(player_hand) > 21:
        print(f"Sorry, you busted with a score of {hand_value(player_hand)}")
        break
    elif hand_value(player_hand) < 21:
        response = int(input("Hit or stay? (hit = 1, stay = 2) "))
        if response == 1:
            player_in = True
            new_player_card = deck.pop()
            player_hand.append(new_player_card)
            print(f"You receive {new_player_card}.")
        else:
            player_in = False
            print("Okay. You stay.")



print("Let's see what the dealer gets.")

while dealer_in:
    dealer_score_string = f"The dealer now has {hand_value(dealer_hand)} with {dealer_hand}"
    print(dealer_score_string)
    if hand_value(dealer_hand) > 21:
        print("Dealer Busts! You win!")
        break
    elif hand_value(dealer_hand) < 17:
        dealer_in = True
        new_dealer_card = deck.pop()
        dealer_hand.append(new_dealer_card)
        print(f"The dealer draws {new_dealer_card}")
    elif hand_value(dealer_hand) >= 17:
        dealer_in = False
        print("The dealer stays.")
    else:
        dealer_in = False

dealer_score = hand_value(dealer_hand)
player_score = hand_value(player_hand)

if player_score > dealer_score and player_score < 22 or dealer_score > 21:
    print("You win!")
elif dealer_score > player_score and dealer_score < 22 or player_score > 21:
    print("Sorry, you lose.")
elif dealer_score == player_score:
    print("Push.")

