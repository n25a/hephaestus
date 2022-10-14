from .tasks import make_job
from .urls import make_url
from .app import make_app


def generate_templates(project_name: str) -> None:
    """
    Generate template.
    """
    make_job(project_name)

    make_url(project_name)

    make_app(project_name)

