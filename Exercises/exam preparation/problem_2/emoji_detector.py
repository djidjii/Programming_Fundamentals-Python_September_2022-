import re

text = input()
emoji_pattern = r"(\*{2}|:{2})([A-Z][a-z]{2,})(\1)"
result = re.findall(emoji_pattern, text)
valid_emojis = []
counter = 0

digit_pattern = r"\d"
all_digits = re.findall(digit_pattern, text)
cool_threshold = 1

for digit in all_digits:
    cool_threshold *= int(digit)

print(f"Cool threshold: {cool_threshold}")

for emoji in result:
    current_coolness = 0
    for character in emoji[1]:
        if character == "*" or character == ":":
            continue
        else:
            current_coolness += ord(character)

    if current_coolness >= cool_threshold:
        valid_emojis.append(emoji[0]+emoji[1]+emoji[0])
    counter += 1

print(f"{counter} emojis found in the text. The cool ones are:")
print(f'\n'.join(valid_emojis))


# In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**

# Cool threshold: 540
# 4 emojis found in the text. The cool ones are:
# ::Smiley::
# **Tigers**
# ::Mooning::
