from flask_proj.gms.lib.components.pytemplates.Section import Section
from flask_proj.gms.lib.components.implementations.json.JsonGoal import JsonGoal

class JsonSection:
    def __init__(self, *, goal, section_name):
        self.__goal = goal
        if 'sections' not in self.__goal[self.__goal.get_name()]:
            self.__section_name = section_name
            self.__goal[self.__goal.get_name()]['sections'] = {}
        if section_name not in self.__goal[self.__goal.get_name()]['sections']:
            self.__goal[self.__goal.get_name()]['sections'] = {
                f'{self.__section_name}': {}
            }
        else:
            print("This section already exists.")
        self.section = self.__goal[self.__goal.get_name()]['sections']

    def get_name(self):
        return self.__section_name

    def delete(self):
        self.__goal[self.__goal.get_name()]['sections'].pop(self.__section_name)
        self.__section_name = None

    def get_goal_label(self):
        return self.__goal

    def __str__(self):
        return str(self.section)

    def __getitem__(self, item):
        return self.section[item]
    
    def __setitem__(self, item, val):
        self.section[item] = val
    
    def __len__(self):
        return len(self.section)