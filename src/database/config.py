from configparser import ConfigParser

class Configuracao:
    def __init__(self, arquivo_config='config.ini'):
        self.parser = ConfigParser()
        self.arquivo_config = arquivo_config
        self.carregar_configuracoes()

    def carregar_configuracoes(self):
        """ Carrega as configurações do arquivo. """
        self.parser.read(self.arquivo_config)

    def obter_configuracao(self, secao='DATABASE'):
        """ Retorna um dicionário com as configurações da seção especificada. """
        configuracoes = {}
        if self.parser.has_section(secao):
            params = self.parser.items(secao)
            for param in params:
                configuracoes[param[0]] = param[1]
        return configuracoes