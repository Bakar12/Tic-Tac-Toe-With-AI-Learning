# Tic-Tac-Toe with AI Learning

This is a Tic-Tac-Toe game implemented in Python with a graphical user interface (GUI) using `Tkinter`. The AI (playing as "O") learns how to improve its strategy through Q-learning, a simple form of reinforcement learning. The AI’s learning progress is saved in a CSV file and retained across multiple game sessions, allowing the AI to get better at playing over time.

## Features

- **Player vs AI**: You (Player X) can play against the AI (Player O).
- **AI Learning**: The AI learns from each game using Q-learning.
- **Persistent Learning**: The AI retains its learning across sessions by saving the Q-table to a CSV file.
- **Graphical Interface**: The game has a simple and easy-to-use graphical interface built with `Tkinter`.

## How It Works

### Q-Learning

Q-learning is a type of reinforcement learning where the AI learns the optimal actions to take in a given state by receiving rewards or penalties based on its actions. In this game:

- **State**: The current state of the Tic-Tac-Toe board (3x3 grid).
- **Action**: A move (placing 'O' in an empty spot on the grid).
- **Reward**: The AI receives a positive reward (+1) for winning, a negative reward (-1) for losing, and no reward (0) for a draw.

The AI stores state-action pairs in a **Q-table** and uses this table to decide future moves based on past experience. Over time, the AI learns to make moves that maximize its chances of winning.

### Game Flow

1. **Player Move**: You (Player X) make your move by clicking a cell in the 3x3 grid.
2. **AI Move**: The AI (Player O) makes its move, either by exploring (random move) or exploiting (making the best known move based on the Q-table).
3. **End of Game**: The game checks if there’s a winner or a draw.
4. **Q-Table Update**: After the game, the Q-table is updated based on the outcome (win, lose, draw), and the AI learns from the result.
5. **Save/Load Q-Table**: The Q-table is saved to a CSV file (`q_table.csv`) after each game and loaded at the start of each new session.

## Prerequisites

- Python 3.x
- Required libraries:
  - `Tkinter` (for GUI, comes with Python standard library)
  - `csv` (for saving/loading Q-table, comes with Python standard library)

## Code Structure

- **`tic_tac_toe.py`**: The main script that runs the game and handles the AI logic.
- **`q_table.csv`**: A CSV file where the Q-table is saved and loaded from. It contains the AI's learned state-action pairs and corresponding Q-values.

### Key Functions

1. **`update_q_table()`**: Updates the Q-values in the Q-table after each game based on the reward and future rewards.
2. **`save_q_table_to_csv()`**: Saves the Q-table to a CSV file so the AI can retain its learning across sessions.
3. **`load_q_table_from_csv()`**: Loads the Q-table from a CSV file when the program starts.
4. **`ai_move()`**: Handles the AI's move, choosing between exploration (random move) and exploitation (best move based on Q-table).
5. **`check_winner()`**: Checks if a player has won the game.
6. **`check_draw()`**: Checks if the game ended in a draw.

## How to Run the Game

1. **Clone the Repository or Copy the Code**: Download the project or copy the provided code into a file named `tic_tac_toe.py`.

2. **Install Python**: Make sure Python 3.x is installed on your system.

3. **Run the Game**:
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved `tic_tac_toe.py`.
   - Run the game using the following command:

   ```bash
   python tic_tac_toe.py
    ```
## Play the Game:
- A GUI window will open with a 3x3 grid.
- You (Player X) make your move by clicking on a cell.
- The AI (Player O) will respond, learning and improving after each game.

---

## Q-Table: Learning and Persistence
The Q-table is a dictionary that maps each board state (a tuple of 9 elements representing the Tic-Tac-Toe grid) and an action (a move the AI made) to a Q-value (how good that move is in that state). The Q-table is saved in a file named `q_table.csv` after every game, so the AI retains its knowledge across sessions.

---

### Example Q-Table CSV
The `q_table.csv` file contains the following columns:

- **State**: The Tic-Tac-Toe board state represented as a tuple.
- **Action**: The index of the move (from 0 to 8) that the AI took.
- **Q-Value**: The Q-value of the state-action pair, representing how good or bad the move was.

#### Example CSV file:

```csv
State,Action,Q-Value
(' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'X'),4,0.5
(' ', ' ', 'X', ' ', 'O', ' ', ' ', ' ', ' '),4,0.7
...
```
## Persistent Learning
- When the program starts, it loads the Q-table from `q_table.csv`. If this file doesn’t exist, it initializes an empty Q-table.
- After each game, the Q-table is updated based on the game result (win, lose, or draw).
- The Q-table is saved back to `q_table.csv`, so the AI's learning persists across game sessions.

---

## Parameters and Customisation
You can customize the AI's learning behavior by tweaking the following parameters in the code:

- **`learning_rate`**: Controls how much new information overrides old information. Values range from 0 to 1.

```python
learning_rate = 0.1  # Default value
```
- discount_factor: Determines how much the AI values future rewards. A value close to 1 means future rewards are highly valued.
- exploration_rate: Controls how often the AI explores new moves instead of exploiting known moves. A value close to 1 means more exploration.

```python'
discount_factor = 0.9  # Default value
exploration_rate = 0.1  # Default value
```


