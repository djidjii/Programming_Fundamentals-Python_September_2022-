import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = input()
matches_number = re.finditer(pattern, numbers)

for match in matches_number:
    print(match.group(), end=" ")
