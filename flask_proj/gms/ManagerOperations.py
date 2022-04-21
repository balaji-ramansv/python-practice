from abc import ABC, abstractmethod

class ManagerOperations(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def view_reportee_goal_label(self, *, goal_label):
        pass

    @abstractmethod
    def create_category(self, *, category):
        pass

    @abstractmethod
    def provide_manager_rating_for_goal(self, *, category, goal, manager_rating):
        pass

    @abstractmethod
    def provide_manager_feedback_for_goal(self, *, category, goal, feedback):
        pass

    @abstractmethod
    def provide_final_rating_for_goal(self, *, category, goal, final_rating):
        pass