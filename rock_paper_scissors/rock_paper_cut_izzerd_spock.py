import random


def battle(user_choice, computer_choice):
    choice_list = {
        1: "rock",
        2: "scissors",
        3: "paper",
        4: "lizard",
        5: "spock"
    }
    user_pick = choice_list[user_choice]
    if user_pick == computer_choice:
        status = f"{choice_list[user_choice]} == {computer_choice} - Draw! \U0001F62C"
    elif (user_pick == "rock" and computer_choice == "scissors") or \
         (user_pick == "scissors" and computer_choice == "paper") or \
         (user_pick == "paper" and computer_choice == "rock") or \
         (user_pick == "rock" and computer_choice == "lizard") or \
         (user_pick == "scissors" and computer_choice == "lizard") or \
         (user_pick == "paper" and computer_choice == "spock") or \
         (user_pick == "lizard" and computer_choice == "paper") or \
         (user_pick == "lizard" and computer_choice == "spock") or \
         (user_pick == "spock" and computer_choice == "scissors") or \
         (user_pick == "spock" and computer_choice == "rock"):
        bite = "bite"
        status = f"{choice_list[user_choice]} {bite} {computer_choice} - You win!  \U0001F600 "
    else:
        status = f"{computer_choice} => {choice_list[user_choice]} - Computer wins! \U0001F612"
    return status


def main_menu():
    choice = int(input("1. Rock \u270A, "
                       "2. Scissors \u270C\uFE0F, "
                       "3. Paper \u270B, "
                       "4. Lizard \U0001F98E, "
                       "5. Spock \U0001F596\n"
                       "Enter the number of your choice (1-5): "))
    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid choice! Please try again.")
        main_menu()
    desk = ["rock", "scissors", "paper", "lizard", "spock"]
    computer = random.choice(desk)
    result = battle(choice, computer)
    print(result)
    main_menu()


if __name__ == "__main__":
    main_menu()




