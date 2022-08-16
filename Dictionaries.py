'''1. Write a program that uses a dictionary to translate the numbers of the days of the week into their names'''

# # Create a dictionary with the days of the week and the corresponding numbers
# days ={
#     1 : "Monday",
#     2 : "Tuesday",
#     3 : "Wednesday",
#     4 : "Thursday",
#     5 : "Friday",
#     6 : "Saturday",
#     7 : "Sunday"
# }
# # Getting number from user and printing corresponding name of the week
# user_choice = int(input("Select the number of the day of the week: "))
# print(f"It is:", days.get(user_choice))



'''2. Write a program that uses the dictionary for calculation
how many times individual characters appear in the given string.'''

# # Defining empty dictionary and asking user to write something.
# string_statistics = {}
# user_input = input("Please write something:\n")
#
# # adding characters to dictionary and creating statistics of occurrence of characters
# for key in user_input:
#     quantity = user_input.count(key)
#     string_statistics[key] = quantity
#
# # showing results
# for key in string_statistics:
#     print(f"Character: {key}, appeared:{string_statistics.get(key)} times!")



'''3. Write a program that will use a dictionary to encode characters using the Caesar cipher
(generally rot-n) for the given shift n.'''

# # Defining empty dictionary, user is providing string for encryption and offset for 'rot-n'
# coded_string = {}
# offset = int(input("Please provide an offset for encryption: \n"))
# message = input("Please write your message: \n").lower()
#
# # Encrypting message where key is original letter and value is encrypted letter:
# for val in message:
#     encryption = ord(val) + offset
#     if 97 <= encryption <= 122:
#         coded_string[val] = chr(encryption)
#     elif encryption > 122:
#         variable_1 = encryption - 122
#         coded_string[val] = chr(96 + variable_1)
#     elif ord(val) == 32:
#         coded_string[val] = " "
#
# # Showing encrypted message
# print("Encrypted message: ")
# for key in message:
#     print("".join(coded_string.get(key)), end="")
#
# # Decryption of message
# print("\n")
# for key, value in coded_string.items():
#     print(f"Letter: {value} means: {key}")



'''4. Write a program that uses a dictionary to encode the given string with the at-bash cipher.'''

# # # Defining empty dictionary, user is providing message for encryption
# coded_message = {}
# message = input("Please write your message: \n").lower()
#
# for val in message:
#     character = ord(val)
#     offset = character - 97
#     coded_message[val] = chr(122 - offset)
#     if ord(val) == 32:
#         coded_message[val] = " "
#
# # Showing encrypted message
# print("Encrypted message: ")
# for key in message:
#     print("".join(coded_message.get(key)), end="")
#
# # Decryption of message
# print("\n")
# for key, value in coded_message.items():
#     print(f"Character: {value} means: {key}")


'''5. Write a program that will encode the given string in the form of the Morse code.'''

# # # Defining dictionary with Morse alphabet. User is providing message for encryption
# morse_alphabet = {'a' : '._',
#                  'b' : '_...',
#                  'c' : '_._.',
#                  'd' : '_..',
#                  'e' : '.',
#                  'f' : '.._.',
#                  'g' : '__.',
#                  'h' : '....',
#                  'i' : '..',
#                  'j' : '.___',
#                  'k' : '_._',
#                  'l' : '._..',
#                  'm' : '__',
#                  'n' : '_.',
#                  'o' : '___',
#                  'p' : '.__.',
#                  'q' : '__._',
#                  'r' : '._.',
#                  's' : '...',
#                  't' : '_',
#                  'u' : '.._',
#                  'v' : '..._',
#                  'w' : '.__',
#                  'x' : '_.._',
#                  'y' : '_.__',
#                  'z' : '__..',
#                  ' ' : '/'
# }
# # Encrypting message to Morse code
# message = input("Please write your message: \n").lower()
# coded_message = []
# for letter in message:
#     value = morse_alphabet.get(letter)
#     coded_message.append(value)
#     if letter not in morse_alphabet:
#         continue
#
# # Showing encrypted message
# print(f"\nYour message in Morse code is: {' '.join(coded_message)}")



'''6. Write a program that will create a new dictionary by replacing keys with values.
Multiple values or those that cannot be keys are not taken into account in the new dictionary.'''

# # Defining original dictionary and new dictionary
# original_dict = {
#     1 : 'orange',
#     2 : 'red',
#     3 : 'green',
#     4 : 'black',
#     5 : 'green'
# }
# new_dict = {}
#
# # Exchange kay and value from original name to new_dict and show results
# for key, values in original_dict.items():
#     if values in new_dict:
#         continue
#     else:
#         new_dict[values] = key
#
# for key, values in new_dict.items():
#     print(f"Key: {key}, Values: {values}")



'''7. Write a program that will create a third dictionary based on two dictionaries, but only with keys,
which do not appear in both dictionaries.'''

# Defining two dictionaries with keys and values and empty new_dict
# first_dict = {
#     1 : 'orange',
#     2 : 'red',
#     3 : 'green',
#     4 : 'black',
#     5 : 'green'
# }
# second_dict = {
#     4 : 'Audi',
#     5 : 'BMW',
#     6 : 'Mercedes',
#     7 : 'Opel',
#     8 : 'KIA'
# }
# new_dict = {}
#
# # Adds keys and their values to a new dictionary, omitting duplicate keys
# for key, value in first_dict.items():
#     new_dict[key] = value
# for key, value in second_dict.items():
#     if key not in new_dict.keys():
#         new_dict[key] = value
#     else:
#         continue
#
# # Showing keys and values in new_dict
# for key, values in new_dict.items():
#     print(f"Key: {key}, Values: {values}")



'''8. Write a program that will create a dictionary with the letters 'A' to 'Z' as keys,
and the ASCII codes of these letters.'''

# # Defining empty dictionary
# ascii_dictionary = {}
#
# # Adding letter from A to Z as key and ASCII code as value corresponding to key
# ascii_counter = 65
# while ascii_counter < 91:
#     ascii_dictionary[chr(ascii_counter)] = ascii_counter
#     ascii_counter += 1
#
# # Showing results
# for key, value in ascii_dictionary.items():
#     print(f"Letter: {key}, has ASCII code: {value}")

'''9. Suggest how you can build a simple database based on dictionaries.
The search should be done using the PESEL number.
For a given PESEL number, we receive information about the name, surname and age.'''

# # Empty dictionary defined
# personal_data = {}
#
# # Getting employee personal data from user and adding them into database
# print("Please provide personal data of employees below:\n")
# active_variable = True
# while active_variable:
#     user_name = input("PLease provide name: ")
#     user_second_name = input("PLease provide second name: ")
#     user_age = int(input("PLease provide age: "))
#     user_pesel =  int(input("PLease provide PESEL number: "))
#
#     personal_data[user_pesel] = {'name': user_name,
#                                  'second name': user_second_name,
#                                  'age' : user_age
#                                  }
#
#     user_continue = input("\tWould you like to continue? (yes / no)").lower()
#     if user_continue == 'no':
#         active_variable = False
#
# # Showing results of personal data based on provided PESEL number
# searched_employee = int(input("\nPlease provide PESEL of employee you looking for: "))
# print(f"\nPESEL: {searched_employee}, is assigned to: {personal_data[searched_employee]}")



'''10. Write a program that will find the key that matches the smallest value in the given dictionary.
We assume that the dictionary values are numbers.'''

# # Defining original dictionary and empty list where values form original_dict will be appended
# dict_values = []
# original_dict = {
#   'orange' : 6,
#   'red' : 2,
#   'green' : 77,
#   'black' : 4,
#   'white' : 9
# }
# # Searching for minimum value
# for key, value in original_dict.items():
#     dict_values.append(value)
#     minimum = min(dict_values)
# print(f"Minimum value is: {minimum}")
#
# # Showing key for minimum value
# for key, value in original_dict.items():
#     if value == minimum:
#         print(f"Key for minimum value is: {key} ")
