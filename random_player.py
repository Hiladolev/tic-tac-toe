import random
import turtle as t
import player_move as moves

randy_starts = False

def checks_if_random_player_start():
    global randy_starts
    screen = t.Screen()
    ans = screen.textinput("Who starts","Hey, my name is Randy.\n Should I start? (y/n): ").strip().lower()
    randy_starts = (ans == 'y')
    if randy_starts:
        return True
    return False

#chooses a random empty cell
def choose_random_cell():
    empties = moves.empty_cells()
    if not empties:
        return None
    return random.choice(empties)

def make_randy_move():
    current_player = 'X' if (moves.turn_count % 2 == 1) else 'O'
    randy_player_char = 'X' if randy_starts else 'O'
    if current_player != randy_player_char:
        return  # not Randy's turn
    cell = choose_random_cell()
    if cell is None:
        return
    # call players_moves with row, col
    moves.players_moves(*cell)



