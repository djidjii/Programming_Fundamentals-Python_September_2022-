number = input().split()
counts_remove_number = int(input())
number_as_digit = []
for current_number in number:
    number_as_digit.append(int(current_number))
for _ in range(counts_remove_number):
    number_as_digit.remove(min(number_as_digit))
for current_number_as_digit in number_as_digit:
   print(current_number_as_digit, end=", ")