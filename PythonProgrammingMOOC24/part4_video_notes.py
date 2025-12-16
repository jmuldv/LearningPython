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

def add_one(number):
    return number + 1


def sub_one(number):
    return number - 1


# num = add_one(add_one(add_one(1)))   #4
num = add_one(sub_one(5))
print(num)
