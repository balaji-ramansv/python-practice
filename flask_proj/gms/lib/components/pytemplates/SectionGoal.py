from abc import ABC, abstractmethod

class SectionGoal(ABC):
    @abstractmethod
    def __init__(self, *, category, desc, weightage):
        pass

    @abstractmethod
    def update_desc(self, *, desc):
        pass

    @abstractmethod
    def update_weightage(self, *, weightage):
        pass

    @abstractmethod
    def update_own_rating(self, *, own_rating):
        pass

    @abstractmethod
    def update_own_justification(self, *, own_justification):
        pass

    @abstractmethod
    def update_manager_rating(self, *, manager_rating):
        pass

    @abstractmethod
    def update_manager_feedback(self, *, manager_feedback):
        pass

    @abstractmethod
    def delete(self):
        pass
