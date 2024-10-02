import random
from colorama import Fore, Back, Style, init

# Colorama
init(autoreset=True)

# Creating boards side by side


def board():
    return [['o' for _ in range(5)] for _ in range(5)]


def boards(board1, board2):
    print("  Your Board     Its Board")
    print("  A B C D E      A B C D E")
    for i in range(5):
        row1 = ' '.join([Fore.YELLOW + 'S' + Style.RESET_ALL if cell == 'S' else
                         Fore.GREEN + '+' + Style.RESET_ALL if cell == 'X' else
                         Fore.RED + 'M' + Style.RESET_ALL if cell == 'M' else 'o'
                         for cell in board1[i]])
        row2 = ' '.join([Fore.GREEN + '+' + Style.RESET_ALL if cell == 'X' else
                         Fore.RED + 'M' + Style.RESET_ALL if cell == 'M' else 'o'
                         for cell in board2[i]])
        print(f"{i+1} {row1}    {i+1} {row2}")

# Place Ships Automatic or Manually


def manual_ship(warzone, ship_number, coord):
    col = ord(coord[0].upper()) - ord('A')
    row = int(coord[1]) - 1

    if 0 <= row < 5 and 0 <= col < 5 and warzone[row][col] == 'o':
        warzone[row][col] = 'S'
    else:
        print(f"{coord} is not accurate coordinate. Please try again.")
    return warzone


def automatic_ship(warzone):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)

        if warzone[row][col] == 'o':
            warzone[row][col] = 'S'
            break
    return warzone


def ship_placement(warzone, manual=True):
    if manual:
        while True:
            placement = input("Welcome to the Battleship Game! You will have 1 unit long 5 ships to place. How would you like to place your ships? Type 'M' for manual or 'A' for automatic.").upper()
            if placement == 'A':
                for _ in range(5):  # 5 Ships will be placed.
                    warzone = automatic_ship(warzone)
                break
            elif placement == 'M':
                ships_placed = 0
                while ships_placed < 5:
                    coord = input(f"Give a coordinate for {ships_placed + 1}. ship. (Example: A1, B2)")
                    if len(coord) == 2 and coord[0].isalpha() and coord[1].isdigit():
                        col = ord(coord[0].upper()) - ord('A')
                        row = int(coord[1]) - 1
                        if 0 <= row < 5 and 0 <= col < 5 and warzone[row][col] == 'o':
                            warzone[row][col] = 'S'
                            ships_placed += 1
                            print(f"{ships_placed}. ship is placed at {coord}.")
                            print("\n Your current board:")
                            boards(warzone, board())
                        else:
                            print(f"{coord} is already full or not accurate. Please try another coordinate.")
                    else:
                        print("Invalid coordinate. Please check and try again.")
                break
            else:
                print("Invalid answer. Please type 'M' or 'A'")
    else:
        for _ in range(5):
            warzone = automatic_ship(warzone)

    return warzone


def game(your_board, its_board):
    your_hits = 0
    its_hits = 0

    while your_hits < 5 and its_hits < 5:
        # Player's turn
        while True:
            your_shot = input("Type the coordinate you want to shoot. Example(A1, C2) or Type 'Q' to quit.").upper()
            if your_shot == 'Q':
                return 'quit'
            if len(your_shot) == 2 and your_shot[0] in 'ABCDE' and your_shot[1] in '12345':
                row = int(your_shot[1]) - 1
                col = ord(your_shot[0]) - ord('A')
                if its_board[row][col] == 'o' or its_board[row][col] == 'S':
                    break
                else:
                    print("You've already typed this coordinate, please type different coordinate.")
            else:
                print("Unvalid coordinate, pleasee try again.")

        if its_board[row][col] == 'S':
            its_board[row][col] = 'X'
            your_hits += 1
            print(Fore.GREEN + "You've hit one target." + Style.RESET_ALL)
        else:
            its_board[row][col] = 'M'
            print(Fore.RED + "You've missed." + Style.RESET_ALL)

        # Computer's Turn
        while True:
            its_row = random.randint(0, 4)
            its_col = random.randint(0, 4)
            if your_board[its_row][its_col] == 'o' or your_board[its_row][its_col] == 'S':
                break
        if your_board[its_row][its_col] == 'S':
            your_board[its_row][its_col] = 'X'
            its_hits += 1
            print(f"Your rival has hit your ship at {chr(its_col + ord('A'))}{its_row + 1} coordinate.")
        else:
            your_board[its_row][its_col] = 'M'
            print(f"Your rival has missed at {chr(its_col + ord('A'))}{its_row + 1} coordinate.")

        boards(your_board, its_board)
        print(f"Your hit: {your_hits} The rival's hit:{its_hits}")
        print()

    if your_hits == 5:
        print(Fore.GREEN + "YOU WON!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "YOUR RIVAL WON!" + Style.RESET_ALL)
    return 'finished'


def main():
    while True:
        your_board = board()
        its_board = board()
        your_board = ship_placement(your_board)
        its_board = ship_placement(its_board, manual=False)

        print("\n All ships are placed. Here is your and rival's boards:")
        boards(your_board, board())
        input("Please press 'ENTER' to start the game.")

        print("\n The game is starting... Your boards:")
        boards(your_board, its_board)

        result = game(your_board, its_board)

        if result == 'quit':
            print("Quitting the game... You can refresh the page to play again.")
            break

        game_again = input("Do you want to play again? (Y/N)").upper()
        if game_again != 'Y':
            print("The game has finished, see you!")
            break


if __name__ == "__main__":
    main()