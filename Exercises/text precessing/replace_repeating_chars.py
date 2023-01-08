text = input()
new_text = ""
letters = ""

for string in text:
    if string != letters:
        new_text += string
        letters = string
print(new_text)
