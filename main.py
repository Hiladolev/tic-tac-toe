# This is the main controller file that integrates all modules to run the Tic-Tac-Toe game
import game_board as board
import player_move as moves
import turtle as t
from handle_win import check_winner, announce_winner
import random_player as randy
import automatic_player as auto
from last_game_board import load_last_game, redraw_board_from_state,save_current_game
from game_history import save_game_result, display_history

PLAYER_MOVE_MS = 200  # delay in milliseconds before/after auto player/randy makes a move
game_over = False
turns_left = 9
screen = t.Screen()
player_mode = 0
human_turn = True #True when the next move should be done by a human
p1_name = None
p2_name = None

# Execute the strategic automatic player's move and update the game state
def auto_move_wrapper():
    global turns_left
    # perform AI move (smart uses the player_move module)
    auto.make_auto_move()
    turns_left -= 1
    t.ontimer(enable_human_turn, PLAYER_MOVE_MS)

# Manage the human player's input for moves or game commands like save and load
def human_moves():
    global turns_left
    while True:
        user_input = screen.textinput("Player Move", "Make a move - type row,col\n"
                                                     "Load previous game - type load\n"
                                                     "Save current game - type save\n"
                                                     "To view past games - type history")
        if user_input is None:
            return False
        user_input = user_input.strip().lower()
        if user_input == 'load':
            loaded = load_last_game()
            if loaded:
                moves_made = sum(1 for v in moves.board_state.values() if v is not None)
                turns_left =   9 - moves_made
                redraw_board_from_state(moves.board_state, moves.board_cells)
                screen.update()
                return "loaded"
            continue
        if user_input == 'history':
            display_history()
            continue
        if user_input == 'save':
            save_current_game()
            continue
        try:
            x_val, y_val = user_input.split(',')
            x_val = int(x_val.strip())
            y_val = int(y_val.strip())
        except ValueError:
            print("Invalid input. Use row,col or 'load'")
            continue
        if x_val < 1 or x_val > 3 or y_val < 1 or y_val > 3:
            print("Invalid input. Row and column must be between 1 and 3.")
            continue

        moves.players_moves(x_val, y_val)
        return True

# Re-enable the human's ability to make a move after a short delay
def enable_human_turn():
    global human_turn
    # enable human turn and schedule next_move so the blocking numinput happens AFTER AI drawing
    human_turn = True
    t.ontimer(next_move, 50)

# Execute the random computer player's move and update the game state
def randy_move_wrapper():
    global turns_left
    # perform AI move
    randy.make_randy_move()
    turns_left -= 1
    # give a short delay to ensure any randy's-drawing animations finish before prompting human
    t.ontimer(enable_human_turn, PLAYER_MOVE_MS)

# Control the game flow by checking for winners, draws, and switching turns
def next_move():
    global turns_left, game_over, human_turn
    if game_over:
        return
    winner, winning_cells = check_winner()
    if winner:
        winner_name = p1_name if winner == 'X' else p2_name
        announce_winner(winning_cells,winner_name)
        save_game_result(p1_name, p2_name, winner_name)
        game_over = True
        t.done()
        return
    if turns_left <= 0 and not game_over:
        save_game_result(p1_name, p2_name, "Draw")
        print("Game over,it's a draw!")
        t.done()
        return

    if human_turn:
        result = human_moves()
        if result == "loaded":
            occupied = sum(1 for v in moves.board_state.values() if v is not None)
            turns_left = 9 - occupied

            if player_mode != 1:
                human_turn = (occupied % 2 == 0)

            print(f"Game loaded! Turns left: {turns_left}")
            t.ontimer(next_move, 100)
            return

        if result is True:
            turns_left -= 1
            if player_mode != 1:
                human_turn = False
            t.ontimer(next_move, 100)
    else:
        if player_mode == 2:
            t.ontimer(randy_move_wrapper, PLAYER_MOVE_MS)
        elif player_mode == 3:
            t.ontimer(auto_move_wrapper, PLAYER_MOVE_MS)

# Initialize the game environment, set the mode, and start the gameplay loop
def main():
    global turns_left, game_over,player_mode, human_turn, p1_name, p2_name
    board.setup_turtle()
    board.draw_board()

    p1_name = screen.textinput("Player 1", "Enter name for Player 1:")
    player_mode_val = screen.numinput(
        "Game Mode",
        "Select game mode:\n"
        "1. Human only\n"
        "2. Human vs Random Player\n"
        "3. Human vs Automatic Player",
        minval=1,
        maxval=3,
    )
    if player_mode_val is None:
        print("No mode selected. Exiting.")
        return

    player_mode = int(player_mode_val)

    #Human always starts first
    if player_mode == 1:
        p2_name = screen.textinput("Player 2", "Enter name for Player 2:")
    elif player_mode == 2:
        p2_name = "Randy"
    else:
        p2_name = "Automatic Player"
    # start the loop
    next_move()

# start the game
main()
t.mainloop()
