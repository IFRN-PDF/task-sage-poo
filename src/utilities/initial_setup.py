from src.database.queries import add_user, criar_database
from src.database.models import criar_tabelas

def initial_setup():
    criar_database()
    criar_tabelas()
    
    add_user("admin", "password123", "administrator")
    add_user("viewer", "password123", "viewer")

if __name__ == "__main__":
    initial_setup()
