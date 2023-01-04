
def calculates(product):
    if product == "coffee":
        return float(num_products) * 1.50
    elif product == "water":
        return float(num_products) * 1.00
    elif product == "coke":
        return float(num_products) * 1.40


product = input()
num_products = input()

print(f"{(calculates(product)):.2f}")
