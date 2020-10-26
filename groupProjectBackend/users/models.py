from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    preferred_name = models.CharField(max_length=25)

    def __str__(self):
        return self.username