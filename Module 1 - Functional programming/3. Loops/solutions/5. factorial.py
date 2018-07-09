number = int(input('Enter a number: '))

# Classical approach using for loop
fac = 1

for n in range(1, number + 1):
    fac *= n


# Using the math module
# from math import factorial
# fac = factorial(number)

print(f'{number}! = {fac}')