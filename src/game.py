import random
import time
from typing import Tuple
from difficulty import Difficulty
from hints import HintSystem
from score_manager import ScoreManager


class Game:
    """Main game logic for the number guessing game."""
    
    def __init__(self, difficulty: Difficulty):
        self.difficulty = difficulty
        self.settings = difficulty.value
        self.secret_number = random.randint(1, 100)
        self.attempts_left = self.settings.attempts
        self.current_attempt = 0
        self.hint_system = HintSystem(self.secret_number)
        self.hints_used = 0
        self.start_time = time.time()
        self.guesses: list = []
    
    def process_guess(self, guess: int) -> Tuple[bool, str]:
        """
        Process a guess and return (is_correct, message).
        
        Args:
            guess: The guessed number
            
        Returns:
            Tuple of (is_correct, feedback_message)
        """
        self.current_attempt += 1
        self.attempts_left -= 1
        self.guesses.append(guess)
        
        if guess == self.secret_number:
            return True, self._get_win_message()
        
        if guess < self.secret_number:
            feedback = f"Incorrect! The number is GREATER than {guess}."
        else:
            feedback = f"Incorrect! The number is LESS than {guess}."
        
        if self.attempts_left == 0:
            feedback += f"\n\nGame Over! You've run out of attempts. The number was {self.secret_number}."
            return False, feedback
        
        feedback += f"\nAttempts remaining: {self.attempts_left}"
        return False, feedback
    
    def _get_win_message(self) -> str:
        """Generate congratulations message on win."""
        elapsed_time = time.time() - self.start_time
        message = f"\n🎉 Congratulations! You guessed the correct number in {self.current_attempt} attempt(s)!"
        message += f"\nTime taken: {elapsed_time:.1f} seconds"
        message += f"\nDifficulty: {self.difficulty.name}"
        return message
    
    def request_hint(self) -> str:
        """Request a hint from the hint system."""
        if self.hints_used >= self.settings.hints_allowed:
            return f"You've used all {self.settings.hints_allowed} hints available at this difficulty level!"
        
        self.hints_used += 1
        hint = self.hint_system.get_hint()
        remaining = self.hint_system.hints_remaining()
        
        return f"💡 Hint: {hint}\nHints remaining: {remaining}"
    
    def get_game_status(self) -> str:
        """Get current game status."""
        status = f"\nAttempt: {self.current_attempt}/{self.settings.attempts}"
        status += f"\nAttempts left: {self.attempts_left}"
        status += f"\nHints available: {self.settings.hints_allowed - self.hints_used}/{self.settings.hints_allowed}"
        return status
    
    def is_game_over(self) -> bool:
        """Check if game is over."""
        return self.attempts_left == 0 or self.secret_number in self.guesses
    
    def is_won(self) -> bool:
        """Check if player won."""
        return self.secret_number in self.guesses
