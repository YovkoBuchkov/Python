list_data = list(map(int, input().split()))
command = input()
while command != "end":
    if command == "decrease":
        list_data = list(map(lambda n: n - 1, list_data))
        #list_data = [n - 1 for n in list_data]
        #koitui = f"decrease - all - 1"
    else:
        command_todo = command.split(" ")
        com_0 = command_todo[0]
        com_1 = int(command_todo[1])
        com_2 = int(command_todo[2])

        if com_0 == "swap":
            list_data[com_1], list_data[com_2] = list_data[com_2], list_data[com_1]
            #koitui = f"{com_0} {com_1}({list_data[com_2]}) and {com_2}({list_data[com_1]})"
        elif com_0 == "multiply":
            list_data[com_1] = list_data[com_1] * list_data[com_2]

    command = input()


print(", ".join(map(str, list_data)))
print(list_data, sep=",")