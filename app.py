from fastapi import FastAPI, HTTPException

from services.tickets_service import (
    get_all_tickets,
    get_completed_objectives,
    get_ticket_by_id,
    create_ticket,
    update_ticket_status,
    delete_ticket,
    get_tickets_filtered
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Backend Python API"
    }


@app.get("/tickets")
def list_tickets(
    status: str | None = None,
    priority: str | None = None
):

    if status or priority:

        return get_tickets_filtered(status, priority)

    return get_all_tickets()

@app.get("/objectives/completed")
def list_completed_objectives():
    return get_completed_objectives()


@app.get("/tickets/{objective_id}")
def find_ticket(ticket_id: int):
    ticket = get_ticket_by_id(ticket_id)

    if ticket is None:
        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    return ticket

@app.post("/tickets", status_code=201)
def create_new_ticket(
    title: str,
    description: str,
    priority: str
):

    return create_ticket(title, description, priority)

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, status: str):

    ticket = update_ticket_status(ticket_id, status)

    if ticket is None:

        raise HTTPException(status_code=404,
            detail="Chamado não encontrado")

    return ticket

@app.delete("/tickets/{ticket_id}")
def deleted_ticket_route(ticket_id: int):
    
    deleted = delete_ticket(ticket_id)

    if deleted is False:

        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    
    return{
        "message": "Chamado removido"
    }
