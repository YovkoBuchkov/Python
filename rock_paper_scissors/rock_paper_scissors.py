import random


def battle(user_choice, computer_choice):
    choice_list = {
        1: "rock",
        2: "scissors",
        3: "paper"
    }
    user_pick = choice_list[user_choice]
    if user_pick == computer_choice:
        status = f"{choice_list[user_choice]} == {computer_choice} - Draw!"
    elif (user_pick == "rock" and computer_choice == "scissors") or \
         (user_pick == "scissors" and computer_choice == "paper") or \
         (user_pick == "paper" and computer_choice == "rock"):
        status = f"{choice_list[user_choice]} => {computer_choice} - You win! "
    else:
        status = f"{computer_choice} => {choice_list[user_choice]} - Computer wins! "
    return status


def main_menu():
    choice = int(input("1. Rock\n"
                       "2. Scissors\n"
                       "3. Paper\n"
                       "Enter the number of your choice (1-3): "))
    if choice not in [1, 2, 3]:
        print("Invalid choice! Please try again.")
        main_menu()
    desk = ["rock", "scissors", "paper"]
    computer = random.choice(desk)
    result = battle(choice, computer)
    print(result)
    main_menu()


if __name__ == "__main__":
    main_menu()



# →
# ®
# print("\u270A")  # Rock :fist:
# print("\u270B")  # Paper :raised_hand:
# print("\u270C")  # Scissors ✌
# print("\u1FAA8")  # Rock
# print("\u1F9C2")  # Paper
# print("\u1F9C7")  # Scissors
# print("\u270A\u270B")  # Rock vs Paper
# print("\u270A\u270C")  # Rock vs Scissors
# print("\u270B\u270C")  # Paper vs Scissors
# print("\u270A\u270A")  # Rock vs Rock
#
# print("\U0001F596")
# print("\U0001F98E")






