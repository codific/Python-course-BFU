username = input('Enter a username: ')

min_username_length = 4

if len(username) < min_username_length:
    print('Error! The username must be at least 4 characters long.')
else:
    print('Username registered.')