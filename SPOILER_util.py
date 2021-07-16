# 👸
# ╔════╦════╦════╦════╦════╦════╦════╦════╗
# ║    ║    ║    ║    ║    ║    ║    ║    ║

# ╠════╬════╬════╬════╬════╬════╬════╬════╣

# ╚════╩════╩════╩════╩════╩════╩════╩════╝

COL_WIDTH = 4
NO_ROW = 8
NO_COL = 8
QUEEN_MARK = 1
QUEEN_EMOJI = '👸'
ROW_POS = 0
COL_POS = 1


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


def get_row_position(position):
    return position[ROW_POS]


def get_col_position(position):
    return position[COL_POS]


def place_queen(chess_board, position):
    chess_board[get_row_position(position) - 1][get_col_position(position) - 1] = QUEEN_MARK


chess_board = [[0 for _ in range(NO_COL)] for _ in range(NO_ROW)]

place_queen(chess_board, (1, 1))
place_queen(chess_board, (4, 4))
place_queen(chess_board, (8, 8))

print_chess_board(chess_board)



# chess borad data structure
# data structure -> print chess board