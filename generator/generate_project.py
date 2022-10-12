from .folders import make_folders
from .docker_file import make_dockerfile
from .make_file import make_makefile

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
