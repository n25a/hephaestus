from .folders import make_folders


def generate_project(answers: dict) -> None:
    """
    Generate project.

    :param answers: answers in dictionary type
    """
    make_folders(
        answers['project_name'],
        answers['celery'],
    )

