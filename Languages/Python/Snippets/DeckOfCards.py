from random import shuffle

class Deck:
    def __init__(self):
        from itertools import product
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]
        suits = ["♠", "♣", "♥", "♦"]
        self.list_of_cards = []
        list(map(
            lambda v: self.list_of_cards.append(Card(*v)),
            list(product(values, suits))
        ))

    def shuffle(self): shuffle(self.list_of_cards)

    def show(self): [ print(card, end=r"    ") for card in self.list_of_cards ]

class Card:
    def __init__(self, value, suit): self.name = f"{value} {suit}"

    def __str__(self): return self.name

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.show()