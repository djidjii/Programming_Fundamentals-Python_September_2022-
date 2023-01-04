num_rows = int(input())

total_sum = 0
for i in range(num_rows):
    string = input()
    total_sum += ord(string)

print(f"The sum equals: {total_sum}")
