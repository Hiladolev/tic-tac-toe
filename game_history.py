#This file manages the game history by saving results and displaying past matches in a text file
import os

HISTORY_FILE = "game_history.txt"

#Saves game result to the history file
def save_game_result(player1_name, player2_name, winner_name):
    append_to_history_file = open(HISTORY_FILE, "a")
    append_to_history_file.write(f"{player1_name},{player2_name},{winner_name}\n")
    append_to_history_file.close()

#    Displays all game history from the file
def display_history():
    if not os.path.exists(HISTORY_FILE):
        print("No game history yet.")
        return

    read_history_file =  open(HISTORY_FILE, "r")
    lines = read_history_file.readlines()

    if not lines:
        print("No game history yet.")
        return

    print("\n" + "=" * 50)
    print("Game History".center(50))
    print("=" * 50)

    for i, line in enumerate(lines, 1):
        parts = line.strip().split(",")
        if len(parts) == 3:
            player1, player2, winner = parts
            print(f"{i}. {player1} vs {player2} - Winner: {winner}")

    print("=" * 50 + "\n")
