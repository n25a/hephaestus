def make_ascii_art(project_name: str) -> None:
    """
    Make ascii art.

    :param project_name: project name
    """
    with open(f"{project_name}/internals/app/ascii_art.py", "w") as ascii_art:
        ascii_art.write("from art import tprint\n\n\n")
        ascii_art.write("def project_name():\n")
        ascii_art.write(f"    tprint('{project_name}'.upper(), font='')\n")
