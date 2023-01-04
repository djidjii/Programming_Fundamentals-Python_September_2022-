n1 = int(input())
n2 = int(input())

for i in range(n2, n1, -1):
    if i % n1 == 0:
        break
print(i)
