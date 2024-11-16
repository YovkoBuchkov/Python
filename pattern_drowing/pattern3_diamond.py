n = int(input()) # odd number

for i in range(n):
    for j in range(n):
        if abs(n // 2 - i) + abs(n // 2 - j) <= n // 2:
            print('*', end="")
        else:
            print('', end=" ")
    print()



# def print_number_diamond(n):
#     for i in range(1, n + 1):
#         print(' ' * (n - i) + ' '.join(str(x) for x in range(1, i + 1)))
#
#     for i in range(n - 1, 0, -1):
#         print(' ' * (n - i) + ' '.join(str(x) for x in range(1, i + 1)))
#
#
# num_rows = int(input())
# print_number_diamond(num_rows)