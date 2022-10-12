def make_dockerfile(project_name: str) -> None:
    """
    Make Dockerfile for project.

    :param project_name: project name in string type (e.g. my_project)
    """

    with open(f'{project_name}/Dockerfile', 'w') as dockerfile:
        dockerfile.write('# pull the official base image\n')
        dockerfile.write('FROM python:3.8-slim\n')

        dockerfile.write('# set work directory\n')
        dockerfile.write(f'WORKDIR /etc/opt/{project_name}\n\n')

        dockerfile.write('# set environment variables\n')
        dockerfile.write('ENV PYTHONDONTWRITEBYTECODE 1\n')
        dockerfile.write('ENV PYTHONUNBUFFERED 1\n\n')

        dockerfile.write('# install dependencies\n')
        dockerfile.write('RUN pip install --upgrade pip\n')
        dockerfile.write(f'COPY requirements.txt /etc/opt/{project_name}/\n')
        dockerfile.write('RUN pip install -r requirements.txt\n\n')

        dockerfile.write('# copy project\n')
        dockerfile.write(f'COPY . /etc/opt/{project_name}/\n\n')
        dockerfile.write('CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]\n')
