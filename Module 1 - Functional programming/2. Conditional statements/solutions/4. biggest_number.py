first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
third_number = float(input('Enter the third number:'))

biggest_number = 0

# Classical approach using if/elif statements
# if first_number > second_number and first_number > third_number:
#     biggest_number = first_number
# elif second_number > first_number and second_number > third_number:
#     biggest_number = second_number
# else:
#     biggest_number = third_number

# We can also use the built-in function max
biggest_number = max(first_number, second_number, third_number)

print(f'The biggest number is: {biggest_number}')