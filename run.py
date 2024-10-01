import random

#Creating boards side by side
def board():
    return[['o' for _ in range(9)] for _ in range(9)]

def boards(board1, board2):
    print("      Your Board          Its Board")
    print("  A B C D E F G H I       A B C D E F G H I")
    for i in range (9):
        row1 = ' '.join(board1[i])
        row2 = ' '.join(['X' if cell == 'X' else 'o' for cell in board2[i]])
        print(f"{i+1} {row1}     {i+1} {row2}")

#Place Ships Automatic or Manually

def manual_ship(warzone, ships):
    while True:
        begin = input(f"{ships}. Please give a coordinate to place your 5 unit long ship. Example: A3").upper()
        direction = input("Plese, enter your ship's direction. Type H for horizontal, V for vertical.").upper()

        if len(begin) != 2 or begin[0] not in 'ABCDEFGHI' or begin[1] not in '123456789':
            print("Please, type an appropriate coordinate.")
            continue

        row = int(begin[1]) - 1
        col = ord(begin[0]) - ord('A')

        if direction == 'H':
            if col + 5 > 9:
                print("The ship is out of the board. Try again.")
                continue
            if any(warzone[row][col+i] == 'S' for i in range(5)):
                print("There is already a ship at this coordinate.")
                continue
            for i in range(5):
                warzone[row][col+i] = "S"
        elif direction == 'V':
            if row + 5 > 9:
                print("The ship is out of the board. Try again.")
                continue
            if any(warzone[row+i][col] == 'S' for i in range(5)):
                print("There is already a ship at this coordinate.")
                continue
            for i in range(5):
                warzone[row+i][col] = "S"
        else:
            print("Please, type an accurate direction.")
            continue
        break
    return warzone

def automatic_ship(warzone):
    while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        direction = random.choice(['H', 'V'])

        if direction == 'H' and col + 5 <= 9:
            if all(warzone[row][col+i] == 'o' for i in range(5)):
                for i in range(5):
                    warzone[row][col+i] = 'S'
                break
        elif direction == 'V' and row + 5 <= 9:
            if all(warzone[row+i][col] == 'o' for i in range(5)):
                for i in range(5):
                    warzone[row+i][col] = 'S'
                break
    return warzone

def ship_placement(warzone, manual=True):
    for ships in [1, 2]:
        if manual:
            while True:
                placement = input(f"Welcome to the Battleship Game! How would you like to place your {ships}. ship which are 5 units long? Type 'M' for manual, 'A' for automatic." ).upper()
                if placement == 'M':
                    warzone = manual_ship(warzone, ships)
                    break
                elif placement == 'A':
                    warzone = automatic_ship(warzone)
                    break
                else:
                    print("Please make an accurate choice. Type 'M' or 'A'")
        else:
            warzone = automatic_ship(warzone)
    return warzone


your_board = board()
its_board = board()

your_board = ship_placement(your_board)
its_board = ship_placement(its_board, manual=False)

boards(your_board, its_board)
