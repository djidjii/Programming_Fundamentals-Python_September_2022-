text = input()

while True:
    command = input().split(" ")
    current_command = command[0]

    if current_command == "Done":
        print(f"Your password is: {text}")
        break

    elif current_command == "TakeOdd":
        text = text[1::2]
        print(text)

    elif current_command == "Cut":
        index, length = int(command[1]), int(command[2])
        start_index = index
        end_index = index + length
        text = text[:start_index] + text[end_index:]
        print(text)

    elif current_command == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")


#Siiceercaroetavm!:?:ahsott.:i:nstupmomceqr
#TakeOdd                                         icecream::hot::summer
#Cut 15 3                                        icecream::hot::mer
#Substitute :: -                                 icecream-hot-mer
#Substitute | ^                                  Nothing to replace!
#Done                                            Your password is: icecream-hot-mer
