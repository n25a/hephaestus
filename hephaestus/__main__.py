from hephaestus.cmd import start_project

import click


@click.group()
@click.version_option('0.0.1')
def main():
    pass


main.add_command(
    start_project,
)

