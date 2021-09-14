# Part 2..........

# Lists

numbers = [1, 2, 3, 4, 5]

print(numbers[1])
print(numbers[-0])
# - index start from the end of the list (i.e. the right)
print(numbers[-1])
print(numbers[-2])

numbers2 = [10, 9, 8, 7, 6]
# concatenate lists using the '+' operator
all_numbers = numbers + numbers2

# sort reorders the current list (list method)
all_numbers.sort()
print(all_numbers)

# sorted creates a new list
num3 = sorted(all_numbers, reverse=True)
print(num3)
