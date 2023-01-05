food_gr = float(input()) * 1000
hay_gr = float(input()) * 1000
cover_gr = float(input()) * 1000
pig_weight_gr = float(input()) * 1000

Flag = False
for i in range(1, 31):
    food_gr -= 300

    if i % 2 == 0:
        hay_gr -= food_gr * 0.05

    if i % 3 == 0:
        cover_gr -= pig_weight_gr / 3

    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        Flag = True
        break
if not Flag:
    food, hay, cover = food_gr / 1000, hay_gr / 1000, cover_gr / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
