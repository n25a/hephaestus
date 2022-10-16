from celery.decorators import task
import time


@task(name='example_job')
def example_job(name: str):
    print(f'Hello {name}!')
    time.sleep(20)
    example_job.apply_async(name='World')
