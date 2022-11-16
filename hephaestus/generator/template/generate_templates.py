from .tasks import make_job
from .urls import make_url
from .app import make_app
from .views import make_view
from .repository import make_repository
from .nats import make_nats


def generate_templates(project_name: str, is_celery_enabled: bool, is_nats_enabled: bool) -> None:
    """
    Generate template.
    """
    if is_celery_enabled:
        make_job(project_name)

    make_url(project_name)

    make_app(project_name)

    make_view(project_name)

    make_repository(project_name)

    if is_nats_enabled:
        make_nats(project_name)