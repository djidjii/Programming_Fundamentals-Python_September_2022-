import re

information = input()
pattern = r'(=|\/)[A-Z][A-Za-z]{3,}\1'
result = re.finditer(pattern, information)

destinations = []
travel_points = 0

for destination in result:
    current_destination = re.split('\/|=', destination.group())[1]
    travel_points += len(current_destination)
    destinations.append(current_destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
