value_list_string = input().split()

absolute_value = []

for i in value_list_string:
    absolute_value.append(abs(float(i)))
print(absolute_value)
