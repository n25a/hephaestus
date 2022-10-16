def make_readme(project_name: str, description: str) -> None:
    """
    Make readme.
    """
    with open(f"{project_name}/README.md", "w") as readme:
        readme.write(f"# {project_name}\n")
        readme.write(f"{description}\n\n")
