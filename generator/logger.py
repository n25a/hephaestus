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
        logging.write("keys=formatter\n")

        logging.write(f"[logger_{project_name}]\n")
        logging.write("level=DEBUG\n")
        logging.write("handlers=consoleHandler\n")
        logging.write(f"qualname={project_name}\n")
        logging.write("propagate=0\n")

        logging.write("[handler_consoleHandler]\n")
        logging.write("class=StreamHandler\n")
        logging.write("level=DEBUG\n")
        logging.write("args=(sys.stdout,)\n")
