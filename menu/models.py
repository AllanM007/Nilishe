from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.db import models
from PIL import Image
import uuid


class Pizza(models.Model):
    name = models.CharField(max_length=20, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    amount = models.IntegerField(null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)