numbers = input().split()

convert = [int(i) for i in numbers]

sort_numbers = sorted(convert)
list_numbers = list(map(int, sort_numbers))

print(list_numbers)
