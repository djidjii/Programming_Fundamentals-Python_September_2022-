def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name, hit_points, mana_points = data[0], int(data[1]), int(data[2])
        heroes_dict[hero_name] = [hit_points, mana_points]


def playing_game(heroes_dict):
    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'CastSpell':
            hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name, damage, attacker = command[1], int(command[2]), command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name, amount = command[1], int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == 'Heal':
            hero_name, amount = command[1], int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")


def print_function(heroes_dict):
    print_result = ''

    for hero in heroes_dict:
        print_result += f'{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}\n'

    return print_result


def heroes_of_code(number):
    # In heroes_dict we have key - hero name and as value we have
    # a list with two elements: HP - index 0, MP - index 1
    heroes_dict = {}

    # This function will create our heroes by adding different specifics for them
    # like HP and MP. HP stands for hit points and MP for mana points
    create_heroes(heroes_dict, number_of_heroes)

    # This is the main function in which the game will develop
    # according to certain conditions
    playing_game(heroes_dict)

    # print_function - Print all members of your party who are still alive
    # and their HP and MP
    print(print_function(heroes_dict))


number_of_heroes = int(input())
heroes_of_code(number_of_heroes)
