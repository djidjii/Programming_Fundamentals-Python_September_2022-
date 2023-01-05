import math

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students_count = int(input())

hour_counter = 0

students_per_our = employee_1 + employee_2 + employee_3
hour_needed = int(math.ceil(students_count / students_per_our))

for i in range(1, hour_needed + 1):
    if i % 4 == 0:
        hour_counter += 1
total_sum_hour = hour_counter + hour_needed

print(f"Time needed: {total_sum_hour}h.")
