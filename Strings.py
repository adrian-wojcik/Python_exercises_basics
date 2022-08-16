# The following tasks should be performed first without using the methods defined on the string class,
# and then using them and compare the complexity of the programs.

'''1. Write a program that takes a string from the user and creates a new string based on it
  in which all lowercase letters have been converted to uppercase.'''

# user_input = input("Write something: \n").upper()
# print(user_input)



'''
2. Write a program that takes a string of characters from the user, and then counts how many letters there are in it,
numbers and other characters.
'''

# amount_of_letters = 0
# amounts_of_numbers = 0
# amounts_of_other_characters = 0
#
# for character in input("Write something: \n").lower():
#     if 48 <= ord(character) <= 57:
#         amounts_of_numbers += 1
#     elif 97 <= ord(character) <= 122:
#         amount_of_letters += 1
#     else:
#         amounts_of_other_characters += 1
#
# print(f"In your string there is: {amount_of_letters} letters, {amounts_of_numbers} numbers, "
#       f"{amounts_of_other_characters} other characters")


'''
3. Write a program that checks if the given string can be converted into an integer.
'''

# user_input = input("Write something: \n")
#
# try:
#     if type(int(user_input)) == int:
#         print("String can be converted into an integer")
# except ValueError:
#         print("String can NOT be converted into an integer")

'''
4. Write a program that will check if the given string can be converted into a real number.
'''

# user_input = input("Write something: \n")
#
# try:
#     if type(float(user_input)) == float:
#         print("String can be converted into real number")
# except ValueError:
#     print("String can NOT be converted into real number")


'''
5. Write a program that will take the string and create a new string by reversing it.
For example, for the string "abc" the result is "cba"
'''

# user_input = input("Write something:")[::-1]
# print(user_input)

'''
6. Write a program that takes a string of characters and then substitutes every two adjacent characters in it.
For example, for the string "abcde" the result will be "badce".
'''

# user_input = input("Write something: \n")
#
# new_string = []
# flag = 0
# active = True
#
# while active:
#     pair = user_input[flag: flag + 2]
#     pair = pair[::-1]
#     print(pair)
#     new_string.append(pair)
#     flag += 2
#
#     if flag >= len(user_input):
#         active = False
#
# print("".join(new_string))



"""7. Write a program that will create a new string that will contain it based on the given string
only Latin letters."""


# user_input = input("Write something: \n").lower()
# new_string = []
#
# for character in user_input:
#     if 97 <= ord(character) <= 122:
#         new_string.append(character)
#     else:
#         continue
#
# print("".join(new_string).title())






"""8. Write a program that will take the string and the character we want to find in that string.
The program should calculate the number of times a given character has occurred."""


# user_input = input("Write something: \n").lower()
# user_choice = input("What character do you want to find: \n").lower()
#
# counter = user_input.count(user_choice)
#
# print(f"\tIn string: {user_input}, character: '{user_choice}', appeared: {counter} times!")





''' 
9. Write a program that takes a string, then a character to search and a character to replace.
The program should create a new string from characters in which it will replace the appropriate characters.
For example, for the sequence "abcade" letters "a" and "z" the result is the sequence "zbczde""
'''

# user_input_1 = input("Write something: \n").lower()
# user_input_2 = input("What character do you want to replace: \n")
# user_input_3 = input("What character do you want to replace it with: \n")
#
#
# new_string = user_input_1.replace(user_input_2, user_input_3)
# print(new_string)




'''10. Write a program that will download a string from the user,
and then, on its basis, it will create a new string of characters in which any adjacent repetitions of 
characters will be removed. For example, for the string "abbcddeffaa" the result is "abcdefa"'''

# user_input = input("Write something: \n").lower()
# new_string = []
#
# for character in user_input:
#     if character not in new_string and character != " ":
#         new_string.append(character)
#     else:
#         continue
# print("".join(new_string))




'''11. Write a program that takes two strings and creates a new string
by alternately copying letters from the given strings.
For example, for the strings "abcde" and "1234", the result is "a1b2c3d4e".
If one string is shorter than the other, we just copy the remaining characters.'''

# user_input_1 = input("Provide first string: \n")
# user_input_2 = input("Provide second string: \n")
#
# new_string = []
# counter = 1
#
# for letter in user_input_1:
#     new_string.append(letter)
# for letter in user_input_2:
#     new_string.insert(counter, letter)
#     counter += 2
#
# print("".join(new_string))


'''12. Write a program that takes two strings and checks if one can be made of the other
by rearranging the characters. All characters must be used.'''

# # Retrieve both words from the user
# user_input_1 = input("Provide first string: \n")
# user_input_2 = input("Provide second string: \n")
#
# # Define empty lists in which we will put individual characters of both words
# first_string = []
# second_string = []
#
# # Adds words to lists
# for character in user_input_1:
#     first_string.append(character)
# for character in user_input_2:
#     second_string.append(character)
#
# # We sort both lists for comparison
# first_string.sort()
# second_string.sort()
#
# # Display the result of comparing both words (list)
# if first_string == second_string:
#     print("You can make the same word from both strings")
# else:
#     print("You can NOT make the same words from both strings")




'''13. Write a program that will retrieve a string and on its basis create a new string,
in which each uppercase letter will be changed to lowercase and lowercase to uppercase.'''

# user_input = input("Write something: \n")
# new_string = []
#
# for character in user_input:
#
#     if 65 <= ord(character) <= 90:
#         new_string.append(character.lower())
#     elif 97 <= ord(character) <= 122:
#         new_string.append(character.upper())
#     else:
#         new_string.append(character)
# print("".join(new_string))




'''14. Rot-n encoding. The rot-n encoding consists in replacing every letter of the alphabet
to a letter n positions away from it to the right. Of course the letters
which "go" beyond the alphabet, we replace with the appropriate letter from the beginning of the alphabet.
For example, for n = 1, the letter a will turn into b, the letter b into c, c into d, etc.
Z becomes 'a'. For n = 2 we have: a-> c, b-> d, c-> e, y-> a, z-> b.
Write a program that will take a string from the user and a number n to specify the offset
and will generate an encoded string. We assume that only Latin letters are encoded.'''

# user_input = input("Write something: \n")
# offset = int(input("Enter a NUMBER to shift rot-n: \n"))
#
# coded_word = []
#
# for character in user_input:
#
#     if 97 <= ord(character) <= 122:
#         character = ord(character) + offset
#         new_character = chr(character)
#
#         if character > 122:
#             new_line = character - 122
#             character = chr(new_line + 96)
#             coded_word.append(character)
#             continue
#
#         coded_word.append(new_character)
#     else:
#         pass
#
# print(f"Your code word is: {''.join(coded_word)}")




'''15. at-bash encoding. The at-basch encoding is where we replace letters on a principle
first to last, second to penultimate, third to third from last etc. that is a-> z, b-> y, c-> x.
Write a program that will take a string from the user and encode it with the "at-bash" algorithm.
We assume that we encode only letters of the Latin alphabet.'''

# user_input = input("Napisz cos: \n")
# coded_sentence = []
#
# for letter in user_input:
#     offset = ord(letter) - 97
#     new_letter = chr(122 - offset)
#     coded_sentence.append(new_letter)
#
# print(f"The code word is: {''.join(coded_sentence)}")



'''16. Write a program that takes a string and then changes the first letter of each word to uppercase.
We assume that the words are separated by spaces.'''


# user_input = input("Write something: \n")
# print(user_input.title())



'''17. Write a program that takes two strings and then creates a new string,
which will consist of characters that appear in one or the other string, but not both.'''

# user_input_1 = input("Write something: \n")
# user_input_2 = input("Write something: \n")
#
# new_string = []
#
# for letter in user_input_1:
#     if letter in user_input_2:
#         pass
#     else:
#         new_string.append(letter)
#
# for letter in user_input_2:
#     if letter in user_input_1:
#         pass
#     else:
#         new_string.append(letter)

# print(f"New string is: {''.join(new_string)}")




'''18. Write a program that will count all the vowels in the given string.'''

# user_input_1 = input("Write something: \n").lower()
# counter = 0
# vowel = ["a", "e", "i", "o", "u", "y"]
#
# for letter in user_input_1:
#     if letter in vowel:
#         counter += 1
#     else:
#         pass
# print(f"In your string is: {counter} vowels!")
