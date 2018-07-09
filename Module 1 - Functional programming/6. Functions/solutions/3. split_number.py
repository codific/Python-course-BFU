# Using string splitting
user_input = input('Enter a floating-point number: ')
number_parts = user_input.split('.')

whole_part = number_parts[0]
decimal_part = '0' if len(number_parts) == 1 else number_parts[1]

print(f'Whole part: {whole_part}')
print(f'Decimal part: {decimal_part}')


# Using division
# number = float(input('Enter a floating-point number: '))
#
# whole_part = int(number // 1)
# decimal_part = number % 1
#
# print(f'Whole part: {whole_part}')
# print(f'Decimal part: {decimal_part:.2f}')


# Using the modf function from the math module
# from math import modf
#
# number = float(input('Enter a floating-point number: '))
# decimal_part, whole_part = modf(number)
#
# print(f'Whole part: {whole_part}')
# print(f'Decimal part: {decimal_part:.2f}')
