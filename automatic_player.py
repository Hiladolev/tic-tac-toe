import random
import player_move as moves
from game_board import board_by_lines

def _find_winning_move(board, symbol):
    lines = board_by_lines()
    for line in lines:
        cells = [board[(r,c)] for r, c in line]
        if cells.count(symbol) == 2 and cells.count(None) == 1:#if there is a row/col/diagonal with 2 of symbol and 1 empty
            empty_idx = cells.index(None)
            return line[empty_idx]
    return None

def choose_strategic_move(board):
    my_sym = 'O'
    opp_sym = 'X'
    mv = _find_winning_move(board, my_sym)#return a winning move if there is at least one
    if mv:
        return mv
    mv = _find_winning_move(board, opp_sym)#block opponent's winning move if there is at least one
    if mv:
        return mv
    if board[(2,2)] is None: #board center is empty, take it
        return 2, 2
    corners = [(1,1),(1,3),(3,1),(3,3)]
    for (r,c) in corners:
        if board[(r,c)] == opp_sym:
            opp_corner = (4-r, 4-c)
            if board[opp_corner] is None:
                return opp_corner
    random.shuffle(corners)#try to take a random corner
    for c in corners:
        if board[c] is None:
            return c
    sides = [(1,2),(2,1),(2,3),(3,2)]
    random.shuffle(sides)
    for s in sides:
        if board[s] is None:
            return s
    empties = moves.empty_cells()
    return random.choice(empties) if empties else None

def make_auto_move():
    board = moves.board_state
    current_player = 'X' if (moves.turn_count % 2 == 1) else 'O'
    auto_player_char = 'O'# human always starts first
    if current_player != auto_player_char:
        return  # not auto player's turn
    mv = choose_strategic_move(board)
    if mv is None:
        return #no moves left
    r, c = mv
    moves.players_moves(r, c)
