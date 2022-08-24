'''1. Write the Person class which has the fields "first_name", "last_name", "born_date", "gender", "pesel",
which represent, respectively: name, surname, date of birth, gender and PESEL number.
  The constructor takes the first name, last name, date of birth (as a string in the form YYYY-MM-DD) and gender.
  The pesel number is generated for the given data in the constructor (see wikipedia - PESEL).
  Name and surname, no matter how it is given, is to be "remembered"
  as words that start with a capital letter and all other characters are lower case letters.
  The constructor should validate the date (use the datetime !!!)
  and the gender as "female" or "male". The PESEL field should be a private field,
  not changeable and read-only. Add a method that returns the current age of the person due to
  today's date (see datetime.date.today)'''

import random as rd
import datetime as time

class Person():

    def __init__(self, first_name, last_name, born_date, gender):
        self.first_name = str(first_name).title()
        self.last_name = str(last_name).title()
        self.born_date = str(born_date)
        self.gender = str(gender).lower()
        self.__pesel = None

    def create_pesel(self):
        """Create pesel number from object data"""
        born_date = self.born_date
        gender = self.gender

        # Create pesel number

        year_of_birth = born_date[2:4]
        month_of_birth = born_date[4:6]
        day_of_birth = born_date[6:8]

        # Gender coding
        if gender == 'male':
            gender_number = str(rd.choice([1, 3, 5, 7, 9]))
        if gender == 'women':
            gender_number = str(rd.choice([0, 2, 4, 6, 8]))

        # Serial number coding:
        serial_number = str(rd.randint(100, 999))

        # pesel without serial number
        pesel_without_control_number = \
            str(year_of_birth + month_of_birth + day_of_birth + serial_number + gender_number)

        # Calculation of the control number
        control_sum = []
        wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        for number in pesel_without_control_number:
            number = int(number)
            wage = wages.pop(0)
            control_sum.append(wage * number)
        control_sum = str(sum(control_sum))

        control_number = 10 - int(control_sum[-1:])
        if control_number == 10:
            control_number = 0

        # Showing PESEL number:
        pesel = (f"{year_of_birth}{month_of_birth}{day_of_birth}{serial_number}{gender_number}{control_number}")
        print(f"Your PESEL numebr is: {pesel}")
        self.__pesel = pesel
        return pesel

    def remember_full_name(self):
        full_name = [self.first_name, self.last_name]
        print(" ".join(full_name))
        return full_name

    def check_date(self):
        try:
            date = time.datetime.strptime(self.born_date, '%Y%m%d')
            print(f"Wprowadzona data: '{date}' urodzenia jest poprawna!")
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYYMMDD")
#
# # Showing the attributes of the Person class for a given instance
# maciek = Person('maciek','swies', 19970514, 'male')
# Person.create_pesel(maciek)
# Person.remember_full_name(maciek)
# Person.check_date(maciek)


'''2. Create a Card class representing a card that has two fields - suit and value.
If the constructor is called with no parameters (Card ()) then a random card will be created,
if the constructor is called with the Card parameters ("diamonds", "A") - the Ace of diamonds card will be created.
  In case of giving a wrong color or value, the "Value Error" exception should be returned.
  Both fields of the card should be private, and their values should be read by the @property decorator'''

import random as rd

class Card:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=rd.choice(suits), value=rd.choice(values)):
        self.__suit = suit
        self.__value = value

    @property  # getter
    def my_suit(self):
        return self.__suit

    @my_suit.setter
    def my_suit(self, suit):
        suit = str(suit).title()
        try:
            if suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
                self.__suit = suit
            else:
                raise ValueError
        except ValueError:
            print("Incorrectly defined suit of the card!!!")

    @property
    def my_value(self):
        return self.__value

    @my_value.setter
    def my_value(self, value):
        value = str(value).title()
        try:
            if value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                self.__value = value
            else:
                raise ValueError
        except ValueError:
            print("Incorrectly defined value of the card!!!")

    def __str__(self):
        return f"Your card is: {self.__value} of {self.__suit}"





'''3. Create a CardDeck class to represent the deck of cards. The class should have "size" fields,
which will contain information on how many cards are currently in the deck, and cards,
which is a list of objects of the class Card (see task 2). The constructor takes one value
- the number of cards in the deck (24 or 52) and on its basis creates objects of the Card class, memorizing them in the "cards" field.
Both size and cards fields must be private fields with appropriate access methods.
The CardDeck class should have a "shuffle" method that will shuffle the cards
(i.e. randomly rearranging objects in the cards list) and the draw () method,
which will "draw" a card from the deck - it means that the last item from the "cards" list
will be returned by this method (and removed from the card deck, the size field will change accordingly).'''


class CardDeck(Card):

    def __init__(self, suit=None, value=None, size=24):
        super().__init__(suit, value)
        self.__size = size
        self.__cards = []

        for suit in self.suits:
            for value in self.values:
                self.__cards.append(f"{value} of {suit}")
        rd.shuffle(self.__cards)
        self.__cards = self.__cards[0:24]

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, user_size):
        if user_size == 52:
            self.__size = user_size
            for suit in self.suits:
                for value in self.values:
                    self.__cards.append(f"{value} of {suit}")
            rd.shuffle(self.__cards)
        else:
            print("Size of deck can be 24 or 52!!! ")

    def show_deck(self):
        return f"My deck of cards is: {' | '.join(self.__cards)}"

    def shuffle(self):
        rd.shuffle(self.__cards)
        return self.__cards

    def draw(self):
        drown_card = self.__cards.pop()
        self.__size -= 1
        return f"Size of deck after drawing card: {self.__size}, you card: {drown_card}"


# my_cards = CardDeck()
#
# my_cards.size = 52
# print(my_cards.show_deck())
#
# my_cards.shuffle()
# print(my_cards.show_deck())
#
# print(my_cards.draw())


'''4. Based on the class from point 3, design your CardHand class to represent the player's cards
- should contain information about how many cards we have, a list with cards, add_card method,
which will add a card to the player's cards (note - assume that it is the bottom of the deck by default) 
and the "draw_card" method, which will draw a player's card (by default, the last one). 
Use points 2, 3 and 4 to write a method, who will deal the cards to the n-players, 
where n is the method parameter.'''

import random as rd

class CardHand:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, size=0):
        self.size = size
        self.cards = []
        if size > 52:
            self.size = 52
        if size < 0:
            self.size = 0

        for suit in self.suits:
            for value in self.values:
                self.cards.append(f"{value} of {suit}")
        rd.shuffle(self.cards)
        self.cards = self.cards[0: self.size]

    def __str__(self):
        if self.size == 0:
            return "You do not have cards to play"
        else:
            return f"You have: {self.size} cards. Let's play!!!"

    def show_deck(self):
        return " | ".join(self.cards)

    def add_card(self, suit, value):
        suit = str(suit).title()
        try:
            if suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Incorrectly defined suit of the card!!!")
        value = str(value).title()
        try:
            if value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Incorrectly defined value of the card!!!")

        if len(self.cards) == 52:
            print(f"There is maximum amount of cards in deck")
        else:
            card = f"{value} of {suit}"
            if card not in self.cards:
                self.cards.append(card)
                self.size += 1

    def draw_card(self):
        card = self.cards.pop()
        return card

    def deal_the_cards(self, amounts_of_players):
        try:
            if amounts_of_players > 1:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Number of players should be greater than 1!")
            exit()

        # Creating list of players
        players = {}
        for number in range(1, amounts_of_players + 1):
            player = f"Player #{number}"
            players[player] = []

        print(players)

        while len(self.cards) > 0:
            for player in players:
                if len(self.cards) == 0:
                    break
                for card in self.cards:
                    self.cards.remove(card)
                    players[player].append(card)
                    break

        for key, value in players.items():
            print(f"Player: {key} have: {value}")


karty_adriana = CardHand(13)
print(karty_adriana.show_deck())
print(karty_adriana.deal_the_cards(3))



'''5. Use points 2, 3, 4 to write a card game of your choice (the easiest way to play is war or blackjack)'''

