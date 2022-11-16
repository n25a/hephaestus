import os


def make_git(project_name: str) -> None:
    """
    Make git.

    :param project_name: project name in string type (e.g. my_project)
    """

    os.chdir(f"{project_name}/")
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")
