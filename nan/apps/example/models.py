from django.db import models


class Example(models.Model):
    param1 = models.IntegerField(default=0)

    param2 = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now=True)

