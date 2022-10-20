# Documentation

In this section, you can see convention documentation of generated project by hephaestus.

The tree of project is like this:

```html
myproject
├── apps
│   └── example
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       └── serializers.py
├── assets
├── internals
│   ├── app
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── ascii_art.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── config_wrapper.py
│   ├── jobs
│   │   └── tasks.py
│   ├── log
│   │   ├── __init__.py
│   │   └── logging.py
│   ├── repositories
│   │   └── example.py
│   └── toolkit
│       ├── __init__.py
│       └── toolkit.py
├── myproject
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── urls
│   └── example.py
├── views
│   └── example.py
├── Dockerfile
├── Makefile
├── README.md
├── config.ini
├── docker-compose.yml
├── logging.conf
├── manage.py
└── requirements.txt
```

Each package and file has a specific role in the project. In the following, we will explain each package.


## apps
It's contain all django app in project. Each app has these files:

* admin.py
* apps.py
* models.py
* serializers.py


## assets
It's contain all static files in project. You can add your static files in this directory.


## internals
It's contain all internal packages in project. This package has these packages as default:

### app
It's contain main general application's class in project. You can use it in everywhere in project. 
The application class in like this:

```python
class App:
    app_name: str = 'myproject'
    repository: Repository = Repository()

    def __init__(self):
        ascii_art.project_name()
```

`app_name` is name of project.  
`repository` is a repository class that you can use it for access to database or using cache. 
If you want to create a new repository, you can create a new class in `repository` package
and use it in `repository` attribute.  

You can use public variable in this package called `app` in everywhere in project.

### config
It's contain config class in project. You can use it for access to config file (config.ini).  
You can use public variable in this package called `config` in everywhere in project.

```python
class Config:
    time_zone: TimeZone = TimeZone()
    logger: Logger = Logger()
    locale: Locale = Locale()
    database: Database = Database()
    redis: Redis = Redis()
    celery: Celery = Celery()

    def __init__(self):
        wrapper(self)
```
### jobs
It's contain celery tasks in project. You can create a new task in this package and use it in everywhere in project.


### log
It's contain logger class in project. You can config it with config file (logging.conf).
You can use public variable in this package called `logger` in everywhere in project that you want log.


### repositories
It's contain all repository classes in project. 
You can create a new repository class in this package and use it in `Repository` class of `Application` class.


### toolkit
It's contain toolkit class in project. It's contain some useful functions.  
It's expire from [jsend](https://github.com/omniti-labs/jsend) rules.


### myproject
It's contain django project files in project. You can change it if you want.  
As default, Hephaestus change `settings.py` file in this package.


## urls
It's contain all urls in project. You can create a new url in this package and 
use it in `urls.py` file of main django project package.


## views
It's contain all views in project. You can create a new view in this package.


## Dockerfile
It's contain docker file for build docker image of project.


## Makefile
It's contain make commands for test, lint, build and run project.


## README.md
It's contain readme file of project.


## config.ini
It's contain config file of project. You can change it if you want. It's wrapped to `Config` class.


## docker-compose.yml
It's contain docker compose file for run project.


## logging.conf
It's contain logging config file of project. You can change it if you want. It's wrapped to `Logger` class.  
Also, you can add new logger in this file and use it in `Logger` class by changing `key` parameter in config.ini file.
For example, you need to add a new logger called `staging_logger` in this file 
to used for deploying in staging environment.


## manage.py
It's contain django manage file of project.


## .gitignore
It's contain git ignore file of project.


## requirements.txt
It's contain requirements of project. It's create according to your answers in questions.

