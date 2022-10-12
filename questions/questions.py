from __future__ import print_function, unicode_literals
from PyInquirer import prompt

questions = [
    {
        'type': 'input',
        'name': 'project_name',
        'message': 'What\'s your project name?',
    },
    {
        'type': 'input',
        'name': 'project_description',
        'message': 'What\'s your project description?',
    },
    {
        'type': 'list',
        'name': 'database',
        'message': 'What database do you need?',
        'choices': ['Mysql', 'Sqlite'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'confirm',
        'name': 'redis',
        'message': 'Do you want to the Redis?',
        'default': False,
    },
    {
        'type': 'confirm',
        'name': 'celery',
        'message': 'Do you want to the Celery?',
        'default': False,
    },
]


def answer_questions() -> dict:
    """
    Asking question to user

    :return: answers in dictionary type
    """
    answers = prompt(questions)

    if answers['celery']:
        ans_tmp = prompt(
            {
                'type': 'list',
                'name': 'broker',
                'message': 'What broker do you need?',
                'choices': ['Redis', 'RabbitMQ'],
                'filter': lambda val: val.lower()
            }
        )

        answers |= ans_tmp
    else:
        answers |= {'broker': ''}

    return answers
