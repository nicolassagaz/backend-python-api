from fastapi import FastAPI

from services.objectives_service import (
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
    return get_objective_by_id(objective_id)

@app.post("/objectives")
def create_objective(title: str):

    return add_objective(title)

@app.put("/objectives/{objective_id}")
def complete_objective(objective_id: int):
    return update_objective(objective_id)

@app.delete("/objective/{objective_id}")
def remove_objective(objective_id: int):
    return delete_objective(objective_id)