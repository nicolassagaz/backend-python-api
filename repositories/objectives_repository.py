from services.file_service import (load_objectives, save_objectives)

def find_all():
    return load_objectives()

def find_by_id(objective_id):
    objectives = load_objectives()

    for objective in objectives:
        if objective["id"] == objective_id:
            return objective
        
    return None

def create(new_objective):
    objectives = load_objectives()

    objectives.append(new_objective)

    save_objectives(objectives)

    return new_objective

def update(objective_id, updated_objective):
    objectives = load_objectives()

    for index, objective in enumerate(objectives):
        if objective["id"] == objective_id:

            objectives[index] = updated_objective

            save_objectives(objectives)

            return updated_objective
    return None

def delete(objective_id):
    objectives = load_objectives()

    for objective in objectives:

        if objective["id"] == objective_id:

            objectives.remove(objective)

            save_objectives(objectives)

            return True
    
    return False