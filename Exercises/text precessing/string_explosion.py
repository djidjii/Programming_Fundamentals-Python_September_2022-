strings = input()
new_text = ""
strength = 0

for index in range(len(strings)):
    if strength > 0 and strings[index] != ">":
        strength -= 1
    elif strings[index] == ">":
        new_text += strings[index]
        strength += int(strings[index + 1])
    else:
        new_text += strings[index]
print(new_text)
