import random
from typing import List, Set


class HintSystem:
    """Manages hints for the guessing game."""
    
    def __init__(self, secret_number: int):
        self.secret_number = secret_number
        self.used_hints: Set[str] = set()
        self.all_hints = self._generate_all_hints()
    
    def _generate_all_hints(self) -> List[str]:
        """Generate all possible hints for the secret number."""
        hints = []
        
        # Parity hint
        if self.secret_number % 2 == 0:
            hints.append("The number is EVEN.")
        else:
            hints.append("The number is ODD.")
        
        # Divisibility hints
        if self.secret_number % 5 == 0:
            hints.append("The number is divisible by 5.")
        if self.secret_number % 10 == 0:
            hints.append("The number is divisible by 10.")
        if self.secret_number % 3 == 0:
            hints.append("The number is divisible by 3.")
        
        # Range hints
        if self.secret_number <= 25:
            hints.append("The number is in the lower quarter (1-25).")
        elif self.secret_number <= 50:
            hints.append("The number is in the lower half (1-50).")
        elif self.secret_number <= 75:
            hints.append("The number is in the upper half (51-100).")
        else:
            hints.append("The number is in the upper quarter (76-100).")
        
        # Digits hint
        if self.secret_number < 10:
            hints.append("The number is a single digit (1-9).")
        elif self.secret_number >= 10:
            hints.append("The number has two digits.")
        
        return hints
    
    def get_hint(self) -> str:
        """Return a random unused hint. Returns None if no hints available."""
        available_hints = [h for h in self.all_hints if h not in self.used_hints]
        
        if not available_hints:
            return "No more hints available!"
        
        hint = random.choice(available_hints)
        self.used_hints.add(hint)
        return hint
    
    def hints_remaining(self) -> int:
        """Return number of unused hints."""
        return len(self.all_hints) - len(self.used_hints)
