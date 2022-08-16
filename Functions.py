'''1. Write a function that returns information to the given integer (True or False)
whether the number is even.'''


# def even_number(number):
#     """checks if the number is even and show True or False"""
#     try:
#         number = int(number)
#     except ValueError:
#         print(f"{number} is not integer!")
#
#     if number % 2 == 0:
#         print(bool(1))
#     else:
#         print(bool(0))
#
# even_number(4)
# even_number(5)
import random

'''2. Write a function that will find the minimum value in the list given as an argument.'''

# def minimmum_value(list):
#     """Finding minimmum value from given list"""
#     print(f"Minimmum value from given list is: {min(list)}")
#
# list = [2, 4, -10, 7]
# minimmum_value(list)



'''3. Write a function that will find the maximum value in the list given as the call argument.'''

# def maximum_value(list):
#     """Finding maximum value from given list"""
#     print(f"Maximum value from given list is: {max(list)}")
#
# list = [9999, 75, 0, 8]
# maximum_value(list)



'''4. Write a function that returns the average value of the value in the list 
given as the argument of the function call.'''

# def average_value(list):
#     import statistics as st
#     """Finding average value from given list"""
#     print(f"Average value from given list is: {st.mean(list)}")
#
# list = [10, 20, 30, 40]
# average_value(list)



'''5. Write a function that checks if the given string is a palindrome'''

# def palindrom(string):
#     """Checking if given string is a palindrome"""
#     if string[::-1] == string:
#         print(f"Given string is palindrome!")
#     else:
#         print(f"Given string is not palindrome!")
#
# palindrom('kajak')
# palindrom('python')




'''6. Write a function that will return a list with prime numbers in the range 2-n,
where n is the function invocation parameter.'''

# def prime_numbers(n):
#     """Return all prime numbers from 2 to n - given parameter"""
#     list_of_prime_numbers = []
#     for val in range(1, n + 1):
#         if val % 2 != 0 and val % 3 != 0 and val % 5 != 0 and val % 7 != 0:
#             list_of_prime_numbers.append(val)
#         if val == 3 or val == 5 or val == 7:
#             list_of_prime_numbers.append(val)
#         else:
#             continue
#     print(f"Prime numbers to number: {n}, are {list_of_prime_numbers}")
#
# prime_numbers(100)



'''7. Write a function that will return the index of the first occurrence of a character in a given string.
If the sign is absent, the function returns -1.'''

# def first_index(string, character):
#     """Showing first index of given character in string,
#     if no character in string - showing '-1' """
#     string = str(string)
#     if character not in string:
#         print(-1)
#     else:
#         idx = string.index(character)
#         print(f"First index of character: {character} is {idx}")
#
# first_index('adrian', 'd')
# first_index('adrian', 'u')



'''8. Write a function that will return a list of indexes of all occurrences of the given character 
in the given string. If the character is absent, the function returns an empty list.'''

# def list_of_indexes(string, character):
#     """Return list of indexes all appearances of given character,
#     if there is no character in string - returns empty list"""
#     index_list = []
#     counter = -1
#     for element in string:
#         counter += 1
#         if element == character:
#             index_list.append(counter)
#         else:
#             continue
#     print(index_list)
#
# list_of_indexes('adrian', 'a')
# list_of_indexes('adrian', 'u')



'''9. Write a program (using the function),
which will represent the given number as the product of prime numbers.'''

# def multiply_prime_numbers(number):
#     """Showing given number as the product of prime numbers."""
#     list_multiply = []
#     number = int(number)
#     while number > 1:
#         if number % 2 == 0:
#             list_multiply.append("2")
#             number = number // 2
#             continue
#         elif number % 3 == 0:
#             list_multiply.append("3")
#             number = number // 3
#             continue
#         elif number % 5 == 0:
#             list_multiply.append("5")
#             number = number // 5
#             continue
#         elif number % 7 == 0:
#             list_multiply.append("7")
#             number = number // 7
#             continue
#         elif number % number == 0:
#             list_multiply.append(str(number))
#             number = 1
#     print(f"Given number can be written asn pruduct of prime numbers:\n{' * '.join(list_multiply)}")
#
# multiply_prime_numbers(16)
# multiply_prime_numbers(1280)
# multiply_prime_numbers(99.999)
# multiply_prime_numbers(228)



'''10. Write a function that takes two lists as arguments and returns a new list consisting of elements,
which appear in both lists.'''

# def merge_lists(list_1, list_2):
#     """merging two given list and return one merged list"""
#     new_list = []
#     new_list.extend(list_1)
#     new_list.extend(list_2)
#     print(new_list)
#
# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
# merge_lists(list_1, list_2)



'''11. Write a function that for the given numbers n, a, b will return an n-element list,
whose elements are random (integers) from a to b.'''

# def random_numbers_list(n, a, b):
#     """returns a list of n elements in the range a to b"""
#     import random as rd
#     lis_of_numbers = []
#     for i in range(n):
#         number = random.randint(a, b)
#         lis_of_numbers.append(str(number))
#
#     print(f"Randomly choose numbers from given range are: {', '.join(lis_of_numbers)}")
#
# random_numbers_list(5,0,10)



'''12. Write a function that takes two dictionaries and checks if they are the same.
We assume that two dictionaries are the same if they have the same keys and corresponding values.'''

# def compering_two_dictionaries(dict_1, dict_2):
#     """Compering two dictionaries with each other - need to have same keys and corresponding values"""
#     for key in dict_1:
#         if dict_1.get(key) == dict_2.get(key):
#             message = ""
#         else:
#             message = "NOT"
#             break
#     print(f"Dictionaries: \n{dict_1} and \n{dict_2} \nare {message} the same!")
#
# dictionary_1 = {
#     1 : 'orange',
#     2 : 'red',
#     3 : 'green',
#     4 : 'black',
#     5 : 'green'
# }
# dictionary_2 = {
#     2 : 'red',
#     5 : 'green',
#     3 : 'green',
#     4 : 'black',
#     1 : 'orange',
# }
# compering_two_dictionaries(dictionary_1, dictionary_2)


'''13. Write a function that will generate a PESEL number for the given year of birth, month, day and gender
(see Wikipedia - PESEL numbers)'''

# def create_pesel():
#     """Creating number PESEL for given year, month and day and gender"""
#     import random as rd
#     year_of_birth = input("Please provide your year of birth: ")
#     month_of_birth = input("Please provide your month of birth: ")
#     day_of_birth = input("Please provide your day of birth: ")
#     gender = input("Please provide your gender: ").lower()
#
#     # month coding based on year of birth
#     if int(year_of_birth) in range(1899, 1999):
#         if len(month_of_birth) < 2:
#             month_of_birth = ("0" + month_of_birth)
#
#     if int(year_of_birth) in range(1999, 2099):
#         if len(month_of_birth) < 2:
#             month_of_birth = ("2" + month_of_birth)
#         elif len(month_of_birth) == 2 and month_of_birth[0:1] == '0':
#             month_of_birth = ("2" + month_of_birth[-1:])
#         elif len(month_of_birth) == 2:
#             month_of_birth = ("3" + month_of_birth[-1:])
#
#
#     # Gender and day number coding
#     if len(day_of_birth) < 2:
#         day_of_birth = ("0" + day_of_birth)
#     if gender == 'male':
#         gender_number = str(rd.choice([1, 3, 5, 7, 9]))
#     if gender == 'women':
#         gender_number = str(rd.choice([0, 2, 4, 6, 8]))
#
#     # Year, serial number coding:
#     serial_number = str(rd.randint(100, 999))
#     year_of_birth = year_of_birth[-2:]
#
#     pesel_without_control_number = \
#         str(year_of_birth + month_of_birth + day_of_birth + serial_number + gender_number)
#
#     # Calculation of the control number
#     control_sum = []
#     wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
#     for number in pesel_without_control_number:
#         number = int(number)
#         wage = wages.pop(0)
#         control_sum.append(wage * number)
#     control_sum = str(sum(control_sum))
#
#     control_number = 10 - int(control_sum[-1:])
#     if control_number == 10:
#         control_number = 0
#
#     # Showing PESEL number:
#     print(f"Your PESEL numebr is: "
#           f"{year_of_birth}{month_of_birth}{day_of_birth}{serial_number}{gender_number}{control_number}")
#
# create_pesel()


'''14. Write a function that will check if the given PESEL number is correct.'''

# def correct_pesel():
#     """checks if the provided PESEL number is correct"""
#     pesel = input("Please provide your PESEL number: ").lower()
#
#     # Calculation of the control number
#     control_sum = []
#     wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
#     for number in pesel:
#         number = int(number)
#         wage = wages.pop(0)
#         control_sum.append(wage * number)
#     control_sum = str(sum(control_sum))
#
#     # If control number is 0, that means that PESEL is correct
#     control_number = int(control_sum[-1:])
#     if control_number == 0:
#         print(f"PESEL {pesel} is correct ")
#     else:
#         print(f"PESEL {pesel} is incorrect! ")
#
# correct_pesel()



'''15. Write a function that converts an integer to binary and returns it as a string.
We assume that the numbers are only positive.'''


# def integer_to_bytes(number):
#     """Changing integer to binary code and return as string"""
#     byte_number = bin(number)
#     print(byte_number)
#     return byte_number
#
#
# integer_to_bytes(9)



'''16. Write a function that takes a string representing an integer in binary
and convert it to a decimal number.
By default, the number is positive, but the function can take the second parameter (sign),
which determines if we have the sign bit.
'''

# def binary_to_decimal(number, sign=""):
#     """Converts a number in binary to the decimal system including sign"""
#     if sign == "-":
#         number = int(sign + number, 2)
#     else:
#         number = int(number, 2)
#     print(number)
#
# binary_to_decimal("-0b111")
# binary_to_decimal("0b111")




'''17. Write a function that converts an integer to its binary representation including sign.'''

# def integer_to_binary(number, sign=''):
#     """Converts a number from integer to binary system including sign"""
#     if sign == "-":
#         number = bin(sign + number)
#     else:
#         number = bin(number)
#     print(number)
#
# integer_to_binary(7)
# integer_to_binary(-7)



'''18. Write a function that will check if all the parentheses in the given string are correct.
For example, "((12asdas) (sdsd (sdsd) (sdsdsd)))" is correct, but "(sdsd (sdf))) (sdf)" is invalid.'''

# def correct_parantheses(string: str):
#     """check if all the parentheses in the given string are correct"""
#     left_parantheses = string.count("(")
#     right_parantheses = string.count(")")
#     if left_parantheses == right_parantheses:
#         print("The sequence of parentheses is valid")
#     else:
#         print("The sequence of parentheses is NOT valid!!!")
#
#
# correct_parantheses('((12asdas)(sdsd(sdsd)(sdsdsd)))')
# correct_parantheses("(sdsd(sdf)))(sdf)")


'''19. Write a function that creates a string of random numbers to represent the numbers in the sudoku game
in the form of 81 consecutive digits (starting from the upper left corner, move right to the end of the line,
then another, another, etc.). The function should print these numbers in the standard "sudoku" fashion.'''

# def sudoku_shape():
#     """Creating sudoku shape from random numbers"""
#     import random as rd
#     numbers = []
#     counter = 1
#
#     # Creating numbers and adding to list 'number'
#     while counter <= 81:
#         number = random.randint(0,9)
#         numbers.append(number)
#         counter += 1
#     print("\n")
#
#     # Showing result
#     counter_2 = 1
#     for number in numbers:
#         print(number, end=" ")
#         if counter_2 % 9 == 0:
#             print("")
#         counter_2 += 1
#
# sudoku_shape()

'''20. Napisz program, który pobierze w postaci stringu wszystkie kolejne liczby z rozwiązanego sudoku
(81 cyfr począwszy od lewego górnego rogu) i sprawdzi czy rozwiązanie jest poprawne.'''

# def sudoku_correctness_check():






'''21. Write a function that takes two integers and checks if they both contain the same digits
in the same amount, but not necessarily in the same order'''

# def same_digits_and_quantity(number_1, number_2):
#     """Check if in bout numbers there is digit with same quantity"""
#     number_1 = str(number_1)
#     number_2 = str(number_2)
#     used_digits = []
#
#     for digit in number_1:
#         if digit in number_2:
#             if number_1.count(digit) == number_2.count(digit) and digit not in used_digits:
#                 print(f"Digit {digit} occurs in both numbers: {number_1.count(digit)} times!")
#                 used_digits.append(digit)
#             else:
#                 continue
#         else:
#             continue
#
# same_digits_and_quantity(122345678999, 1225999)
