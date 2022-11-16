def make_app(project_name: str, is_nats_enabled: bool) -> None:
    """
    Make app.

    :param project_name: project name in string type (e.g. my_project)
    :param is_nats_enabled: nat is enabled or not
   """
    with open(f"{project_name}/internals/app/app.py", "w") as app:
        app.write("from typing import Optional\n")
        app.write("from internals.nats import nats as internal_nats\n")
        app.write("from internals.app import ascii_art\n")
        app.write("from internals.repositories.example import ExampleRepository\n\n")
        app.write("import nats\n\n\n")

        app.write("# ----------------------------------------------------------------\n")
        app.write("#                             Repository\n")
        app.write("# ----------------------------------------------------------------\n\n")
        app.write("class Repository:\n")
        app.write("    example: ExampleRepository = ExampleRepository()\n\n\n")

        app.write("# ----------------------------------------------------------------\n")
        app.write("#                                App\n")
        app.write("# ----------------------------------------------------------------\n\n")
        app.write("class App:\n")
        app.write(f"    app_name: str = '{project_name}'\n")
        app.write("    repository: Repository = Repository()\n")

        if is_nats_enabled:
            app.write("    nats_client: Optional[nats.NATS] = None\n")

        app.write("\n    def __init__(self):\n")
        app.write("        ascii_art.project_name()\n")

        if is_nats_enabled:
            app.write("        self.nats_client = await internal_nats.create_client()\n")

        app.write("\n\n")

        app.write("# ----------------------------------------------------------------\n")
        app.write("#                         public App variable\n")
        app.write("# ----------------------------------------------------------------\n\n")
        app.write("app: App = App()\n")

    with open(f"{project_name}/internals/app/__init__.py", "w") as init:
        init.write("from .app import app\n")
