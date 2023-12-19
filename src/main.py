import configparser
import getpass
from utilities.initial_setup import initial_setup
from database.queries import BancoDeDados, Usuario
from ui.menu import show_menu

class Autenticacao:
    def __init__(self, db):
        self.usuario = Usuario(db)

    def login(self):
        print("Bem-vindo ao Sistema!")
        username = input("Digite seu nome de usuário: ")
        password = getpass.getpass("Digite sua senha: ")  
        user_type = self.usuario.login(username, password)
        return user_type is not None, user_type

class Sistema:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.db = BancoDeDados()
        self.__autenticacao = Autenticacao(self.db)

    def __carregar_configuracoes(self):
        self.__config.read('config.ini')

    def __verificar_configuracoes_iniciais(self):
        if self.__config.get('SETTINGS', 'execute_initial_setup').lower() == 'yes':
            initial_setup()

    def iniciar(self):
        self.__carregar_configuracoes()
        self.__verificar_configuracoes_iniciais()

        logged_in, user_type = self.__autenticacao.login()
        if not logged_in:
            print("Login falhou!")
        else:
            show_menu(user_type)

if __name__ == "__main__":
    sistema = Sistema()
    sistema.iniciar()
