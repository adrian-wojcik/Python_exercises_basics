'''1. Get 10 numbers from the user, write them on the screen and calculate their sum and average'''

# #It is creating empty list for user numbers and variable "counter" for taking only 10 inputs.
# user_integers = []
# counter = 0
#
# #It retrieves and save user numbers
# while counter < 10:
#     user_input = int(input("Please provide the number: "))
#     counter += 1
#     user_integers.append(user_input)
#
# #It sums up, calculates the average and displays the result
# element_sum = sum(user_integers)
# element_average = element_sum / counter
# print(f'Numbers you provide are: {user_integers}\n'
#       f'Sum of these numbers is: {element_sum}\n'
#       f'Average of these numbers is: {element_average}\n')


'''2. Ask the user to enter numbers from the keyboard until he types 0.
After you finish entering the numbers, display them on the screen,
then find the smallest and largest number that was given.'''


# active_variable = True
# user_numbers = []
#
# #Getting number from user till he/she provide '0' and print all inputs.
# while active_variable:
#     user_input = int(input("Please provide the number: "))
#     if user_input == 0:
#         active_variable = False
#     else:
#         user_numbers.append(user_input)
#
# #Showing all user numbers with minimum and maximum value.
# print(f"\nNumbers you provide ar: {user_numbers} \n"
#       f"Your smallest number is: {min(user_numbers)}\n"
#       f"Your biggest number is: {max(user_numbers)}\n")



'''3. On the basis of the given list (e.g. random numbers) create a new list,
which will be created by shifting the list elements to the right by n positions.
Items "dropping" from the list on the right go into it on the left.
For example, for [1, 2, 3, 4, 5] and n = 2 the result is [4, 5, 1, 2, 3]'''

# import random
#
# #Providing offset and list length by user. Two empty list for operation defined.
# offset = int(input("Please provide offset (for example: 2): "))
# list_length = int(input("How many numbers would you like (for example: 5): "))
# first_list = []
# new_list = []
#
# # Creating 5 random numbers and append them into 'first_list'.
# counter = 0
# while counter < list_length:
#     first_list.append(random.randint(0,10))
#     counter += 1
# print(f"\nRandom numbers: {first_list}")
#
# # Slicing 'first_list' and offsetting last numbers to the start of list.
# new_list = first_list[-offset : ]
# slice_2 = first_list[0 : len(first_list) - offset]
# new_list.extend(slice_2)
#
# # Showing result of above operation
# print(f"New number order based on your offset is: {new_list}")



'''4. Write a program that will arrange the numbers in the given list from lowest to highest.
Write the sorting algorithm yourself.'''

# import random
#
# # User is deciding how much numbers put into the list. Two empty lists for operation defined.
# list_length = int(input("How many numbers would you like (for example: 5): "))
# first_list = []
# new_list = []
#
# # Providing randomly selected numbers into the 'first_list'
# counter = 0
# while counter < list_length:
#     first_list.append(random.randint(0,9))
#     counter += 1
# print(f"\nRandom numbers: {first_list}")
#
# # Using algorythm to sort the list in ascending order.
# active_variable = True
# while active_variable:
#     minimum_index = first_list.index(min(first_list))
#     smallest_number = first_list.pop(minimum_index)
#     new_list.append(smallest_number)
#
#     if len(first_list) == 0:
#         active_variable = False
#
# print(f"\nNumbers sorted from lowest to highest: {new_list}")


'''5. Write a program that will create a new list based on the given string of characters,
in such a way that no character appears twice in the list.'''



# # # User is providing string. Two empty lists for operation defined.
# user_input = input("Please write something: ")
# first_list = []
# new_list = []
#
# # Creating a list from user string.
# for val in user_input:
#     first_list.append(val)
#
# # Removing multiplied letters from user string
# for val in first_list:
#     if val not in new_list:
#         new_list.append(val)
# print(new_list)




'''6. Write a program that checks if the two given lists have exactly the same elements'''

# # User is providing two string. Two empty lists for operation defined.
# list_1 = []
# list_2 = []
# user_string_1 = input("Please provide first string of 5  characters: ")
# user_string_2 = input("\nPlease provide second string of 5  characters: ")
#
# # Elements from user string append into both empty lists.
# for val in user_string_1:
#     list_1.append(val)
# for val in user_string_2:
#     list_2.append(val)
#
# # Both lists are being sort.
# list_1.sort()
# list_2.sort()
#
# # Both list are being compared.
# if list_2 == list_1:
#     print("Both list have the same characters")
# else:
#     print("Both list do not have the same characters")



'''7. Write a program that for the given string of characters (we assume only lowercase letters of the Latin alphabet)
will calculate the statistics of the occurrence of letters.'''

# # User is providing two string. Two empty lists for operation defined.
# list_1 = []
# user_string = input("Please provide the string of characters: ").lower()
#
# # Elements from user string append into empty list.
# for val in user_string:
#     list_1.append(val)
#
# # Creating statistics of characters in string.
# for val in list_1:
#     characters_count = list_1.count(val)
#     print(f"There is: {characters_count} characters: {val} in your string!")



'''8. Write a program that for two lists will generate a third list consisting of elements,
which do not appear in both lists at the same time.'''

# # User is providing two string. Three empty lists for operation defined.
# list_1 = []
# list_2 = []
# list_3 = []
# user_string_1 = input("Please provide first string of characters: ")
# user_string_2 = input("\nPlease provide second string of characters: ")
#
# # Elements from user string append into both empty lists.
# for val in user_string_1:
#     list_1.append(val)
# for val in user_string_2:
#     list_2.append(val)
#
# # Comparison of two list in order to find duplicated characters.
# if len(list_1) > len(list_2):
#     for val in list_1:
#         if val not in list_2:
#             list_3.append(val)
#         else:
#             continue
# else:
#     for val in list_2:
#         if val not in list_1:
#             list_3.append(val)
#         else:
#             continue
#
# print(f"\nCharacters which do not duplicate in both strings: {', '.join(list_3)}")



'''9. Write a program that finds prime numbers to n (user supplied)
Eratosthenes sieve method (see eg Wikipedia).'''

# # User is providing number. Empty lists for operation defined.
# list_1 = []
# user_input = int(input("Please enter the number to look for prime numbers: "))
#
# # Looking for all pride numbers in range chosen by user.
# for val in range(4, user_input):
#     if val % 2 == 0 or val % 3 == 0 or val % 5 == 0:
#         continue
#     else:
#         val = str(val)
#         list_1.append(val)
#
# print(f"Prime numbers to numner: {user_input}, are: {', '.join(list_1)}")




'''10. Write a program that "shuffles" the data in list.'''

# # User is providing string of characters. Empty list for operation defined.
# import random
# list_1 = []
# user_string = input("Please provide string of charakters: ")
#
# # Shuffling data with random function and printing result.
# for val in user_string:
#     random_index = random.randint(0, len(user_string))
#     list_1.insert(random_index, val)
#
# print(f"\nList after shuffling data: {''.join(list_1)}")




'''11. Write a program that will return random elements from the given list, without repetition,
as long as there are still elements that were not selected'''

# # User is providing string of characters which will be added to empty list.
# import random
#
# list_1 = []
# new_list = []
# user_string = input("Please provide string of charakters: ")
# for val in user_string:
#     list_1.append(val)
#
# # Randomly select element from list and print it without duplicates.
# for i in range(0, len(user_string)):
#     random_index = random.randint(0, len(list_1) - 1)
#     selected_character = list_1.pop(random_index)
#
#     if selected_character not in new_list:
#         new_list.append(selected_character)
#         print(", ".join(new_list))
#     else:
#         continue
#
# print("END")



'''12. Suppose we have a list with different data. On its basis, create a separate list with only integers,
a list with only floating point numbers, and a third list with the rest of the elements.'''

# # Defining one list with various data and 3 empty lists.
# various_data_list = ['Hello', 4, 5.758, 'bike', 3.14, 78, 20, '%']
# integer_list = []
# float_list = []
# other_list = []
#
# # Assigning items to individual lists based on the type of value
# for val in various_data_list:
#     if type(val) == int:
#         integer_list.append(val)
#     elif type(val) == float:
#         float_list.append(val)
#     else:
#         other_list.append(val)
#
# # Showing results of assignment
# print(f"Integers: {integer_list}\n")
# print(f"Float: {float_list}\n")
# print(f"other: {other_list}\n")



'''13. Find the two largest numbers in the given list.'''

# # Defining list with numbers and one empty list.
# numbers_list = [-10, 5.55, 88, 3.14, 0, 100, 150, 8.999]
# new_list =[]
#
# # Finding two biggest numbers from number_list
# for val in numbers_list:
#     biggest_number = max(numbers_list)
#     idx = numbers_list.index(biggest_number)
#     popped_number = numbers_list.pop(idx)
#     new_list.append(popped_number)
#     if len(new_list) == 2:
#         break
#
# # Showing results:
# print(f"\nTwo the biggest numbers in list are: {new_list}")




'''14. In the following list, find the two values with the smallest difference between them.'''

# # Defining 3 list with numbers: one with numbers to substract, second with substractors
# # (same numbers but without first one) and one empty list for differences.
# numbers_list = [-10, 5.55, 88, 3.14, 0, 100, 150, 8.999]
# difference_list = []
# subtractors_list = numbers_list[1:]
#
# # Sorting 'number_list' in order to make subtraction
# numbers_list.sort()
# numbers_list = numbers_list[::-1]
#
# # Getting all differences between numbers and appending them into list 'difference_list'
# counter = 1
# for digit in numbers_list:
#     for subtractors_digit in subtractors_list:
#         difference = digit - subtractors_digit
#         # Removing used subtractor digit in order to not repeat first digit
#         subtractors_list.remove(subtractors_digit)
#         counter += 1
#         difference_list.append(difference)
#         break
#
# # Showing list with differences and getting the smallest difference with it index
# print(difference_list)
# smallest_difference = min(difference_list)
# smallest_index = difference_list.index(smallest_difference)
#
# # Printing results:
# print(f"\nThe smallest difference is {smallest_difference},"
#       f"and it is between numbers {numbers_list[smallest_index]} "
#       f"and {numbers_list[smallest_index + 1]}")



'''15. Suppose we have an n-element list of numbers in the range <0, k>.
Write a program that will count the number of times each number appears in this list
(i.e. a histogram of the occurrence of numbers).'''

# # Defining list with numbers and one empty list.
# numbers_list = [-10, 5, 88, 3, 0, 100, 150, 88, 5]
#
# # Calculation of the amount of repeated numbers and showing statistics.
# for val in numbers_list:
#     count = numbers_list.count(val)
#     print(f"Number {val} occurs {count} times in list!")



'''16. Create a two-dimensional list with dimensions n x m, where n and m are provided by the user. 
The elements of the list are to be zeros.'''

# import numpy as np
#
# # Providing height and width of matrix by user
# user_input_height = int(input("Please provide height of the list: "))
# user_input_width = int(input("Please provide width of the list: "))
#
# # Creating lists into list by using generator in generator and show results:
# new_list = np.array([[0 for val in range(user_input_width)] for val_2 in range(user_input_height)])
#
# print(new_list)


'''17. For a two-dimensional list n x n (n is given by the user)
filled with random numbers calculate the sum of the elements on the diagonals.'''

# import numpy as np
# import random as rd
# # Providing height and width of matrix by user by parameter 'n':
# user_input = int(input("Please provide parameter for height and width of matrix: "))
#
# # Creating lists into list by using generator in generator and show results:
# matrix = np.array([[random.randint(0,9) for val in range(user_input)] for val_2 in range(user_input)])
# print(f"\n{matrix}")
#
# # setting up variables and empty lists for below operations.
# variable_1 = 0
# variable_2 = -1
# matrix_length = len(matrix)
# diagonal_1 = []
# diagonal_2 = []
#
# # Preparing lists with only diagonal numbers in order to sum them.
# while variable_1 < matrix_length:
#     element_1 = matrix[variable_1, variable_1]
#     element_2 = matrix[variable_1, variable_2]
#
#     diagonal_1.append(element_1)
#     diagonal_2.append(element_2)
#
#     variable_2 -= 1
#     variable_1 += 1
#
# # Printing results of diagonal sum.
# elements_sum = sum(diagonal_1)
# elements_sum_2 = sum(diagonal_2)
# print(f"\nSum of elements in first diagonal is equal: {elements_sum}"
#       f"\nSum of elements in second diagonal is equal: {elements_sum_2}")

