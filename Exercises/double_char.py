text = []

while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for char in command:
        text.append(char * 2)
    print("".join(text))
    text = []
