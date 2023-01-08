text = input()

new_text = ""
for character in text:
    new_symbol = chr(ord(character) + 3)
    new_text += new_symbol

print(new_text)

