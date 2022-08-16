'''WARM UP'''

'''1. Take the real number from the keyboard and write the rounded integer on the screen.
For example, for 3.2 the result is 3, for 3.5 the result is 4'''

# user_choice = float(input("Please provide a real number: "))
#
# print(int(round(user_choice, 0)))


'''2. Retrieve a real number from the keyboard and write its whole part and decimal part on the screen.
Have you noticed anything strange? Check the result for different cases.'''

# user_choice = float(input("Please provide a real number: "))
# flag_1 = (int(user_choice))
#
# print(flag_1)
# print(f"{user_choice - flag_1}")


'''3. Ask the user about the year of birth and on this basis calculate his current age (in year).'''

# from datetime import date
# year = int(input("Enter your year of birth: "))
#
# current_year = date.today().year
# print(f"Your age is: {current_year - year}")


'''4. Ask the user for the year and month (as integers) and then how many months they want to add to the given date.
Write a new date (year and month)'''

# year = int(input("Please enter any year: "))
# month = int(input("Please enter any month: "))
# insert_month = int(input("How many month would you add?: "))
#
# # Specification of the month after addition in three main variants:
# # 1. no change in the year 2. change for the next year 3. change for an unlimited number of years
# if month + insert_month <= 12:
#     new_month = month + insert_month
#     print(year, new_month, sep=" month: ")
# elif 12 < month + insert_month <= 24:
#     new_month = (month + insert_month - 12)
#     print(year + 1, new_month, sep=" month: ")
# elif month + insert_month > 24:
#     new_month = ((month + insert_month) % 12)
#     if new_month == 0:
#         new_month = 1
#     year = year + ((month + insert_month - 1) // 12)
#     print(year, new_month, sep=" month: ")


'''5. Ask the user how old he is, and then calculate the birth date,
the year in which he / she turns 18 and the year in which he / she will be 100 years old.'''

# from datetime import date
# age = int(input("Ile masz lat rocznikowo: "))
#
# if age < 0:
#     raise Exception("Wiek nie moze byc liczba ujemna")
#
# current_year = date.today().year
#
# year_of_birth = current_year - age
# passing_18_years = year_of_birth + 18
# passing_100_years = year_of_birth + 100
#
# print(year_of_birth)
# print(passing_18_years)
# print(passing_100_years)


'''6. Get two numbers from the keyboard, save them in two variables and write them on the screen.
Then swap the values between the variables and write them back to the screen.'''

# number_1 = input("Please provide first number")
# number_2 = input("Please provide second number")
#
# print(number_1)
# print(number_2)
#
# variable_auxiliary = number_1
#
# number_1 = number_2
# number_2 = variable_auxiliary
#
# print(number_1)
# print(number_2)


"""The if condition and logical operators (not, and, or)"""

'''1. Get an integer from the keyboard and write on the screen whether it is even or not.'''

# user_choice = input("Please provide real number")
#
# if user_choice % 2 == 0:
#     print("Number:", user_choice, "is even")
# elif user_choice % 2 != 0:
#     print("Number:", user_choice, "is odd")
# else:
#     print("The number entered is not a real number")


'''2. Get a number from the keyboard and print it on whether it is addition, negative or equal to 0.'''

# user_choice = float(input("Please provide real number"))
#
# if user_choice > 0:
#     print(f"Number: {user_choice} is positive\n")
# elif user_choice < 0:
#     print(f"Number: {user_choice} is negative\n")
# elif user_choice == 0:
#     print(f"Number: {user_choice} is zero\n")
# else:
#     print("The number entered is not a real number")


'''3. Get two numbers from the keyboard and write on the screen first the bigger one, then the smaller one.'''

# user_input = int(input("Please provide real number"))
# user_input_2 = int(input("Please provide real number"))
#
# if user_input > user_input_2:
#     print(user_input, user_input_2, sep=" >>> ")
# elif user_input < user_input_2:
#     print(user_input_2, user_input, sep=" >>> ")
# else:
#     print("The number entered is not a real number")


'''4. Get a number from the keyboard and write it down if it is divisible by 5 and 7.'''

# user_input = int(input("Please provide real number"))
#
# if user_input % 5 == 0 and user_input % 7 == 0:
#     print(f"Number {user_input} is divisible by 5 and by 7 \n")
# else:
#     print(f"Number {user_input} is not divisible by 5 and by 7 \n")


'''5. Get three numbers from the keyboard and write the appropriate message: three different, 
two different, all equal.'''

# user_input_1 = int(input("Please provide real number\n"))
# user_input_2 = int(input("Please provide real number\n"))
# user_input_3 = int(input("Please provide real number\n"))
#
# if user_input_1 == user_input_2 == user_input_3:
#     print(f"Liczby: {user_input_1, user_input_2, user_input_3}, are equal!\n")
# elif user_input_1 == user_input_2 or user_input_1 == user_input_3 or user_input_3 == user_input_2:
#     print(f"Among the Numbers: {user_input_1, user_input_2, user_input_3}, are two of the same!\n")
# elif user_input_1 != user_input_2 != user_input_3:
#     print(f"Numbers: {user_input_1, user_input_2, user_input_3}, are not equal!\n")


'''6. Write a program that will convert the dog's age to "human" age
We assume the first year is 11 years, the second year is 10, each successive number is 5 human years'''

# dog_age = float(input("Enter the age of your dog\n"))
# while dog_age < 0:
#     dog_age = float(input("Enter the age of your dog - it cannot be negative\n"))
#
# year_1 = 11
# year_2 = 10
# year_n = 5
# variable_n = (dog_age - 2)
#
# if dog_age <= 1:
#     print(f"Your dog is {year_1} human years or less")
# elif dog_age <= 2:
#     print(f"Your dog is {year_1 + year_2} human years")
# elif dog_age > 2:
#     print(f"Your dog is {year_1 + year_2 + (variable_n * year_n)} human years")


'''6B. We take from the keyboard the number of the day of the week and write its name on the screen
(1- Monday, 2-Tuesday etc).'''

# user_input = int(input("Enter the day number 'in numbers from 1 to 7'\n"))
#
# while 7 < user_input < 1 :
#     user_input = int(input("Enter the day number 'in numbers from 1 to 7'\n"))
#
# if user_input == 1:
#     print("1 - Monday")
# elif user_input == 2:
#     print("2 - Tuesday")
# elif user_input == 3:
#     print("3 - Wednesday")
# elif user_input == 4:
#     print("4 - Thursday")
# elif user_input == 5:
#     print("5 - Friday")
# elif user_input == 6:
#     print("6 - Saturday")
# elif user_input == 7:
#     print("7 - Sunday")


'''7. We download the year of birth from the keyboard, and then calculate 
and display the information in which age category
there is a player (PEGI 3, 7, 12, 16, 18)'''

# user_input = int(input("Enter the year of birth\n"))
#
# while user_input < 0:
#     user_input = int(input("Year of birth cannot be negative - try again\n"))
#
# user_age = 2022 - user_input
#
# if user_age < 3:
#     print("The player is not in any category")
# elif user_age >= 3 and user_age < 7:
#     print("The player is in the PEGI category: 3")
# elif user_age >= 7 and user_age < 12:
#     print("The player is in the PEGI category: 7")
# elif user_age >= 12 and user_age < 16:
#     print("The player is in the PEGI category: 12")
# elif user_age >= 16 and user_age < 18:
#     print("The player is in the PEGI category: 16")
# elif user_age >= 18:
#     print("The player is in the PEGI category: 18")


'''8. Take the matriculation result from the keyboard (points 0-100) and convert it to the "American" A-F scale,
according to the rules: 0-50 -> F, 51-60 -> E, 61-75 -> D, 76-85 -> C, 86-95 -> B, 96-100 -> A'''

# user_input = int(input("Enter your 'matura' result\n"))
#
# while user_input < 0 or user_input > 100:
#     user_input = int(input("The result entered is outside the possible range\n"))
#
# if user_input <= 50:
#     print("You have received the grade: F")
# elif user_input >= 51 and user_input <= 60:
#     print("You have received the grade: E")
# elif user_input >= 61 and user_input <= 75:
#     print("You have received the grade: D")
# elif user_input >= 76 and user_input <= 85:
#     print("You have received the grade: C")
# elif user_input >= 86 and user_input <= 95:
#     print("You have received the grade: b")
# elif user_input >= 96:
#     print("You have received the grade: A")


'''9. We take three numbers from the keyboard and print them in descending order.'''

# user_input_1 = int(input("Enter a real number\n"))
# user_input_2 = int(input("Enter a real number\n"))
# user_input_3 = int(input("Enter a real number\n"))
#
# if user_input_1 >= user_input_2 >= user_input_3:
#     print(user_input_1, user_input_2, user_input_3, sep=" >>> ")
#
# elif user_input_1 >= user_input_3 >= user_input_2:
#     print(user_input_1, user_input_3, user_input_2, sep=" >>> ")
#
# elif user_input_2 >= user_input_1 >= user_input_3:
#     print(user_input_2, user_input_1, user_input_3, sep=" >>> ")
#
# elif user_input_2 >= user_input_3 >= user_input_1:
#     print(user_input_2, user_input_3, user_input_1, sep=" >>> ")
#
# elif user_input_3 >= user_input_1 >= user_input_2:
#     print(user_input_3, user_input_1, user_input_2, sep=" >>> ")
#
# elif user_input_3 >= user_input_2 >= user_input_1:
#     print(user_input_3, user_input_2, user_input_1, sep=" >>> ")


'''10. Take three numbers from the user and check if they match up to three decimal places.'''

# user_input_1 = float(input("Enter a real number\n"))
# user_input_2 = float(input("Enter a real number\n"))
# user_input_3 = float(input("Enter a real number\n"))
#
# round(user_input_1, 3)
# round(user_input_2, 3)
# round(user_input_3, 3)
#
# if user_input_1 == user_input_2 and user_input_1 == user_input_3:
#     print(user_input_1, user_input_2, user_input_3, "- all numbers are equal", sep=" = ")
# elif user_input_1 == user_input_2 and user_input_1 != user_input_3:
#     print(user_input_1, user_input_2, user_input_3, "- only the first and second numbers are equal", sep=" , ")
# elif user_input_1 != user_input_2 and user_input_3 == user_input_2:
#     print(user_input_1, user_input_2, user_input_3, "- only the second and third numbers are equal", sep=" , ")
# elif user_input_1 == user_input_3 and user_input_1 != user_input_2:
#     print(user_input_1, user_input_2, user_input_3, "- only the first and third numbers are equal", sep=" , ")
# else:
#     print(user_input_1, user_input_2, user_input_3, "- no number is equal to each other", sep=" != ")


'''11. Get the length of the three sides of the triangle from the user.
Check if you can form a triangle with them
(the sum of the lengths of any two sides must be greater than the length of the third side)'''

# user_input_1 = float(input("Enter a real number\n"))
# user_input_2 = float(input("Enter a real number\n"))
# user_input_3 = float(input("Enter a real number\n"))
#
# if user_input_3 <= 0 or user_input_1 <= 0 or user_input_2 <= 0:
#     print("The side length must be a positive number")
#     exit()
#
# if (user_input_1 + user_input_2) > user_input_3:
#     print(f"You can make a triangle with sides: {user_input_1, user_input_2, user_input_3} \n")
# elif (user_input_1 + user_input_3) > user_input_2:
#     print(f"You can make a triangle with sides: {user_input_1, user_input_2, user_input_3} \n")
# elif (user_input_2 + user_input_3) > user_input_1:
#     print(f"You can make a triangle with sides: {user_input_1, user_input_2, user_input_3} \n")
# else:
#     print(f"It is NOT possible to make triangle with sides: {user_input_1, user_input_2, user_input_3} \n ")


'''12. Enter the year and check if it is a leap year.
Leap years are years divisible by 4 but not divisible by 100.
The exception is years divisible by 400.'''

# user_input_1 = int(input("Enter any year\n"))
#
# if user_input_1 <= 0:
#     print("The year must be a positive number")
#     exit()
# else:
#     pass
#
# if user_input_1 % 100 == 0 and user_input_1 % 400 == 0 and user_input_1 % 4 == 0:
#     print(f"Year {user_input_1} is a leap year \n")
# elif user_input_1 % 100 == 0:
#     print(f"Year {user_input_1} is NOT a leap year \n")
# elif user_input_1 % 4 == 0 and user_input_1 % 100 != 0:
#     print(f"Year {user_input_1} is a leap year \n")
# else:
#     print(f"Year {user_input_1} is NOT a leap year \n")


'''13. Write a program that will ask you to enter the temperature and scale in which it was measured,
and then write the temperature in the other two scales on the screen.
We assume that our program supports three scales: Celsius, Kelvin, and Fahrenheid.'''

# while True:
#     user_input_1 = float(input("Enter the temperature\n"))
#     user_input_2 = input("Enter the letter corresponding to the temperature scale: "
#                          "('c = celsius', ' k = kelvin' or 'f = fahrenheit'\n").casefold()
#
#     celsius_kelvin = 273.15 + user_input_1, "K"
#     celsius_fahrenheit = (9 / 5 * user_input_1 + 32), "F"
#
#     fahrenheit_kelvin = (user_input_1 + 459.67) * 5 / 9, "K"
#     fahrenheit_celsius = 5 / 9 * (user_input_1 - 32), "C"
#
#     kelvin_fahrenheit = (user_input_1 * 9 / 5) - 459.67, "F"
#     kelvin_celsius = user_input_1 - 273.15, "C"
#     if user_input_2 == "c":
#         print(f"The temperature in Kelvin is: {celsius_kelvin}")
#         print(f"The temperature in Fahrenheits is: {celsius_fahrenheit}")
#     elif user_input_2 == "k":
#         print(f"The temperature in Celsius is: {kelvin_celsius}")
#         print(f"The temperature in Fahrenheits is: {kelvin_fahrenheit}")
#     elif user_input_2 == "f":
#         print(f"The temperature in Celsius is: {fahrenheit_celsius}")
#         print(f"The temperature in Kelvin is: {fahrenheit_kelvin}")
#     else:
#         print("Something went wrong, please try again ;)")
#     continue

'''14. Write a program that for the given month (January 1, February 2, etc.)
will print the number of days in that month. For February it will print "28/29"'''

# while True:
#     user_input_1 = input("Enter the name of the month\n").title()
#
#     if user_input_1 == "January" or user_input_1 == "March" or user_input_1 == "May" \
#     or user_input_1 == "July" or user_input_1 == "August" or user_input_1 == "October" \
#     or user_input_1 == "December":
#         print(f"Month: {user_input_1} have 31 days")
#     elif user_input_1 == "April" or user_input_1 == "June" or user_input_1 == "September" \
#     or user_input_1 == "November":
#         print(f"Month: {user_input_1} have 30 days")
#     elif user_input_1 == "February":
#         print(f"Month: {user_input_1} have 28/29 days")
#     else:
#         print("Something went wrong, please try again ;)")
#     continue


'''15. Write a program that for the given date (year, month, day) will calculate the date of the next day.'''

# while True:
#     user_input_1 = int(input("Enter day: \n"))
#     user_input_2 = int(input("Enter the month: \n"))
#     user_input_3 = int(input("Enter the year: \n"))
#
#     if user_input_1 <= 0 or user_input_2 <= 0 or user_input_3 <= 0:
#         print("The date must be a positive number")
#         continue
#     elif user_input_1 > 31 or user_input_2 > 12:
#         print("The date entered is out of range")
#         continue
#     else:
#         pass
#
#     if user_input_2 == (1 or 3 or 5 or 7 or 8 or 10) and user_input_1 == 31:
#         user_input_2 = user_input_2 + 1
#         user_input_1 = 1
#         print("New date:", user_input_3, user_input_2, user_input_1)
#     elif user_input_2 == (4 or 6 or 9 or 11) and user_input_2 == 30:
#         user_input_2 = user_input_2 + 1
#         user_input_1 = 1
#         print("New date:", user_input_3, user_input_2, user_input_1)
#     elif user_input_2 == 2 and user_input_1 == 28:
#         user_input_2 = user_input_2 + 1
#         user_input_1 = 1
#         print("New date:", user_input_3, user_input_2, user_input_1)
#     elif user_input_2 == 12 and user_input_1 == 31:
#         user_input_2 = 1
#         user_input_1 = 1
#         user_input_3 = user_input_3 + 1
#         print("New date:", user_input_3, user_input_2, user_input_1)
#     elif user_input_2 == (4 or 6 or 9 or 11) and user_input_1 > 30:
#         print("The date entered is out of range")
#     elif user_input_2 == 2 and user_input_1 > 28:
#         print("The date entered is out of range")
#
#     else:
#         user_input_1 = user_input_1 + 1
#         print("New date:", user_input_3, user_input_2, user_input_1)
