import turtle
import time

BOARD_SIZE = 600
CELL_SIZE = BOARD_SIZE / 3
WIN_CONDITIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

clicked_row = None
clicked_col = None

def setup_screen():
    window = turtle.Screen()
    window.setworldcoordinates(0, 0, BOARD_SIZE, BOARD_SIZE)
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    return window, pen

def drawTTT():
    for i in range(1, 3):
        pen.penup()
        pen.goto(CELL_SIZE * i, 0)
        pen.pendown()
        pen.goto(CELL_SIZE * i, BOARD_SIZE)
        pen.penup()
        pen.goto(0, CELL_SIZE * i)
        pen.pendown()
        pen.goto(BOARD_SIZE, CELL_SIZE * i)
        pen.penup()

def drawX(x, y):
    padding = CELL_SIZE * 0.1
    pen.pencolor("red")
    pen.penup()
    pen.goto(x + padding, y + padding)
    pen.pendown()
    pen.goto(x + CELL_SIZE - padding, y + CELL_SIZE - padding)
    pen.penup()
    pen.goto(x + CELL_SIZE - padding, y + padding)
    pen.pendown()
    pen.goto(x + padding, y + CELL_SIZE - padding)
    pen.penup()

def drawO(x, y):
    radius = CELL_SIZE * 0.4
    pen.penup()
    pen.pencolor("blue")
    pen.goto(x + CELL_SIZE / 2, y + CELL_SIZE / 2 - radius)
    pen.pendown()
    pen.circle(radius)
    pen.penup()

# FIX 5: Renamed draw_Symbol → draw_symbol (consistent casing)
def draw_symbol(row, col, current_symbol):
    start_x = col * CELL_SIZE
    start_y = (2 - row) * CELL_SIZE
    if current_symbol == "X":
        drawX(start_x, start_y)
    elif current_symbol == "O":
        drawO(start_x, start_y)

def ttt():
    board = []
    for i in range(3):
        row = []
        for j in range(3):  # FIX 8: was `i`, shadowing outer loop variable
            row.append('')
        board.append(row)
    return board

def check_full(board):
    for row in board:
        for col in row:
            if col == '':  # FIX 3: was ' ' (space), board uses '' (empty string)
                return False
    return True

# FIX 4: Takes current_symbol as a parameter instead of using an implicit global
def switch_symbol(current_symbol):
    if current_symbol == "X":
        return "O"
    else:
        return "X"

def check_win(board):
    for condition in WIN_CONDITIONS:
        if board[condition[0][0]][condition[0][1]] == \
           board[condition[1][0]][condition[1][1]] == \
           board[condition[2][0]][condition[2][1]] != '':  # FIX 3: was ' '
            # FIX 2: this `if` was not indented inside the `for` loop
            return True
    return False  # FIX 10: was missing — returned None implicitly

def record_click_position(x, y):
    global clicked_row, clicked_col
    col = int(x // CELL_SIZE)
    row = int((BOARD_SIZE - y) // CELL_SIZE)
    if 0 <= row < 3 and 0 <= col < 3:
        clicked_row = row
        clicked_col = col

def wait_for_click():
    global clicked_row, clicked_col
    clicked_row = None
    clicked_col = None
    window.onclick(record_click_position)  # FIX 6: was `screen`, renamed to `window`
    # FIX 6: These three lines were outside the function at module level
    while clicked_row is None:
        turtle.update()
        time.sleep(0.01)  # FIX 1: requires `import time`
    window.onclick(None)  # FIX 6: was `screen`
    return clicked_row, clicked_col

def get_player_move_turtle(board, current_symbol):
    while True:
        row, col = wait_for_click()
        # FIX 7: this block was outside the while loop due to wrong indentation
        if board[row][col] == '':  # FIX 3: was ' '
            board[row][col] = current_symbol
            draw_symbol(row, col, current_symbol)  # FIX 5: was draw_Symbol
            break
        else:
            print("Spot already taken! Choose again.")

board = ttt()
window, pen = setup_screen()
drawTTT()
current_symbol = "X"

# FIX 9: Removed the old console-based for loop that conflicted with the turtle loop
while True:
    get_player_move_turtle(board, current_symbol)
    if check_win(board):
        print(f"{current_symbol} wins!")
        break
    if check_full(board):
        print("It's a draw!")
        break
    current_symbol = switch_symbol(current_symbol)

window.mainloop()