def make_makefile(project_name: str) -> None:
    """
    Make Makefile for project.

    :param project_name: project name in string type (e.g. my_project)
    """

    with open(f'{project_name}/Makefile', 'w') as makefile:
        makefile.write('HOST=127.0.0.1\n')
        makefile.write('TEST_PATH=./\n')
        makefile.write(f'PROJECT_NAME="{project_name}"\n\n')

        makefile.write('help:\n')
        makefile.write('    @echo "make help - Show this help message."\n')
        makefile.write('    @echo "make run - Run project with docker-compose."\n\n')

        makefile.write('isort:\n')
        makefile.write(
            '    - isort --skip-glob=.tox --reverse-sort --profile=black .\n\n'
        )

        makefile.write('flake8:\n')
        makefile.write(
            "    - flake8 --exclude='.tox','__init__.py','venv/','settings.py' --extend-exclude='*_pb2*.py' .\n\n"
        )

        makefile.write('blue:\n')
        makefile.write(
            '    - blue .\n\n'
        )

        makefile.write('lint: isort blue flake8\n\n')

        makefile.write('test:\n')
        makefile.write('    python manage.py test .\n\n')

        makefile.write('run:\n')
        makefile.write('    python manage.py runserver\n\n')

        makefile.write('docker-run:\n')
        makefile.write('    docker build \\\n')
        makefile.write('      --file=./Dockerfile \\\n')
        makefile.write('      --tag=$(PROJECT_NAME) ./\n')
        makefile.write('    docker run \\\n')
        makefile.write('      --detach=false \\\n')
        makefile.write('      --name=$(PROJECT_NAME) \\\n')
        makefile.write('      --publish=$(HOST):8080 \\\n')
        makefile.write('      $(PROJECT_NAME)\n')
