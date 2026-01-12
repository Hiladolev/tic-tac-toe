import turtle as t
from constants import ROWS, COLS

#function to set up the turtle environment
def setup_turtle():
    t.title("Tic-Tac-Toe Board")
    t.bgcolor("white")
    t.color("black")
    t.setup(width=600, height=600)

#function to draw a Tic-Tac-Toe board
def draw_board():
    t.speed(0)
    t.pensize(5)

    # Draw vertical lines
    for x in [-100, 100]:
        t.penup()
        t.goto(x, 300)
        t.pendown()
        t.goto(x, -300)

    # Draw horizontal lines
    for y in [-100, 100]:
        t.penup()
        t.goto(-300, y)
        t.pendown()
        t.goto(300, y)

    t.hideturtle()

def board_by_lines():
    lines = []
    # rows
    for r in range(1, ROWS + 1):
        lines.append([(r, 1), (r, 2), (r, 3)])
    # cols
    for c in range(1, COLS + 1):
        lines.append([(1, c), (2, c), (3, c)])
    # diagonals
    lines.append([(1, 1), (2, 2), (3, 3)])
    lines.append([(1, 3), (2, 2), (3, 1)])
    return lines

