def make_logger(project_name: str) -> None:
    """
    Make logger.
    :param project_name: project name
    """
    with open(f"{project_name}/logging.conf", "w") as logging:
        logging.write("[loggers]\n")
        logging.write(f"keys={project_name}\n\n")

        logging.write("[handlers]\n")
        logging.write("keys=consoleHandler\n\n")

        logging.write("[formatters]\n")
        logging.write("keys=formatter\n\n")

        logging.write(f"[logger_{project_name}]\n")
        logging.write("level=INFO\n")
        logging.write("handlers=consoleHandler\n")
        logging.write(f"qualname={project_name}\n")
        logging.write("propagate=0\n\n")

        logging.write("[handler_consoleHandler]\n")
        logging.write("class=StreamHandler\n")
        logging.write("level=DEBUG\n")
        logging.write("args=(sys.stdout,)\n")

    with open(f"{project_name}/internals/log/logging.py", "a") as logging:
        logging.write("import logging\n")
        logging.write("import logging.config\n")
        logging.write("from typing import Optional\n")
        logging.write("from internal.config import config\n\n\n")

        logging.write("logger: Optional[logging.Logger] = None")

        logging.write("def init_logger() -> None:\n")
        logging.write("    global logger\n")
        logging.write("    logging.config.fileConfig('logging.conf')\n")
        logging.write("    self.logger = logging.getLogger(config.logger.key)\n")

    with open(f"{project_name}/internals/log/__init__.py", "a") as logging_init:
        logging_init.write("from .logging import logger, init_logger\n")
