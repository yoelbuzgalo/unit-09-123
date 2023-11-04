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

def add_to_set_list(grid, row_set_list, col_set_list, reg_set_list):
    """
    Helper function that iterates over a board and adds sets to a list
    """
    n = int(math.sqrt(len(grid)))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value = grid[i][j]
            if value != 0:
                # Adds values in order based on row/column index
                row_set_list[i].add(value)
                col_set_list[j].add(value)

                # Calculate region index
                region_row = i//n
                region_col = j//n

                # Add values to the list of region set
                reg_set_list[region_row][region_col].add(value)
    return

def make_puzzle(N):
    """
    This function makes and returns a sudoku puzzle given a NxN size.
    """
    board = [[0 for _ in range(N)] for _ in range(N)] # Create a board (NxN)

    board = add_random_puzzle(board, N) # Calls helper function and attempts to fill ins in 1 to N at randomly
    n = int(math.sqrt(N)) # Get region size

    # Initialize set lists
    row_sets_list = [set() for _ in range(N)]
    col_sets_list = [set() for _ in range(N)]
    reg_sets_list = [[set() for _ in range(n)] for _ in range(n)] # Create a list of set with smaller region

    add_to_set_list(board, row_sets_list, col_sets_list, reg_sets_list) # Calls helper function and appends to list

    # Create puzzle dict containing all of the informations
    puzzle_dict = {
        'board' : board,
        'row_sets': row_sets_list,
        'col_sets': col_sets_list,
        'reg_sets': reg_sets_list
    }

    return puzzle_dict

def get_square(puzzle, row, col):
    """
    This function gets relevant information from a puzzle at a given row and col index
    """

    # Store values from dict seperately for analysis
    puzzle_board = puzzle['board']
    puzzle_row_sets = puzzle['row_sets']
    puzzle_col_sets = puzzle['col_sets']
    puzzle_reg_sets = puzzle['reg_sets']
    n = int(math.sqrt(len(puzzle_board))) # Get the smaller n size for region set

    value = puzzle_board[row][col]
    row_set = puzzle_row_sets[row]
    col_set = puzzle_col_sets[col]
    reg_set = puzzle_reg_sets[row//n][col//n] # Region size is always smaller in ratio, divide by floor division with n

    return {
        'value': value,
        'row_set': row_set,
        'col_set': col_set,
        'reg_set': reg_set,
    } # Return as a dict of relevant information

def move(puzzle, row, col, new_value):
    """
    This function checks if the position at row, col is empty and attempts to add a new value there without breaking the rules. Returns True if successful otherwise False.
    """
    
    check_puzzle = get_square(puzzle, row, col) # Get the relevant information at the desired square

    if check_puzzle['value'] != 0:
        return False # Returns False if the square is not 0 (occupied)

    if new_value in check_puzzle['row_set'] or new_value in check_puzzle['col_set'] or new_value in check_puzzle['reg_set']:
        return False # Returns if the new value number exists within a row or col of that puzzle target

    return True # Returns True upon success

def fill_puzzle(puzzle):
    pass

def main():
    N = 9
    print("Board size:", N, "x", N)
    puzzle = make_puzzle(N)
    # for row in puzzle['board']:
    #     print(row)
    
    print(puzzle)
    
    # if move(puzzle, 0,0, 3):
    #     print()
    #     print()
    #     puzzle['board'][0][0] == 3
    #     for row in puzzle['board']:
    #         print(row)
    # else:
    #     print("Denied")
    
    # print(puzzle)
    # print("Initial board:")
    # print_board(puzzle['board'])
    pass

     
main()
