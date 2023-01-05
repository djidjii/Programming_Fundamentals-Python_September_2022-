def inventory_fnc(items):

    while True:
        command = input().split(" ")

        if command == "END":
            # print(f"{element1}, {element2}, {element3}, … {elementN}")
            break

        if command == "add to start":
            num = command[3:1]
            items.append(num)

        elif command == "replace":
            old_num, new_num = command[1], command[2]
            items.replace(old_num, new_num)

        elif command == "remove":
            command = command[3]
            for i in items:
                if i > 5:
                    items.remove(command)

        elif command == "find even":
            even_numbers = map(lambda x: x if items[x] % 2 == 0 else range(len(items)))
            print(even_numbers)

        elif command == "find odd":
            odd_numbers = map(lambda x: x if items[x] % 2 != 0 else range(len(items)))
            print(odd_numbers)


numbers_list = input().split(" ")
inventory_fnc(numbers_list)
