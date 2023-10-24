from configparser import ConfigParser

def config(section='DATABASE'):
    parser = ConfigParser()
    parser.read('config.ini')
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    return db
