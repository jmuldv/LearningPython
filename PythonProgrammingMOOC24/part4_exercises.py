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
# List all of the functions for a string
# Can remove print if done at an interpreter prompt
print(dir("this is a string"))
# List all of the functions for a list
print(dir([]))

# To close the interpreter when you are finished use the commands quit() or exit() will close it,
# as will the key combo Control+D (Linux/Mac) or Control+Z (Windows). Especially in
# Visual Studio Code this is important, as trying to execute another Python program
# while the interpreter is still running results in a rather cryptic error message
