def main_menu():
    choice = input("1. Strings\n"
                   "2. Numbers\n"
                   "3. Booleans\n"
                   "4. Additional Data Types (List, Tuple, Dictionary)\n"
                   "Enter the number of your choice (1-4): ")

    if choice == '1':
        sentence = "Learning Python is fun!"
        extract_substring = sentence[9:16]
        print(extract_substring)
        extract_substring_uppercase = extract_substring.upper()
        print(extract_substring_uppercase)
        sentence = sentence.replace("fun", "awesome")
        print(sentence)

    elif choice == '2':
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        print(f"Addition: {num1 + num2}")
        print(f"Subtraction: {num1 - num2}")
        print(f"Multiplication: {num1 * num2}")
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Division: {num1 / num2}")
        print(f"{num1} raised to the power of {num2} is: {num1 ** num2}")

    elif choice == '3':
        is_python_fun = input("Is Python fun? Write True or False:")
        is_sunny = input("Is Sunny? Write True or False:")
        if is_python_fun and not is_sunny:
            print("Learning Python is fun, but the weather is not sunny.")
        elif is_python_fun or is_sunny:
            print("Learning Python is fun, and maybe sunny.")
        else:
            print("There is no rainbow in the sky.")

    elif choice == '4':
        choice2 = input("1.List\n"
                        "2.Tuple\n"
                        "3.Dictionary\n"
                        "Enter the number of your choice (1-3): ")

        if choice2 == '1':
            lst = [1, 2, 3, True, "Expeliamus", False, "Crucio"]
            lst.append("Aveda cadabra")
            print(lst)
            print("Fifth symbol in list is:")
            print(lst[4])
        elif choice2 == "2":
            tpl = ("apple", "banana", "strawberry")
            print(len(tpl))
            try:
                tpl[2] = "patato"
            except TypeError as e:
                print("Try to change tuple object:")
                print(f"Oops! Caught an error: {e}")

        elif choice2 == "3":
            dicts = {"name": "Ivan",
                     "age": 25,
                     "city": "Sofia"}

            print(dicts["age"])
            print("Add new value in dictionary 'hobby'")
            dicts["hobby"] = "read books"
            print(dicts)
    else:
        print("Invalid choose. Please try again")
        main_menu()


main_menu()

