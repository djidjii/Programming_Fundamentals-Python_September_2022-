data = input()

while True:
    command = input().split(" ")
    current_command = command

    if current_command[0] == "For" and current_command[1] == "Azeroth":
        break

    elif current_command[0] == "GladiatorStance":
        data = data.replace(data, data.upper())
        print(data)

    elif current_command[0] == "DefensiveStance":
        data = data.replace(data, data.lower())
        print(data)

    elif current_command[0] == "Dispel":
        index, letter = int(command[1]), command[2]
        if index <= len(data):
            data = data.replace(data[index], letter)
            print("Success!")
        else:
            print("Dispel too weak.")

    elif current_command[0] == "Target" and current_command[1] == "Change":
        first_substring, second_substring = command[2], command[3]
        if first_substring in data:
            data = data.replace(first_substring, second_substring)
            print(data)
        else:
            print(data)

    elif current_command[0] == "Target" and current_command[1] == "Remove":
        substring = command[2]
        if substring in data:
            data = data.replace(substring, '')
            print(data)
        else:
            continue

    else:
        print("Command doesn't exist!")
