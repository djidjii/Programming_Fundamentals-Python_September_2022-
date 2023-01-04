import math

number_people = int(input())
capacity = int(input())

result = number_people / capacity
print(math.ceil(result))
