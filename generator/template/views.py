def make_view(project_name: str) -> None:
    """
    Make view.
    """
    with open(f"{project_name}/views/example.py", "w") as views:
        views.write("from rest_framework.views import APIView\n")
        views.write("from rest_framework.permissions import IsAuthenticated\n")
        views.write("from rest_framework.authentication import TokenAuthentication\n")
        views.write("from rest_framework import status\n\n")

        views.write("from internals.toolkit import response_creator\n")
        views.write("from internals.app import app\n\n")

        views.write("class ExampleView(APIView):\n\n")
        views.write("    authentication_classes = [TokenAuthentication]\n")
        views.write("    permission_classes = [IsAuthenticated]\n\n")

        views.write("    def post(self, request):\n")
        views.write("        err = app.repository.example.create_example(request.data)\n")
        views.write("        if err:\n")
        views.write("            return err\n\n")
        views.write("        return response_creator(\n")
        views.write("            data='penalty added successfully.',\n")
        views.write("            status='success',\n")
        views.write("            status_code=status.HTTP_201_CREATED,\n")
        views.write("        )\n")
