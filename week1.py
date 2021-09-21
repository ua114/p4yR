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

# ...........................................................................
# Part 2
# ...........................................................................

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

# a = list(range(5))
# print(a)
#
# b = range(1,6) # Range starts at 1 and ends at 5
# for number in b:
#     print(number)
#
# c = range(0,11,2)
# print(list(c))

# Sets.........
# sets are unordered collections of distinct hashable objects
# They can be used for immubtable objects like numbers and strings but not for
# mutable objects like lists and dictionnaries
# There are two types of sets: sets and frozen sets
# The difference is that frozen sets once created are not mutable
# sets cannot be indexed

# num = set([1,2,3,3,4,5,6])
# print(num)
#
# num.add(7)
# print(num)
#
# num.add(7) #7 is already present do doesnt add
# print(num)
#
# # Intersections and unions
# vegetables = set(['carrot','potato','onion','tomato'])
# fruits = set(['tomato','banana','orange'])
#
# all = vegetables | fruits
# print(all)
#
# both = vegetables & fruits
# print(both)

# x = {1,2,3}
# y = {2,3,4}
# z = {4,5,6}
#
# print(x | y | z)
#
# # x1.difference(x2) and x1 - x2 return the set of all elements that are
# # in x1 but not in x2
#
# x1 = {'foo', 'bar', 'baz'}
# x2 = {'baz', 'qux', 'quux'}
#
# print(x1 - x2)
# x3 = x1.difference(x2)
# print(x3)
#
# # x1.symmetric_difference(x2) and x1 ^ x2 return the set of all
# # elements in either x1 or x2, but not both:
#
# x4 = x2.symmetric_difference(x1)
# print(x4)

# The ^ operator also allows more than two sets, .symmetric_difference does not
# a = {1, 2, 3, 4, 5}
# b = {10, 2, 3, 4, 50}
# c = {1, 50, 100}
# print(a ^ b ^ c)
#
# # Determine whether one set is a subset of the other.
# d = {1,2,3,4}
# e = {1,2,3,4,5,6}
# print(d.issubset(e))

# More set commands on https://realpython.com/python-sets/

# Dictionnaries...
# Dictionaries consists of Key:Value pairs, where the keys must be immutable

# ...........................................................................
# Part3
# ...........................................................................

# Dynamic typing...
# For more explainations, watch Video 1.3.1: Dynamic Typing


# l1 = [2,3,4]
# l2 = l1
# print(l1,l2)
# l1[0] = 24
# print(l1,l2)
# # Because python uses dynamic typing, both variables l1 and l2, reference the
# # same object
#
# x = 7
# y = x
# print(x,y)
# y = y -1
# print(x,y)
#Because 3 is an immutable object, y must refer to a new object when reduced
# by 1, leaving the value of x unchanged.

# # Each object in Python has a type, value, and an identity
# # Mutable objects in Python can be identical in content
# # and yet be actually different objects.
#
# L = [1,2,3]
# M = [1,2,3]
# print(L == M)
# print(L is M)
#
# # The id function corresponds to the object's location in memory
#
# print(id(L))
# print(id(M))

# By typing list parentheses L, Python will create a completely new object
# or by using M = L[:]
# L = [1,2,3]
# M = list(L)
# M[0] = 4
# print(L,M)

# Copies...
# There are two types of copies that are available.
# A shallow copy constructs a new compound object
# and then insert its references into it to the original object.
# In contrast, a deep copy constructs a new compound object and then
# recursively inserts copies into it of the original objects.

# import copy
# L = [1,2,3]
# x = copy.copy(L)
# y = copy.deepcopy(L)
# print(L,x,y)
# L[0] = 4
# print(L,x,y)

# List comprehensions....
# More info on https://www.w3schools.com/python/python_lists_comprehension.asp
# conducting operations on all members of a lists

# 1st way - using loops
# numbers = range(10)
# squares = list()
#
# for number in numbers:
#     square = number**2
#     squares.append(square)
# print(squares)
#
# # 2nd way - list comprehension method
#
# squares2 = [number**2 for number in numbers]
# print(squares2)
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [fruit for fruit in fruits if fruit == "mango"]
# print(newlist)

# sum the odd numbers from 0 to 9
# numbers = range(10)
# x = sum([number for number in numbers if number%2 != 0])
# print(x)

# limit = 10
# numbers = range(2,limit+1)
# primes = list()
# for num in numbers:
#     test_num = range(2,num)
#     for i in test_num:
#         if num%i == 0:
#             continue
# print(primes)

# l1 = range(3)
# l2 = range(10,31,10)
#
# for i in l1:
#     for j in l2:
#         if i==2 and j==20:
#             print('Break')
#             break
#         print(i,j)

# l1 = [1, 2, 3]
# l2 = [10, 20, 30]
# for i in l1:
#     print('Start outer loop')
#
#     for j in l2:
#         print('--', i, j)
#         if i == 2 and j == 20:
#             print('-- BREAK inner loop')
#             break
#     else:
#         print('-- Finish inner loop without BREAK')
#         continue
#
#     print('BREAK outer loop')
#     break

# Files.................

# Creating and looping through a file
# F = open('output.txt','w') #'w' tells python a file is being written
# F.write('Hello\nHow is it going\nDoes this actually work\n') #using .write() to write to the file
# F.close()
#
# fopen = open('output.txt')
# for line in fopen:
#     line = line.rstrip()
#     print(line)

# Functions...............
# all names created or assigned in a function are local of that function
# and they exist only while the function runs.

# def multiply(a,b):
#     product = a * b
#     return product
#
# print(multiply(3,7))
#
# # Using tuples to return multiple values
#
# def multiply_and_divide(a,b):
#     product = a*b
#     quotient = a/b
#     return (product,quotient)
#
# print(multiply_and_divide(2,4))
#
# # Functions can also be renamed and used
#
# def add(a,b):
#     mysum = a + b
#     return mysum
#
# print(add(2,3))
#
# newadd = add
# print(newadd(5,7))

# Functions on mutable objects

# def mylist(a):
#     a[0] /= 2
#     return(a)
#
# b = mylist([4,6,8])
# print(b)

# More function examples......

# unique list function

# def unique(l1,l2):
#     union = []
#     for x in l1:
#         if x not in l2:
#             union.append(x)
#     for y in l2:
#         if y not in l1:
#             union.append(y)
#     return union
#
# print(unique([1,2,3,4],[3,4,5,6]))

# Generate a random password

# import random
#
# def password(length):
#     pw = str()
#     characters = 'abcdefghijklmnopqrestuvwxyz' + '0123456789'
#     # this will returnone of the characters chosen at random
#     for i in range(length):
#         pw += random.choice(characters)
#     return pw
# print(password(10))

# Factroial funcion

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#     	N = 1
#     for i in range(1, n+1):
#         N *= i
#     return(N)
#
# print(factorial(5))

# ...........................................................................
# Questions
# ...........................................................................

# Working towards monte carlo method for pi..........

# Distance between 2 points

def distance(x, y):
    length = math.sqrt( ((y[0])**2 - (x[0])**2) + (y[1]**2 - x[1]**2) )
    return(length)

distance((0,0),(1,1))

# Determine if point lies in circle

# method 1
def in_circle(x, origin = [0,0]):
    if x[0]**2 + x[1]**2 <= 1:
        return True
    else:
        return False

in_circle((1,1),)

# method 2 - using distance function made earlier
def in_circle(x, origin = [0,0]):
    if distance( (x[0],x[1]) , tuple(origin) )  <= 1:
        return True
    else: return False

in_circle((1,1),)

# Create a list inside of R=10000 booleans that determines whether or not
# a point falls within the unit circle centered at (0,0)
R = 1000
inside = list()
for i in range(1,R+1):
    x = rand()
    y = rand()
    inside.append( in_circle((x,y),) )
monte_carlo = inside.count(True)/R
print(monte_carlo)

difference = monte_carlo - math.pi/4
print(difference)
