n = int(input())

positive_num = 0
negative_num = 0
positive_list = []
negative_list = []

for i in range(n):
    num = int(input())
    if num >= 0:
        positive_num += 1
        positive_list.append(num)
    else:
        negative_num += num
        negative_list.append(num)
print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_num}")
print(f"Sum of negatives: {negative_num}")
