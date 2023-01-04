# input_list = input()
# notes = [0] * 10
tasks = []

while True:
    command = input()
    if command == "End":
        break

    split_commands = command.split("-")
    priority = int(split_commands[0])
    note = split_commands[1]

    tasks.append(priority, note)
sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
