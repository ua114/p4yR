# Basic Arithematic Operations

# x = 123 + 64
# print(x)
#
# y = 123 * 64
# print(y)
#
# z = 123 ** 64
# print(z)
#
# a = 123 / 64
# print(a)
#
# b = 123 // 64 # Integer division
# print(b)
#
# # Extra commands that use the math module
# import math
#
# c = math.factorial(5)
# print(c)

# Using random module

# import random
#
# d = random.choice([2,44,55,66]) #Picks a random number from the list
# print(d)
#
# e = random.choice(['apple','orange','banana'])
# print(e)

# Boolean operators

# print(type(True))
#
# print(True or False)
# print(False or False)
# print(True and False)
# print(not True)
#
# a = [1,2,4]
# b = [1,2,4]
# c = [3,5,6]
#
# # Comparative statmenets return True or False
# print(a == b)
# print(a != b)
# print(a == c)
# print(c > a)
#
# print(a is b) # False as a and b contain the same but are diff objects

# == tests whether objects have the same value, whereas is tests whether...
# ...objects have the same identity.
# Part 2..........

# Lists

# numbers = [1, 2, 3, 4, 5]
#
# print(numbers[1])
# print(numbers[-0])
# # - index start from the end of the list (i.e. the right)
# print(numbers[-1])
# print(numbers[-2])
#
# numbers2 = [10, 9, 8, 7, 6]
# # concatenate lists using the '+' operator
# all_numbers = numbers + numbers2
#
# # sort reorders the current list (list method)
# all_numbers.sort()
# print(all_numbers)
#
# # sorted creates a new list
# num3 = sorted(all_numbers, reverse=True)
# print(num3)

# Tuples.........
# They are immutable sequences of objects

# indeing Tuples

# T = (1,2,3,4)
# print(T[1])
#
# # Packing and unpacking Tuples
# x = 5
# y = 10
# cordinate = (x,y)
#
# (c1,c2) = cordinate
# print(type(c1))
#
# # Using tuples to loop
# cordinates = [(0,0),(1,2),(2,4),(3,6)]
#
# for x,y in cordinates:
#     print(x,y)

# Constructing a one value tuple

# t1 = (2,)
# print(type(t1))
# t2 = (2)
# print(type(t2)) # Output is an integer
#
# x = (1,2,3)
# print(x.count(3))
# print(sum(x)

# Ranges.....
# ranges are immutable sequences of integers
# range(start, stop, step)

a = list(range(5))
print(a)

b = range(1,6) # Range starts at 1 and ends at 5
for number in b:
    print(number)

c = range(0,11,2)
print(list(c))
