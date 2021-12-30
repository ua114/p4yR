import numpy as np

def create_board():
    board = np.array([[0,0,0],[0,0,0],[0,0,0]])
    return board

# Ex2...........................
def place(board, player, position):

    if player == 1:
        if board[position] != 0:
            print('Cannot place piece there')
        else:
            board[position] = 1
    elif player == 2:
        if board[position] != 0:
            print('Cannot place piece there')
        else:
            board[position] = 2
    else:
        print('player number should be 1 or 2')

    return board

# Ex3...........................
board = create_board()
board = place(board,1,(0,0))

def possibilities(board):
    free_spaces = np.where(board == 0)
    return free_spaces
a = possibilities(board)
print(a)

# Ex4...........................
import random
random.seed(1)

def random_place(board,player):
    index = random.choice(range(len(possibilities(board)[0]))) #finds length of 'possibilities' and makes a range from it
    coordinates = (possibilities(board)[0][index],possibilities(board)[1][index])
    place(board,player,coordinates)

print(board)
random_place(board,2)
print(board)

# Ex5...........................
random.seed(1)
board = create_board()

for i in range(3):
    random_place(board,1)
    random_place(board,2)
    print(board)

# Ex6...........................
