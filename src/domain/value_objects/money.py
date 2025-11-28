from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    
    def __post_init__(self):
        """Validate the amount after initialization."""
        if not self.is_valid(self.amount):
            raise ValueError(f"Invalid money amount: {self.amount}")
        
        
    @staticmethod
    def is_valid(amount: float) -> bool:
        """Validate that the amount is a non-negative number."""
        return isinstance(amount, (int, float)) and amount >= 0