def even_or_odd_numbers(number):
    sum_of_odd_digit = 0
    sum_of_even_digit = 0
    for i in number:
        if int(i) % 2 == 0:
            sum_of_even_digit += int(i)
        else:
            sum_of_odd_digit += int(i)
    return sum_of_odd_digit, sum_of_even_digit


number_as_string = input()
sum_of_odd_digit, sum_of_even_digit = even_or_odd_numbers(number_as_string)
print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digit}")
