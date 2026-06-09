from repositories.tickets_repository import(find_all, find_by_id, create, update, delete)

from utils.validations import validate_title

def get_all_tickets():

    return find_all()

def get_completed_objectives():
    objectives = find_all()

    completed = []

    for objective in objectives:

        if objective["completed"]:
            completed.append(objective)

    return completed

def get_ticket_by_id(objective_id):

    return find_by_id(objective_id)

def add_ticket(title):

    objectives = find_all()

    if validate_title(title) == False:

        return None

    new_objective = {
        "id": len(objectives) + 1,
        "title": title,
        "completed": False
    }

    return create(new_objective)

def update_ticket(objective_id):
    objective = find_by_id(objective_id)

    if objective is None:
        return None
    
    objective["completed"] = True

    return update(objective_id, objective)

def delete_ticket(objective_id):
    return delete(objective_id)