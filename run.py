import random

#Creating boards side by side
def board():
    return[['o' for _ in range(9)] for _ in range(9)]

def boards(board1, board2):
    print("      Your Board          Its Board")
    print("  A B C D E F G H I       A B C D E F G H I")
    for i in range (9):
        row1 = ' '.join(board1[i])
        row2 = ' '.join(board2[i])
        print(f"{i+1} {row1}     {i+1} {row2}")

your_board = board()
its_board = board()

#Place Ships Automatic or Manuelly

