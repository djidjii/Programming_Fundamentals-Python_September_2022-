budget = float(input())
kg_flour = float(input())

bread_counter = 0
eggs_counter = 0

eggs_price = kg_flour * 0.75
milk_price = kg_flour * 1.25 / 4
price_one_bread = kg_flour + eggs_price + milk_price

while budget >= price_one_bread:
    budget -= price_one_bread
    bread_counter += 1
    eggs_counter += 3
    if bread_counter % 3 == 0:
        eggs_counter -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")