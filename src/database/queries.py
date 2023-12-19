import bcrypt
import psycopg2
from .config import Configuracao

class BancoDeDados:
    def __init__(self):
        self.configuracao = Configuracao().obter_configuracao()

    def conectar(self):
        return psycopg2.connect(**self.configuracao)

    def criar_database(self):
        params = self.configuracao.copy()
        database_name = params.pop('database', None)
        conn = psycopg2.connect(**params)
        conn.autocommit = True
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {database_name};")
        finally:
            conn.close()
    def search_data(self, tabela):
        """Busca todos os dados de uma tabela especificada."""
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {tabela}")
                result = cursor.fetchall()
        return result
class Usuario:
    def __init__(self, db):
        self.db = db

    def adicionar(self, username, password, user_type):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (username, password, user_type) VALUES (%s, %s, %s)",
                    (username, hashed.decode('utf-8'), user_type)
                )

    def login(self, username, password):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT password, user_type FROM users WHERE username = %s", (username,))
                result = cursor.fetchone()
                if result:
                    hashed_password = result[0].encode('utf-8')
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                        return result[1]
        return None

class Projeto:
    def __init__(self, db):
        self.db = db

    def adicionar(self, name, begin_date, end_date):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projects (name, begin_date, end_date) VALUES (%s, %s, %s)",
                    (name, begin_date, end_date)
                )

    def remover(self, project_id):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM projects WHERE id = %s",
                    (project_id,)
                )

    def atualizar(self, project_id, name, begin_date, end_date):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE projects SET name = %s, begin_date = %s, end_date = %s WHERE id = %s",
                    (name, begin_date, end_date, project_id)
                )

    # Métodos adicionais conforme necessário...

class Tarefa:
    def __init__(self, db):
        self.db = db

    def adicionar(self, name, priority, status_id, project_id, begin_date, end_date):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tasks (name, priority, status_id, project_id, begin_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (name, priority, status_id, project_id, begin_date, end_date)
                )

    def remover(self, task_id):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM tasks WHERE id = %s",
                    (task_id,)
                )

    def atualizar(self, task_id, name, priority, status_id, project_id, begin_date, end_date):
        with self.db.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE tasks SET name = %s, priority = %s, status_id = %s, project_id = %s, begin_date = %s, end_date = %s WHERE id = %s",
                    (name, priority, status_id, project_id, begin_date, end_date, task_id)
                )
