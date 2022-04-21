import datetime
from gms.lib.components.pytemplates.Goal import Goal

class JsonGoal(Goal):
    def __init__(self, *, goal_name, official_start_time=None, official_end_time=None):
        self.__creation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
        self.__official_start_time = official_start_time
        self.__official_end_time = official_end_time
        self.__goal_name = goal_name
        self.goal = { 
            f'{self.__goal_name}': {
                'creation_time': self.__creation_time,
                'official_start_time': self.__official_start_time,
                'official_end_time': self.__official_end_time,
                'final_review_time': None
            }
        }

    def get_name(self):
        return self.__goal_name

    def delete(self):
        self.goal = None
    
    def __str__(self):
        return str(self.goal)
    
    def __getitem__(self, item):
         return self.goal[item]

