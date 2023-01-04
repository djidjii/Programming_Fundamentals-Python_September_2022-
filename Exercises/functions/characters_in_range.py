def collect_characters(first, second):
    character = []
    for i in range(ord(first_character) + 1, ord(second_character)):
        character.append(chr(i))
    return character

first_character = input()
second_character = input()

result = collect_characters(first_character, second_character)
print(' '.join(result))
