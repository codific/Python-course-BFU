fruits = []
commands = ('add', 'remove', 'list', 'exit')

while True:
    user_input = input('Enter a command: ')
    if not user_input:
        print('Invalid input.')
        continue

    splitted_input = user_input.split(' ')
    command = splitted_input[0]
    if command not in commands:
        print('Unknown command. Available commands are: ' + ', '.join(commands))

    if command == 'exit':
        print('Exiting...')
        break
    elif command == 'list':
        if len(fruits) == 0:
            print('The basket is empty.')
            continue

        print('Fruits in the basket:')
        for idx, fruit in enumerate(fruits, start=1):
            print(f'{idx}. {fruit}')
    elif command == 'add':
        # Should contain the add command and fruit e.g. ['add', 'fruit']
        if len(splitted_input) != 2:
            print('Invalid fruit to add.')
            continue

        fruit_to_add = splitted_input[1]
        fruits.append(fruit_to_add)
    elif command == 'remove':
        # Should contain the remove command and fruit e.g. ['remove', 'fruit']
        if len(splitted_input) != 2:
            print('Invalid fruit to remove.')
            continue

        fruit_to_remove = splitted_input[1]
        if fruit_to_remove not in fruits:
            print(f'{fruit_to_remove.title()} is not in the basket.')
            continue
        fruits.remove(fruit_to_remove)

