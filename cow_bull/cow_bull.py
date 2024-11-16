while True:
    user_input = input("4 digits without duplication: ")
    if len(user_input) == 4 and user_input.isdigit() and len(set(user_input)) == 4:
        print("Valid number")
        print("Now guess:")

        while True:
            check_number = input()
            if check_number == user_input:
                print(f"You guessed my number")
                break
            bull = 0
            cow = 0
            if user_input[0] == check_number[0]:
                bull += 1
            else:
                if check_number[1] == user_input[0] or check_number[2] == user_input[0] or check_number[3] == user_input[0]:
                    cow += 1
            if user_input[1] == check_number[1]:
                bull += 1
            else:
                if check_number[0] == user_input[1] or check_number[2] == user_input[1] or check_number[3] == user_input[1]:
                    cow += 1
            if user_input[2] == check_number[2]:
                bull += 1
            else:
                if check_number[0] == user_input[2] or check_number[1] == user_input[2] or check_number[3] == user_input[2]:
                    cow += 1
            if user_input[3] == check_number[3]:
                bull += 1
            else:
                if check_number[0] == user_input[3] or check_number[1] == user_input[3] or check_number[2] == user_input[3]:
                    cow += 1

            print(f"You guess {cow} Cows and {bull} Bull!")

        else:
            print(f"You guess my number")

    else:
        print("Invalid number. Please, try again.")