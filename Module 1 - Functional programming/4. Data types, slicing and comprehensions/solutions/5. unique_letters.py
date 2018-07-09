from string import ascii_lowercase

user_input = input('Enter some string: ')

unique_symbols = set(user_input.lower())

unique_letters = []

for symbol in unique_symbols:
    if symbol in ascii_lowercase:
        unique_letters.append(symbol)

sorted_unique_letters = sorted(unique_letters)
print('Unique letters: ' + ', '.join(sorted_unique_letters))