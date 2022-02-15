import random
from replit import clear

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 11
}

def deal():
  card = random.choice(cards)
  return card

def calculate_cards(cards_on_hands, res_list = [0]):
  res = 0
  #res_list - list for return: [cards_sum, index_of_ace, index_of_ace, ...]
  ace_on_hand = False
  for card in cards_on_hands:
    res += card[1]
    if card[1] == 11:
      ace_on_hand = True
  if res > 21 and ace_on_hand:
    i = cards_on_hands.index(['A', 11])
    cards_on_hands[i][1] = 1
    res_list.append(i)
    calculate_cards(cards_on_hands, res_list)
  else:
    res_list[0] = res
  return res_list

def blackjack(cards_on_hands):
  if len(cards_on_hands) == 2 and calculate_cards(cards_on_hands)[0] == 21:
    return True

def show_cards(cards_on_hands, player, is_final):
  cards_line = ""
  if player == "computer" and not is_final:
      cards_line = cards_line + " " + cards_on_hands[0][0] + " " + "*" 
  elif player == "computer":
    for card in cards_on_hands:
      cards_line = cards_line + " " + card[0]  
  else:
    for card in cards_on_hands:
      cards_line = cards_line + " " + card[0]
  return cards_line

play_again = True

while play_again:
  player_score = 0
  dealer_score = 0
  player_cards = []
  dealer_cards = []
  move_over = False
  game_over = False
  for _ in range(2):
    player_cards.append(deal())
    dealer_cards.append(deal())
  
  #check_if_bj_dealer
  if blackjack(dealer_cards):
    cards_listed = show_cards(dealer_cards, "computer", True)
    print(f"Dealer wins!\nDealer cards: {cards_listed}")
    cards_listed = show_cards(player_cards, "player", True)
    print(f"Player cards: {cards_listed}")
    move_over = True
    game_over = True
  elif blackjack(player_cards):
    cards_listed = show_cards(dealer_cards, "computer", True)
    print(f"Player wins!\nDealer cards: {cards_listed}")
    cards_listed = show_cards(player_cards, "player", True)
    print(f"Player cards: {cards_listed}")
    move_over = True
    game_over = True
  else:
    cards_listed = show_cards(dealer_cards, "computer", False)
    print(f"Dealer cards: {cards_listed}")
    cards_listed = show_cards(player_cards, "player", False)
    print(f"Player's cards: {cards_listed}")
    player_score = calculate_cards(player_cards)[0]
    print(f"Player's score: {player_score}")
    next_move = input("Would You like to hit another card Insert 'y' or 'n': ")
    if next_move != 'y':
      move_over = True
  while not move_over:
  #def player_moves(play_cards, deal_cards):  
    player_cards.append(deal())
    cards_listed = show_cards(dealer_cards, "computer", False)
    print(f"Dealer cards: {cards_listed}")
    cards_listed = show_cards(player_cards, "player", False)
    print(f"Player's cards: {cards_listed}")
    player_score = calculate_cards(player_cards)[0]
    print(f"Player's score: {player_score}")
    if player_score > 21:
      print("Game over! Dealer wins!")
      move_over = True
      game_over = True
      cards_listed = show_cards(dealer_cards, "computer", move_over)
      print(f"Dealer cards: {cards_listed}")
      dealer_score = calculate_cards(dealer_cards)[0]
      print(f"Dealer's score: {dealer_score}")
    else:
      next_move = input("Would You like to hit another card Insert 'y' or 'n': ")
      if next_move != 'y':
        move_over = True
  while not game_over:
    print("Dealer moves!")
    cards_listed = show_cards(dealer_cards, "computer", move_over)
    print(f"Dealer cards: {cards_listed}")
    dealer_score = calculate_cards(dealer_cards)[0]
    print(f"Dealer's score: {dealer_score}")
    cards_listed = show_cards(player_cards, "player", False)
    print(f"Player's cards: {cards_listed}")
    print(f"Player's score: {player_score}")
    print("Dealer's next move:")
    if dealer_score > 21:
      print("Game over! Player wins!")
      game_over = True
    elif dealer_score > 16:
      print("PAS!")
      game_over = True
      if dealer_score < player_score:
        print("Game over! Player wins!")
        game_over = True
      elif dealer_score > player_score:
        print("Game over! Dealer wins!")
        game_over = True
      elif dealer_score == player_score:
        print("Game over! Draw!")
        game_over = True
    else:
      print("Hit!")
      dealer_cards.append(deal())
  again = input("Would you like to play another game? Hit 'y' for new game or other key to cancel: ")
  if again == "y":
    play_again = True
  else:
    play_again = False

