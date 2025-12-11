
# Loops with conditions

# Please write a program which prints out all the even numbers between two
# and thirty, using a loop. Print each number on a separate line.

# The beginning of your output should look like this:

# Sample output

# 2
# 4
# 6
# 8
# etc...

# number = 2
# while number < 31:
#     print(number)
#     number += 2


# The program below has some syntactic issues:

# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number = 0:
# print(number)
# print("Now!")
# Please fix it so that it prints out the following:

# Sample output
# Are you ready?
# Please type in a number: 5
# 5
# 4
# 3
# 2
# 1
# Now!

# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number > 0:
#     print(number)
#     number -= 1
# print("Now!")


# Please write a program which asks the user for a number. The program
# then prints out all integer numbers greater than zero but smaller than the input.

# Sample output
# Upper limit: 5
# 1
# 2
# 3
# 4

# upper_limit = int(input("Upper limit: "))
# num = 1
# if upper_limit > 1:
#     while upper_limit > num:
#         print(f"{num}")
#         num += 1
# else:
#     print("The number needs to be higher than 1.")


# Please write a program which asks the user to type in an upper limit.
# The program then prints out numbers so that each subsequent number is
# the previous one doubled, starting from the number 1. That is, the
# program prints out powers of two in order.

# The execution of the program finishes when the next number to be printed
# would be greater than the limit set by the user. No numbers greater than
# the limit should be printed.

# Upper limit: 8
# 1
# 2
# 4
# 8

# Upper limit: 100
# 1
# 2
# 4
# 8
# 16
# 32
# 64

# What are powers of two? The first power of two is the number 1. The next
# one is 1 times 2, which is 2. The next is 2 times 2, which is 4. The next
# is 4 times 2, which is 8, and so forth. Each power in the sequence is
# multiplied by two to produce the next one.

# upper_limit = int(input("Upper limit: "))
# num = 1
# if upper_limit > 1:
#     while upper_limit >= num:
#         print(f"{num}")
#         num += num
# else:
#     print("The number needs to be higher than 1.")


# Please change the program from the previous exercise so that the user
# gets to input also the base which is multiplied ( in the previous
# program the base was always 2).

# Sample output
# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27

# Sample output
# Upper limit: 1234567
# Base: 10
# 1
# 10
# 100
# 1000
# 10000
# 100000
# 1000000

# upper_limit = int(input("Upper limit: "))
# base = int(input("Base: "))
# num = 1
# if upper_limit > 1:
#     while upper_limit >= num:
#         if num == 1:
#             print(f"{num}")
#             num = base
#         else:
#             print(f"{num}")
#             num *= base
# else:
#     print("The number needs to be higher than 1.")


# Please write a program which asks the user to type in a limit. The
# program then calculates the sum of consecutive numbers(1 + 2 + 3 + ...)
# until the sum is at least equal to the limit set by the user. The
# program should function as follows:

# Sample output
# Limit: 2
# 3

# Sample output
# Limit: 10
# 10

# Sample output
# Limit: 18
# 21

# limit = int(input("Limit: "))
# total = 0
# counter = 1
# if limit > 1:
#     while limit > total:
#         total += counter
#         counter += 1
# else:
#     print("The number needs to be higher than 1.")
# print(f"{total}")


# Please write a new version of the program in the previous exercise.
# In addition to the result it should also print out the calculation
# performed:

# Sample output

# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Sample output
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10

# Sample output
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

# limit = int(input("Limit: "))
# total = 0
# counter = 1
# total_string = ""
# if limit > 1:
#     while limit > total:
#         total += counter
#         if counter == 1:
#             total_string += f"{counter}"
#         else:
#             total_string += f" + {counter}"
#         counter += 1
# else:
#     print("The number needs to be higher than 1.")
# print(f"{total_string} = {total}")


# Working with strings

# This looks like a Christmas tree
# n = 5  # number of layers in the pyramid
# row = "*"

# while n > 0:
#     print(" " * n + row)
#     row += "**"
#     n -= 1


# Please write a program which asks the user for a string and an amount.
# The program then prints out the string as many times as specified by
# the amount. The printout should all be on one line, with no extra
# spaces or symbols added.

# An example of expected behaviour:

# Sample output

# Please type in a string: hiya
# Please type in an amount: 4
# hiyahiyahiyahiya

# word = input("Please type in a string: ")
# amt = int(input("Please type in an amount: "))
# print(word * amt)


# Please write a program which asks the user for two strings and then prints
# out whichever is the longer of the two - that is, whichever has the more
# characters. If the strings are of equal length, the program should print
# out "The strings are equally long".

# Some examples of expected behaviour:

# Sample output

# Please type in string 1: hey
# Please type in string 2: hiya
# hiya is longer

# Sample output

# Please type in string 1: howdy doody
# Please type in string 2: hola
# howdy doody is longer

# Please type in string 1: hey
# Please type in string 2: bye
# The strings are equally long

# word1 = input("Please type in string 1: ")
# word2 = input("Please type in string 2: ")

# if len(word1) > len(word2):
#     print(f"{word1} is longer")
# if len(word2) > len(word1):
#     print(f"{word2} is longer")
# else:
#     print("The strings are equally long")


# Please write a program which asks the user for a string. The program then
# prints out the input string in reversed order, from end to beginning.
# Each character should be on a separate line.

# An example of expected behaviour:

# Sample output

# Please type in a string: hiya
# a
# y
# i
# h

# word1 = input("Please type in a string: ")
# index = len(word1) * -1
# count = -1
# while count >= index:
#     print(word1[count])
#     count -= 1

# input_string = input("Please type in a string: ")
# index = 0
# while index < len(input_string):
#     print(input_string[index])
#     index += 1


# Please write a program which asks the user for a string. The program then
# prints out a message based on whether the second character and the second
# to last character are the same or not . See the examples below.

# Sample output

# Please type in a string: python
# The second and the second to last characters are different

# Sample output

# Please type in a string: pascal
# The second and the second to last characters are a

# word1 = input("Please enter a string: ")
# second = word1[1]
# second_last = word1[-2]
# if second != second_last:
#     print("The second and the second to last characters are different")
# else:
#     print(f"The second and the second to last characters are {second}")


# Please write a program which prints out a line of hash characters, the
# width of which is chosen by the user.

# Sample output
# Width: 3
# ###

# Sample output
# Width: 8
# ########

# wide = int(input("Width: "))
# print(f"{'#' * (wide)}")


# Please modify the previous program so that it also asks for the height,
# and prints out a rectangle of hash characters accordingly.

# Sample output
# Width: 10
# Height: 3
# ##########
# ##########
# ##########

# wide = int(input("Width: "))
# tall = int(input("Height: "))
# count = 1
# while count <= tall:
#     print(f"{'#' * (wide)}")
#     count += 1


# Please write a program which asks the user for strings using a loop.
# The program prints out each string underlined as shown in the examples
# below. The execution ends when the user inputs an empty string - that is ,
# just presses Enter at the prompt.

# Sample output
# Please type in a string: Hi there!

# Hi there!
# ---------
# Please type in a string: This is a test

# This is a test
# --------------
# Please type in a string: a

# a
# -
# Please type in a string:
# string1 = " "
# while string1 != "":
#     string1 = input("Please type in a string: ")
#     if string1 == "":
#         break
#     else:
#         print(string1)
#         print("-" * len(string1))


# Please write a program which asks the user for a string and then prints it
# out so that exactly 20 characters are displayed. If the input is shorter
# than 20 characters, the beginning of the line is filled in with * characters.

# You may assume the input string is at most 20 characters long.

# Sample output
# Please type in a string: python

# **************python
# Sample output
# Please type in a string: alongerstring

# *******alongerstring
# Sample output
# Please type in a string: averyverylongstring

# *averyverylongstring

# string1 = input("Please type in a string: ")
# masklen = 20 - len(string1)
# print(f"{'*' * (masklen) + string1}")


# Please write a program which asks the user for a string and then prints
# out a frame of * characters with the word in the centre. The width of
# the frame should be 30 characters. You may assume the input string will
# always fit inside the frame.

# If the length of the input string is an odd number, you may print out the
# word in either of the two possible centre locations.

# Sample output
# Word: testing

# ******************************
# *          testing           *
# ******************************
# Sample output
# Word: python

# ******************************
# *           python           *
# ******************************

# word = input("Word: ")
# spacebefore = " " * (13 - (-(-len(word) // 2)))
# spaceafter = " " * (28 - len(spacebefore) - len(word))
# begend = "******************************"
# print(begend)
# print(f"{'*' + (spacebefore) + (word) + (spaceafter) + '*'}")
# print(begend)


# Please write a program which asks the user to type in a string. The
# program then prints out all the substrings which begin with the first
# character, from the shortest to the longest. Have a look at the
# example below.

# Sample output
# Please type in a string: test
# t
# te
# tes
# test

# string1 = input("Please type in a string: ")
# strlen = len(string1)
# counter = 0
# string2 = ''
# while counter < strlen:
#     string2 += string1[counter]
#     print(string2)
#     counter += 1


# Please write a program which asks the user to type in a string. The program
# then prints out all the substrings which end with the last character, from
# the shortest to the longest. Have a look at the example below.

# Sample output
# Please type in a string: test
# t
# st
# est
# test

# string1 = "testing"
# strlen = len(string1)
# lenctr = len(string1) - 1
# while lenctr >= 0:
#     print(string1[lenctr:strlen])
#     lenctr -= 1


# Please write a program which asks the user to input a string. The program
# then prints out different messages if the string contains any of the
# vowels a, e or o.

# You may assume the input will be in lowercase entirely. Have a look at the
# examples below.

# Sample output
# Please type in a string: hello there
# a not found
# e found
# o found

# Sample output
# Please type in a string: hiya
# a found
# e not found
# o not found

# input_string = input("Please type in a string: ")

# if "a" in input_string.lower():
#     print("a found")
# else:
#     print("a not found")

# if "e" in input_string.lower():
#     print("e found")
# else:
#     print("e not found")

# if "o" in input_string.lower():
#     print("o found")
# else:
#     print("o not found")


# Please write a program which asks the user to type in a string and a
# single character. The program then prints the first three character
# slice which begins with the character specified by the user. You may
# assume the input string is at least three characters long. The program
# must print out three characters, or else nothing.

# Pay special attention to when there are less than two characters left in
# the string after the first occurrence of the character looked for . In
# that case nothing should be printed out, and there should not be any
# indexing errors when executing the program.

# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam

# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

# Sample output
# Please type in a word: tomato
# Please type in a character: x

# Sample output
# Please type in a word: python
# Please type in a character: n

# word = input("Please type in a word: ").lower()
# search = input("Please type in a character: ").lower()
# wordlen = len(word)
# counter = 0

# if search.lower() in word.lower():
#     while word[counter] != search:
#         counter += 1
#     if (wordlen - 3) >= counter:
#         print(word[counter:(counter + 3)])
#     else:
#         print("")
# else:
#     print("")


# Please make an extended version of the previous program, which prints
# out all the substrings which are at least three characters long, and
# which begin with the character specified by the user. You may assume the
# input string is at least three characters long.

# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot

# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

# word = input("Please type in a word: ").lower()
# search = input("Please type in a character: ").lower()
# wordlen = len(word)
# counter = 0
# overall_count = 1

# if search.lower() in word.lower():
#     while overall_count <= wordlen - 3:
#         if word[counter] != search:
#             overall_count += 1
#             counter += 1
#         else:
#             print(word[counter:(counter + 3)])
#             overall_count += 1
#             counter += 1
# else:
#     print("")


# Please write a program which finds the second occurrence of a substring.
# If there is no second ( or first) occurrence, the program should print
# out a message accordingly.

# In this exercise the occurrences cannot overlap. For example, in the
# string aaaa the second occurrence of the substring aa is at index 2.

# Some examples of expected behaviour:

# Sample output
# Please type in a string: abcabc
# Please type in a substring: ab
# The second occurrence of the substring is at index 3.

# Sample output
# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.

# Sample output
# Please type in a string: aybabtu
# Please type in a substring: ba
# The substring does not occur twice in the string.

# word = input("Please type in a word: ").lower()
# search = input("Please type in a substring: ").lower()
# searchlen = len(search)
# wordlen = len(word)
# counter = 0
# overall_count = 0
# index = 0
# found = 0

# if search.lower() in word.lower():
#     while overall_count <= (wordlen - searchlen):
#         if word[counter:(counter + searchlen)] != search:
#             overall_count += 1
#             counter += 1
#             index += 1
#         else:
#             found += 1
#             index += 1
#             overall_count += 1
#             counter += 1
#             if found == 2:
#                 break

# if found == 2:
#     print(f"The second occurence of the substring is at index {index}.")
# else:
#     print("The substring does not occur twice in the string.")


# Please write a program which asks the user for a positive integer number.
# The program then prints out a list of multiplication operations until both
# operands reach the number given by the user. See the examples below for details:

# Sample output
# Please type in a number: 2
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

# Sample output
# Please type in a number: 3
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

# number = int(input("Please type in a number: "))
# x = 1
# y = 1
# while x <= number and y <= number:
#     print(f"{x} x {y} = {x * y}")
#     y += 1
#     if y == number + 1:
#         y = 1
#         x += 1
#         if x == number + 1:
#             break


# Please write a program which asks the user to type in a sentence.
# The program then prints out the first letter of each word in the
# sentence, each letter on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w
# from 0 to the first space or length of string - 1
# counter keeps track of where the space is at then adds 1 if
# it's not at the end of the string and then it performs another
# find until the next space or until the end of the string - 1

# sentence = input("Please type in a sentence: ").strip()
# sentlen = len(sentence)
# index = 0
# space = " "

# while index <= sentlen - 1:
#     if index == 0 or sentence[index] == space:
#         if index == 0:
#             print(sentence[index])
#             index += 1
#         else:
#             print(sentence[(index + 1)])
#             index += 2
#     else:
#         index += 1


# Factorial
# Please write a program which asks the user to type in an integer number.
# If the user types in a number equal to or below 0, the execution ends.
# Otherwise the program prints out the factorial of the number.

# The factorial of a number involves multiplying the number by all the
# positive integers smaller than itself. In other words, it is the product
# of all positive integers less than or equal to the number. For example,
# the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

# Some examples of expected behaviour:

# Sample output
# Please type in a number: 3
# The factorial of the number 3 is 6
# Please type in a number: 4
# The factorial of the number 4 is 24
# Please type in a number: -1
# Thanks and bye!

# Sample output
# Please type in a number: 1
# The factorial of the number 1 is 1
# Please type in a number: 0
# Thanks and bye!

# factorial = 1
# counter = 1

# while True:
#     number = int(input("Please type in a number: "))
#     if number <= 0:
#         break
#     else:
#         while counter <= number:
#             factorial *= counter
#             counter += 1
#         print(f"The factorial of the number {number} is {factorial}")

# Flip the pairs
# Please write a program which asks the user to type in a number. The
# program then prints out all the positive integer values from 1 up to
# the number. However, the order of the numbers is changed so that each
# pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and
# so forth. See the examples below for details.

# Sample output
# Please type in a number: 5
# 2
# 1
# 4
# 3
# 5

# Sample output
# Please type in a number: 6
# 2
# 1
# 4
# 3
# 6
# 5

# 1 2 3 4 5 6 7 8

# counter = 0
# number = int(input("Please type in a number: "))

# while counter <= number:
#     counter += 2
#     num_before = counter - 1
#     if num_before > number:
#         counter = 0
#         break
#     elif counter > number:
#         print(num_before)
#     else:
#         print(counter)
#         print(num_before)

# print('\r')

# # Check if the number is positive
# if number < 1:
#     print("Please enter a positive number.")
# else:
#     # Generate a list of numbers from 1 to num
#     numbers = list(range(1, number + 1))

#     # Print the numbers on one line, separated by spaces
#     print(*numbers)


# Taking turns
# Please write a program which asks the user to type in a number.
# The program then prints out the positive integers between 1 and
# the number itself, alternating between the two ends of the range
# as in the examples below.

# Sample output
# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3

# Sample output
# Please type in a number: 6
# 1
# 6
# 2
# 5
# 3
# 4

start = 1
number = int(input("Please type in a number greater than 1: "))

while start < number:
    print(start)
    print(number)
    start += 1
    number -= 1

if start == number:
    print(start)
