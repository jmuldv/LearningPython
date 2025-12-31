# Ex: Hello Visual Studio Code
# Please write a program which asks the user which editor they are using. The program
# should keep on asking until the user types in Visual Studio Code.

# Have a look at the example of expected behaviour below:

# Sample output
# Editor: Emacs
# not good
# Editor: Vim
# not good
# Editor: Word
# awful
# Editor: Atom
# not good
# Editor: Visual Studio Code
# an excellent choice!

# The program should be case-insensitive in its reactions. That is, the same user
# input in lowercase, uppercase or mixed case should trigger the same reaction:

# Sample output
# Editor: NOTEPAD
# awful
# Editor: viSUal STudiO cODe
# an excellent choice!


# print(editor.lower())

# while True:
#     editor = input("Which editor are you using: ")
#     if editor.lower() == "visual studio code" or editor.lower() == "vs code":
#         print("an excellent choice!")
#         break
#     else:
#         print("awful")

# Notes:
# # List all of the functions for a string
# # Can remove print if done at an interpreter prompt
# print(dir("this is a string"))
# # List all of the functions for a list
# print(dir([]))

# To close the interpreter when you are finished use the commands quit() or exit() will close it,
# as will the key combo Control+D (Linux/Mac) or Control+Z (Windows). Especially in
# Visual Studio Code this is important, as trying to execute another Python program
# while the interpreter is still running results in a rather cryptic error message


# Section 2: More functions

# Programming exercise: Line
# Please write a function named line, which takes two arguments: an integer and a
# string. The function prints out a line of text, the length of which is specified by the
# first argument. The character used to draw the line should be the first character in the
# second argument. If the second argument is an empty string, the line should consist of stars.

# An example of expected behaviour:

# line(7, "%")
# line(10, "LOL")
# line(3, "")
# Sample output
# % % % % % % %
# LLLLLLLLLL
# ***

# def line(integer, string):
#     if string == "":
#         print("*" * integer)
#     else:
#         print(string * integer)


# line(7, "%")
# line(10, "LOL")
# line(3, "")


# Note: You can call a function within a function.

# def greet(name):
#     print("Hello there,", name)


# def greet_many_times(name, times):
#     while times > 0:
#         greet(name)
#         times -= 1

# greet_many_times("Emily", 3)


# Programming exercise: A box of hashes
# Please write a function named box_of_hashes, which prints out a rectangle of hash characters.
# The function takes one argument, which specifies the height of the rectangle. The rectangle
# should be ten characters wide.

# The function should call the function line from the exercise above for the actual printing
# out. Copy your solution to that exercise above the code for this exercise. Please don't
# change anything in your line function.

# Some examples of how the function should work:

# box_of_hashes(5)
# print()
# box_of_hashes(2)

# ##########
# ##########
# ##########
# ##########
# ##########

# ##########
# ##########
