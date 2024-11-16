name = input("Three or four char name: ")

for i in range(6):
    for j in range(7):
        if (i == 0 and (0 < j < 3 or 3 < j < 6)) \
                or (i == 1 and (j == 0 or j == 3 or j == 6)) \
                or (i == 2 and (j == 0 or j == 6)) \
                or (i == 3 and (j == 1 or j == 5)) \
                or (i == 4 and (j == 2 or j == 4)) \
                or (i == 5 and j == 3):
            print("*", end=" ")
        elif i == 2 and j == 2 and len(name) == 3:
            print(name.upper()[0], end=" ")
        elif i == 2 and j == 3 and len(name) == 3:
            print(name.upper()[1], end=" ")
        elif i == 2 and j == 4 and len(name) == 3:
            print(name.upper()[2], end=" ")
        elif i == 2 and j == 1 and len(name) == 4:
            print(f' {name.upper()[0]}', end=" ")
        elif i == 2 and j == 2 and len(name) == 4:
            print(name.upper()[1], end=" ")
        elif i == 2 and j == 3 and len(name) == 4:
            print(name.upper()[2], end=" ")
        elif i == 2 and j == 4 and len(name) == 4:
            print(name.upper()[3], end="")
        elif i == 3 and j == 3:
            print("❤", end=" ")
        else:
            print(" ", end=" ")

    print()