# 2-1: Fix syntax errors
# Output should look like this for the number 13:
# Please type in a number: 13
# 13 must be my lucky number!
# Have a nice day!

# Sample output for the number 101:
# Please type in a number: 101
# The number was greater than one hundred
# Now its value has decreased by one hundred
# Its value is now 1
# 1 must be my lucky number!
# Have a nice day!

# number = int(input("Please type in a number: "))
# if number > 100:
#     print("The number was greater than one hundred")
#     number -= 100
#     print("Now its value has decreased by one hundred")
#     print(f"Its value is now {number}")
# print(f"{number} must be my lucky number!")
# print("Have a nice day!")


# 2-2: Length of a string
# word = "abcd"
# print(len(word))

# print(len("hi there"))

# word2 = "howdydoody"
# length = len(word2)
# print(length)

# empty_string = ""
# length = len(empty_string)
# print(length)

# Please type in a word: hey
# There are 3 letters in the word hey
# Thank you!

# Sample output
# Please type in a word: banana
# There are 6 letters in the word banana
# Thank you!

# Sample output
# Please type in a word: b
# Thank you!

# word = input("Please type in a word: ")
# length = len(word)

# if length < 2:
#     print("Thank you!")
# else:
#     print(f"There are {length} letters in the word {word}\nThank you!")


# 2-3a: Typecasting
# temperature = float(input("Please type in a temperature: "))
# print(f"The temperature is {temperature}")
# print("...and rounded down it is", int(temperature))

# 2-3b: Typecasting
# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.
# You can assume the number given by the user is always greater than zero.
# An example of expected behaviour:

# Sample output
# Please type in a number: 1.34
# Integer part: 1
# Decimal part: 0.34

# number = float(input("Please type in a number: "))
# print(f"Integer part: {int(number)}")
# length = str(number).split('.')[1]
# print(f"Decimal part: 0.{int(length)}")


# More conditionals

# Please write a program which asks the user for their age. The program
# should then print out a message based on whether the user is of age
# or not, using 18 as the age of maturity.
# Some examples of expected behaviour:

# Sample output
# How old are you? 12
# You are not of age!

# Sample output
# How old are you? 32
# You are of age!
# age = int(input("How old are you? "))

# if age < 18:
#     print("You are not of age!")
# else:
#     print("You are of age!")


# Greater than or equal to
# Please write a program which asks for two integer numbers. The program
# should then print out whichever is greater. If the numbers are equal,
# the program should print a different message.

# Some examples of expected behaviour:
# Sample output
# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5

# Sample output
# Please type in the first number: 5
# Please type in another number: 8
# The greater number was: 8

# Sample output
# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

# num1 = int(input("Please type in the first number: "))
# num2 = int(input("Please type in another number: "))

# if num1 > num2:
#     print(f"The greater number is {num1}")
# elif num2 > num1:
#     print(f"The greater number is {num2}")
# else:
#     print("The numbers are equal")


# The elder
# Please write a program which asks for the names and ages of two
# persons. The program should then print out the name of the elder.

# Some examples of expected behaviour:
# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

# Sample output
# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age
# person1 = input("Person 1: \nName: ")
# person1_age = int(input("Age: "))

# person2 = input("Person 2: \nName: ")
# person2_age = int(input("Age: "))

# if person1_age > person2_age:
#     print(f"The elder is {person1}")
# elif person2_age > person1_age:
#     print(f"The elder is {person2}")
# else:
#     print(f"{person1} and {person2} are the same age")


# Alphabetically last
# first_word = input("Please type in the 1st word: ")
# second_word = input("Please type in the 2nd word: ")

# if first_word.upper() > second_word.upper():
#     print(f"{first_word} is alphabetically last")
# elif second_word.upper() > first_word.upper():
#     print(f"{second_word} is alphabetically last")
# else:
#     print("You gave the same word twice")


# Combining conditions

# Please write a program which asks for the user's age. If the
# age is not plausible, that is, it is under 5 or something that
# can't be an actual human age, the program should print out a comment.

# Have a look at the examples of expected behaviour below to figure out
# which comment is applicable in each case.

# age = int(input("What is your age? "))
# if age <= 0:
#     print("That must be a mistake!")
# elif age < 5:
#     print("I suspect you can't write quite yet...")
# else:
#     print(f"Ok, you're {age} years old")


# Please write a program which asks for the user's name. If the name is Huey,
# Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

# In a similar fashion, if the name is Morty or Ferdie, the program should
# recognise the user as one of Mickey Mouse's nephews.

# name = input("Please type in your name: ")
# if name == "Huey" or name == "Dewey" or name == "Louie":
#     print("I think you might be one of Donald Duck's nephews.")
# elif name == "Morty" or name == "Ferdie":
#     print("I think you might be one of Mickey Mouse's nephews.")
# else:
#     print("You're not a nephew of any character I know of.")


# The table below outlines the grade boundaries on a certain university
# course. Please write a program which asks for the amount of points received
# and then prints out the grade attained according to the table.

# points = int(input("How many points [0-100]: "))
# if points < 0 or points > 100:
#     print("Grade: Impossible")
# elif points >= 0 and points < 50:
#     print("Grade: Fail")
# elif points >= 50 and points < 60:
#     print("Grade: 1")
# elif points >= 60 and points < 70:
#     print("Grade: 2")
# elif points >= 70 and points < 80:
#     print("Grade: 3")
# elif points >= 80 and points < 90:
#     print("Grade: 4")
# elif points >= 90 and points <= 100:
#     print("Grade: 5")


# Please write a program which asks the user for an integer number.
# If the number is divisible by three, the program should print out Fizz.
# If the number is divisible by five, the program should print out Buzz.
# If the number is divisible by both three and five, the program should print out FizzBuzz.

# number = int(input("Number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")


# Generally, any year that is divisible by four is a leap year. However,
# if the year is additionally divisible by 100, it is a leap year only if
# it also divisible by 400.

# Please write a program which asks the user for a year, and then prints out
# whether that year is a leap year or not.

# year = int(input("Please type in a year: "))

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# Please write a program which asks the user for three letters. The program
# should then print out whichever of the three letters would be in the middle
# if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.

# first = input("1st letter: ")
# second = input("2nd letter: ")
# third = input("3rd letter: ")

# if first.upper() > second.upper() > third.upper():
#     print(f"The letter in the middle is {second}")
# elif first.upper() > third.upper() > second.upper():
#     print(f"The letter in the middle is {third}")
# elif second.upper() > first.upper() > third.upper():
#     print(f"The letter in the middle is {first}")
# elif second.upper() > third.upper() > first.upper():
#     print(f"The letter in the middle is {third}")
# elif third.upper() > first.upper() > second.upper():
#     print(f"The letter in the middle is {second}")
# elif third.upper() > second.upper() > first.upper():
#     print(f"The letter in the middle is {first}")


# Some say paying taxes makes Finns happy, so let's see if the secret
# of happiness lies in one of the taxes set out in Finnish tax code.

# According to the Finnish Tax Administration, a gift is a transfer of
# property to another person against no compensation or payment. If the
# total value of the gifts you receive from the same donor in the course
# of 3 years is €5,000 or more, you must pay gift tax.

# When the gift is received from a close relative or a family member, the
# amount of tax to be paid is determined by the following table, which is
# also available on this website:

# Value of gift	Tax at the lower limit	Tax rate for the exceeding part ( % )
# 5 000 — 25 000	100	8
# 25 000 — 55 000	1 700	10
# 55 000 — 200 000	4 700	12
# 200 000 — 1 000 000	22 100	15
# 1 000 000 —	142 100	17

# So, for a gift of 6 000 euros the recipient pays a tax of 180 euros
# (100 + (6 000 - 5 000) * 0.08). Similarly, for a gift of 75 000 euros
# the recipient pays a tax of 7 100 euros(4 700 + (75 000 - 55 000) * 0.12).

# giftvalue = int(input("Value of gift: "))

# if giftvalue < 5000:
#     print("No tax!")
# elif giftvalue >= 5000 and giftvalue < 25000:
#     tax = 100 + (giftvalue - 5000) * 0.08
#     print(f"Amount of tax: {tax} euros")
# elif giftvalue >= 25000 and giftvalue < 55000:
#     tax = 1700 + (giftvalue - 25000) * 0.1
#     print(f"Amount of tax: {tax} euros")
# elif giftvalue >= 55000 and giftvalue < 200000:
#     tax = 4700 + (giftvalue - 55000) * 0.12
#     print(f"Amount of tax: {tax} euros")
# elif giftvalue >= 200000 and giftvalue < 1000000:
#     tax = 22100 + (giftvalue - 200000) * 0.15
#     print(f"Amount of tax: {tax} euros")
# elif giftvalue >= 1000000:
#     tax = 142100 + (giftvalue - 1000000) * 0.17
#     print(f"Amount of tax: {tax} euros")


# Simple loops

# Let's create a program along the lines of the example above. This
# program should print out the message "hi" and then ask "Shall we continue?"
# until the user inputs "no". Then the program should print out "okay then"
# and finish. Please have a look at the example below.

# while True:
#     answer = input("Hi\nShall we continue? ")
#     if answer.lower() == "no":
#         break

# print("okay then")


# from math import sqrt

# while True:
#     number = int(input("Please type in a number: "))
#     if number > 0:
#         print(sqrt(number))
#     elif number < 0:
#         print("Invalid number")
#     else:
#         break

# print("Exiting...")


# Fix the code: Countdown
# This should print out
# Sample output...
# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!

# number = 5
# print("Countdown!")
# while True:
#     print(number)
#     number -= 1
#     if number <= 0:
#         break

# print("Now!")


# Password
# pass1 = input("Password: ")

# while True:
#     pass2 = input("Repeat password: ")
#     if pass1 == pass2:
#         print("User account created")
#         break
#     else:
#         print("They do not match")


# Pin number and attempts
# Please write a program which keeps asking the user for a PIN code
# until they type in the correct one, which is 4321. The program should
# then print out the number of times the user tried different codes.

# attempted = 0

# while True:
#     pin = input("PIN: ")
#     attempted += 1

#     if pin == "4321":
#         print(f"Correct! It took you {attempted} attempt(s)")
#         break
#     else:
#         print("Wrong")


# The next leap year
# year = int(input("Year: "))
# leap_year = year

# while True:
#     leap_year += 1
#     if leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0):
#         year_add = leap_year - year
#         break

# print(f"The next leap year after {year} is {year + year_add}")


# Story
# Please write a program which keeps asking the user for words. If
# the user types in end, the program should print out the story the
# words formed, and finish.

# Sample output
# Please type in a word: Once
# Please type in a word: upon
# Please type in a word: a
# Please type in a word: time
# Please type in a word: there
# Please type in a word: was
# Please type in a word: a
# Please type in a word: girl
# Please type in a word: end
# Once upon a time there was a girl

# story = ""
# while True:
#     word = input("Please type in a word: ")
#     if word.lower() == "end":
#         print(f"{story}")
#         break
#     else:
#         story += word + " "


# Change the program so that the loop ends also if the user types
# in the same word twice in a row.

# story = ""
# last_word = ""
# while True:
#     word = input("Please type in a word: ")
#     if word.lower() == "end" or last_word == word:
#         print(f"{story}")
#         break
#     else:
#         story += word + " "
#         last_word = word


# Please write a program which asks the user for integer numbers.
# The program should keep asking for numbers until the user types in zero.

# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

# After reading in the numbers the program should print out how many numbers
# were typed in. The zero at the end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# print("Please type in integer numbers. Type 0 to finish")
# counter = 0
# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         print(f"...the program asks for numbers\nNumbers typed in {counter}")
#         break
#     else:
#         counter += 1


# Part 2: Sum
# The program should also print out the sum of all the numbers typed in. The zero
# at the end should not be included in the calculation.

# The program should now print out the following:

# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34

# print("Please type in integer numbers. Type 0 to finish")
# counter = 0
# number_sum = 0
# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         print(f"...the program asks for numbers\nNumbers typed in {counter}")
#         print(f"The sum of the numbers is {number_sum}")
#         break
#     else:
#         counter += 1
#         number_sum += number


# Part 3: Mean
# The program should also print out the mean of the numbers. The zero at the
# end should not be included in the calculation. You may assume the user will
# always type in at least one valid non-zero number.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5

# print("Please type in integer numbers. Type 0 to finish")
# counter = 0
# number_sum = 0
# # mean = 0
# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         print(f"...the program asks for numbers\nNumbers typed in {counter}")
#         print(f"The sum of the numbers is {number_sum}")
#         print(f"The mean of the numbers is {number_sum / counter:.2f}")
#         break
#     else:
#         counter += 1
#         number_sum += number


# Part 4: Positives and negatives
# The program should also print out statistics on how many of the numbers
# were positive and how many were negative. The zero at the end should not
# be included in the calculation.

# Sample output
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1

print("Please type in integer numbers. Type 0 to finish")
counter = 0
number_sum = 0
pos = 0
neg = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        print(f"...the program asks for numbers\nNumbers typed in {counter}")
        print(f"The sum of the numbers is {number_sum}")
        print(f"The mean of the numbers is {number_sum / counter:.2f}")
        print(f"Positive numbers {pos}")
        print(f"Negative numbers {neg}")
        break
    elif number > 0:
        pos += 1
        counter += 1
        number_sum += number
    elif number < 0:
        neg += 1
        counter += 1
        number_sum += number
    # else:
    #     counter += 1
    #     number_sum += number
