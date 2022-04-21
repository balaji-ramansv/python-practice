from abc import ABC, abstractmethod

class ReporteeOperations(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def create_category(self, *, category):
        pass

    @abstractmethod
    def delete_category(self, *, category):
        pass

    @abstractmethod
    def add_goal(self, *, category, goal_desc, weightage):
        pass

    @abstractmethod
    def remove_goal(self, *, category, goal):
        pass

    @abstractmethod
    def edit_goal(self, *, category, goal, updated_goal):
        pass
        
            
    