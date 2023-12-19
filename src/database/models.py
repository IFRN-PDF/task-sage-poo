from .queries import BancoDeDados

class ModeloBD:
    def __init__(self):
        self.db = BancoDeDados()

    def criar_tabelas(self):
        """ Cria as tabelas no banco de dados. """
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                self._criar_tabela_projetos(cursor)
                self._criar_tabela_tarefas(cursor)
                self._criar_tabela_usuarios(cursor)

    def _criar_tabela_projetos(self, cursor):
        """ Cria a tabela de projetos. """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id serial PRIMARY KEY,
                name text NOT NULL,
                begin_date text,
                end_date text
            );
        """)

    def _criar_tabela_tarefas(self, cursor):
        """ Cria a tabela de tarefas. """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id serial PRIMARY KEY,
                name text NOT NULL,
                priority integer,
                status_id integer NOT NULL,
                project_id integer NOT NULL,
                begin_date text NOT NULL,
                end_date text NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            );
        """)

    def _criar_tabela_usuarios(self, cursor):
        """ Cria a tabela de usuários. """
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                username text NOT NULL,
                password text NOT NULL,
                user_type text NOT NULL CHECK (user_type IN ('administrator', 'viewer'))
            );
        """)