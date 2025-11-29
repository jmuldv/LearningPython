# Please write a program which prints out an emoticon: :-)
# print(":-)")

# Please write a program which prints out the following lines exactly as they are written here, punctuation and all:
# print("""
# Row, row, row your boat,
# Gently down the stream.
# Merrily, merrily, merrily, merrily,
# Life is but a dream.""")

# print("Row, row, row your boat,")
# print("Gently down the stream.")
# print("Merrily, merrily, merrily, merrily,")
# print("Life is but a dream.")


# Please write a program which prints out the number of minutes in a year. Use Python code to perform the calculation, as in the previous code example.
# print(60 * 24 * 365)

# Thus far, you have probably used double quotation marks " to print out strings. In addition to the double quotation marks, Python also accepts single quotation marks '.
# Please write a program which prints out the following: print("Hello there!")
# print('print("Hello there!")')

# Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.
# What is your name? Paul
# Paul
# Paul

# name = input("What is your name? ")
# print((name + "\n") * 2)
# print(name)


# Please write a program which asks for the user's name and then prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.
# The program should function as follows:

# Sample output
# What is your name? Paul
# !Paul!Paul!
# name = input("What is your name? ")
# print(f"!{name}!{name}!")


# Please write a program which asks for the user's name and address. The program should also
# print out the given information, as follows:
# Sample output
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

# name = input("Given name: ")
# family_name = input("Family name: ")
# street_address = input("Street address: ")
# city_postal_code = input("City and postal code: ")
# print(f"{name} {family_name}\n{street_address}\n{city_postal_code}")


# Here is a program which should ask for three utterances and print them out, like so:
# Sample output
# The 1st part: hickory
# The 2nd part: dickory
# The 3rd part: dock
# hickory-dickory-dock!

# part1 = input("The 1st part: ")
# part2 = input("The 2nd part: ")
# part3 = input("The 3rd part: ")
# print(f"{part1}-{part2}-{part3}!")


# Please write a program which prints out the following story. The user gives a
# name and a year, which should be inserted into the printout.
# Sample output
# Please type in a name: Mary
# Please type in a year: 1572

# Mary is a valiant knight, born in the year 1572. One morning Mary woke up to
# an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.

# name = input("Please type in a name: ")
# year = input("Please type in a year: ")
# print(f"""{name} is a valiant knight, born in the year {year}. One morning {name} woke up to an awful
# racket: a dragon was approaching the village. Only {name} could save the village's residents.""")


# The program should print out exactly the following:
# Sample output
# my name is Tim Tester, I am 20 years old

# my skills are
# - python(beginner)
# - java(veteran)
# - programming(semiprofessional)

# I am looking for a job with a salary of 2000-3000 euros per month

# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000

# print(f"my name is {name}, I am {age} years old")
# print("my skills are")
# print(f" - {skill1} ({level1})")
# print(f" - {skill2} ({level2})")
# print(f" - {skill3} ({level3})")
# print(
#     f"I am looking for a job with a salary of {lower}-{upper} euros per month")


# Arithmetic operations


# This program already contains two integer variables, x and y:
# x = 27
# y = 15
# Please complete the program so that it also prints out the following:

# Sample output
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8

# The program should work correctly even if the values of the variables are changed. That is , if the first two lines are replaced with this
# x = 4
# y = 9
# the program should print out the following:

# Sample output
# 4 + 9 = 13
# 4 - 9 = -5
# 4 * 9 = 36
# 4 / 9 = 0.4444444444444444

# x = input("x = ")
# y = input("y = ")

# print(f"{x} + {y} = {int(x) + int(y)}")
# print(f"{x} - {y} = {int(x) - int(y)}")
# print(f"{x} * {y} = {int(x) * int(y)}")
# print(f"{x} / {y} = {int(x) / int(y)}")


# Each print command usually prints out a line of its own, complete with a change
# of line at the end. However, if the print command is given an additional
# argument end = "", it will not print a line change.

# For example:
# print("Hi ", end="")
# print("there!")
# Sample output
# Hi there!

# Please fix this program so that the entire calculation, complete with result,
# is printed out on a single line. Do not change the number of print commands used.
# print(5)
# print(" + ")
# print(8)
# print(" - ")
# print(4)
# print(" = ")
# print(5 + 8 - 4)

# print("Hi ", end="")
# print("there!")

# print(5, end="")
# print(" + ", end="")
# print(8, end="")
# print(" - ", end="")
# print(4, end="")
# print(" = ", end="")
# print(5 + 8 - 4)


# Please write a program which asks the user for a number. The program then prints out the number multiplied by five.
# The program should function as follows:

# Sample output
# Please type in a number: 3
# 3 times 5 is 15

# number = input("Please type in a number: ")
# print(f"{number} times 5 is {int(number) * 5}")


# Please write a program which asks the user for their name and year of birth. The program then prints
# out a message as follows:
# Sample output
# What is your name? Frances Fictitious
# Which year were you born? 1990
# Hi Frances Fictitious, you will be 31 years old at the end of the year 2028

# name = input("What is your name? ")
# year_of_birth = input("Which year were you born? ")
# print(f"Hi {name}, you will be {2028 - int(year_of_birth)} years old at the end of the year 2028")


# Please write a program which asks the user for a number of days. The program then prints out the number
# of seconds in the amount of days given.

# The program should function as follows:
# Sample output
# How many days? 1
# Seconds in that many days: 86400

# Another example:
# Sample output
# How many days? 7
# Seconds in that many days: 604800

# days = input("How many days? ")
# seconds = int(days) * 24 * 60 * 60
# print(f"Seconds in that many days: {seconds}")


# This program asks the user for three numbers. The program then prints out their product, that is,
# the numbers multiplied by each other. There is , however, something wrong with the
# program - it doesn't work quite right, as you can see if you run it. Please fix it.

# An example of the expected execution of the program:
# Sample output
# Please type in the first number: 2
# Please type in the second number: 3
# Please type in the third number: 5
# The product is 30

# first = input("Please type in the first number: ")
# second = input("Please type in the second number: ")
# third = input("Please type in the third number: ")
# product = int(first) * int(second) * int(third)
# print(f"The product is {product}")


# Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

# The program should function as follows:
# Sample output
# Number 1: 3
# Number 2: 7
# The sum of the numbers: 10
# The product of the numbers: 21

# num1 = input("Number 1: ")
# num2 = input("Number 2: ")
# sum_result = int(num1) + int(num2)
# product_result = int(num1) * int(num2)
# print(f"The sum of the numbers: {sum_result}")
# print(f"The product of the numbers: {product_result}")


# Please write a program which asks the user for four numbers. The program then prints out the sum
# and the mean of the numbers.

# The program should function as follows:
# Sample output
# Number 1: 2
# Number 2: 1
# Number 3: 6
# Number 4: 7
# The sum of the numbers is 16 and the mean is 4.0

# num1 = input("Number 1: ")
# num2 = input("Number 2: ")
# num3 = input("Number 3: ")
# num4 = input("Number 4: ")
# sum_result = int(num1) + int(num2) + int(num3) + int(num4)
# mean_result = sum_result / 4
# print(
#     f"The sum of the numbers is {sum_result} and the mean is {mean_result:.1f}")


# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for
# the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# The program should function as follows:
# Sample output
# How many times a week do you eat at the student cafeteria? 4
# The price of a typical student lunch? 2.5
# How much money do you spend on groceries in a week? 28.5

# Average food expenditure:
# Daily: 5.5 euros
# Weekly: 38.5 euros

# cafeteria_visits = input(
#     "How many times a week do you eat at the student cafeteria? ")
# cafeteria_price = input(
#     "The price of a typical student lunch? ")
# groceries = input(
#     "How much money do you spend on groceries in a week? ")
# weekly_expenditure = int(cafeteria_visits) * \
#     float(cafeteria_price) + float(groceries)
# daily_expenditure = weekly_expenditure / 7
# print(
#     f"Average food expenditure:\nDaily: {daily_expenditure:.1f} euros\nWeekly: {weekly_expenditure:.1f} euros")


# Please write a program which asks for the number of students on a course and the desired group size. The
# program will then print out the number of groups formed from the students on the course. If the division
# is not even, one of the groups may have fewer members than specified.

# If you can't get your code working as expected, it is absolutely okay to move on and come back to this
# exercise later. The topic of the next section is conditional statements. This exercise can also be solved
# using a conditional construction.
# Sample output
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2

# Sample output
# How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4

# students = input("How many students on the course? ")
# group_size = input("Desired group size? ")
# number_of_groups = int(students) // int(group_size)
# if int(students) % int(group_size) != 0:
#     number_of_groups += 1
# print(f"Number of groups formed: {number_of_groups}")


# Conditional statements
# age = int(input("How old are you? "))

# if age > 17:
#     print("You are of age!")
#     print("Here's a copy of GTA6 for you.")

# print("Next customer, please!")


# Ex 1
# Please write a program which asks the user for an integer number. The program should print
# out "Orwell" if the number is exactly 1984, and otherwise do nothing.
# number = int(input("Please type in a number: "))

# if number == 1984:
#     print("Orwell")


# Ex 2
# Please write a program which asks the user for an integer number. If the number is less than zero,
# the program should print out the number multiplied by - 1. Otherwise the program prints out the number
# as is . Please have a look at the examples of expected behaviour below.
# number = int(input("Please type in a number: "))
# if number < 0:
#     print(number * -1)
# else:
#     print(number)


# Ex 3
# Please write a program which asks for the user's name. If the name is anything but "Jerry", the program
# then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.
# name = input("Please type in a number: ")

# if name == "Jerry":
#     print("Next please!")
# else:
#     portions = int(input("How many portions of soup? "))
#     print(f"The total cost is {portions * 5.90}")


# Ex 4
# Please write a program which asks the user for an integer number. The program should then print out the
# magnitude of the number according to the following examples.
# number = int(input("Please type in a number: "))
# if number < 10:
#     print("The number is less than 1000")
#     print("The number is less than 100")
#     print("The number is less than 10")
#     print("Thank you!")
# elif number < 100:
#     print("The number is less than 1000")
#     print("The number is less than 100")
#     print("Thank you!")
# elif number < 1000:
#     print("The number is less than 1000")
#     print("Thank you!")
# else:
#     print("Thank you!")


# Ex 5
# Please write a program which asks the user for two numbers and an operation. If the operation is add,
# multiply or subtract, the program should calculate and print out the result of the operation with the
# given numbers. If the user types in anything else, the program should print out nothing.
# num1, num2 = input("Please type in two numbers: ").split()
# num1 = input("Number 1: ")
# num2 = input("Number 2: ")
# operation = input(
#     "Please type in an operation (add, subtract, multiply, divide): ")

# if operation == "add":
#     print(f"{num1} + {num2} = {int(num1) + int(num2)}")
# elif operation == "subtract":
#     print(f"{num1} - {num2} = {int(num1) - int(num2)}")
# elif operation == "multiply":
#     print(f"{num1} * {num2} = {int(num1) * int(num2)}")
# else:
#     if int(num2) == 0:
#         print("Cannot divide by zero!")
#     else:
#         print(f"{num1} / {num2} = {int(num1) / int(num2)}")


# Ex 6
# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out
# the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program
# should also print out "Brr! It's cold in here!".
# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search
# engine of your choice.
# temperature = int(input("Please type in a temperature (F): "))
# temp_conversion = (temperature - 32) * 5 / 9

# if temp_conversion < 0:
#     print(f"{temperature} degrees Fahrenheit equals {temp_conversion:.1f} degrees Celsius")
#     print("Brr! It's cold in here!")
# else:
#     print(f"{temperature} degrees Fahrenheit equals {temp_conversion:.1f} degrees Celsius")


# Ex 7
# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program
# should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on
# Sundays when the hourly wage is doubled.
# hourly_wage = float(input("Hourly wage: "))
# hours_worked = int(input("Hours worked: "))
# day_of_week = input("Day of the week: ")

# if day_of_week.lower() == "sunday":
#     print(f"Daily wages: {(hourly_wage * 2) * hours_worked:.1f} euros")
# else:
#     print(f"Daily wages: {hourly_wage * hours_worked:.1f} euros")


# Ex 8
# This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is
# calculated with the following formula:
# - If there are less than a hundred points on the card, the bonus is 10 %
# - In any other case the bonus is 15 %
# points = int(input("How many points are on your card? "))

# if points >= 100:
#     print("Your bonus is 15%")
#     print(f"You now have {points * 1.15:.1f} points")
# else:
#     print("Your bonus is 10%")
#     print(f"You now have {points * 1.10:.1f} points")


# Ex 9
# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.
# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees,
# and also if there is rain on the radar.

# print("What is the weather forecast for tomorrow?")
# temperature = int(input("Temperature (C): "))
# rain = input("Will it rain (yes/no): ")

# if temperature > 20:
#     message = "Wear jeans and a T-shirt."
# elif temperature > 10:
#     message = "Wear jeans and a T-shirt" \
#         "\nI recommend a jumper as well"
# elif temperature > 5:
#     message = "Wear jeans and a T-shirt" \
#         "\nI recommend a jumper as well" \
#         "\nTake a jacket with you"
# else:
#     message = "Wear jeans and a T-shirt" \
#         "\nI recommend a jumper as well" \
#         "\nTake a jacket with you" \
#         "\nMake it a warm coat, actually" \
#         "\nI think gloves are in order"

# if rain.lower() == "yes" or rain.lower() == "y":
#     message += "\nDon't forget your umbrella!"
#     print(message)
# else:
#     print(message)


# Ex 10
from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

x = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
y = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)

print(f"The roots are {x:.1f} and {y:.1f}")
