from typing import List
import os


def reformat_manage_py(project_name: str) -> None:
    """
    Reformat manage.py.
    :param project_name:
    """

    manage_file: List[str] = []
    with open(f"{project_name}/manage.py", "r") as f:
        manage_file = f.readlines()

    os.remove(f"{project_name}/manage.py")

    with open(f"{project_name}/manage.py", "w") as manage:
        for line in manage_file:
            if line.startswith("import sys"):
                manage.write(line)
                manage.write("\nfrom internals.log import init_logger\n")
            elif line.startswith("if __name__ == '__main__':"):
                manage.write(line)
                manage.write("    init_logger()\n")
            else:
                manage.write(line)
