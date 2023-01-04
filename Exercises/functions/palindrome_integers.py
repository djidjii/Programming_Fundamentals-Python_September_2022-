input_string = input("Enter the list elements: ").split(", ")
list_numbers = list(map(int, input_string))


def palindrome_numbers(string):
    for i in range(0, string):
        if input_string == input_string[::-1]:
            return True
        return False

# print(palindrome_numbers(input_string))
