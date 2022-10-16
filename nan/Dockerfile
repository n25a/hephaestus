# pull the official base image
FROM python:3.8-slim

# set work directory
WORKDIR /etc/opt/nan

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /etc/opt/nan/
RUN pip install -r requirements.txt

# copy project
COPY . /etc/opt/nan/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
