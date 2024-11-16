#Write a Python script that prints a square pattern where stars and dashes alternate in each row.
# The size of the square should be provided by the user. Here's an example for user input of 5:


size = int(input())
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print('-', end='')
    print()

