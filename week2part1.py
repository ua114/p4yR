# ...........................................................................
# Scope Rules
# ...........................................................................
# LEGB rule
# L stands for "local," E stands for "enclosing function," G for "global,"
# and B stands for "built-in."
# local is the current function you're in.
# Enclosing function is the function that called the current function, if any.
# Global refers to the module in which the function was defined.
# And built-in refers to Python's built-in namespace.

# global layer or scope does contain an object called x
# def update():
#     x.append(1)
#
# x = [1,2]
# update()
# print(x)

# This example focusing in scope rules shows that you can manipulate
# global variables, variables defined in the global scope, from within functions.
# Functions that modify either their inputs or objects defined in other parts
# of the program in this type of behind the scenes manner are said
# to have "side effects."

# update acts on the variables n and x defined in main while the final print
# statement calls the local variables n,x defined in main
# def update(n,x):
#     n = 2
#     x.append(4)
#     print('update: ',n,x)
#
# def main():
#     n = 5
#     x = [1,2,3]
#     print(n,x)
#     update(n,x)
#     print(n,x)
#
# main()
#
# # Another example
# def increment(n):
#     n += 1
#     print(n)
#
# n = 1
# increment(n)
# print(n)
# While n is defined globally on line 3, it is also defined locally in increment
# Therefore, the function will print one greater than 1 due to the function
# and its argument, but the local n will not change.

# ...........................................................................
# Classes
# ...........................................................................
# Also see chapter 14 in py4e for more info
# By convention, the name of the class instance is called "self",

# class mylist(list):
#     def remove_min(self):
#         self.remove(min(self))
#     def remove_max(self):
#         self.remove(max(self))

# x = [1,2,3,4,5]
# y = mylist(x)
# y.remove_min()
# print(y,x)
