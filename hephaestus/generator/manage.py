from typing import List
import os


def reformat_manage_py(project_name: str, is_nats_enabled: bool) -> None:
    """
    Reformat manage.py.
    :param project_name: project name in string type (e.g. my_project)
    :param is_nats_enabled: nat is enabled or not
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
                manage.write("from internals.app import app\n")
                manage.write("from internals.nats import unsubscribe_all_subscribers, subscribe_all_topics\n")

            elif line.startswith("if __name__ == '__main__':"):
                manage.write(line)
                manage.write("    init_logger()\n")
                if is_nats_enabled:
                    manage.write("    subscribe_all_topics()\n")

            elif "main()" in line and "def" not in line:
                manage.write(line)
                if is_nats_enabled:
                    manage.write("    await unsubscribe_all_subscribers()\n")
                    manage.write("    await app.nats_client.drain()\n")
            else:
                manage.write(line)
