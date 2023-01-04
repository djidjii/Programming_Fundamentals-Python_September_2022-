input_numbers = input().split()

list_numbers = list(map(int, input_numbers))

def min_num():
    return min(list_numbers)
def max_num():
    return max(list_numbers)
def sum_nums():
    return sum(list_numbers)


print(f"The minimum number is {min_num()}")

print(f"The maximum number is {max_num()}")

print(f"The sum number is: {sum_nums()}")
