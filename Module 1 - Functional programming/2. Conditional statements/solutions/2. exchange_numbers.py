first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

print('Original values:')
print(f'First number: {first_number}')
print(f'Second number: {second_number}')

# Classical approach with a temp variable
# temp_number = first_number
# first_number = second_number
# second_number = temp_number

# Using tuple unpacking
first_number, second_number = second_number, first_number

print('Exchanged values:')
print(f'First number: {first_number}')
print(f'Second number: {second_number}')