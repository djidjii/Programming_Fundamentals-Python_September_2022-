text = input().split(", ")
# counter = int(input())

money_list_num = []
for i in text:
    money_list_num.append(int(i))

number_of_beggars = int(input())
final_sum = []
start_index = 0

while start_index < number_of_beggars:
    sum_for_current_beggars = 0
    for current_index in range(start_index, len(money_list_num), number_of_beggars):
        sum_for_current_beggars += money_list_num[current_index]

    final_sum.append(sum_for_current_beggars)
    start_index += 1
print(final_sum)