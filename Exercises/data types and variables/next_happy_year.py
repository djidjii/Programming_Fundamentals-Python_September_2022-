year = int(input())
happy_new_condition = False

while not happy_new_condition:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year))

    happy_new_condition = len(set_year) == len(str(year))
print(year)
