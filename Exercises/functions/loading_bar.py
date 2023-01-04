number = int(input())
loading_list = []
def loading_bar(some_number):
    for i in range(0, 101, 10):
        if i == number:
            return 