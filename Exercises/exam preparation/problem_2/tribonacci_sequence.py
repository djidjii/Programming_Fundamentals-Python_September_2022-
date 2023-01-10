def tibonacci(num):
    sequence = [1]
    for i in range(1, num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return ' '.join([str(num) for num in sequence])


n = int(input("Enter number: "))
print(tibonacci(n))
