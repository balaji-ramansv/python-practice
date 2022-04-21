from flask_proj.gms.lib.components.pytemplates.SectionGoal import SectionGoal
from flask_proj.gms.lib.components.implementations.json.JsonSection import JsonSection

class JsonSectionGoal(SectionGoal):
    def __init__(self, *, section, desc, weightage):
        #import pdb; pdb.set_trace()
        self.section = section
        self.__section_goal_id = self.__generate_section_goal_id()
        print(f"section -- {self.section}")
        print(f"section_goal_id -- {self.__section_goal_id}")
        self.validate_weightage(weightage=weightage)
        self.__section_goal = {
            'desc': desc,
            'weightage': weightage,
            'own_rating': None,
            'own_justification': None,
            'manager_rating': None,
            'manager_feedback': None,
            'final_rating': None
        }
        self.section[f"{self.section.get_name()}"][f"{self.__section_goal_id}"] = self.__section_goal

    def __generate_section_goal_id(self):
        if len(self.section[self.section.get_name()]) == 0:
            return "1"
        ids = []
        for id in self.section[self.section.get_name()]:
            ids.append(int(id))
        print(f"ids -- {ids}")
        return str(max(ids) + 1)

    def validate_weightage(self, *, weightage):
        weightages = []
        weightages.append(weightage)
        if len(self.section[self.section.get_name()]) >= 1:    
            for goal in self.section[self.section.get_name()]:
                weightages.append(goal['weightage'])
        assert sum(weightages) <= 100, f'Maximum weightage that can be assigned is {100 - sum(weightages[1:])}'

    def update_desc(self, *, desc):
        self.__section_goal['desc'] = desc

    def update_weightage(self, *, weightage):
        self.validate_weightage(weightage=weightage)
        self.__section_goal['weightage'] = weightage

    def update_own_rating(self, *, own_rating):
        assert own_rating <= 5, f'{own_rating} is invalid. The valid range is 1-5.'
        self.__section_goal['own_rating'] = own_rating
    
    def update_own_justification(self, *, own_justification):
        self.__section_goal['own_justification'] = own_justification

    def update_manager_rating(self, *, manager_rating):
        assert manager_rating <= 5, f'{manager_rating} is invalid. The valid range is 1-5.'
        self.__section_goal['manager_rating'] = manager_rating

    def update_manager_feedback(self, *, manager_feedback):
        self.__section_goal['manager_feedback'] = manager_feedback

    def delete(self):
        self.__section_goal = None

    def __str__(self):
        return str(self.__section_goal)
    
    def __getitem__(self, item):
        print(f"item -- {item}")
        return self.__section_goal_id[item]
    
    def __setitem__(self, item, value):
        setattr(self.__section_goal_id, item, value)