n = int(input())
word = str(input())

text_list = []

for i in range(n):
    text = str(input())
    text_list.append(text)
print(text_list)

for i in range(len(text_list) -1, -1, -1):
    if word not in text_list[i]:
        text_list.remove(text_list[i])
print(text_list)
