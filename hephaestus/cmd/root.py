from .start_project import start_project_group

import click


cli = click.CommandCollection(
    sources=[
        start_project_group,
    ]
)
