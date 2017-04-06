# Design a deck of cards.

class CardDeck():
  def __init__(self, cards):
    if cards:
      self.cards = cards
    else:
      self.cards = []
  
  def shuffle(self):
    for i in xrange(len(self.cards)):
      o = random.randint(i)
      self.cards[i], self.cards[o] = self.cards[o], self.cards[i]
  
  def draw_card(self):
    return self.cards.pop()
  
class BlackjackHand(CardDeck):
  def value(self):
    value, aces = 0, 0
    for card in self.cards:
      value += min(card.number, 10)
      aces += 1
    while value <= 11:
      if aces:
        value += 10
        aces -= 1
    return value

class Card():
  def __init__(self, number, suit):
    self.number, self.suit = number, suit

import unittest

class Test(unittest.TestCase):
  def test_card_deck(self):
    deck = CardDeck([Card(2, "Hearts"), Card(4, "Clubs")])
    self.assertEqual(deck.draw_card().suit, "Clubs")
  
  def test_blackjack_hand(self):
    hand = BlackjackHand([Card(5,"Diamonds"), Card(7,"Clubs")])
    self.assertEqual(hand.value(), 12)
    hand = BlackjackHand([Card(5,"Diamonds"), Card(1,"Clubs")])
    self.assertEqual(hand.value(), 16)
    hand = BlackjackHand([Card(12,"Diamonds"),Card(1,"Clubs")])
    self.assertEqual(hand.value(), 21)
    hand = BlackjackHand([Card(12,"Diamonds"),Card(1,"Clubs"),Card(1,"Hearts")])
    self.assertEqual(hand.value(), 12)

if __name__ == "__main__":
  unittest.main()

