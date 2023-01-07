import re

bought_furniture = []
total_money = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    valid_information = re.search(pattern, command)
    if valid_information:
        furniture, price, quantity = valid_information.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * float(quantity)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
