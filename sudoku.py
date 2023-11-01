import math 

def print_board(board):
    RED = "\033[31m"
    BLACK = "\033[37m"
    
    N = len(board)
    n = math.floor(math.sqrt(N))
    assert N == n*n

    board_string = ""
    for row in range(N):
        if row > 0 and row % n == 0:
            board_string += "\n"
        for col in range(N):
            if col > 0 and col % n == 0: 
                board_string += " "
            value = board[row][col]
            if value != 0:
                board_string += RED
            else:
                board_string += BLACK
            board_string += "[{:02.0f}]".format(value)
            
        board_string += "\n" + BLACK

    print(board_string)

def make_puzzle(N):
    pass

def get_square(puzzle, row, col):
    pass

def move(puzzle, row, col, new_value):
    pass

def fill_puzzle(puzzle):
    pass

def main():
    # N = 16
    # print("Board size:", N, "x", N)
    # puzzle = make_puzzle(N)
    # print("Initial puzzle:")
    # print(puzzle)
    # print("Initial board:")
    # print_board(puzzle['board'])
    pass

     
main()
