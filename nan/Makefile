HOST=127.0.0.1
TEST_PATH=./
PROJECT_NAME="nan"

help:
    @echo "make help - Show this help message."
    @echo "make run - Run project with docker-compose."

isort:
    - isort --skip-glob=.tox --reverse-sort --profile=black .

flake8:
    - flake8 --exclude='.tox','__init__.py','venv/','settings.py' --extend-exclude='*_pb2*.py' .

blue:
    - blue . --exclude=['.tox','__init__.py','venv/','tests/']

lint: isort blue flake8

test:
    python manage.py test .

run:
    python manage.py runserver

docker-run:
    docker build \
      --file=./Dockerfile \
      --tag=$(PROJECT_NAME) ./
    docker run \
      --detach=false \
      --name=$(PROJECT_NAME) \
      --publish=$(HOST):8080 \
      $(PROJECT_NAME)
