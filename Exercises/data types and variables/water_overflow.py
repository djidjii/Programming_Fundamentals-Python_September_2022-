num = int(input())

sum_liters = 0
for i in range(num):
    liters = int(input())
    sum_liters += liters
    if sum_liters < 255:
        sum_liters += liters
        continue
print(f"Insufficient capacity!")
