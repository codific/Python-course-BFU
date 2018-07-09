n = int(input('How many Fibonacci numbers to print: '))

first, second = 0, 1

for number in range(1, n + 1):
    print(first)
    first, second = second, first + second