def calculations(operator):
    if operator == "multiply":
        return num_1 * num_2
    if operator == "divide":
        return num_1 / num_2
    if operator == "add":
        return num_1 + num_2
    if operator == "subtract":
        return num_1 - num_2
operator = input()
num_1 = int(input())
num_2 = int(input())
print(int(calculations(operator)))
