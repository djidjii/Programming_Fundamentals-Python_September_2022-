data = input()

while True:
    command = input().split(" ")
    current_command = command[0]

    if current_command == "Finish":
        break

    elif current_command == "Replace":
        current_char, new_char = command[1], command[2]
        data = data.replace(current_char, new_char)
        print(data)

    elif current_command == "Cut":
        start_index, end_index = int(command[1]), int(command[2])
        if start_index > 0 and end_index < len(data):
            data = data[:start_index + 1] + data[end_index + 2:]
            print(data)
        else:
            print("Invalid indices!")

    elif current_command == "Make":
        letters = command[1]
        if letters == "Upper":
            data = data.upper()
            print(data)

        elif letters == "Lower":
            data = data.lower()
            print(data)

    elif current_command == "Check":
        text = command[1]
        if text in data:
            print(f"Message contains {text}")
        else:
            print(f"Message doesn't contain {text}")

    elif current_command == "Sum":
        total_sum = 0
        start_index, end_index = int(command[1]), int(command[2])
        substring = data[start_index:end_index + 1]

        if start_index > 0 and end_index > 0:
            for letters in substring:
                total_sum += ord(letters)
            if end_index < len(data):
                print(total_sum)
            else:
                print("Invalid indices!")
        else:
            print("Invalid indices!")
