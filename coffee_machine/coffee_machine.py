MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
money = {'penny': 0, 'dime': 0, 'nickel': 0, 'quarter': 0}
value_money = {'penny': 1, 'dime': 10, 'nickel': 5, 'quarter': 25}


def money_and_change(user_choice):
    global money
    print("Please insert coins.")

    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dims?: "))
    nickel = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))

    money['quarter'] += quarter
    money['dime'] += dime
    money['nickel'] += nickel
    money['penny'] += penny

    total_inserted = quarter * value_money['quarter'] + dime * value_money['dime'] + nickel * value_money['nickel'] + penny * value_money['penny']

    cost = MENU[user_choice]["cost"] * 100

    if total_inserted > cost:
        total_change = total_inserted - cost
        print(f"Here is ${(total_change / 100):.2f} in change")
        coffee_emoji = "\u2615"
        print(f"Here is your late.{coffee_emoji} Enjoy!")

        while total_change > 0:
            if total_change >= 25 and money['quarter'] > 0:
                money['quarter'] -= 1
                total_change -= 25
            elif total_change >= 10 and money['dime'] > 0:
                money['dime'] -= 1
                total_change -= 10
            elif total_change >= 5 and money['nickel'] > 0:
                money['nickel'] -= 1
                total_change -= 5
            elif total_change >= 1 and money['penny'] > 0:
                money['penny'] -= 1
                total_change -= 1
            else:
                print("Sorry, not enough coins for change. Transaction cancelled.")
                money['quarter'] -= quarter
                money['dime'] -= dime
                money['nickel'] -= nickel
                money['penny'] -= penny
                start_coffee_machine()
                return
        start_coffee_machine()
    else:
        print("Sorry that\'s mot enough money. Money refunded")
        money['quarter'] -= quarter
        money['dime'] -= dime
        money['nickel'] -= nickel
        money['penny'] -= penny
        start_coffee_machine()


def choice_drink(user_choice):
    for item in user_choice:
        if user_choice[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def start_coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        for res, ml in resources.items():
            print(f"{res}: {ml}ml")
        total_sum = 0
        print("Coin inventory:")
        for coin, count in money.items():
            value = value_money[coin]
            total_value = count * value
            total_sum += count * value
            if count:
                print(f"        {int(count)} coins x {value} cents. Total: ${(total_value / 100):.2f}.")

        print(f"Money: ${(total_sum / 100):.2f}")
        start_coffee_machine()

    elif user_choice not in MENU:
        print("Invalid drink selected.")
        start_coffee_machine()
    else:
        drink = MENU[user_choice]
        if choice_drink(drink['ingredients']):
            for item in drink["ingredients"]:
                resources[item] -= drink["ingredients"][item]
            money_and_change(user_choice)


start_coffee_machine()