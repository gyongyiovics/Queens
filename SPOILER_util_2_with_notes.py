from os import system, name

# variables
COL_WIDTH = 4
NO_ROW = 8
NO_COL = 8
QUEEN_MARK = 1
QUEEN_EMOJI = '👸'
ROW_POS = 0
COL_POS = 1

# we get the sides of the rows and also print the emojis in the cells
def get_row(row):
    row_str = ""
    for cell in row:
        row_str += "║"
        if cell == QUEEN_MARK:
            row_str += f" {QUEEN_EMOJI} "
        else:
            row_str += f"{COL_WIDTH * ' '}"
    row_str += "║"
    return row_str

# print the chess board to the empty one and adds the emojis from the above function (get_row)
def print_chess_board(chess_board):
    header = f"╔{(COL_WIDTH * '═' + '╦') * NO_COL}"[:-1] + '╗'
    separa = f"╠{(COL_WIDTH * '═' + '╬') * NO_COL}"[:-1] + '╣'
    footer = f"╚{(COL_WIDTH * '═' + '╩') * NO_COL}"[:-1] + '╝'
    print(header)
    for row in range(NO_ROW):
        print(get_row(chess_board[row]))
        if row != NO_ROW - 1:
            print(separa)
    print(footer)

# gets the first position of the emoji (vertical)
def get_row_position(position):
    return position[ROW_POS]

# gets the first position of the emoji (horizontal)
def get_col_position(position):
    return position[COL_POS]

# puts ONE emoji on the board
def place_queen(chess_board, position):
    chess_board[get_row_position(position)][get_col_position(position)] = QUEEN_MARK

# checks if the next position is in the same row as the previous emoji-placement
# reference_position = is the pos of the PLACED emoji
# position = is the pos of the NEW emoji
def is_in_same_row(reference_position, position):
    if get_row_position(reference_position) == get_row_position(position):
        return True
    else:
        return False

# checks if the next position is in the same diagonal pos as the previous emoji-placement
def is_in_same_diagonal(reference_position, position):
    if (abs(get_row_position(reference_position) - get_row_position(position))) == (abs(get_col_position(reference_position) - get_col_position(position))):
        return True
    else:
        return False

# checks if there is a valid position for the NEW emoji (not crossing any of the PLACED emojis vert-hor-or-diagonally)
def is_valid_position(queens_row, position):
    for cell in range(NO_COL):
        if queens_row[cell] == 0:
            break
        reference_position = (queens_row[cell], cell + 1)
        if is_in_same_row(reference_position, position) is True:
            return False
        if is_in_same_diagonal(reference_position, position) is True:
            return False
    return True

# checks the next possible position for the NEW emoji on the board
def get_next_possible_pos(queens_row, row, col):
    row = queens_row[col - 2] + 1
    queens_row[col - 2] = 0
    col -= 1
    return row, col

# uses the is_valid_position and the get_next_possible_pos to place the NEW emoji
# places the NEW emoji
def place_queen_gen(queens_row, row, col):
    board = [[0 for _ in range(NO_COL)] for _ in range(NO_ROW)]
    while 8 >= col >= 0:
        valid_position = False
        while row <= 8:
            position = row, col
            valid_position = is_valid_position(queens_row, position)
            if valid_position is True:
                break
            row += 1
        if valid_position:
            queens_row[col - 1] = row
            row = 1
            col += 1
        else:
            row, col = get_next_possible_pos(queens_row, row, col)
            while row > 8:
                row, col = get_next_possible_pos(queens_row, row, col)
        if col == 9:
            row = queens_row[7] + 1
            col = 8
            yield queens_row

# uses the place_queen_gen
# shows the whole board with the positioned emojist
def transform_row_to_board(queens_row, board):
    for col in range(NO_COL):
        position = queens_row[col] - 1, col
        place_queen(board, position)

# returns the user_input (here it is just an Enter press)
def get_user_input():
    return input('Press enter to get the next combination!')

# returns the empty board to place emojis on it
def get_empty_board():
    return [[0 for _ in range(NO_COL)] for _ in range(NO_ROW)]

# clears the screen between 2 inputs
def clear_screen():
    system('cls' if name == 'nt' else 'clear')

# the maain!
def main():
	# at first, gives a position for the 8 emojis
    queens_row = [0 for _ in range(NO_COL)]
    queens_row[0] = 1
    queens_gen = place_queen_gen(queens_row, 1, 2)
    
	# we get the user input and then another combination appears on the board
    while get_user_input() == "":
        solution = next(queens_gen)
        chess_borad = get_empty_board()
        transform_row_to_board(solution, chess_borad)
        clear_screen()
        print_chess_board(chess_borad)


if __name__ == "__main__":
    main()



# chess borad data structure
# data structure -> print chess board

#[1,2,3,4,5,6,7,8]
