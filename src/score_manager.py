import json
import os
from pathlib import Path
from typing import List, Dict, Optional


class ScoreManager:
    """Manages high scores storage and retrieval."""
    
    def __init__(self, scores_file: str = "data/scores.json"):
        self.scores_file = scores_file
        self.scores = self._load_scores()
    
    def _load_scores(self) -> Dict[str, List[int]]:
        """Load scores from JSON file."""
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._initialize_scores()
        return self._initialize_scores()
    
    def _initialize_scores(self) -> Dict[str, List[int]]:
        """Initialize empty scores structure."""
        return {
            "easy": [],
            "medium": [],
            "hard": []
        }
    
    def _save_scores(self) -> None:
        """Save scores to JSON file."""
        # Create data directory if it doesn't exist
        Path(os.path.dirname(self.scores_file)).mkdir(parents=True, exist_ok=True)
        
        with open(self.scores_file, 'w') as f:
            json.dump(self.scores, f, indent=2)
    
    def add_score(self, difficulty: str, attempts: int) -> None:
        """Add a new score for a difficulty level."""
        difficulty_key = difficulty.lower()
        if difficulty_key in self.scores:
            self.scores[difficulty_key].append(attempts)
            self._save_scores()
    
    def get_best_score(self, difficulty: str) -> Optional[int]:
        """Get the best (lowest) score for a difficulty level."""
        difficulty_key = difficulty.lower()
        scores = self.scores.get(difficulty_key, [])
        return min(scores) if scores else None
    
    def get_all_scores(self, difficulty: str) -> List[int]:
        """Get all scores for a difficulty level."""
        difficulty_key = difficulty.lower()
        return sorted(self.scores.get(difficulty_key, []))
    
    def get_statistics(self, difficulty: str) -> Dict[str, any]:
        """Get statistics for a difficulty level."""
        difficulty_key = difficulty.lower()
        scores = self.scores.get(difficulty_key, [])
        
        if not scores:
            return {
                'games_played': 0,
                'best_score': None,
                'average_score': None,
                'total_games': 0
            }
        
        return {
            'games_played': len(scores),
            'best_score': min(scores),
            'average_score': sum(scores) / len(scores),
            'total_games': len(scores)
        }
