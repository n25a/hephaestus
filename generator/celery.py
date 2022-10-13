def make_celery(project_name: str) -> None:
    """
    Make celery.

    :param project_name: project name in string type (e.g. my_project)
    """

    with open(f'{project_name}/{project_name}/celery.py', "w") as celery:
        celery.write("import os\n")
        celery.write("from celery import Celery\n\n")
        celery.write(f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')\n\n")
        celery.write(f"app = Celery('{project_name}')\n")
        celery.write("app.config_from_object('django.conf:settings', namespace='CELERY')\n")
        celery.write("app.autodiscover_tasks(\n")
        celery.write("    ['internals.jobs'],\n")
        celery.write(")\n")

    with open(f"{project_name}/{project_name}/__init__.py", "a") as celery_init:
        celery_init.write("from .celery import app as celery_app\n\n")
        celery_init.write("__all__ = ['celery_app']\n")
