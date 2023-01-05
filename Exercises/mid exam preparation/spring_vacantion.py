day_of_the_vacation = int(input())
budget = float(input())
people = int(input())
price_per_kilometer = float(input())
food_expenses = float(input())
price_per_night = float(input())

if people > 10:
    price_per_night -= price_per_night * 0.25

total_price = (food_expenses + price_per_night) * day_of_the_vacation * people

for i in range(1, day_of_the_vacation + 1):
    traveled_distance = float(input())
    total_price += traveled_distance * price_per_kilometer

    if i % 3 == 0 or i % 5 == 0:
        total_price += total_price * 0.4

    if i % 7 == 0:
        received_money = total_price / people
        total_price -= received_money

if total_price > budget:
    needed_money = total_price - budget
    print(f"Not enough money to continue the trip. You need {needed_money:.2f}$ more.")
else:
    money_left = budget - total_price
    print(f"You have reached the destination. You have {money_left:.2f}$ budget left.")