from queries import conectar_db

def criar_tabelas():
    with conectar_db() as conn:
        with conn.cursor() as cursor:
            # Tabela de Projetos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id serial integer PRIMARY KEY,
                    name text NOT NULL,
                    begin_date text,
                    end_date text
                );
            """)

            # Tabela de Tarefas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id serial integer PRIMARY KEY,
                    name text NOT NULL,
                    priority integer,
                    status_id integer NOT NULL,
                    project_id integer NOT NULL,
                    begin_date text NOT NULL,
                    end_date text NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects (id)
                );
            """)

            # Tabela de Usuários
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id serial PRIMARY KEY,
                    username text NOT NULL,
                    password text NOT NULL,
                    user_type text NOT NULL CHECK (user_type IN ('administrator', 'viewer'))
                );
            """)
