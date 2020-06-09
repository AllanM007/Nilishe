from django.db import models
from PIL import Image
import uuid


class Pizza(models.Model):
    name = models.CharField(max_length=20, blank=True)
    amount = models.IntegerField(null=True)
    topping = models.CharField(max_length=20, blank=True)
    sauce = models.CharField(max_length=20, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name