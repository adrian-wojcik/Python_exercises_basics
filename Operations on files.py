'''1. Write a program that will do a statistics on the occurrence of letters in the given text file.
Let's count the number of occurrences of only letters of the Latin alphabet, and we are not case-sensitive
(that is, sign a and A, are the same sign). Then save the result to a file named "Exercise 1.txt".
Sample output file:
     a - 100
     b - 34
     c - 87
     (e.t.c)'''

# # Open file 'Exercise 1" with name 'statistic_file"
# with open("Exercise 1.txt") as statistic_file:
#
#     # Creating empty dictionary statistic and read every single character, then putting into list "data"
#     statistics = {}
#     data = statistic_file.read()
#     characters = list(data)
#     data = data.lower()
#
#     "Creating statistics of characters and adding to dictionary"
#     for letter in characters:
#         if "a" <= letter <= "z":
#             if letter in statistics:
#                 statistics[letter] = statistics[letter] + 1
#             else:
#                 statistics[letter] = 1
#
#     # Showing results
#     for key, value in statistics.items():
#         print(f"Letter {key} appeared: {value} times ")
import random

'''2. Write a program that will do statistics on the occurrence of words in a text file.
By a word we mean any string of characters separated by at least one space from the rest of the string.
Save the result to a new text file named "Exercise 2.txt"'''

# # Open .txt file and append all characters ass elements in list
# with open("Exercise 1.txt") as word_statistics:
#     statistics = {}
#
#     words = list(word_statistics.read())
#
#     # Extracting characters that are not latin alphabet letters
#     for character in words:
#         if "a" < character < "z" or "A" < character < "Z" or character == " ":
#             continue
#         else:
#             words.remove(character)
#
#     # Creating statistics of (words are created as slices from the list 'word'
#     counter = 0
#     start_counter = 0
#     for character in words:
#         if character == " ":
#             word = "".join(words[start_counter:counter])
#             start_counter = counter + 1
#             if word in statistics:
#                 statistics[word] = statistics[word] + 1
#             else:
#                 statistics[word] = 1
#             counter += 1
#         else:
#             counter += 1
#
# # Saving results to selected .txt file 'Exercise 2'
# with open("Exercise 2.txt", "w", encoding="utf-8") as show_statistics:
#     for key, value in statistics.items():
#         show_statistics.write(f"Word '{key}' appeared: {value} times\n")



'''3. Write a program that will copy its content to a new file for a given text file,
but so that each word will start with a capital letter.'''

# # Open file with text
# with open("Exercise 3.txt") as start_file:
#
#     # change the letter in each word to uppercase
#     words = []
#     for line in start_file:
#         line = line.title()
#         words.append(line)
#     print(words)
#
# # Save result to new text file
# with open("Exercise 3 - result.txt", "w") as result_file:
#     result_file.write("".join(words))



'''4. Write a program that for the given text file and the given two characters,
will copy this file so that the characters in the new file will be interchanged with each other.'''

# # Open file with two characters
# with open("Exercise 4.txt") as start_file:
#
#     # reordering two characters in text file
#     characters = list(start_file.read())
#     characters = characters[::-1]
#     print(characters)
#
# # Save result to new text file
# with open("Exercise 4 - result.txt", "w") as result_file:
#     result_file.write("".join(characters))


'''5. Write a program that will download a text file and encrypt it with the at_bash algorithm (see wikipedia).
The encrypted message is saved in a new file.
We only encrypt letters of the Latin alphabet and distinguish between upper and lower case letters.'''

# with open("Exercise 5.txt") as unencrypted_file:
#
#     characters = list(unencrypted_file.read())
#     coded_characters = []
#     for element in characters:
#         element = ord(element)
#         if 97 <= element <= 122:
#             element = chr(122 - (element - 97))
#             coded_characters.append(element)
#         elif 65 <= element <= 90:
#             element = chr(90 - (element - 65))
#             coded_characters.append(element)
#         else:
#             element = chr(element)
#             coded_characters.append(element)
#     print(coded_characters)
#
# with open("Exercise 5 - result.txt", "w") as result_file:
#     result_file.write("".join(coded_characters))


'''6. Write a program that for the given text file
will copy it to a new file from the end (character by character).'''

# with open("Exercise 6.txt") as start_file:
#     content = start_file.read()
#
# with open("Exercise 6.txt - result.txt", "a") as result_file:
#     result_file.write(content)

'''7. Suppose we have a text file in which each line consists of an English word (sentence),
a semicolon and a sentence equivalent in Polish, e.g .:

    dog; pies
    cat; kot
    green; zielony
    red; czerwony 
    look for; szukac
    look after; opiekowac sie
      
  Write a program that reads all lines and then conducts a vocabulary test.
  The words are to be chosen randomly without repetition. Each line should appear twice 
  (in the test, not in the file!)
   We ignore case and trailing white space when checking for responses
   and the beginning of the word (s) to be translated. After finished "game" to the file named "results"
   we add a line in the form: date, filename_with_vords, correct_polish, correct_po_english'''

# import random as rd
# import datetime as data
#
# with open("Exercise 7.txt") as english_vocabulary:
#
#     # function to return key for any value in dictionary
#     def get_key(val):
#         for key, value in guess.items():
#             if val == value:
#                 return key
#
#         return "key doesn't exist"
#
#     # Defining list for getting lines from open txt file
#     # and one dictionary for getting words from and putting into list in order to not repeat
#     words = []
#     guess = {}
#     already_guessed = []
#
#     # Creating two counters variables for correct answers and changing lines form txt. file to
#     # list 'word'
#     correct_polish = 0
#     correct_english = 0
#     for line in english_vocabulary:
#         line = line.split("; ")
#         words.append(line)
#     # print(words)
#
#     # From list 'words' creating dictionary for better accessing words in both languages
#     for line_2 in words:
#         guess[line_2.pop(0)] = line_2.pop(1).rstrip("\n")
#     # print(guess)
#
#     # The proper body of the program:
#     # First - randomly choose words in English (keys) and asking for provide same word in Polish (values)
#     # Second - randomly choose words in Polish (values) and asking for provide same word in English (keys)
#     counter = 0
#     while counter < 1:
#
#         if counter == 0:
#             while len(already_guessed) < len(words):
#                 word = rd.choice(list(guess.keys()))
#                 word = "".join(word)
#
#                 if word not in already_guessed:
#                     user_answer = input(f"please write: <{word}> in Polish:\n").lower().strip()
#
#                     if user_answer == guess.get(word):
#                         correct_polish += 1
#                         already_guessed.append(word)
#                     else:
#                         already_guessed.append(word)
#                 else:
#                     continue
#             counter += 1
#
#         print(f"\n Okey, lets switch language!")
#         already_guessed.clear()
#         if counter == 1:
#             while len(already_guessed) < len(words):
#                 word = rd.choice(list(guess.values()))
#                 word = "".join(word)
#
#                 if word not in already_guessed:
#                     user_answer = input(f"please write: <{word}> in English:\n").lower().strip()
#
#                     if user_answer == str(get_key(word)):
#                         correct_english += 1
#                         already_guessed.append(word)
#                     else:
#                         already_guessed.append(word)
#                 else:
#                     continue
#
# # Providing summary of user result into txt. file 'Exercise 7 - result'
# with open("Exercise 7 - results.txt", "w") as result_file:
#     result_file.write(f"{data.date.today()}"
#                       f", {'Excercise 7'},"
#                       f", you guessed {correct_polish}/{len(guess)} words in polish"
#                       f", you guessed {correct_english}/{len(guess)} words in english")



'''8. Let's assume that for testing we need to generate a file with birthdates,
gender and social security number. Each line is separate data. See how the PESEL number is created
(wikipedia) and write a program that generates the above data.'''


def create_pesel():
    """Creating number PESEL for given year, month and day and gender"""
    import random as rd
    year_of_birth = input("Please provide your year of birth: ")
    month_of_birth = input("Please provide your month of birth: ")
    day_of_birth = input("Please provide your day of birth: ")
    gender = input("Please provide your gender: ").lower()

    # month coding based on year of birth
    if int(year_of_birth) in range(1899, 1999):
        if len(month_of_birth) < 2:
            month_of_birth = ("0" + month_of_birth)

    if int(year_of_birth) in range(1999, 2099):
        if len(month_of_birth) < 2:
            month_of_birth = ("2" + month_of_birth)
        elif len(month_of_birth) == 2 and month_of_birth[0:1] == '0':
            month_of_birth = ("2" + month_of_birth[-1:])
        elif len(month_of_birth) == 2:
            month_of_birth = ("3" + month_of_birth[-1:])


    # Gender and day number coding
    if len(day_of_birth) < 2:
        day_of_birth = ("0" + day_of_birth)
    if gender == 'male':
        gender_number = str(rd.choice([1, 3, 5, 7, 9]))
    if gender == 'women':
        gender_number = str(rd.choice([0, 2, 4, 6, 8]))

    # Year, serial number coding:
    serial_number = str(rd.randint(100, 999))
    year_of_birth = year_of_birth[-2:]

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

    # Saving results to file
    with open("Exercise 8.txt", "a") as result_file:

        result_file.write(f"Born date: {day_of_birth}.{month_of_birth}.{year_of_birth}\n"
                          f"Gender: {gender}\n"
                          f"PESEL: {pesel}\n")

create_pesel()


'''9. Write a program that will read the file from the previous task and check the correctness of the PESEL number'''


# with open("Exercise 8.txt") as check_data:
#
#
#     """checks if the provided PESEL number is correct"""
#     # Getting PESEl from check_data
#     pesels_to_check = []
#     for line in check_data:
#         line = line.rstrip("\n")
#         if line[:5] == "PESEL":
#             pesels_to_check.append(line[-11:])
#     print(pesels_to_check)
#
#     # CHacking pesels numbers one by one
#     for pesel in pesels_to_check:
#
#         # Calculation of the control number
#         control_sum = []
#         wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
#         for number in pesel:
#             number = int(number)
#             wage = wages.pop(0)
#             control_sum.append(wage * number)
#         control_sum = str(sum(control_sum))
#
#         # If control number is 0, that means that PESEL is correct
#         control_number = int(control_sum[-1:])
#         if control_number == 0:
#             print(f"PESEL {pesel} is correct ")
#         else:
#             print(f"PESEL {pesel} is incorrect! ")


'''10. Write a program that will find the longest word in the given text file.'''

# with open("Exercise 10.txt") as sentance:
#     length_of_words = []
#     the_longest_words = []
#
#     # Getting words from txt. file
#     for line in sentance:
#         words = line.split(" ")
#
#     # Looking for lenght of longest word
#     for word in words:
#         length = len(word)
#         length_of_words.append(length)
#         longest_word = max(length_of_words)
#
#     # Getting all words with the highest number of characters
#     for word in words:
#         if len(word) == longest_word:
#             the_longest_words.append(word)
#
#     #Showing results
#     print(f"The longest word with {max(length_of_words)} characters is/are: {', '.join(the_longest_words)}")

