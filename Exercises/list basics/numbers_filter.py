n = int(input())

command_even = "even"
command_odd = "odd"
command_negative = "negative"
command_positive = "positive"

numbers = []
filtered_numbers = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)
command = input()
for number in numbers:
    filtered = (
            (command == command_even and number % 2 == 0) or
            (command == command_odd and number % 2 != 0) or
            (command == command_negative and number < 0) or
            (command == command_positive and number >= 0)
    )
    if filtered:
        filtered_numbers.append(number)

print(filtered_numbers)