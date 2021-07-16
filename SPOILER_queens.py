# 👸
# ╔════╦════╦════╦════╦════╦════╦════╦════╗
# ║    ║    ║    ║    ║    ║    ║    ║    ║

# ╠════╬════╬════╬════╬════╬════╬════╬════╣

# ╚════╩════╩════╩════╩════╩════╩════╩════╝


# print_chess_borad
# chess_borad
# megkeresni a jó kombinációkat

NO_COL = 8
NO_ROW = 8
QUEEN_EMOJI = "👸"
QUEEN_MARK = 1
ROW_POS = 0
COL_POS = 1



def init_board():
    return [[0 for _ in range(NO_COL)] for _ in range(NO_ROW)]


def get_row_text(row):
    row_str = ""
    for cell in row:
        row_str += "║"
        if cell == 1:
            row_str += f" {QUEEN_EMOJI} "
        else:
            row_str += "    "
    row_str += "║"
    return row_str


def print_chess_borad(board):
    CELL_WIDTH = 4
    
    header = f"╔{((CELL_WIDTH * '═') + '╦') * NO_COL}"[:-1] + '╗'
    separa = f"╠{((CELL_WIDTH * '═') + '╬') * NO_COL}"[:-1] + '╣'
    footer = f"╚{((CELL_WIDTH * '═') + '╩') * NO_COL}"[:-1] + '╝'

    print(header)
    for row in range(NO_ROW):
        print(get_row_text(board[row]))
        if row != NO_ROW - 1:
            print(separa)
    print(footer)


def get_row_position(position):
    return position[ROW_POS]


def get_col_position(position):
    return position[COL_POS]


def place_queen(board, position):
    board[get_row_position(position)][get_col_position(position)] = QUEEN_MARK


def is_in_same_row(reference_position, position):
    if get_row_position(reference_position) == get_row_position(position):
        return True
    else:
        return False


def is_in_same_diagonal(reference_position, position):
    if (abs(get_row_position(reference_position) - get_row_position(position))) == \
       (abs((get_col_position(reference_position)) - (get_col_position(position)))):
       return True
    else:
        return False


def is_valid_postion(queens_row, position):
    for col in range(NO_COL):
        if queens_row[col] == 0:
            break
        reference_position = queens_row[col], col + 1
        if is_in_same_row(reference_position, position) is True:
            return False
        if is_in_same_diagonal(reference_position, position) is True:
            return False
    return True


def get_next_possible_pos(queens_row, row, col):
    row = queens_row[col - 2] + 1
    queens_row[col - 2] = 0
    col -= 1
    return row, col


def place_queens_generator(queens_row, row, col):
    while col > 0 and col <= 8:
        valid_positon = False
        while row <= 8:
            position = row, col
            valid_positon = is_valid_postion(queens_row, position)
            if valid_positon is True:
                break
            row += 1
        if valid_positon is True:
            queens_row[col - 1] = row
            col += 1
            row = 1
        else:
            row, col = get_next_possible_pos(queens_row, row, col)
            while row > 8:
                row, col = get_next_possible_pos(queens_row, row, col)
        if col == 9:
            row = queens_row[7] + 1
            col = 8
            yield queens_row


def transform_row_to_board(queens_row, board):
    for col in range(NO_COL):
        position = queens_row[col] - 1, col
        place_queen(board, position)


queens_row = [0 for _ in range(NO_COL)]
queens_row[0] = 1

queens_place_gen = place_queens_generator(queens_row, 1, 2)

solution = next(queens_place_gen)
print(solution)

board = init_board()
transform_row_to_board(solution, board)
print_chess_borad(board)

solution = next(queens_place_gen)
board = init_board()
transform_row_to_board(solution, board)
print_chess_borad(board)
