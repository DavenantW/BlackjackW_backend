import random
# def game(players: list):
#     card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#     cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
#     deck = [(card, category) for category in card_categories for card in cards_list]
#     random.shuffle(deck)
#
#     for player in players:
#         player: {
#             'card': [deck.pop(), deck.pop()],
#             'score': 0
#         }
#
#     while True:
#         for player in players:
#             player['score'] = sum(card_value(card) for card in player['card'])
#
#         if player_score > 21:
#
#             break
#         if dealer_score > 21:
#             print("Cards Dealer Has:", dealer_card)
#             print("Score Of The Dealer:", dealer_score)
#             print("Cards Player Has:", player_card)
#             print("Score Of The Player:", player_score, '\n')
#             print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")
#             break
#
#         if player_score == 21:
#             print("Cards Dealer Has:", dealer_card)
#             print("Score Of The Dealer:", dealer_score)
#             print("Cards Player Has:", player_card)
#             print("Score Of The Player:", player_score, '\n')
#             print("Player wins (Player Has 21)")
#             break
#
#         choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()
#         if choice == "play":
#             new_card = deck.pop()
#             print(new_card)
#             if new_card[0] == 'Ace':
#                 new_card = ('Ace', 1)
#             player_card.append(new_card)
#         elif choice == "stop":
#             break
#         else:
#             print("Invalid choice. Please try again.")
#             continue
#
#         while dealer_score < 17 and not player_score > 21:
#             new_card = deck.pop()
#             dealer_card.append(new_card)
#             dealer_score += card_value(new_card)
#
#         print("Cards Dealer Has:", dealer_card)
#         print("Score Of The Dealer:", dealer_score, '\n')


class Game:
    def __init__(self, player1=None, player2=None, player3=None, player4=None, player5=None):
        self.dealer = Player(0)
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.player5 = player5

    def end(self):
        pass


class Player(Game):
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    DECK = [(card, category) for category in card_categories for card in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']]
    random.shuffle(DECK)

    def __init__(self, bet):
        self.bet = bet
        self.card = [self.DECK.pop(), self.DECK.pop()]
        self.score = sum(self.card_value(val) for val in self.card)

    def new_card(self, double=False):
        if double:
            self.bet = self.bet * 2
        new_card = self.DECK.pop()
        self.card.append(new_card)
        self.score += 1 if new_card[0] == 'Ace' else self.card_value(new_card)

    @classmethod
    def card_value(cls, card):
        if card[0] in ['Jack', 'Queen', 'King']:
            return 10
        elif card[0] == 'Ace':
            return 11
        else:
            return int(card[0])


p = Player(10)
p.new_card()
g = Game()
print(g)
