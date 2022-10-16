import os


def make_git() -> None:
    """
    Make git.
    """

    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")
