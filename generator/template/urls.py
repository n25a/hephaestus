def make_url(project_name: str) -> None:
    """
    Make url.

    :param project_name: project name
    """
    with open(f"{project_name}/urls/example.py", "w") as urls:
        urls.write("from django.urls import path\n")
        urls.write("from views.example import ExampleView\n\n")
        urls.write("urlpatterns = [\n")
        urls.write("    path('example', ExampleView.as_view(),\n")
        urls.write("]\n")
