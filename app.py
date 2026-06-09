from fastapi import FastAPI, HTTPException

from services.tickets_service import (
    get_all_tickets,
    get_completed_objectives,
    get_ticket_by_id,
    create_ticket,
    update_ticket,
    delete_ticket
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Backend Python API"
    }


@app.get("/objectives")
def list_objectives():
    return get_all_tickets()


@app.get("/objectives/completed")
def list_completed_objectives():
    return get_completed_objectives()


@app.get("/objectives/{objective_id}")
def find_objective(objective_id: int):
    objective = get_ticket_by_id(objective_id)

    if objective is None:
        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    return objective

@app.post("/tickets", status_code=201)
def create_new_ticket(
    title: str,
    description: str,
    priority: str
):

    return create_ticket(title, description, priority)

@app.put("/objectives/{objective_id}")
def complete_objective(objective_id: int):
    
    objective = update_ticket(objective_id)

    if objective is None:

        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    
    return objective

@app.delete("/objectives/{objective_id}")
def remove_objective(objective_id: int):
    
    deleted = delete_ticket(objective_id)

    if deleted is False:

        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    
    return{
        "message": "Objetivo removido"
    }
