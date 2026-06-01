from services.file_service import (load_objectives,save_objectives)

from utils.validations import validate_title

def get_all_objectives():

    return load_objectives()

def get_completed_objectives():
    objectives = load_objectives()

    completed = []

    for objective in objectives:

        if objective["completed"]:
            completed.append(objective)

    return completed

def get_objective_by_id(objective_id):

    objectives = load_objectives()

    for objective in objectives:

        if objective["id"] == objective_id:
            return objective

    return None

def add_objective(title):

    objectives = load_objectives()

    if validate_title(title) == False:

        return None

    new_objective = {
        "id": len(objectives) + 1,
        "title": title,
        "completed": False
    }

    objectives.append(new_objective)

    save_objectives(objectives)

    return new_objective