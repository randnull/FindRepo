import configparser


def get_config():
    config = configparser.ConfigParser()

    config.read('FindRepo/common/config/config.ini')

    return config


config = get_config()
