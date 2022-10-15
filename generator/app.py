def make_app(project_name: str) -> None:
    """
    Make app.
    """
    with open(f"{project_name}/internals/app/app.py", "w") as app:
        app.write("from internals.app import ascii_art\n")
        app.write("from repositories.example import ExampleRepository\n\n\n")

        app.write("# ----------------------------------------------------------------\n")
        app.write("#                             Repository\n")
        app.write("# ----------------------------------------------------------------\n\n")
        app.write("class Repository:\n")
        app.write("    example: ExampleRepository = ExampleRepository()\n\n")

        app.write("# ----------------------------------------------------------------\n")
        app.write("#                                App\n")
        app.write("# ----------------------------------------------------------------\n\n")
        app.write("class App:\n")
        app.write(f"    app_name: str = '{project_name}'\n")
        app.write("    repository: Repository = Repository()\n\n")

        app.write("    def __init__(self):\n")
        app.write("        ascii_art.project_name()\n\n")

        app.write("# ----------------------------------------------------------------\n")
        app.write("#                         public App variable\n")
        app.write("# ----------------------------------------------------------------\n\n")
        app.write("app: App = App()\n")
