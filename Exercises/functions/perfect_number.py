def perfect_number(some_number):
    sum_num = 0
    for i in range(1, some_number):
        if number % i == 0:
            sum_num += i
    if sum_num == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
