from hephaestus.questions import answer_questions
from hephaestus.generator import generate_project

import click


start_project_group = click.Group(name=None)


@start_project_group.command('start_project')
def start_project():
    """
    Start a new Django project.

    """
    answers = answer_questions()
    generate_project(answers)
