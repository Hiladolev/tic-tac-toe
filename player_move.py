import turtle as t
from constants import BOARD_LEFT, BOARD_TOP, CELL_SIZE, ROWS, COLS

def generate_cells():
    cells = {}
    for r in range(1, ROWS + 1):
        for c in range(1, COLS + 1):
            x_min = BOARD_LEFT + (c - 1) * CELL_SIZE
            x_max = x_min + CELL_SIZE
            y_max = BOARD_TOP - (r - 1) * CELL_SIZE
            y_min = y_max - CELL_SIZE
            cx = (x_min + x_max) / 2
            cy = (y_min + y_max) / 2
            cells[(r, c)] = {'bounds_info': (x_min, x_max, y_min, y_max), 'center': (cx, cy)}
    return cells

board_cells = generate_cells()
board_state = {pos: None for pos in board_cells.keys()}  # None => 'X' or 'O'
turn_count = 1  # first move -> X (odd), second -> O (even)

def draw_x(cx, cy):
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color('black')
    pen.pensize(6)
    offset = CELL_SIZE * 0.35
    pen.goto(cx - offset, cy - offset)
    pen.pendown()
    pen.goto(cx + offset, cy + offset)
    pen.penup()
    pen.goto(cx - offset, cy + offset)
    pen.pendown()
    pen.goto(cx + offset, cy - offset)
    pen.penup()

def draw_o(cx, cy):
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color('black')
    pen.pensize(6)
    pen.goto(cx, cy - CELL_SIZE * 0.35)
    pen.pendown()
    pen.circle(CELL_SIZE * 0.35)
    pen.penup()

def cell_from_coordinates(x, y):
    for (r, c), cell_info in board_cells.items():
        x_min, x_max, y_min, y_max = cell_info['bounds_info']
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return r, c
    return None


def players_moves(x_index,y_index):
    global turn_count
    cell_index = x_index, y_index
    if board_state[cell_index] is not None:
        print(f"Cell {cell_index} already occupied by {board_state[cell_index]}")
        return
    player = 'X' if (turn_count % 2 == 1) else 'O'
    cx, cy = board_cells[cell_index]['center']
    if player == 'X':
        draw_x(cx, cy)
    else:
        draw_o(cx, cy)
    board_state[cell_index] = player
    turn_count += 1

def empty_cells():
    # returns list of empty cell tuples only => pos=(row, col), val=None
    return [pos for pos, val in board_state.items() if val is None]