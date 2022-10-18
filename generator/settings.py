from typing import List
import os


def reformat_settings_py(project_name: str, is_redis_enabled: bool, is_celery_enabled: bool, database: str) -> None:
    """
    Reformat settings.py.
    :param database: database type (postgres, mysql, sqlite)
    :param project_name: project name in string type (e.g. my_project)
    :param is_redis_enabled: redis enabled or not
    :param is_celery_enabled: celery enabled or not
    """

    settings_file: List[str] = []
    with open(f"{project_name}/{project_name}/settings.py", "r") as f:
        settings_file = f.readlines()

    os.remove(f"{project_name}/{project_name}/settings.py")

    with open(f"{project_name}/{project_name}/settings.py", "w") as manage:
        for line in settings_file:
            if line.startswith("from pathlib import Path"):
                manage.write(line)
                manage.write("\nfrom internals.config import config\n")
                manage.write("import os\n\n")

            elif line.startswith("BASE_DIR = Path(__file__).resolve().parent.parent"):
                manage.write(line)
                manage.write("MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n")
                manage.write("STATIC_ROOT = os.path.join(BASE_DIR, 'static')\n")

            elif line.startswith("ALLOWED_HOSTS = []"):
                manage.write("ALLOWED_HOSTS = ['*']\n\n")
                manage.write("CORS_ORIGIN_ALLOW_ALL = True\n")

            elif line.startswith("    'django.contrib.staticfiles',"):
                manage.write(line)
                manage.write("    'rest_framework',\n")
                manage.write("    'rest_framework.authtoken',\n")

            elif line.startswith("    'django.middleware.security.SecurityMiddleware',"):
                manage.write("    'corsheaders.middleware.CorsMiddleware',\n")
                manage.write(line)

            elif line.startswith("WSGI_APPLICATION = "):
                manage.write(line)
                manage.write("\nREST_FRAMEWORK = {\n")
                manage.write("    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'\n")
                manage.write("}\n\n")
                manage.write("REST_AUTH_SERIALIZERS = {\n")
                manage.write("    'USER_DETAILS_SERIALIZER': 'apps.user.serializers.UserSerializer',  # replace your user serializer\n")
                manage.write("}\n")

            elif line.startswith("DATABASES = {"):
                manage.write(line)
                if database == "Postgresql":
                    manage.write("    'default': {\n")
                    manage.write("        'ENGINE': 'django.db.backends.postgresql_psycopg2',\n")
                    manage.write("        'NAME': config.database.db,\n")
                    manage.write("        'USER': config.database.user,\n")
                    manage.write("        'PASSWORD': config.database.password,\n")
                    manage.write("        'HOST': config.database.host,\n")
                    manage.write("        'PORT': config.database.port,\n")
                elif database == "mysql":
                    manage.write("    'default': {\n")
                    manage.write("        'ENGINE': 'django.db.backends.mysql',\n")
                    manage.write("        'NAME': config.database.db,\n")
                    manage.write("        'USER': config.database.user,\n")
                    manage.write("        'PASSWORD': config.database.password,\n")
                    manage.write("        'HOST': config.database.host,\n")
                    manage.write("        'PORT': config.database.port,\n")
                elif database == "sqlite":
                    manage.write("    'default': {\n")
                    manage.write("        'ENGINE': 'django.db.backends.sqlite3',\n")
                    manage.write("        'NAME': BASE_DIR / 'db.sqlite3',\n")

            elif line.startswith("    'default': {") or \
                    line.startswith("        'ENGINE': 'django.db.backends.sqlite3',") or \
                    line.startswith("        'NAME': BASE_DIR / 'db.sqlite3',"):
                continue

            elif line.startswith("# Password validation"):
                manage.write("# let Django know to use the new User class\n")
                manage.write("AUTH_USER_MODEL = 'user.CustomUser'  # replace your custom user\n\n")
                manage.write(line)

            elif line.startswith("# Internationalization"):
                if is_redis_enabled:
                    manage.write("# Cache setting\n")
                    manage.write("CACHES = {\n")
                    manage.write("    'default': {\n")
                    manage.write("        'BACKEND': 'django_redis.cache.RedisCache',\n")
                    manage.write("        'LOCATION': config.redis.address,\n")
                    manage.write("        'TIMEOUT': config.redis.timeout\n")
                    manage.write("        'OPTIONS': {\n")
                    manage.write("            'CLIENT_CLASS': 'django_redis.client.DefaultClient',\n")
                    manage.write("            'no_delay': True,\n")
                    manage.write("            'use_pooling': True,\n")
                    manage.write("            'max_pool_size': config.redis.max_pool_size,\n")
                    manage.write("            'username': config.redis.username,\n")
                    manage.write("            'password': config.redis.password,\n")
                    manage.write("        },\n")
                    manage.write("        'KEY_PREFIX': config.redis.key_prefix,\n")
                    manage.write("    }\n")
                    manage.write("}\n\n")

                if is_celery_enabled:
                    manage.write("# config rabbitmq as broker for celery to send or receive messages from django\n")
                    manage.write("CELERY_BROKER_URL = config.celery.broker\n\n")
                    manage.write("CELERY_RESULT_BACKEND = config.celery.result_backend\n\n")

                manage.write(line)

            elif line.startswith("TIME_ZONE = 'UTC'"):
                manage.write("TIME_ZONE = config.time_zone.time_zone\n")

            elif line.startswith("STATIC_URL = 'static/'"):
                manage.write(line)
                manage.write("MEDIA_URL = 'media/'\n\n")

            else:
                manage.write(line)
