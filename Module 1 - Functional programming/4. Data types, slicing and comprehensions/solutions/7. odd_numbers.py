n = int(input('Enter a number: '))

odd_numbers = [str(number) for number in range(1, n + 1) if number % 2 == 1]

print(f'Odd numbers in the range 1..{n}:')
print(', '.join(odd_numbers))
