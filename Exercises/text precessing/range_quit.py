date = input().upper()
output_string = ''
last_index = 0
repeatedly = 0

for index in range(len(date)):
    if date[index].isdigit():
        if index + 1 < len(date) and date[index + 1].isdigit():
            repeatedly = int(date[index] + date[index + 1])
            output_string += date[last_index:index] * repeatedly
            last_index = index + 1
        else:
            repeatedly = int(date[index])
            output_string += date[last_index:index] * repeatedly
            last_index = index + 1
print(f"Unique symbols used: {len(set(output_string))}")
print(output_string)
