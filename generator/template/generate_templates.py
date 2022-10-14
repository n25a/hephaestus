from .tasks import make_job


def generate_templates(project_name: str) -> None:
    """
    Generate template.
    """
    make_job(project_name)

