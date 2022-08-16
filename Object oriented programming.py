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

# import random as rd
# import datetime as time
#
# class Person():
#
#     def __init__(self, first_name, last_name, born_date, gender):
#         self.first_name = str(first_name).title()
#         self.last_name = str(last_name).title()
#         self.born_date = str(born_date)
#         self.gender = str(gender).lower()
#         self.__pesel = None
#
#     def create_pesel(self):
#         """Create pesel number from object data"""
#         born_date = self.born_date
#         gender = self.gender
#
#         # Create pesel number
#
#         year_of_birth = born_date[2:4]
#         month_of_birth = born_date[4:6]
#         day_of_birth = born_date[6:8]
#
#         # Gender coding
#         if gender == 'male':
#             gender_number = str(rd.choice([1, 3, 5, 7, 9]))
#         if gender == 'women':
#             gender_number = str(rd.choice([0, 2, 4, 6, 8]))
#
#         # Serial number coding:
#         serial_number = str(rd.randint(100, 999))
#
#         # pesel without serial number
#         pesel_without_control_number = \
#             str(year_of_birth + month_of_birth + day_of_birth + serial_number + gender_number)
#
#         # Calculation of the control number
#         control_sum = []
#         wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
#         for number in pesel_without_control_number:
#             number = int(number)
#             wage = wages.pop(0)
#             control_sum.append(wage * number)
#         control_sum = str(sum(control_sum))
#
#         control_number = 10 - int(control_sum[-1:])
#         if control_number == 10:
#             control_number = 0
#
#         # Showing PESEL number:
#         pesel = (f"{year_of_birth}{month_of_birth}{day_of_birth}{serial_number}{gender_number}{control_number}")
#         print(f"Your PESEL numebr is: {pesel}")
#         self.__pesel = pesel
#         return pesel
#
#     def remember_full_name(self):
#         full_name = [self.first_name, self.last_name]
#         print(" ".join(full_name))
#         return full_name
#
#     def check_date(self):
#         try:
#             date = time.datetime.strptime(self.born_date, '%Y%m%d')
#             print(f"Wprowadzona data: '{date}' urodzenia jest poprawna!")
#         except ValueError:
#             raise ValueError("Incorrect data format, should be YYYYMMDD")
#
# # Showing the attributes of the Person class for a given instance
# maciek = Person('maciek','swies', 19970514, 'male')
# Person.create_pesel(maciek)
# Person.remember_full_name(maciek)
# Person.check_date(maciek)


'''2. Stwórz klasę Card reprezentująca kartę, która ma dwa pola - suit (kolor) oraz value (wartość). 
Jeżeli konstruktor zostanie wywołany bez parametrów (Card() ) to zostanie utworzona losowa karta, 
jeżeli konstruktor zostanie wywołany z parametrami Card("karo", "A") - to zostanie utworzona karta As karo.
 W przypadku podania błędnego koloru lub wartości powinien zostać zwrócony wyjątek "Value Error". 
 Oba pola karty powinny być prywatne, a odczyt ich wartości powinien być zrealizowany przez dekorator @property'''

import random as rd


class Card():
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


# my_card.my_suit = "maciek"
# my_card.my_value = "adrian"
# print(my_card)


'''3. Utwórz klasę CardDeck reprezentującą talię kart. Klasa powinna mieć pola "size", 
które będzie zawierało informację ile kart jest aktualnie w talii, oraz cards, 
które jest listą obiektów klasy Card (patrz zadanie 2). Konstruktor przyjmuje jedną wartość 
- liczbę kart w talii (24 lub 52) i na jej podstawie tworzy obiekty klasy Card zapamiętując je w polu "cards". 
Oba pola - size i cards muszą być polami prywatnymi z odpowiednimi metodami dostępowymi. 
Klasa CardDeck powinna  mieć metody "shuffle", która spowoduje potasowanie kart 
(czyli losowe poprzestawianie obiektów w liście cards) oraz metodę draw(), 
która "wyciągnie" kartę z talii - to znaczy, że ostatni obieket z listy "cards" 
zostanie zwrócony przez tę metodę (i usunięty z talii kart, odpowiednio zmieni się też wartość pola size).'''


class CardDeck(Card):

    def __init__(self, size=24):
        super().__init__()
        self.__size = size
        self.__cards = []

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, user_size):
        if user_size == 52:
            self.__size = 52
            self.__cards = self.__cards.append(f"{self.my_suit} of {self.my_value}")
        else:
            self.__size = 24
            print("Size of deck can be 24 or 52!!! ")
        print(self.size)

        while True:
            cards_temporary = []
            card = f"{self.my_suit} of {self.my_value}"
            if card not in cards_temporary:
                cards_temporary.append(card)
            if len(cards_temporary) == user_size:
                self.__cards = cards_temporary
                break

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self):
        while True:
            cards_temporary = []
            card = f"{self.my_suit} of {self.my_value}"
            if card not in cards_temporary:
                cards_temporary.append(card)
            if len(cards_temporary) == self.__size:
                self.__cards.extend(cards_temporary)
                break

    def shuffle(self):
        return rd.shuffle(self.__cards)

    def draw(self):
        drown_card = self.__cards.pop()
        self.__size -= 1
        return self.__size, drown_card

    def karty(self):
        print(f"{self.my_suit} of {self.my_value}")


my_card = CardDeck(52)
size = my_card.size
talia = my_card.cards
print(size)
print(talia)


