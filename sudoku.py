import math
import random

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

def add_random_puzzle(board, N):
    """
    Helper function that attempts to fill in random number between 1 to N in a Board 
    """

    for num in range(1, N+1):
        while True:
            i = random.randrange(0, N)
            j = random.randrange(0, N)
            if board[i][j] == 0:
                board[i][j] = num
                break
    
    return board

def add_to_set_list(grid, set_list, type):
    """
    Helper function that iterates over a board and adds sets to a list
    """
    if type == "Row":
        # Loops over rows and columns accordingly
        for i in range(len(grid)):
            tmp_set = set()
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    tmp_set.add(grid[i][j])
            set_list.append(tmp_set)
    elif type == "Column":
        # Loops over columns
        for j in range(len(grid[0])):
            tmp_set = set()
            for i in range(len(grid)):
                if grid[i][j] != 0:
                    tmp_set.add(grid[i][j])
            set_list.append(tmp_set)
    return

def add_reg_set_list(board, set_list, n):
    """
    Helper function that iterates over a board and adds sets to reg set list
    """
    # Loops over rows and columns accordingly
    for i in range(len(board)):
        for j in range(len(board[i])):
            region_row = i//n # floor division to get the region row index in ratio (smaller set list)
            region_col = j//n # floor division to get the region column index in ratio (smaller set list)
            region_set = set_list[region_row][region_col] # select the set in the list passed to this at its index accordingly
            if board[i][j] != 0:
                region_set.add(board[i][j]) # Add the value to region set in the set list from the board
    return

def make_puzzle(N):
    """
    This function makes and returns a sudoku puzzle given a NxN size.
    """
    board = [[0 for _ in range(N)] for _ in range(N)] # Create a board (NxN)

    board = add_random_puzzle(board, N) # Calls helper function and attempts to fill ins in 1 to N at randomly
    n = int(math.sqrt(N)) # Get region size

    # Initialize set lists
    row_sets_list = []
    col_sets_list = []
    reg_sets_list = [[set() for _ in range(n)] for _ in range(n)] # Create a list of set with smaller region

    add_to_set_list(board, row_sets_list, "Row") # Calls helper function and appends to list
    add_to_set_list(board, col_sets_list, "Column") # Calls helper function and appends to list
    add_reg_set_list(board, reg_sets_list, n) # Calls helper function and updates reg_sets_list

    # Create puzzle dict containing all of the informations
    puzzle_dict = {
        'board' : board,
        'row_sets': row_sets_list,
        'col_sets': col_sets_list,
        'reg_sets': reg_sets_list
    }

    return puzzle_dict

def get_square(puzzle, row, col):
    pass

def move(puzzle, row, col, new_value):
    pass

def fill_puzzle(puzzle):
    pass

def main():
    N = 9
    print("Board size:", N, "x", N)
    puzzle = make_puzzle(N)
    print(puzzle['board'])
    print(puzzle['row_sets'])
    # print(puzzle)
    # print("Initial board:")
    # print_board(puzzle['board'])
    pass

     
main()
