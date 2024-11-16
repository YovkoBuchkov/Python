for i in range(6):
    for n in range(7):
        if (i == 0 and n % 3 != 0) or (i == 1 and n % 3 == 0) or (i - n == 2) or (i + n == 8):
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()


def print_heart(size):
    for i in range(size//2, size, 2):
        for j in range(1, size-i, 2):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        for j in range(1, size-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        print()

    for i in range(size, 0, -1):
        for j in range(i, size):
            print(" ", end="")
        for j in range(1, i*2):
            print("*", end="")
        print()

# Пример за използване на функцията
print_heart(6)
