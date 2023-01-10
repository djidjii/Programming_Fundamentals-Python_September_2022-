class Password:

    def __init__(self, main_string):
        self.main_string = main_string

    def take_odd(self):
        self.main_string = self.main_string[1::2]
        Password.print_string(self)

    def cut(self, index, length):
        start_index = index
        end_index = index + length
        self.main_string = self.main_string[:start_index] + self.main_string[end_index:]
        Password.print_string(self)

    def substitute(self, substring, new_word):
        if substring in self.main_string:
            self.main_string = self.main_string.replace(substring, new_word)
            Password.print_string(self)
        elif substring not in self.main_string:
            print("Nothing to replace!")

    def print_string(self):
        print(self.main_string)

    def __repr__(self):
        return f"{self.main_string}"


text = input()
main_text = Password(text)
operations = {
    'TakeOdd': main_text.take_odd,
    'Cut': main_text.cut,
    'Substitute': main_text.substitute
}
command = input()
while command != "Done":
    task, *info = [int(item) if item.isdigit() else item for item in command.split()]
    operations[task](*info)
    # if task == 'TakeOdd':
    #     main_text.take_odd()
    # elif task == 'Cut':
    #     main_text.cut(*info)
    # elif task == 'Substitute':
    #     main_text.substitute(*info)
    command = input()
print(f"Your password is: {main_text}")

