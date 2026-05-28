from data.objectives import objectives

def get_all_objectives():
    return objectives

def get_completed_objectives():
    completed = []

    for objective in objectives:
        if objective["completed"] == True:
            completed.append(objective)

    return completed

def add_objective(title):
    new_objective = {
        "id": len(objectives) + 1,
        "title": title,
        "completed": False
    }
    objectives.append(new_objective)
    return new_objective