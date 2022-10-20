from questions import answer_questions
from generator import generate_project

import click


start_project_group = click.Group('start_project')


@start_project_group.command()
def start_project():
    """
    Start a new project

    """
    answers = answer_questions()
    generate_project(answers)
