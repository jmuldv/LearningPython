# def output_sum(first, second):
#     print(first + second)

# output_sum(1, 2)
# output_sum(10, 25)
# output_sum("ab", "cd")

# def shout(message):
#     message += "!!!!"
#     # message = "New message!"
#     print(message)


# shout("Hello")
# # print(message)   # This does not work
# shout("How are you")


# name = "Peter Python"
# length = len(name)
# print(length * 2)


# def multiply(first, second):
#     return first * second
#     # print(first * second)

# # This does not work unless a "return" is used...and a print statement is used.
# print(multiply(10, 20) + multiply(30, 40))
# result = multiply(10, 10) * 5
# print(result)


# def factorial(n):
#     k = n
#     result = 1
#     while k >= 2:
#         result *= k
#         k -= 1
#     return result

# print(factorial(5))
# result = factorial(3) + factorial(5) + factorial(7)
# print(result)


# def truncate_string(string):
#     string = string[1:-1]
#     return string

# print(truncate_string("Hello"))
# s = input("Give a string: ")
# print(f"The string truncated is {truncate_string(s)}")
# s = truncate_string(truncate_string(s))
# print(s)

# def add_one(number):
#     return number + 1


# def sub_one(number):
#     return number - 1


# # num = add_one(add_one(add_one(1)))   #4
# num = add_one(sub_one(5))
# print(num)

# Variables have a type but we don't need to define the type.
# name = "Peter"
# age = 54
# height = 175.5

# def join(first: int, second: int):  # Added type hints
#     return first + second


# print(join(10, 20))  # 30
# print(join("abc", "def"))  # abc def
# print(join("abc", 10))    # throws an error.
# result = join(20, 30)


# def factorial(n: int):
#     print(n)

# factorial(10.5)
# factorial(True)

# def join(first: int, second: int) -> float: # The return type isn't needed but it can be expressly stated.
#     return float(first + second)

# join()

# def do_something(n: int):
#     print("Hello")
#     return n * 2        # Return is like a break on a function.
#     print("Hello again")

# do_something(4)


# def get_larger(number1: int, number2: int):
#     if number1 > number2:
#         return number1
#     else:
#         print("The second number is larger!")


# n1 = 10
# n2 = 30
# print(get_larger(n1, n2))
# The second number is larger!
# None     # None is output because no value was returned.
# In the above example, it would be best to have a return statement in both if and else.


# This is another way the above could be written but using else is a bit more clear..
# def get_larger(number1: int, number2: int):
#     if number1 > number2:
#         return number1

#     return number2

# n1 = 10
# n2 = 60
# print(get_larger(n1, n2))


# name1 = "Peter"
# name2 = "Paul"
# name3 = "Mary"
# name4 = "Anne"
# # If I wanted to add a ! at the end of each, I'd need to write each out like this...
# name1 += "!"   # ...and so on.
# # Instead of the above, you'd want a data structure

# names = ["Peter", "Paul", "Mary", "Anne"]
# results = [1, 3, 4, 2, 4, 5, 4, 4, 56, 7, 3, 2, -1]
# print(names)  # Prints entire list
# print(results)  # Prints entire list
# print(names[0])  # Prints Peter
# print(names[-1])  # Prints Anne
# print(len(names))  # Prints 4
# # Difference between lists and strings is lists are mutable (can append)
# names.append("John")
# names.append("Jane")
# print(names)


numbers = []

while True:
    num = int(input("Give a number, 0 stops: "))
    if num == 0:
        break

    numbers.append(num)

print(numbers)
