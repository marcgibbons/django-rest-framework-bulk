from __future__ import unicode_literals, print_function
import django
import uuid
from django.db import models


class SimpleModel(models.Model):
    number = models.IntegerField()
    contents = models.CharField(max_length=16)


class SimpleUUIDPKModel(models.Model):
    if django.VERSION >= (1, 8, 0):
        id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
        )
    number = models.IntegerField()
    contents = models.CharField(max_length=16)
