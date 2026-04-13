from enum import Enum
from typing import NamedTuple


class DifficultySettings(NamedTuple):
    """Settings for each difficulty level."""
    attempts: int
    hints_allowed: int


class Difficulty(Enum):
    """Difficulty levels with their configurations."""
    EASY = DifficultySettings(attempts=10, hints_allowed=5)
    MEDIUM = DifficultySettings(attempts=5, hints_allowed=3)
    HARD = DifficultySettings(attempts=3, hints_allowed=1)


def get_difficulty_from_choice(choice: str) -> Difficulty:
    """Convert user input to Difficulty level."""
    choice_map = {
        '1': Difficulty.EASY,
        '2': Difficulty.MEDIUM,
        '3': Difficulty.HARD,
    }
    return choice_map.get(choice.strip())


def display_difficulty_menu() -> Difficulty:
    """Display difficulty selection menu and return chosen difficulty."""
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        difficulty = get_difficulty_from_choice(choice)
        
        if difficulty:
            return difficulty
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
