def make_logger(project_name: str) -> None:
    """
    Make logger.
    :param project_name: project name
    """
    with open(f"{project_name}/logging.conf", "w") as logging:
        logging.write("[loggers]\n")
        logging.write(f"keys=root,django,{project_name}\n\n")

        logging.write("[handlers]\n")
        logging.write("keys=consoleHandler\n\n")

        logging.write("[formatters]\n")
        logging.write("keys=defaultFormatter\n\n")

        logging.write(f"[logger_root]\n")
        logging.write("level=INFO\n")
        logging.write("handlers=consoleHandler\n\n")

        logging.write(f"[logger_django]\n")
        logging.write("level=INFO\n")
        logging.write("handlers=consoleHandler,fileHandler\n")
        logging.write("qualname=django\n")
        logging.write("propagate=0\n\n")

        logging.write(f"[logger_{project_name}]\n")
        logging.write("level=INFO\n")
        logging.write("handlers=consoleHandler\n")
        logging.write(f"qualname={project_name}\n")
        logging.write("propagate=0\n\n")

        logging.write("[handler_fileHandler]\n")
        logging.write("class=FileHandler\n")
        logging.write("level=DEBUG\n")
        logging.write("formatter=defaultFormatter\n")
        logging.write(f"args=('%(asctime)s' + '_{project_name}.log', 'w')\n\n")

        logging.write("[handler_consoleHandler]\n")
        logging.write("class=StreamHandler\n")
        logging.write("level=DEBUG\n")
        logging.write("formatter=defaultFormatter\n")
        logging.write("args=(sys.stdout,)\n\n")

        logging.write("[formatter_defaultFormatter]\n")
        logging.write("format=%(asctime)s - %(levelname)s - %(name)s - %(module)s - %(message)s\n")

    with open(f"{project_name}/internals/log/logging.py", "a") as logging:
        logging.write("import logging\n")
        logging.write("import logging.config\n")
        logging.write("from internal.config import config\n\n\n")

        logging.write("logging.config.fileConfig('logging.conf')\n")
        logging.write("logger: logging.Logger = logging.getLogger(config.logger.key)")

    with open(f"{project_name}/internals/log/__init__.py", "a") as logging_init:
        logging_init.write("from .logging import logger\n")
