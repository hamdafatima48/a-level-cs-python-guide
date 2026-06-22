"""
Cambridge International AS & A Level Computer Science 9618
Paper 42 Practical - May/June 2022
Question: 3

Short description:
This question was about using OOP for a card game.
It required a Card class to store the number and colour of each card.
The program reads card data from a file and allows a player to choose cards without selecting the same card twice.
"""

class Card:
  def__init__(self, num, clr):
    # Paper 4 expects us to show the private attributes and their data types.
    self.__Number = num                 # PRIVATE Number As INTEGER
    self.__Colour = clr                 # PRIVATE Colour As STRING


  # Getter methods because the attributes are private.
  def GetNumber(self):
      return self.__Number
  
  def GetColour(self):
      return self.__Colour


def ChooseCard():
  # selected_cards keeps track of which card positions have already been chosen.
  # num tells us where to store the next selected card in selected_cards.
  global selected_cards, num
  
  
  available = False
  
  # This loop keeps running until the user chooses a card that has not already been selected.
  while not available:
      available = True
      done = False
  
      # This loop makes sure the card number entered is between 1 and 30.
      while not done:
          index = int(input("enter a value between 1 and 30 inclusive"))
          if 31 > index > 0:
              done = True
  
      # Check if this card number has already been chosen before.
      for c in range(30):
          if index == selected_cards[c]:
              available = False
  
      if available:
          # Store the chosen card number so it cannot be chosen again.
          selected_cards[num] = index
          num = num + 1
  
          # The user chooses cards from 1 to 30,
          # but the array indexes are from 0 to 29.
          return index - 1   # user said i need first card but it is stored at index 0


# **MAIN***

# This array will store the 30 Card objects read from the file.

CardArray = [0]*30

try:
  f = open('CardValues.txt', 'r')


  for i in range(30):
      # Each card has two lines in the file:
      # number first, then colour.
      Cnum = int(f.readline().strip())
      Ccolour = f.readline().strip()
  
      # A Card object is created and stored in the array.
      CardArray[i] = Card(Cnum, Ccolour)
  
  f.close()


except IOError:
  print("File does not exist")

selected_cards = [0]*30
# This array stores the card numbers already selected by the player.


num = 0   # num starts from 0 because no cards have been selected yet.

# This creates the player's hand.

Player1 = []*4
# [] * 4 still gives an empty list, then the selected cards are added using append().

# ChooseCard returns the position of a valid card,

# then that Card object is added to Player1.

Player1.append(CardArray[ChooseCard()])
Player1.append(CardArray[ChooseCard()])
Player1.append(CardArray[ChooseCard()])
Player1.append(CardArray[ChooseCard()])


for k in range(4):
  print(Player1[k].GetNumber())
  print(Player1[k].GetColour())
# number and colour of each card chosen by Player 1 is printed
