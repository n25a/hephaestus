from .config import Config
import configparser


def wrapper(config: Config) -> None:
    """
    Map config.ini to Config class
    """
    __config = configparser.ConfigParser()
    __config.read('config.ini')

    config.time_zone.zone = __config['TIMEZONE']['zone']
    config.logger.level = __config['LOGGER']['level']
    config.locale.default = __config['LOCALE']['default']
    config.database.host = __config['DATABASE']['host']
    config.database.port = __config['DATABASE']['port']
    config.database.db = __config['DATABASE']['db']
    config.database.user = __config['DATABASE']['user']
    config.database.password = __config['DATABASE']['password']
    config.redis.address = __config['REDIS']['address']
    config.redis.ttl = __config['REDIS']['ttl']
    config.redis.key_prefix = __config['REDIS']['key_prefix']
    config.celery.broker = __config['CELERY']['broker']
