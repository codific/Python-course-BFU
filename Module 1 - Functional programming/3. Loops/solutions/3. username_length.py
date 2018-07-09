min_username_length = 4

while True:
    username = input('Enter a username: ')
    if len(username) < min_username_length:
        continue

    print('Valid username.')
    break