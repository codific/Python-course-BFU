# sample input - 1 2 3 4 5 apple orange banana 7.12
user_input = input('Enter list items (separated with an interval): ')

list_items = user_input.split(' ')

# e.g. 5
n = int(input('Enter the number of items you would like to get from that list: '))

def get_first_n(items, n):
    if len(items) < n:
        return 'The list does not have that many items.'

    result_items = []

    for i in items[:n]:
        result_items.append(i)

    return ', '.join(result_items)


result = get_first_n(list_items, n)
print(result)