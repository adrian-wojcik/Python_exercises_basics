'''WHILE LOOP'''

'''1. Retrieve data from the keyboard until the user enters the number 0.'''

# while int(input("Please provide integer ('0' end teh program): ")) != 0:
#     print("Please provide next integer!")


'''2. Retrieve data from the keyboard until the user enters the number 0.
After entering the number 0, the program displays how many numbers have been given.'''

# user_try = 0
# while int(input("Please provide integer ('0' end teh program): ")) != 0:
#     print("Please provide next integer!")
#     user_try += 1
#
# print(f"Amount of inputted integers: {user_try}.\n")


'''3. Retrieve data from the keyboard until the user enters the number 0.
After entering the number 0, the program displays how many numbers were given and their sum.'''

# user_try = 0
# sum_try = 0
# while True:
#     user_input = int(input("Please provide integer ('0' end teh program): "))
#
#     if user_input != 0:
#         print("Please provide next integer!")
#         user_try += 1
#         sum_try = user_input + sum_try
#     else:
#         break
# print(f"Amount of inputted integers: {user_try}, sum of inputted integers: {sum_try}\n")


'''4. Retrieve data from the keyboard until the user enters the number 0.
After entering the number 0, the program displays how many numbers have been given even numbers,
their sum and how many odd numbers and their sum were given.'''

# user_try_even = 0
# user_try_odd = 0
# sum_odd = 0
# sum_even = 0
#
# while True:
#     user_input = int(input("Please provide integer ('0' end teh program): "))
#
#     if user_input != 0 and user_input % 2 ==0:
#         print("Please provide next integer!")
#         user_try_even += 1
#         sum_even = user_input + sum_even
#     elif user_input != 0 and user_input % 3 ==0:
#         print("Please provide next integer!")
#         user_try_odd += 1
#         sum_odd = user_input + sum_odd
#     else:
#         break
# print(f"Amount of even numbers: {user_try_even} and they sum: {sum_even},"
#       f" amount of odd numbers: {user_try_odd}, and they sum: {sum_odd}.\n")


'''5. Get numbers from the user until the sum of the given numbers is less than 100.
When finished, write down how many numbers were given.'''

# sum_input = 0
# user_try = 0
#
# while sum_input < 100:
#     user_input = int(input("Please provide integer"))
#     sum_input = user_input + sum_input
#     user_try += 1
#
# print(f"User gave: {user_try} integers.")


'''6. Ask the user for the letter "T" or "t".
If the user enters a different character, the program will again ask for the letter 'T' or 't'.'''

# while True:
#     user_input = str(input("Provide letter: t or T \n"))
#
#     if user_input == 't':
#         print("You provided correct letter")
#         break
#     elif user_input == 'T':
#         print("You provided correct letter")
#         break
#     else:
#         print("\tWrong letter!!!")
#         continue


'''7. Ask the user for an integer, and then write its numbers on the following lines.'''

# user_input = str(input("Please provide integer:"))
#
# offset = 0
# while offset != len(user_input):
#      output_1 = user_input[offset]
#      offset += 1
#      print(output_1)


'''8. Write a program using random numbers to guess numbers 1-100.
The computer randomizes the number and asks the user to guess.
If the user enters a smaller number, the computer should display the message "Too small".
If we give too high a number, the computer will write "Too Big".
After guessing, the computer should display how many tries we needed to give the correct number.'''

# import random
#
# python_choice = random.randint(0,100)
# turns = 0
# while True:
#      user_imput = int(input("Guess the Python number - 1 to 100 ;)\n"))
#
#      if user_imput < python_choice:
#           turns += 1
#           print(f"Python number is greater than {user_input}, try again!")
#      elif user_imput > python_choice:
#           turns += 1
#           print(f"Python number is less than {user_input}, try again!")
#      elif user_imput == python_choice:
#           turns += 1
#           print(f"Well done, you guessed the python number! Number of tries: {turns}")


'''9. For the given integer, count the sum of its digits'''

# user_input = input("Please provide integer: ")
#
# digit_sum = 0
# for digit in user_input:
#     digit = int(digit)
#     digit_sum += digit
# print(f"The sum of your digits is equal to: {digit_sum})


'''10. The user enters a natural number N.
If N is even, divides it by 2, if odd, multiplies by 3 and adds 1.
Then it repeats this procedure for the newly obtained number.
The program runs as long as the result is different from 1.
List how many activities have been performed until the end of the program.'''

# user_input = int(input("Enter a natural number (0 to 9) \n"))
#
# variable_1 = 0
# turns = 0
# while user_input != 1:
#     if user_input % 2 == 0:
#         user_input = user_input / 2
#         turns += 1
#     elif user_input % 3 == 0:
#         user_input = user_input * 3 + 1
#         turns += 1
#     else:
#         pass
#
# print(f"Number of actions performed by the program: {turns}")


'''11. Imagine you are in a dark tunnel and can only move in one position
left or right. From the "start" point, the tunnel ends after four moves to the right or three to the left.
Write a program that asks the user to enter the direction (L or R)
and repeats this procedure until the user reaches the end of the tunnel.
When finished, the program prints the information how many times we went left and how many times to the right.
After each move, the program draws a "map" in the form: - - - * - - - - where "-" means the tunnel, and '*' 
means the current position.'''

# turns_l = 3
# turns_p = 4
#
# while turns_l != 0 and turns_p != 0:
#     user_input = input("Enter the direction: L or R \n").lower()
#     if user_input == "l":
#         turns_l -= 1
#         map = str((f"{'-' * turns_l}*{'-' * turns_p}"))
#         print(map)
#     elif user_input == "p":
#         turns_p -= 1
#         map = str((f"{'-' * turns_l}*{'-' * turns_p}"))
#         print(map)


'''12. Expand the program in guessing numbers (task 8) so that the computer plays with itself.
Use an algorithm in which guessing consists in drawing a number between 1-100,
a "brute force" algorithm that checks the numbers from 1 to 100 sequentially, 
an algorithm that corresponds to a human game
(i.e. we take into account that the number was too small or too large 
and we narrow down the range from which we draw)
and an algorithm in which we always select a number in the half of the current range (the closest integer)'''

# import random
#
# python_choice = random.randint(0, 100)
# turns = 0
# range_start = 0
# range_end = 100
#
# while True:
#     python_guess = random.choice(range(range_start, range_end))
#     print(python_guess)
#
#     if python_choice < python_guess:
#         turns += 1
#         range_end = python_guess
#     elif python_choice > python_guess:
#         turns += 1
#         range_start = python_guess
#     elif python_guess == python_choice:
#         turns += 1
#         print(f"Well done, you guessed the python number: {python_choice}! Number of tries: {turns}")
#         break

'''
13. Write a program that will simulate a currency exchange office.
The program should display the current Euro and Dollar exchange rates for both buy and sell.
It should ask if we want to buy or sell, what currency and amount.
As a result, we will receive information about how much we have to pay or how much we will receive.
'''

# print("Buy rate EUR/USD: 0.90")
# print("Sell rate EUR/USD: 1.10")
#
# eur_usd = 0.90
# usd_eur = 1.10
# while True:
#     user_input_SB = input("Do you want to 'buy' or 'sell'?\n").casefold()
#     user_input_currency = input("What currency?\n").casefold()
#     user_input_amount = float(input("What amount?\n"))
#
# # The client wants to buy:
#     if user_input_SB == "buy":
#         # The client wants to buy EUR
#         if user_input_currency == "eur":
#             result = user_input_amount * eur_usd
#             print("Amount to pay:", user_input_amount, f"The amount you will receive: {result}")
#             break
#         #The client wants to buy USD
#         elif user_input_currency == "usd":
#             result = user_input_amount * usd_eur
#             print("Amount to pay:", user_input_amount, f"The amount you will receive: {result}")
#             break
# # The client wants to sell:
#     elif user_input_SB == "sell":
#         # The client wants to sell EUR
#         if user_input_currency == "eur":
#             result = user_input_amount * usd_eur
#             print("Amount to pay:", user_input_amount, f"The amount you will receive: {result}")
#             break
#         # The client wants to sell EUR
#         elif user_input_currency == "usd":
#             result = user_input_amount * eur_usd
#             print("Amount to pay:", user_input_amount, f"The amount you will receive: {result}")
#             break


'''
14. Write a program that finds the least common multiple of two user-specified numbers.
Use the "brute force" algorithm, which it will check for successive multiples of a smaller number
or is it also a multiple of a greater number.
'''

# # User input of two integers
# user_input_1 = int(input("Please provide integer"))
# user_input_2 = int(input("Please provide integer"))
#
# # Calculating LCM using a "flag" with the value 0 to check the next integer with each loop::
#
# least_common_multiple = 0
# turns = 100
# while turns > 0:
#     least_common_multiple += 1
#     turns -= 1
#     if least_common_multiple % user_input_1 == 0 and least_common_multiple % user_input_2 == 0:
#         print(f"Number: {least_common_multiple} is a common multiple"
#               f"integers: {user_input_1} and {user_input_2}\n")
#     else:
#         print(f"Number: {least_common_multiple} is not a common multiple"
#               f" integers: {user_input_1} and {user_input_2}")
#
# # Brute force algorithm
# # Specify a smaller number (it is necessary to 'pass' otherwise the function will stop on these conditions)
#
# if user_input_2 > user_input_1:
#     lower_number = user_input_1
#     bigger_number = user_input_2
#     pass
# elif user_input_2 < user_input_1:
#     lower_number = user_input_2
#     bigger_number = user_input_1
#     pass
#
# # Brute force algorithm (I used the name 'smallest w.w' again, but it's just a simple multiple!
#
# while turns > 0:
#     least_common_multiple += lower_number
#     if least_common_multiple % bigger_number == 0:
#         turns -= 1
#         print(f"\tSUCCESS!!! Number: {least_common_multiple} is a common multiple"
#               f" integers: {lower_number} and {bigger_number}\n")
#     elif least_common_multiple % bigger_number != 0:
#         turns -= 1
#         print(f"NUmber: {least_common_multiple} is not a common multiple"
#               f" integers: {lower_number} and {bigger_number}")
#     else:
#         break


'''
15. Write a program that will find the first and last digits of the given number and calculate their sum.
'''

# # Calling a number from the user - the number should start with a string!
# user_input = input("Please provide number: \n")
#
# # Convert a string to an integer value specifying the first digit and the last - FORM STRING
# first_integer = int(user_input[0])
# last_integer = int(user_input[-1])
#
# offset = 0
# sum = first_integer + last_integer
# print(f"\tThe sum of the first and last digit entered by the user is:", sum)


"""LOOPS FOR!!!"""

'''
1. for loop and range1 statement. Get the number n i from the keyboard
display all integers from 0 to n on the screen.
'''

# user_input = int(input("Please provide number:"))
#
# for integer in range(0, user_input+1):
#     print(integer)


'''2. Get three integers from the keyboard: start, end, step
and write on the screen all the integers from start to end every step.
For example, for start = 1, end = 10, step = 3, the program prints: 1, 4, 7, 10'''

# start = int(input("Please provide integer 'start':\n"))
# end = int(input("Please provide integer 'end':\n"))
# step = int(input("Please provide integer 'step':\n"))
#
# for integer in range(start, end + 1, step):
#     print(integer)


'''3. As in task 2, but if start is greater than end
the program prints the numbers from end to start with a "" negative "step.
So for start = 10, end = 1, step = 3 the result is: 10, 7, 4, 1'''

# start = int(input("Please provide integer 'start':\n"))
# end = int(input("Please provide integer 'end':\n"))
# step = int(input("Please provide integer 'step':\n"))
#
# # Regular case
# if start > end:
#     end_2 = start + 1
#     start_2 = end
#     for integer in reversed(range(start_2, end_2, step)):
#         print(integer)
# # The case where start is greater than end
# else:
#     end_2 = end + 1
#     start_2 = start
#     for integer in range(start_2, end_2, step):
#         print(integer)


'''
4. For the given integer n, calculate the sum 1 + 2 + 3 + (...) + n
'''

# user_input = int(input("Please provide integer 'start':\n"))
#
# flag_1 = 0
# for integer in range(1, user_input + 1):
#     sum = integer + flag_1
#     flag_1 += integer
#     print(sum)


'''5. For the given integer n, calculate the sum in the form: 1 - 2 + 3 - 4 + 5 - 6 + .... + n'''

# user_input = int(input("Please provide integer 'start':\n"))

# flaga_1 = 0
# for integer in range(1, user_input + 1):
#     if integer % 2 == 0:
#         sum = flaga_1 - integer
#         flaga_1 += integer
#         print(sum)
#     elif integer % 3 == 0 or integer == 1:
#         sum = flaga_1 + integer
#         flaga_1 += integer
#         print(sum)


'''6. Write a program which for the given range of numbers (a, b)
will find the sum of numbers divisible by k. Parameters a, b and k are given by the user.'''

# start_range = int(input("Please provide integer 'start':\n"))
# end_range = int(input("Please provide integer 'end':\n"))
# divider = int(input("Please provide integer 'divider':\n"))
#
# flag_1 = 0
# for integer in range(start_range, end_range + 1):
#     if integer % divider == 0:
#         sum = integer + flag_1
#         flag_1 += integer
#     else:
#         pass
# print(f"\tThe sum of numbers divisible by: {divider}:", sum)


'''7. We count the sum of the numbers 1 + 2 + 3 + 4 until the result is equal to or the last less than the given number n.
As a result, the program should output the last number added
for which the sum is still <= the number n and the calculated sum.
For example, for the given n = 10, the result is: last 4, sum 10.'''

# user_input = int(input("Enter an integer:\n"))

# We create two flags: one to create the sum and the other to determine the last added number which will be the
# number from the last loop (during which the sum exceeded n) subtract the value of this number (to get the 'last')

# flag_1 = 0
# turn = 0
# for integer in range(1, user_input):
#     sum = integer + flag_1
#     flag_1 += integer
#     turn += 1
#
#     if sum > user_input:
#         sum -= integer
#         turn -= 1
#         print(f"For the given n = {user_input} the result is: {turn}, sum: {sum}")
#         break
#     elif sum == user_input:
#         print(f"For the given n = {user_input} the result is: {turn}, sum: {sum}")
#         break
#     else:
#         pass


'''8. Calculate 1 * 2 * 3 * 4 * ... * n for the given n. Watch out for large numbers !!!'''

# user_input = int(input("Please provide integer:\n"))
#
# product = 1
# for integer in range(1, user_input + 1):
#     product *= integer
#     print(product)


'''9. Find all divisors of the given number n and calculate their sum.'''

# user_input = int(input("Please provide integer:\n"))
#
# flag_1 = 0
# for integer in range(1, user_input + 1):
#     if user_input % integer == 0:
#         sum = integer + flag_1
#         flag_1 += integer
#         print(f"Divider: {integer}, sum: {sum}")
#     else:
#         pass


'''10. Check that the given number n is a prime number.'''

# while True:
#     user_input = int(input("Please provide integer greater than 1:\n"))
#     if user_input <= 1:
#         print("Wrong number!")
#     else:
#         break
#
# for integer in range(1, user_input):
#     if user_input % integer == 0 and integer != 1 and integer != user_input:
#         print(f"Number {user_input}, is not a prime number")
#         break
# else:
#     print(f"Number {user_input}, is a prime number")


'''11. For the given number n, write 01010101 on the screen, where all zeros and ones are n.
For example, for n = 5 the result is 01010'''

# # The commutative property of multiplication by a negative number should be used
# # to obtain the commutative effect of each loop
# user_input = int(input("Please provide integer:\n"))
#
# flag_1 = 1
# for integer in range(1, user_input + 1):
#     flag_1 = flag_1 * -1
#     if flag_1 == -1:
#         print("0")
#     elif flag_1 == 1:
#         print("1")


'''12. For given number n display "square" z *, for example for n = 4
     ****
     ****
     ****
     ****
    '''

# user_input = int(input("Please provide integer:\n"))
#
# flag_1 = 0
# for integer in range(0, user_input):
#     square = user_input * "*"
#     print(square)


'''13. For the given number n display the following figure on the screen (example for n = 4):
     *
     **
     ***
     ****'''

# # Range must start with 1, because for 0 times '*' will give empty output
# user_input = int(input("Please provide integer:\n"))
#
# for integer in range(1, user_input):
#     element = integer * "*"
#     print(element)


'''14.For the given number n display the following figure on the screen (example for n = 4)
    1
    12
    123
    1234'''

# user_input = int(input("Please provide integer:\n"))
#
# for integer in range(1, user_input + 1):
#     for element in range(1, integer + 1):
#         print(element, end="")
#     print()

# The second print here is responsible for printing the numbers one by one instead of one line
# The end separator causes the numbers to be printed side by side on each line instead of matching each other and spaced apart
# between the lines (ask the lecturers about it)
# in the second rank is up to +1 to increase because for the number 1 the element will be 2


'''15. For the given number n display the following figure on the screen (example for n = 4)
     1
     22
     333
     4444'''

# user_input = int(input("Please provide integer:\n"))
#
# flag_1 = 1
# for integer in range(1, user_input + 1):
#     integer = str(integer)
#     element = flag_1 * integer
#     print(element)
#     flag_1 += 1

'''16. For the given number n display the following figure on the screen (example for n = 4)
        *
       **
      ***
     ****
'''

# user_input = int(input("Please provide integer:\n"))
#
# excision = user_input
# for integer in range(1, user_input + 1):
#     excision -= 1
#     character = "*" * integer
#     print(f"{' ' * excision}",character)


'''17. Draw for the given number n (example for n = 7)
	*******
	**    *
	* *   *
	*  *  *
	*   * *	
	*    **
	*******
'''

# user_input = int(input("Please provide integer:\n"))
#
# flag_l = user_input - 3
# flag_r = 0
# excision = " "
# for integer in range(1, user_input + 1):
#     if integer == 1 or integer == user_input:
#         print("*" * user_input)
#     else:
#         print("*"f"{flag_r * excision}{'*'}{flag_l * excision}""*")
#         flag_l -= 1
#         flag_r += 1

'''18. For the given number n, draw a chessboard with zeros and ones (e.g. for n = 6):
	010101
	101010
	010101
	101010
	010101
	101010
'''

# user_input = int(input("Please provide integer:\n"))
#
# flag_1 = user_input // 2
# for integer in range(1, user_input + 1):
#     if integer % 2 == 0:
#         print("01" * flag_1)
#     else:
#         print("10" * flag_1)


'''19. Find all primes in the range 2 to n, where n is given by the user.'''

# user_input = int(input("Please provide integer:\n"))
#
# for integer in range(2, user_input + 1):
#     if integer == 2 or integer == 3 or integer % 2 != 0 and integer %3 != 0 and integer %5 != 0:
#         print(f"\t{integer}, is an prime number!!!")
#     else:
#         print(f"{integer},  is not an prime number")


'''20. For the given number n, calculate the sum: 1 + 22 + 333 + 4444 + + nnnnnn and write all its words on the screen.
For example, for n = 5 the result is 1 + 22 + 333 + 4444 + 5555 = 60355'''

# user_input = int(input("Please provide integer:\n"))
#
# sum = 0
# for integer in range(1, user_input + 1):
#     for element in range(1, integer + 1):
#         print(element, end="")
#         sum += integer
#     print()
# print(f"Sum amount is: {sum}")
