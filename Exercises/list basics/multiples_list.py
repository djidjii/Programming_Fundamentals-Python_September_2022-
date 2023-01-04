factor = int(input())
counts = int(input())

length_list = []

for i in range(1, counts + 1):
    length_list.append(i * factor)

print(length_list)
