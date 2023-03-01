from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom User model created in order to have different application
    access depending on if the user is an artist or not
    """

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['is_artist']

    username = models.CharField(unique=True, max_length=50)
    is_artist = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
