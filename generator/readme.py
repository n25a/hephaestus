def make_readme(project_name: str, description: str) -> None:
    """
    Make readme.

    :param project_name: project name
    :param description: project description
    """
    with open(f"{project_name}/README.md", "w") as readme:
        readme.write(f"# {project_name}\n")
        readme.write(f"{description}\n\n")
