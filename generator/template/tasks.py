def make_job(project_name: str) -> None:
    """
    Create example job for celery
    """

    with open(f"{project_name}/internals/jobs/tasks.py", "w") as job:
        job.write("from celery.decorators import task\n")
        job.write("import time\n\n")
        job.write("@task(name='example_job'\n")
        job.write("def example_job(name: str):\n")
        job.write("    print(f'Hello {name}!')\n")
        job.write("    time.sleep(20)\n")
        job.write("    example_job.apply_async(name='world')\n")
