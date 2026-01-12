import pickle
import os
import player_move as pm
import turtle as t
from game_board import setup_turtle, draw_board

SAVE_FILE = "last_board_state.pkl"

def load_last_game():
    if not os.path.exists(SAVE_FILE):
        print("No saved game found.")
        return False  # file not found

    read_binary_file = open(SAVE_FILE, "rb")
    pm.board_state = pickle.load(read_binary_file)
    read_binary_file.close()

    # update turn count based on loaded board state + 1
    pm.turn_count = sum(1 for v in pm.board_state.values() if v is not None)
    print("Loaded last saved game.")
    return True

def save_current_game():
    write_binary_file = open(SAVE_FILE, "wb")
    pickle.dump(pm.board_state, write_binary_file)
    write_binary_file.close()

def redraw_board_from_state(board_state, board_cells):
    t.clearscreen()
    # Redraw the board grid
    setup_turtle()
    draw_board()
    for (r, c), value in board_state.items():
        if value is None:# empty cell
            continue
        cx, cy = board_cells[(r, c)]['center']
        if value == 'X':
            pm.draw_x(cx, cy)
        elif value == 'O':
            pm.draw_o(cx, cy)