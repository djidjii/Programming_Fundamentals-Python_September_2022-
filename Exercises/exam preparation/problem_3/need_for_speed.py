number_of_cars = int(input())
cars = {}

for automobile in range(number_of_cars):
    current_car = input().split("|")
    car = current_car[0]
    mileage = int(current_car[1])
    total_fuel = int(current_car[2])
    cars[car] = mileage, total_fuel

while True:
    command = input().split(":")
    current_command = command[0]

    if current_command == "Stop":
        break

    elif current_command == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car][1] - fuel < 0:
            print("Not enough fuel to make that ride""Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            cars[car][0] += distance
            cars[car][1] -= fuel
        if cars[car][0] >= 100000:
            del cars[car]

    elif current_command == "Refuel":
        fuel_to_refill = int(command[2])
        needed_fuel = 75 - cars[car][1]
        cars[car][1] += needed_fuel
        if cars[car][1] > 75:
            cars[car][1] = 75
            print(f"{car} refueled with {cars[car][1] - fuel_to_refill} liters")

    elif current_command == "Revert":
        car = command[1]
        kilometers = int(command[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, (mileage, fuel) in cars.items():
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
