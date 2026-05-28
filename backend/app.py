from services.objectives_service import (
    get_all_objectives,
    get_completed_objectives,
    get_objective_by_id,
    add_objective
)
def show_menu():

    print("\n=== BACKEND PYTHON ===\n")
    print("1 - Listar objetivos")
    print("2 - Objetivos concluídos")
    print("3 - Buscar objetivo por ID")
    print("4 - Adicionar objetivo")
    print("5 - Sair")

while True:

    show_menu()

    option = input("\nEscolha uma opção: ")

    if option == '1':
        objectives = get_all_objectives()

        print("\nLISTA DE OBJETIVOS:\n")

        for objective in objectives:
            print(objective)

    elif option == "2":
        completed = get_completed_objectives()

        print("\nOBJETIVOS CONCLUÍDOS:\n")

        for objective in completed:
            print(objective)

    elif option == '3':
        objective_id = int(input("\nDigite o ID do objetivo: "))

        objective = get_objective_by_id(objective_id)

        if objective:

            print("\nOBJETIVO ENCONTRADO:\n")
            print(objective)

        else:

            print("\nObjetivo não encontrado.")
        
    elif option == "4":

        title = input(
            "\nDigite o nome do objetivo: "
        )

        new_objective = add_objective(title)

        if new_objective:

            print("\nObjetivo criado com sucesso.\n")
            print(new_objective)

        else:

            print("\nTítulo inválido.")

    elif option == "5":

        print("\nEncerrando aplicação...")
        break

    else:

        print("\nOpção inválida.")

