def make_docker_compose(
        project_name: str,
        is_redis_enable: bool,
        is_rabbitmq_enable: bool,
        is_celery_enable: bool,
        broker: str,
) -> None:
    """
    Make docker-compose.yml for project.

    :param broker: is celery broker (rabbitmq or redis)
    :param project_name: project name in string type (e.g. my_project)
    :param is_rabbitmq_enable: is rabbitmq enable in boolean type
    :param is_redis_enable: is redis enable in boolean type
    :param is_celery_enable: is celery enable in boolean type
    """
    with open(f'{project_name}/docker-compose.yml', 'w') as docker_compose:
        docker_compose.write('version: "3.9"\n\n')
        docker_compose.write('services:\n')
        docker_compose.write('  web:\n')
        docker_compose.write('    build: .\n')
        docker_compose.write('    command: python manage.py runserver 0.0.0.0:8000\n')
        docker_compose.write('    ports:\n')
        docker_compose.write('      - "8000:8000"\n')
        docker_compose.write('    depends_on:\n')
        docker_compose.write('      - db\n')
        if is_redis_enable:
            docker_compose.write('      - redis\n')
        if is_rabbitmq_enable:
            docker_compose.write('      - rabbitmq\n')
        if is_celery_enable:
            docker_compose.write('      - celery\n')

        docker_compose.write('  db:\n')
        docker_compose.write('    image: mariadb:10.4.8\n')
        docker_compose.write('    ports:\n')
        docker_compose.write('      - "3306:3306"\n')
        docker_compose.write('    environment:\n')
        docker_compose.write('      MYSQL_ROOT_PASSWORD: "root-secure-password"\n')
        docker_compose.write(f'      MYSQL_DATABASE: "{project_name}"\n')
        docker_compose.write(f'      MYSQL_USER: "{project_name}_app"\n')
        docker_compose.write(f'      MYSQL_PASSWORD: "password"\n')
        docker_compose.write('    volumes:\n')
        docker_compose.write('      - ./db:/var/lib/mysql\n')
        docker_compose.write('    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_general_ci\n')

        if is_redis_enable:
            docker_compose.write('  redis:\n')
            docker_compose.write('    image: redis:6.0.5\n')
            docker_compose.write('    ports:\n')
            docker_compose.write('      - "6379:6379"\n')

        if is_rabbitmq_enable:
            docker_compose.write('  rabbitmq:\n')
            docker_compose.write('    image: rabbitmq:3.8.3\n')
            docker_compose.write('    ports:\n')
            docker_compose.write('      - "5672:5672"\n')

        if is_celery_enable:
            docker_compose.write('  celery:\n')
            docker_compose.write('    image: celery\n')
            docker_compose.write('    restart: on-failure\n')
            docker_compose.write(
                f'    command: celery -A {project_name} beat -l info && celery -A {project_name} worker -l info\n'
            )
            docker_compose.write('    depends_on:\n')
            docker_compose.write('      - db\n')
            if broker == 'redis':
                docker_compose.write('      - redis\n')
            elif broker == 'rabbitmq':
                docker_compose.write('      - rabbitmq\n')
