from data.objectives import objectives
from utils.validations import validate_title

def get_all_objectives():
    return objectives

def get_completed_objectives():
    completed = []

    for objective in objectives:
        if objective["completed"] == True:
            completed.append(objective)

    return completed

def get_objective_by_id(objective_id):

    for objective in objectives:

        if objective["id"] == objective_id:
            return objective

    return None


def add_objective(title):

    title_is_valid = validate_title(title)

    if title_is_valid == False:
        return None

    new_objective = {
        "id": len(objectives) + 1,
        "title": title,
        "completed": False
    }

    objectives.append(new_objective)

    return new_objective