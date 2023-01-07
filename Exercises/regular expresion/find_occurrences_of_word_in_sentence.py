import re

text = input()
word = input()
pattern = fr"\b{word}\b"
matched_words = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(matched_words))

