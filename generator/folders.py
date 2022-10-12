import os


def make_folders(project_name: str, is_celery_enabled: bool) -> None:
    """
    Make folders for project.

    :param project_name: project name in string type (e.g. my_project)
    :param is_celery_enabled: celery is enabled or not in boolean type
    """

    if not os.path.exists(project_name):
        raise Exception('Project folder is exist. Please try again with another name.')

    os.makedirs(project_name)
    os.makedirs(f'{project_name}/apps')
    os.makedirs(f'{project_name}/urls')
    os.makedirs(f'{project_name}/assets')
    os.makedirs(f'{project_name}/repositories')
    os.makedirs(f'{project_name}/views')

    os.makedirs(f'{project_name}/internals')
    os.makedirs(f'{project_name}/internals/toolkit')
    os.makedirs(f'{project_name}/internals/app')
    os.makedirs(f'{project_name}/internals/config')

    if is_celery_enabled:
        os.makedirs(f'{project_name}/internals/jobs')

    os.system(f'django-admin startproject {project_name} {project_name}')
