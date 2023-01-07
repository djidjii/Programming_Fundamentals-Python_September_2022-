import re

match_date = r"(\d{2})(\/|.|-)([A-Z][a-z]{2})\2(\d{4})"
date = input()
result = re.findall(match_date, date)
for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
