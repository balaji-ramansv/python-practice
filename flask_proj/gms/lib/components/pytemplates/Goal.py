from abc import ABC, abstractmethod

class Goal(ABC):
    """Abstract class on permitted operations in GoalLabels"""
    @abstractmethod
    def __init__(self, *, goal_text, start_date_time=None, end_date_time=None):
        pass
    
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def delete(self):
        pass