def even(number):
    if number % 2 == 0:
        return True
    return False


numbers_list = [int(i) for i in input().split()]
even_filter = filter(even, numbers_list)
even_list = list(even_filter)
print(even_list)
