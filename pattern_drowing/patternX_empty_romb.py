n = 7  # Размерът на ромба (трябва да е нечетно число)

for i in range(n):
    for j in range(n):
        if abs(n // 2 - i) + abs(n // 2 - j) <= n // 2:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()


n = 7  # Размерът на ромба (трябва да е нечетно число)

for i in range(n):
    for j in range(n):
        if (i + j == n // 2) or (j - i == n // 2) or (i - j == n // 2) or (i + j == (n - 1) + n // 2):
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()