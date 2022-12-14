def make_config(
        project_name: str,
        is_redis_enabled: bool,
        is_celery_enabled: bool,
        is_nats_enabled: bool,
        broker: str,
        result_backend: str,
        database: str
) -> None:
    """
    Make config.

    :param database: database in string type (e.g. postgresql)
    :param result_backend: result backend in string type (e.g. redis)
    :param broker: celery broker. (e.g. redis or rabbitmq)
    :param project_name: project name
    :param is_redis_enabled: redis is enabled or not
    :param is_celery_enabled: celery is enabled or not
    :param is_nats_enabled: nats is enabled or not
    """
    with open(f"{project_name}/config.ini", "w") as config:
        config.write("[TIMEZONE]\n")
        config.write("time_zone = 'Asia/Tehran'\n\n")

        config.write("[LOGGER]\n")
        config.write(f"key = '{project_name}'\n\n")

        config.write("[LOCALE]\n")
        config.write("default = 'fa'\n\n")

        config.write("[DATABASE]\n")
        config.write("host = 127.0.0.1\n")
        if database == 'mysql':
            config.write("port = 3306\n")
        elif database == 'postgresql':
            config.write("port = 5432\n")
        elif database == 'sqlite':
            config.write("port = 0\n")

        config.write(f"db = '{project_name}'\n")
        config.write(f"user = '{project_name}_app'\n")
        config.write("password = 'password'\n\n")

        if is_redis_enabled:
            config.write("[REDIS]\n")
            config.write("address = 'redis://127.0.0.1:6379'\n")
            config.write("timeout = 300\n")
            config.write(f"key_prefix = '{project_name}'\n")
            config.write(f"username = ''\n")
            config.write("password = ''\n")
            config.write("max_pool_size = 4\n")

        if is_celery_enabled:
            config.write("\n[CELERY]\n")
            if broker == 'redis':
                config.write("broker = 'redis://localhost:6379'\n")
            elif broker == 'rabbitmq':
                config.write("broker = 'amqp://localhost'\n")

            if result_backend == 'redis':
                config.write("result_backend = 'redis://localhost:6379'\n")
            elif result_backend == 'rabbitmq':
                config.write("result_backend = 'amqp://localhost'\n")

        if is_nats_enabled:
            config.write("\n[NATS]\n")
            config.write("address = 'nats://localhost:4222'\n")
            config.write(f"name = '{project_name}'\n")
            config.write("username = ''\n")
            config.write("password = ''\n")
            config.write("drain_timeout = 30\n")
            config.write("flush_timeout = 2\n")
            config.write("connect_timeout = 2\n")
            config.write("reconnect_time_wait = 2\n")

    with open(f"{project_name}/internals/config/config.py", "w") as config:
        config.write("from .config_wrapper import wrapper\n\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                            Time Zone\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class TimeZone:\n")
        config.write("    time_zone: str = ''\n\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                              Logger\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Logger:\n")
        config.write("    key: str = ''\n\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                              Locale\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Locale:\n")
        config.write("    default: str = ''\n\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                               DB\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("class Database:\n")
        config.write("    host: str = ''\n")
        config.write("    port: str = ''\n")
        config.write("    db: str = ''\n")
        config.write("    user: str = ''\n")
        config.write("    password: str = ''\n\n\n")

        if is_redis_enabled:
            config.write("# ----------------------------------------------------------------\n")
            config.write("#                              Redis\n")
            config.write("# ----------------------------------------------------------------\n\n")
            config.write("class Redis:\n")
            config.write("    address: str = ''\n")
            config.write("    timeout: str = 300\n")
            config.write("    key_prefix: str = ''\n")
            config.write("    username: str = ''\n")
            config.write("    password: str = ''\n")
            config.write("    max_pool_size: int = 0\n\n\n")

        if is_celery_enabled:
            config.write("# ----------------------------------------------------------------\n")
            config.write("#                              Celery\n")
            config.write("# ----------------------------------------------------------------\n\n")
            config.write("class Celery:\n")
            config.write("    broker: str = ''\n")
            config.write("    result_backend: str = ''\n\n\n")

        if is_nats_enabled:
            config.write("# ----------------------------------------------------------------\n")
            config.write("#                               Nats\n")
            config.write("# ----------------------------------------------------------------\n\n")
            config.write("class Nats:\n")
            config.write("    address: str = ''\n")
            config.write("    name: str = ''\n")
            config.write("    username: Optional[str] = None\n")
            config.write("    password: Optional[str] = None\n")
            config.write("    drain_timeout: int = 30\n")
            config.write("    flush_timeout: Optional[int] = None\n")
            config.write("    connect_timeout: int = 2\n")
            config.write("    reconnect_time_wait: int = 2\n\n\n")

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

        if is_nats_enabled:
            config.write("    nats: Nats = Nats()\n")

        config.write("\n    def __init__(self):\n")
        config.write("        wrapper(self)\n\n\n")

        config.write("# ----------------------------------------------------------------\n")
        config.write("#                       public config variable\n")
        config.write("# ----------------------------------------------------------------\n\n")
        config.write("config: Config = Config()\n")

    with open(f"{project_name}/internals/config/config_wrapper.py", "w") as wrapper:
        wrapper.write("from .config import Config\n")
        wrapper.write("import configparser\n\n\n")
        wrapper.write("def wrapper(config: Config) -> None:\n")
        wrapper.write('    """\n')
        wrapper.write("    Map config.ini to Config class\n")
        wrapper.write('    """\n')

        wrapper.write("    __config = configparser.ConfigParser()\n")
        wrapper.write("    __config.read('config.ini')\n\n")

        wrapper.write("    config.time_zone.time_zone = __config['TIMEZONE']['time_zone']\n")
        wrapper.write("    config.logger.key = __config['LOGGER']['key']\n")
        wrapper.write("    config.locale.default = __config['LOCALE']['default']\n")
        wrapper.write("    config.database.host = __config['DATABASE']['host']\n")
        wrapper.write("    config.database.port = __config['DATABASE']['port']\n")
        wrapper.write("    config.database.db = __config['DATABASE']['db']\n")
        wrapper.write("    config.database.user = __config['DATABASE']['user']\n")
        wrapper.write("    config.database.password = __config['DATABASE']['password']\n")

        if is_redis_enabled:
            wrapper.write("    config.redis.address = __config['REDIS']['address']\n")
            wrapper.write("    config.redis.timeout = __config['REDIS']['timeout']\n")
            wrapper.write("    config.redis.key_prefix = __config['REDIS']['key_prefix']\n")
            wrapper.write("    config.redis.username = __config['REDIS']['username']\n")
            wrapper.write("    config.redis.password = __config['REDIS']['password']\n")
            wrapper.write("    config.redis.password = __config['REDIS']['max_pool_size']\n")

        if is_celery_enabled:
            wrapper.write("    config.celery.broker = __config['CELERY']['broker']\n")
            wrapper.write("    config.celery.result_backend = __config['CELERY']['result_backend']\n")

        if is_nats_enabled:
            wrapper.write("    config.celery.address = __config['NATS']['address']\n")
            wrapper.write("    config.celery.name = __config['NATS']['name']\n")
            wrapper.write("    config.celery.username = __config['NATS']['username']\n")
            wrapper.write("    config.celery.password = __config['NATS']['password']\n")
            wrapper.write("    config.celery.drain_timeout = __config['NATS']['drain_timeout']\n")
            wrapper.write("    config.celery.flush_timeout = __config['NATS']['flush_timeout']\n")
            wrapper.write("    config.celery.connect_timeout = __config['NATS']['connect_timeout']\n")
            wrapper.write("    config.celery.reconnect_time_wait = __config['NATS']['reconnect_time_wait']\n")

    with open(f"{project_name}/internals/config/__init__.py", "w") as init:
        init.write("from .config import config\n")
