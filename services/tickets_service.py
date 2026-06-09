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

def create_ticket(title, description, priority):

    tickets = find_all()

    new_ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Aberto"
    }

    return create(new_ticket)

def update_ticket_status(ticket_id, status):

    ticket = find_by_id(ticket_id)

    if ticket is None:
        return None

    ticket["status"] = status

    return update(ticket_id, ticket)

def delete_ticket(objective_id):
    return delete(objective_id)