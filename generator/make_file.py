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
        makefile.write('\t@echo "make help - Show this help message."\n')
        makefile.write('\t@echo "make run - Run project with docker-compose."\n\n')

        makefile.write('isort:\n')
        makefile.write(
            '\t- isort --skip-glob=.tox --reverse-sort --profile=black .\n\n'
        )

        makefile.write('flake8:\n')
        makefile.write(
            "\t- flake8 --exclude='.tox','__init__.py','venv/','settings.py' --extend-exclude='*_pb2*.py' .\n\n"
        )

        makefile.write('blue:\n')
        makefile.write(
            '\t- blue .\n\n'
        )

        makefile.write('lint: isort blue flake8\n\n')

        makefile.write('test:\n')
        makefile.write('\tpython manage.py test .\n\n')

        makefile.write('run:\n')
        makefile.write('\tpython manage.py runserver\n\n')

        makefile.write('docker-run:\n')
        makefile.write('\tdocker build \\\n')
        makefile.write('\t  --file=./Dockerfile \\\n')
        makefile.write('\t  --tag=$(PROJECT_NAME) ./\n')
        makefile.write('\tdocker run \\\n')
        makefile.write('\t  --detach=false \\\n')
        makefile.write('\t  --name=$(PROJECT_NAME) \\\n')
        makefile.write('\t  --publish=$(HOST):8080 \\\n')
        makefile.write('\t  $(PROJECT_NAME)\n')
