from fastapi import FastAPI, HTTPException

from services.tickets_service import (
    get_all_objectives,
    get_completed_objectives,
    get_objective_by_id,
    add_objective,
    update_objective,
    delete_objective
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Backend Python API"
    }


@app.get("/objectives")
def list_objectives():
    return get_all_objectives()


@app.get("/objectives/completed")
def list_completed_objectives():
    return get_completed_objectives()


@app.get("/objectives/{objective_id}")
def find_objective(objective_id: int):
    objective = get_objective_by_id(objective_id)

    if objective is None:
        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    return objective

@app.post("/objectives", status_code=201)
def create_objective(title: str):

    objective = add_objective(title)

    if objective is None:
        raise HTTPException(status_code=400, detail="Título inválido")
    
    return objective

@app.put("/objectives/{objective_id}")
def complete_objective(objective_id: int):
    
    objective = update_objective(objective_id)

    if objective is None:

        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    
    return objective

@app.delete("/objectives/{objective_id}")
def remove_objective(objective_id: int):
    
    deleted = delete_objective(objective_id)

    if deleted is False:

        raise HTTPException(status_code=404, detail="Objetivo não encontrado")
    
    return{
        "message": "Objetivo removido"
    }