from database.queries import Projeto, Tarefa, BancoDeDados

class Menu:
    def __init__(self, user_type):
        self.user_type = user_type
        self.db = BancoDeDados()
        self.projeto = Projeto(self.db)
        self.tarefa = Tarefa(self.db)

    def get_input_for_project(self):
        name = input("Nome do projeto: ")
        begin_date = input("Data de início (AAAA-MM-DD): ")
        end_date = input("Data de término (AAAA-MM-DD): ")
        return name, begin_date, end_date

    def get_input_for_task(self):
        name = input("Nome da tarefa: ")
        priority = int(input("Prioridade (número): "))  
        status_id = int(input("ID do Status: ")) 
        project_id = int(input("ID do projeto: ")) 
        begin_date = input("Data de início (AAAA-MM-DD): ")
        end_date = input("Data de conclusão (AAAA-MM-DD): ")
        return name, priority, status_id, project_id, begin_date, end_date

    def display_data(self, tabela):
        data = self.db.search_data(tabela)
        for item in data:
            print(item)
    def admin_project_options(self):
        while True:
            print("\n-- Projetos --")
            print("1. Adicionar projeto")
            print("2. Remover projeto")
            print("3. Atualizar projeto")
            print("4. Visualizar projetos")
            print("X. Voltar ao menu principal")

            choice = input("\nEscolha uma opção: ")

            if choice == "1":
                name, begin_date, end_date = self.get_input_for_project()
                self.projeto.adicionar(name=name, begin_date=begin_date, end_date=end_date)
            elif choice == "2":
                project_id = input("ID do projeto a ser removido: ")
                self.projeto.remover(project_id)
            elif choice == "3":
                project_id = input("ID do projeto a ser atualizado: ")
                name, begin_date, end_date = self.get_input_for_project()
                self.projeto.atualizar(project_id, name=name, begin_date=begin_date, end_date=end_date)
            elif choice == "4":
                self.display_data("projects")
            elif choice.lower() == 'x':
                break

    def admin_task_options(self):
        while True:
            print("\n-- Tarefas --")
            print("1. Adicionar tarefa")
            print("2. Remover tarefa")
            print("3. Atualizar tarefa")
            print("4. Visualizar tarefas")
            print("X. Voltar ao menu principal")

            choice = input("\nEscolha uma opção: ")

            if choice == "1":
                name, priority, status_id, project_id, begin_date, end_date = self.get_input_for_task()
                self.tarefa.adicionar(name=name, priority=priority, status_id=status_id, project_id=project_id, begin_date=begin_date, end_date=end_date)
            elif choice == "2":
                task_id = input("ID da tarefa a ser removida: ")
                self.tarefa.remover(task_id)
            elif choice == "3":
                task_id = input("ID da tarefa a ser atualizada: ")
                name, priority, status_id, project_id, begin_date, end_date = self.get_input_for_task()
                self.tarefa.atualizar(task_id, name=name, priority=priority, status_id=status_id, project_id=project_id, begin_date=begin_date, end_date=end_date)
            elif choice == "4":
                self.display_data("tasks")
            elif choice.lower() == 'x':
                break
    def show(self):
        while True:
            if self.user_type == "administrator":
                print("\n-- Menu Administrador --")
                print("1. Projetos")
                print("2. Tarefas")
                print("X. Sair")
                
                choice = input("\nEscolha uma opção: ")
                if choice == "1":
                    self.admin_project_options()
                elif choice == "2":
                    self.admin_task_options()
                elif choice.lower() == 'x':
                    break

            elif self.user_type == "viewer":
                print("\n-- Menu Visualizador --")
                print("1. Visualizar projetos")
                print("2. Visualizar tarefas")
                print("X. Sair")

                choice = input("\nEscolha uma opção: ")

                if choice == "1":
                    self.display_data("projects")
                elif choice == "2":
                    self.display_data("tasks")
                elif choice.lower() == 'x':
                    break
def show_menu(user_type):
    menu = Menu(user_type)
    menu.show()