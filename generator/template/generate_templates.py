from .tasks import make_job
from .urls import make_url


def generate_templates(project_name: str) -> None:
    """
    Generate template.
    """
    make_job(project_name)

    make_url(project_name)

