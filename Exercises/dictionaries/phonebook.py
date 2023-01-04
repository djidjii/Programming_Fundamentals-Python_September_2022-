
information = {}
while True:
    input_information = input()
    if "-" not in input_information:
        break
    name, phone = input_information.split("-")
    information[name] = phone
for check in range(int(input_information)):
    searched_name = input()
    if searched_name in information.keys():
        print(f"{searched_name} -> {information[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")