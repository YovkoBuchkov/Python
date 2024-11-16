def print_number_diamond(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ''.join(str(x) for x in range(1, i + 1)) + ''.join(str(x) for x in range(i - 1, 0, -1)))

    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + ''.join(str(x) for x in range(1, i + 1)) + ''.join(str(x) for x in range(i - 1, 0, -1)))


num_rows = int(input())
print_number_diamond(num_rows)
