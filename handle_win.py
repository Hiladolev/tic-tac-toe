import player_move as moves
import math
from constants import CELL_SIZE, ROWS, COLS
import turtle as t
from game_board import board_by_lines

# Check rows, columns, and diagonals for a winner
def check_winner():
    lines = board_by_lines()
    for line in lines:
        vals = [moves.board_state[pos] for pos in line]
        if vals[0] is not None and vals[0] == vals[1] == vals[2]:
            return vals[0], line  # Return winner ('X' or 'O') and winning cells
    return None, None  # No winner yet

def announce_winner(winning_cells, winner_name):
    print(f"Player {winner_name} wins! Winning cells: {winning_cells}")
    draw_win_line(winning_cells)

def draw_win_line(cells):
    (x1, y1) = moves.board_cells[cells[0]]['center'] #(x,y) center coordinates of first cell
    (x3, y3) = moves.board_cells[cells[2]]['center'] #(x,y) center coordinates of last cell
    dx = x3 - x1 #d - difference
    dy = y3 - y1
    length = math.hypot(dx, dy)
    if length == 0: # Prevent division by zero for identical points(should not happen in Tic-Tac-Toe)
        start = (x1, y1)
        end = (x3, y3)
    else: # Calculate extended line points for winning line
        ext = CELL_SIZE * 0.3 #extension length beyond cell centers
        ux = dx / length #unit vector components
        uy = dy / length #unit vector components
        start = (x1 - ux * ext, y1 - uy * ext) #extended start point
        end = (x3 + ux * ext, y3 + uy * ext) #extended end point
        # Draw the line
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color('red')
    pen.pensize(8)
    pen.goto(start)
    pen.pendown()
    pen.goto(end)
    pen.penup()