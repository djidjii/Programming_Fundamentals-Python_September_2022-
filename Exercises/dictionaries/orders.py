product_information = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = input().split()

    if name not in product_information.keys():
        product_information[name] = [0.00, 0]
    product_information[name][0] = float(price)
    product_information[name][1] += int(quantity)


for key, value in product_information.keys():
    total = value[0] * value[1]
    print(f"{key} -> {total:.2f}")