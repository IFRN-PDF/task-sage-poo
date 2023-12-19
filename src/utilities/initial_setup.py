from database.queries import BancoDeDados, Usuario
from database.models import ModeloBD

def initial_setup():
    # Criar banco de dados e tabelas
    db = BancoDeDados()
    db.criar_database()

    modelo = ModeloBD(db)
    modelo.criar_tabelas()

    # Adicionar usuários
    usuario = Usuario(db)
    usuario.adicionar("admin", "password123", "administrator")
    usuario.adicionar("viewer", "password123", "viewer")
