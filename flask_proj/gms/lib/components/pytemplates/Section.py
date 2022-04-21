from abc import ABC, abstractmethod

class Section(ABC):
    @abstractmethod
    def __init__(self, *, goal_label, section_name):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get_goal_label(self):
        pass
