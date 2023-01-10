number_pieces = int(input("Enter number of pieces: "))
pieces = {}

for _ in range(number_pieces):
    data = input().split("|")
    piece, composer, key = data[0], data[1], data[2]
    pieces[piece] = [composer, key]

while True:
    command = input().split("|")
    current_command = command[0]

    if current_command == "Stop":
        break

    elif current_command == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif current_command == "Remove":
        piece = command[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_command == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

# pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1][0])))


for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece][0]}, Key: {pieces[piece][1]}")
