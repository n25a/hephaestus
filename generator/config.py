def make_config(project_name: str, is_redis_enabled: bool, is_celery_enabled: bool) -> None:
    """
    Make config.

    :param project_name: project name
    :param is_redis_enabled: redis is enabled or not
    :param is_celery_enabled: celery is enabled or not
    """
    with open(f"{project_name}/config.ini", "w") as config:
        config.write("[TIMEZONE]\n")
        config.write("zone = 'Asia/Tehran'\n\n")

        config.write("[LOCALE]\n")
        config.write("default = 'fa'\n\n")

        config.write("[DATABASE]\n")
        config.write("host = 127.0.0.1\n")
        config.write("port = 3306\n")
        config.write(f"db = '{project_name}'\n")
        config.write(f"user = '{project_name}_app'\n")
        config.write("password = 'password'\n\n")

        if is_redis_enabled:
            config.write("[REDIS]\n")
            config.write("address = 'redis://127.0.0.1:6379/1'\n")
            config.write("ttl = 3600\n")
            config.write(f"key_prefix = '{project_name}'\n\n")

        if is_celery_enabled:
            config.write("[CELERY]\n")
            config.write("broker = 'redis://localhost:6379'\n\n")

    with open(f"{project_name}/internals/config/config.py", "w") as config:
        config.write("# ----------------------------------------------------------------\n")
        config.write("#                            Time Zone\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class TimeZone:\n")
        config.write("    zone: str = ''\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                              Logger\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Logger:\n")
        config.write("    level: str = ''\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                              Locale\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Locale:\n")
        config.write("    default: str = ''\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                               DB\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Database:\n")
        config.write("    host: str = ''\n")
        config.write("    port: str = ''\n")
        config.write("    db: str = ''\n")
        config.write("    user: str = ''\n")
        config.write("    password: str = ''\n\n")

        if is_redis_enabled:
            config.write("# ----------------------------------------------------------------\n")
            config.write("#                              Redis\n")
            config.write("# ----------------------------------------------------------------\n\n")
            config.write("class Redis:\n")
            config.write("    address: str = ''\n")
            config.write("    ttl: str = 60\n")
            config.write("    key_prefix: str = ''\n\n")

        if is_celery_enabled:
            config.write("# ----------------------------------------------------------------\n")
            config.write("#                              Celery\n")
            config.write("# ----------------------------------------------------------------\n\n")
            config.write("class Celery:\n")
            config.write("    broker: str = ''\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                              Config\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Config:\n")
        config.write("    time_zone: TimeZone = TimeZone()\n")
        config.write("    logger: Logger = Logger()\n")
        config.write("    locale: Locale = Locale()\n")
        config.write("    database: Database = Database()\n")

        if is_redis_enabled:
            config.write("    redis: Redis = Redis()\n")

        if is_celery_enabled:
            config.write("    celery: Celery = Celery()\n")
        config.write("\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                       public config variable\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("config: Config = Config()\n")

    with open(f"{project_name}/internals/config/config_wrapper.py", "w") as wrapper:
        wrapper.write("from .config import config\n")
        wrapper.write("import configparser\n\n")
        wrapper.write("def wrapper() -> None:\n")
        wrapper.write('    """\n')
        wrapper.write("    Map config.ini to Config class\n")
        wrapper.write('    """\n')

        wrapper.write("__config = configparser.ConfigParser()\n")
        wrapper.write("__config.read('config.ini')\n\n")

        wrapper.write("config.time_zone.zone = __config['TIMEZONE']['zone']\n")
        wrapper.write("config.logger.level = __config['LOGGER']['level']\n")
        wrapper.write("config.locale.default = __config['LOCALE']['default']\n")
        wrapper.write("config.database.host = __config['DATABASE']['host']\n")
        wrapper.write("config.database.port = __config['DATABASE']['port']\n")
        wrapper.write("config.database.db = __config['DATABASE']['db']\n")
        wrapper.write("config.database.user = __config['DATABASE']['user']\n")
        wrapper.write("config.database.password = __config['DATABASE']['password']\n")

        if is_redis_enabled:
            wrapper.write("config.redis.address = __config['REDIS']['address']\n")
            wrapper.write("config.redis.ttl = __config['REDIS']['ttl']\n")
            wrapper.write("config.redis.key_prefix = __config['REDIS']['key_prefix']\n")

        if is_celery_enabled:
            wrapper.write("config.celery.broker = __config['CELERY']['broker']\n")
