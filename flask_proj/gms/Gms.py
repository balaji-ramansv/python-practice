

class Goal:
    def __init__(self, *, goal):
        if goal not in self.goal:
            self.goal[goal] = {}
            self.categories = []
            self.goal_name = goal
            print(f"Goal {goal} created.")
        else:
            raise Exception(f"The goal named {goal} already exists.")

    def create_category(self, *, category_name):
        if category_name in self.goal[self.goal_name]:
            self.goal[self.goal_name][category_name] = []
        else:
            raise Exception(f"The category name {category_name} already exists.")

    def add_goal_under_category(self, *, category_name, goal_desc, weightage):
        self.goal[self.goal_name][category_name].append(
            {
                'goal_id': self.__get_goal_id(category_name=category_name),
                'goal_desc': goal_desc,
                'weightage': weightage,
                'self_rating': 'NA',
                'self_justification': 'NA',
                'manager_rating': 'NA',
                'manager_remarks': 'NA',
                'final_rating': 'NA'
            }
        )

    def __get_goal_id(self, *, category_name):
        ids = []
        for i in self.goal[self.goal_name][category_name]:
            ids.append(i['goal_id'])
        if not ids:
            return 1
        else:
            return max(ids) + 1

    def add_goal_under_category(self, *, category_name, ):