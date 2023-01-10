import re

text = input()
pattern = r'(@|#)+([a-z]{3,})(@|#)+(\W)*?(\/+)(\d+)(\/+)'
result = re.findall(pattern, text)

for color_and_amount in result:
    color_name = color_and_amount[1]
    amount = color_and_amount[-2]
    print(f"You found {amount} {color_name} eggs!")
