import os, sys
import json
sys.path.insert(1, os.getcwd())

from flask_proj.gms.lib.components.implementations.json.JsonGoal import JsonGoal
from flask_proj.gms.lib.components.implementations.json.JsonSection import JsonSection
from flask_proj.gms.lib.components.implementations.json.JsonSectionGoal import JsonSectionGoal


g = JsonGoal(goal_name='Q1')
print("\n\ngoal\n\n")
print(g)

c = JsonSection(goal=g, section_name='personal')
print("\n\nsection\n\n")
print(c)
print(g)

go = JsonSectionGoal(section=c, desc="Go through K8S materials and complete", weightage=20)
print("\n\nsection goal\n\n")
print(go)
print(c)
print(g)