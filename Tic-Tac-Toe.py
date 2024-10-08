import tkinter as tk
import random
import csv

# Initialize the Q-table
q_table = {}
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 0.2


# Update the Q-table after each game
def update_q_table(q_table, state, action, reward, next_state):
    state_action_pair = (tuple(state), action)
    old_q_value = q_table.get(state_action_pair, 0)

    # Calculate future reward
    future_rewards = [q_table.get((tuple(next_state), a), 0) for a in range(9) if next_state[a] == ' ']
    best_future_reward = max(future_rewards, default=0)

    # Update the Q-value
    new_q_value = old_q_value + learning_rate * (reward + discount_factor * best_future_reward - old_q_value)
    q_table[state_action_pair] = new_q_value


# Display the Q-table
def display_q_table(q_table):
    print("\n--- Q-Table ---")
    for key, value in q_table.items():
        state, action = key
        print(f"State: {state} | Action: {action} | Q-Value: {value}")
    print("----------------\n")


# Save Q-table to CSV
def save_q_table_to_csv(q_table, filename='q_table.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['State', 'Action', 'Q-Value'])
        for (state, action), q_value in q_table.items():
            writer.writerow([state, action, q_value])


# Load Q-table from CSV
def load_q_table_from_csv(filename='q_table.csv'):
    q_table = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                state = eval(row['State'])  # Convert string representation of tuple back to tuple
                action = int(row['Action'])
                q_value = float(row['Q-Value'])
                q_table[(state, action)] = q_value
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty Q-table
        pass
    return q_table


# Initialize the board
def init_board():
    return [' ' for _ in range(9)]  # 3x3 grid represented as a list of 9 elements


# Check for a winner
def check_winner(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_combinations)


# Check for a draw
def check_draw(board):
    return ' ' not in board


# AI move (O)
def ai_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == ' ']

    # Use exploration vs exploitation
    if random.uniform(0, 1) < exploration_rate:
        # Exploration: make a random move
        move = random.choice(empty_spots)
    else:
        # Exploitation: choose the best move from the Q-table
        state = tuple(board)
        q_values = [q_table.get((state, i), 0) for i in empty_spots]
        move = empty_spots[q_values.index(max(q_values))]

    board[move] = 'O'
    return move


# GUI Setup
class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe with AI Learning")

        # Initialize game state
        self.board = init_board()
        self.buttons = []
        self.create_buttons()
        self.current_player = 'X'  # X starts the game

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font='normal 20 bold', width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    # Player move (X)
    def player_move(self, index):
        if self.board[index] == ' ' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state=tk.DISABLED)
            if self.check_end_game():
                return
            self.current_player = 'O'
            self.ai_turn()

    # AI turn (O)
    def ai_turn(self):
        move = ai_move(self.board)
        self.buttons[move].config(text='O', state=tk.DISABLED)
        self.current_player = 'X'
        self.check_end_game()

    # Check end game
    def check_end_game(self):
        if check_winner(self.board, 'X'):
            self.end_game("Player wins!")
            return True
        elif check_winner(self.board, 'O'):
            self.end_game("AI wins!")
            return True
        elif check_draw(self.board):
            self.end_game("It's a draw!")
            return True
        return False

    # End game
    def end_game(self, message):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        self.update_q_table_after_game()
        self.show_end_message(message)

    def show_end_message(self, message):
        end_popup = tk.Toplevel(self.root)
        end_popup.title("Game Over")
        label = tk.Label(end_popup, text=message, font='normal 20 bold')
        label.pack()
        replay_button = tk.Button(end_popup, text="Play Again",
                                  command=lambda: [self.reset_game(), end_popup.destroy()])
        replay_button.pack()

    # Reset the game for a new round
    def reset_game(self):
        self.board = init_board()
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ', state=tk.NORMAL)

    # Q-learning update after each game
    def update_q_table_after_game(self):
        winner = 'X' if check_winner(self.board, 'X') else 'O' if check_winner(self.board, 'O') else None
        reward = 1 if winner == 'O' else -1 if winner == 'X' else 0  # AI wins = +1, AI loses = -1, Draw = 0

        move_history = [(self.board.copy(), i) for i, spot in enumerate(self.board) if spot == 'O']
        for previous_state, action in move_history:
            update_q_table(q_table, previous_state, action, reward, self.board)

        # Display the Q-table after updating it
        display_q_table(q_table)

        # Save the Q-table to a CSV file after each game
        save_q_table_to_csv(q_table)


# Main program execution
if __name__ == "__main__":
    # Load the Q-table from CSV file
    q_table = load_q_table_from_csv()

    root = tk.Tk()
    game = TicTacToeGame(root)

    # Run the game
    root.mainloop()

    # Save the Q-table when the program is closed
    save_q_table_to_csv(q_table)


