from src.database.models import criar_tabelas
from src.database.queries import add_user

def initial_setup():

    criar_tabelas()
    
    add_user("admin", "password123", "administrator")
    add_user("viewer", "password123", "viewer")

if __name__ == "__main__":
    initial_setup()
