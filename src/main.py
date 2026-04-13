"""
Number Guessing Game - Main Entry Point
A CLI-based number guessing game with multiple difficulty levels,
hints system, and high score tracking.
"""

import os
import sys
from typing import Optional
from game import Game
from difficulty import Difficulty, display_difficulty_menu
from score_manager import ScoreManager


def clear_screen():
    """Clear console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_welcome_message():
    """Display welcome message and game rules."""
    print("=" * 60)
    print("Welcome to the Number Guessing Game!".center(60))
    print("=" * 60)
    print("\n📋 GAME RULES:")
    print("-" * 60)
    print("1. I'm thinking of a number between 1 and 100.")
    print("2. You need to guess the correct number.")
    print("3. Select a difficulty level to determine your chances.")
    print("4. After each wrong guess, you'll be told if the number")
    print("   is greater or less than your guess.")
    print("5. You can request hints to help you guess correctly.")
    print("6. The game ends when you guess correctly or run out of chances.")
    print("\n✨ FEATURES:")
    print("   • Multiple difficulty levels (Easy, Medium, Hard)")
    print("   • Hint system to help you guess")
    print("   • Timer to track how long you take")
    print("   • High score tracking")
    print("   • Play multiple rounds")
    print("-" * 60)


def get_valid_guess() -> int:
    """Get a valid guess from user."""
    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❌ Please enter a number between 1 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def display_game_menu():
    """Display in-game menu options."""
    print("\nWhat would you like to do?")
    print("1. Make a guess")
    print("2. Get a hint")
    print("3. Show game status")
    print("4. Quit game")
    choice = input("Enter your choice (1/2/3/4): ").strip()
    return choice


def play_round(score_manager: ScoreManager) -> bool:
    """
    Play a single round of the game.
    
    Returns:
        True if player wants to play again, False otherwise.
    """
    print("\n" + "=" * 60)
    
    # Select difficulty
    difficulty = display_difficulty_menu()
    
    print(f"\n✓ You have selected the {difficulty.name} difficulty level.")
    print("Let's start the game!\n")
    
    # Initialize game
    game = Game(difficulty)
    
    # Game loop
    while not game.is_game_over():
        print(game.get_game_status())
        choice = display_game_menu()
        
        if choice == '1':
            guess = get_valid_guess()
            is_correct, message = game.process_guess(guess)
            print(message)
            
            if is_correct:
                # Save score
                difficulty_name = difficulty.name.lower()
                score_manager.add_score(difficulty_name, game.current_attempt)
                
                # Display stats
                stats = score_manager.get_statistics(difficulty_name)
                if stats['games_played'] > 1:
                    print(f"\n📊 Your stats on {difficulty.name}:")
                    print(f"   Best score: {stats['best_score']} attempts")
                    print(f"   Average: {stats['average_score']:.1f} attempts")
                    print(f"   Total games: {stats['games_played']}")
                
                break
        
        elif choice == '2':
            hint_message = game.request_hint()
            print(hint_message)
        
        elif choice == '3':
            print(game.get_game_status())
        
        elif choice == '4':
            print("\nThanks for playing! Game ended.")
            return play_again()
        
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
    
    # Ask to play again
    return play_again()


def play_again() -> bool:
    """Ask player if they want to play again."""
    while True:
        choice = input("\n\nWould you like to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def display_goodbye_message():
    """Display goodbye message."""
    print("\n" + "=" * 60)
    print("Thanks for playing the Number Guessing Game!".center(60))
    print("=" * 60)
    print("Goodbye! 👋\n")


def main():
    """Main game loop."""
    score_manager = ScoreManager()
    
    display_welcome_message()
    
    try:
        while True:
            if not play_round(score_manager):
                break
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Game interrupted by user.")
    
    display_goodbye_message()


if __name__ == "__main__":
    main()
