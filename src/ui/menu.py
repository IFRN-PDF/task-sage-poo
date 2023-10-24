from ..database.queries import add_project, remove_project, update_project, search_data, add_task, remove_task, update_task

def get_input_for_project():
    name = input("Nome do projeto: ")
    begin_date = input("Data de início (AAAA-MM-DD): ")
    end_date = input("Data de término (AAAA-MM-DD): ")
    return name, begin_date, end_date

def get_input_for_task():
    name = input("Nome da tarefa: ")
    project_id = input("ID do projeto: ")
    due_date = input("Data de conclusão (AAAA-MM-DD): ")
    status = input("Status da tarefa: ")
    return name, project_id, due_date, status

def display_data(tabela):
    data = search_data(tabela)
    for item in data:
        print(item)

def admin_project_options():
    while True:
        print("\n-- Projetos --")
        print("1. Adicionar projeto")
        print("2. Remover projeto")
        print("3. Atualizar projeto")
        print("4. Visualizar projetos")
        print("X. Voltar ao menu principal")

        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            add_project(*get_input_for_project())
        elif choice == "2":
            project_id = input("ID do projeto a ser removido: ")
            remove_project(project_id)
        elif choice == "3":
            project_id = input("ID do projeto a ser atualizado: ")
            name, begin_date, end_date = get_input_for_project()
            update_project(project_id, name=name, begin_date=begin_date, end_date=end_date)
        elif choice == "4":
            display_data("projects")
        elif choice.lower() == 'x':
            break

def admin_task_options():
    while True:
        print("\n-- Tarefas --")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Atualizar tarefa")
        print("4. Visualizar tarefas")
        print("X. Voltar ao menu principal")

        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            add_task(*get_input_for_task())
        elif choice == "2":
            task_id = input("ID da tarefa a ser removida: ")
            remove_task(task_id)
        elif choice == "3":
            task_id = input("ID da tarefa a ser atualizada: ")
            name, project_id, due_date, status = get_input_for_task()
            update_task(task_id, name=name, project_id=project_id, due_date=due_date, status=status)
        elif choice == "4":
            display_data("tasks")
        elif choice.lower() == 'x':
            break

def show_menu(user_type):
    while True:
        if user_type == "admin":
            print("\n-- Menu Administrador --")
            print("1. Projetos")
            print("2. Tarefas")
            print("X. Sair")
            
            choice = input("\nEscolha uma opção: ")
            if choice == "1":
                admin_project_options()
            elif choice == "2":
                admin_task_options()
            elif choice.lower() == 'x':
                break

        elif user_type == "viewer":
            print("\n-- Menu Visualizador --")
            print("1. Visualizar projetos")
            print("2. Visualizar tarefas")
            print("X. Sair")

            choice = input("\nEscolha uma opção: ")

            if choice == "1":
                display_data("projects")
            elif choice == "2":
                display_data("tasks")
            elif choice.lower() == 'x':
                break
