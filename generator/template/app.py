import os


def make_app(project_name: str) -> None:
    """
    Make app.
    """
    os.mkdir(f"{project_name}/apps/example")

    with open(f"{project_name}/apps/example/__init__.py", "w") as init:
        init.write("\n")

    with open(f"{project_name}/apps/example/models.py", "w") as models:
        models.write("from django.db import models\n\n\n")
        models.write("class Example(models.Model):\n")
        models.write("    param1 = models.IntegerField(default=0)\n\n")
        models.write("    param2 = models.BooleanField(default=False)\n\n")
        models.write("    create_at = models.DateTimeField(auto_now_add=True)\n\n")
        models.write("    modified_at = models.DateTimeField(auto_now=True)\n\n")

    with open(f"{project_name}/apps/example/serializers.py", "w") as serializers:
        serializers.write("from rest_framework import serializers\n\n")
        serializers.write("from .models import Example\n\n\n")
        serializers.write("class ExampleSerializer(serializers.ModelSerializer):\n")
        serializers.write("    class Meta:\n")
        serializers.write("        model = Example\n")
        serializers.write("        fields = '__all__'\n\n")

    with open(f"{project_name}/apps/example/apps.py", "w") as apps:
        apps.write("from django.apps import AppConfig\n\n\n")
        apps.write("class ExampleConfig(AppConfig):\n")
        apps.write("    default_auto_field = 'django.db.models.BigAutoField'\n\n")
        apps.write("    name = 'example'\n")

    with open(f"{project_name}/apps/example/admin.py", "w") as admin:
        admin.write("# from django.contrib import admin\n\n")
        admin.write("# Register your models here.\n")
