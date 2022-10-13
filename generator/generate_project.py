from .folders import make_folders
from .docker_file import make_dockerfile
from .make_file import make_makefile
from .docker_compose import make_docker_compose
from .toolkit import make_toolkit
from .celery import make_celery
from .ascii_art import make_ascii_art


def generate_project(answers: dict) -> None:
    """
    Generate project.

    :param answers: answers in dictionary type
    """
    make_folders(
        answers['project_name'],
        answers['celery'],
    )

    make_dockerfile(answers['project_name'])

    make_makefile(answers['project_name'])

    is_rabbitmq_enable = True if answers['broker'] == 'rabbitmq' else False
    make_docker_compose(
        answers['project_name'],
        answers['redis'],
        is_rabbitmq_enable,
        answers['celery'],
        answers['broker']
    )

    make_toolkit(answers['project_name'])

    if answers['celery']:
        make_celery(answers['project_name'])

    make_ascii_art(answers['project_name'])
