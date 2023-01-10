activation_key = input()

while True:
    command = input().split(">>>")
    current_command = command[0]

    if current_command == "Generate":
        print(f"Your activation key is: {activation_key}")
        break

    elif current_command == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current_command == "Flip":
        letters, start_index, end_index = command[1], int(command[2]), int(command[3])
        key = activation_key[start_index:end_index]

        if letters == "Upper":
            activation_key = activation_key.replace(key, key.upper())
            print(activation_key)

        elif letters == "Lower":
            activation_key = activation_key.replace(key, key.lower())
            print(activation_key)

    elif current_command == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)


# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6                 abghijklmnopqrstuvwxyz
# Flip>>>Upper>>>3>>>14         abgHIJKLMNOPQRstuvwxyz
# Flip>>>Lower>>>5>>>7          abgHIjkLMNOPQRstuvwxyz
# Contains>>>def                Substring not found!
# Contains>>>deF                Substring not found!
# Generate                      Your activation key is: abgHIjkLMNOPQRstuvwxyz

