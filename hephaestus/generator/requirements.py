def make_requirements(
        project_name: str,
        is_redis_enabled: bool,
        is_celery_enabled: bool,
        is_nats_enabled: bool,
        database: str,
):
    """
    Make requirements.

    :param database: database in string type (e.g. postgresql)
    :param project_name: project name in string type (e.g. my_project)
    :param is_redis_enabled: redis is enabled or not
    :param is_celery_enabled: celery is enabled or not
    :param is_nats_enabled: nats is enabled or not
    """
    with open(f'{project_name}/requirements.txt', 'w') as requirements:
        requirements.write('art==5.7\n')
        requirements.write('asgiref==3.5.2\n')
        requirements.write('Django==4.1.2\n')
        requirements.write('djangorestframework==3.14.0\n')
        requirements.write('pytz==2022.4\n')
        requirements.write('sqlparse==0.4.3\n')

        if is_redis_enabled:
            requirements.write('async-timeout==4.0.2\n')
            requirements.write('Deprecated==1.2.13\n')
            requirements.write('packaging==21.3\n')
            requirements.write('pyparsing==3.0.9\n')
            requirements.write('redis==4.3.4\n')
            requirements.write('wrapt==1.14.1\n')

        if is_celery_enabled:
            requirements.write('billiard==3.6.4.0\n')
            requirements.write('celery==5.2.7\n')
            requirements.write('kombu==5.2.4\n')
            requirements.write('prompt-toolkit==3.0.31\n')
            requirements.write('six==1.16.0\n')
            requirements.write('vine==5.0.0\n')
            requirements.write('wcwidth==0.2.5\n')
            requirements.write('amqp==5.1.1\n')

        if is_nats_enabled:
            requirements.write('nats-python')

        if database == 'postgrersql':
            requirements.write("psycopg2-binary==2.9.4\n")