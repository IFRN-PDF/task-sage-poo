import configparser
from utilities.initial_setup import initial_setup
from src.database.queries import login_user
import getpass 
from src.ui.menu import show_menu

def login():
    print("Bem-vindo ao Sistema!")
    username = input("Digite seu nome de usuário: ")
    password = getpass.getpass("Digite sua senha: ")  
    user_type = login_user(username, password)
    return user_type is not None, user_type

if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read('config.ini')

    if config.get('SETTINGS', 'execute_initial_setup').lower() == 'yes':
        initial_setup()
    
    logged_in, user_type = login()
    if not logged_in:
        print("Login falhou!")
    else:
        show_menu(user_type)
