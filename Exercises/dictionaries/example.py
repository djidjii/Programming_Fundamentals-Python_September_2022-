orders = {}

while True:

    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split()

    if name not in orders.keys():
        orders[name] = [0.00, 0]
    orders[name][0] = float(price)
    orders[name][1] += int(quantity)


for key, value in orders.items():
    total = value[0] * value[1]
    print(f"{key} -> {total:.2f}")
