text_1 = input()
text_2 = input()
last_string = text_1

for i in range(len(text_1)):
    left_part = text_2[:i + 1]
    right_part = text_1[i + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string