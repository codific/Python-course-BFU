def sum_of_numbers(*args):
    sum = 0

    for arg in args:
        sum += arg

    return sum


result = sum_of_numbers(1, 2.84, 3, 4, 5, 6.12, 7)
print(result)