def calculations(number):
    for i in range(1, number):
        number *= i
    return number

num_1 = int(input())
num_2 = int(input())
first_num_factorial = calculations(num_1)
second_num_factorial = calculations(num_2)
final_result = first_num_factorial / second_num_factorial
print(f"{final_result:.2f}")
