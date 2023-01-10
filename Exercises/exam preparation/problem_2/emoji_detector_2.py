import re

data = input()
emoji_pattern = r"(\*|:){2}([A-Z][a-z]{2,})(\1){2}"
threshold_pattern = r"\d"

emoji_result = re.findall(emoji_pattern, data)
threshold = re.findall(threshold_pattern, data)

threshold = [int(x) for x in threshold]
threshold_result = 1
for num in threshold:
    threshold_result *= num

emoji_count = 0
symbol_result = 0

print(f"Cool threshold: {threshold_result}")
for c_emoji in emoji_result:
    emoji_count += 1
    if emoji_count == len(emoji_result):
        break
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in emoji_result:
    current_emoji = emoji[1]
    left_pattern = emoji[0] * 2
    right_pattern = emoji[2] * 2
    for char in current_emoji:
        current_character = ord(char)
        symbol_result += current_character
        if symbol_result > threshold_result:
            symbol_result = 0
            print(f"{left_pattern}{current_emoji}{right_pattern}")
            break