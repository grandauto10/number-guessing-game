# Number Guessing Game 🎲

A command-line based number guessing game built in Python where players try to guess a randomly selected number with limited attempts.

## Features

- 🎯 **Multiple Difficulty Levels**
  - Easy: 10 chances
  - Medium: 5 chances
  - Hard: 3 chances

- 💡 **Smart Hint System**
  - Hints about parity (even/odd)
  - Divisibility clues
  - Range information
  - Digit count hints

- ⏱️ **Timer**
  - Tracks how long it takes to guess the number

- 📊 **High Score Tracking**
  - Stores best scores per difficulty level
  - Shows statistics (best score, average attempts, total games)

- 🔄 **Multiple Rounds**
  - Play as many rounds as you want
  - Statistics persist across sessions

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Installation

1. Navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```

2. Run the game:
   ```bash
   python src/main.py
   ```

## How to Play

1. **Start the Game:**
   - Run `python src/main.py`
   - Read the welcome message and rules

2. **Select Difficulty:**
   - Choose from Easy (10 chances), Medium (5 chances), or Hard (3 chances)

3. **Make Guesses:**
   - Enter numbers between 1 and 100
   - The game tells you if the number is greater or less than your guess

4. **Use Hints (Optional):**
   - Request hints when you're stuck
   - The number of hints available depends on difficulty level

5. **Win or Lose:**
   - Win: Guess the correct number and see your stats
   - Lose: Run out of attempts and the number is revealed

6. **Play Again:**
   - Choose to play another round or quit

## Project Structure

```
number-guessing-game/
├── src/
│   ├── main.py              # Game entry point & main loop
│   ├── game.py              # Core game logic
│   ├── difficulty.py        # Difficulty levels configuration
│   ├── hints.py             # Hint system
│   └── score_manager.py     # High scores management
├── data/
│   └── scores.json          # High scores storage
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

## File Descriptions

### main.py
- Entry point for the game
- Handles main game loop and user interface
- Manages difficulty selection and replay logic
- Displays welcome message and statistics

### game.py
- Core `Game` class with all game logic
- Handles guess validation and feedback
- Manages attempts and hint tracking
- Tracks game time and status

### difficulty.py
- Defines difficulty levels (Easy, Medium, Hard)
- Configures attempts and hints per level
- Handles user input for difficulty selection

### hints.py
- `HintSystem` class for generating contextual hints
- Creates hints based on secret number properties
- Tracks used hints to avoid repeats
- Provides hints about parity, divisibility, and range

### score_manager.py
- `ScoreManager` class for persistent score storage
- Reads/writes scores to JSON file
- Calculates statistics (best score, average, total games)
- Maintains scores across game sessions

## Example Gameplay

```
Welcome to the Number Guessing Game!
...
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2

✓ You have selected the MEDIUM difficulty level.
Let's start the game!

Attempt: 1/5
Attempts left: 5
Hints available: 3/3

What would you like to do?
1. Make a guess
2. Get a hint
3. Show game status
4. Quit game
Enter your choice (1/2/3/4): 1

Enter your guess (1-100): 50
Incorrect! The number is LESS than 50.
Attempts remaining: 4

...

🎉 Congratulations! You guessed the correct number in 4 attempt(s)!
Time taken: 45.3 seconds
Difficulty: MEDIUM

📊 Your stats on medium:
   Best score: 4 attempts
   Average: 5.5 attempts
   Total games: 2

Would you like to play again? (yes/no): no
```

## Technical Details

- **Language:** Python 3.6+
- **Architecture:** Modular design with separation of concerns
- **Data Storage:** JSON file for persistent high scores
- **Platform:** Cross-platform (Windows, macOS, Linux)

## Future Enhancements

Possible features for future versions:
- Leaderboard with player names
- Difficulty achievements/badges
- Different number ranges
- Multiplayer mode
- Web interface
- Customizable game settings

## Troubleshooting

**Q: Scores not saving?**
- Ensure the `data/` directory exists
- Check file permissions on `data/scores.json`
- Try deleting `scores.json` to reset

**Q: Game crashes when accessing hints?**
- Make sure all Python files are in the `src/` directory
- Verify Python version is 3.6 or higher

**Q: On Windows, clear screen doesn't work?**
- This is a known issue with some terminal emulators
- The game will still function normally, just without screen clearing

## License

Free to use and modify for educational purposes.

## Author

Created as a Python learning project.

Enjoy the game! 🎮
