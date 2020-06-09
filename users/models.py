from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.db import models
from django.contrib.gis.db import models
from PIL import Image
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    joined = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    slug = models.SlugField(null=True, blank=True, unique=True)
    profurl = models.URLField(null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.first_name)

        return super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    body = models.TextField()
    reviewed_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)

    class Meta:
        ordering = ['reviewed_on']

    def approve(self):
        self.active = True
        self.save()

    def __str__(self):
        return self.body

    def __str__(self):
        return 'Review {} by {}'.format(self.body, self.name)