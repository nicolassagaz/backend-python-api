from services.file_service import (load_objectives, save_objectives)

def find_all():
    return load_objectives()

def find_by_id(objective_id):
    tickets = load_objectives()

    for objective in tickets:
        if objective["id"] == objective_id:
            return objective
        
    return None

def create(new_objective):
    tickets = load_objectives()

    tickets.append(new_objective)

    save_objectives(tickets)

    return new_objective

def update(objective_id, updated_objective):
    tickets = load_objectives()

    for index, objective in enumerate(tickets):
        if objective["id"] == objective_id:

            tickets[index] = updated_objective

            save_objectives(tickets)

            return updated_objective
    return None

def delete(objective_id):
    tickets = load_objectives()

    for objective in tickets:

        if objective["id"] == objective_id:

            tickets.remove(objective)

            save_objectives(tickets)

            return True
    
    return False