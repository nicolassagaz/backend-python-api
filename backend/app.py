from services.objectives_service import (
    get_all_objectives,
    get_completed_objectives,
    add_objective
)

print("\nTODOS OS OBJETIVOS:\n")

all_objectives = get_all_objectives()

for objective in all_objectives:
    print(objective)

print("\nOBJETIVOS CONCLUÍDOS:\n")

completed_objectives = get_completed_objectives()

for objective in completed_objectives:
    print(objective)

print("\nNOVO OBJETIVO:\n")

new_objective = add_objective(
    "Aprender FastAPI"
)
print(new_objective)

print("\nLISTA ATUALIZADA:\n")

updated_objectives = get_all_objectives()

for objective in updated_objectives:
    print(objective)