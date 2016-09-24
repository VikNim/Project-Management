from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    username = models.CharField(max_length = 50)
    Position_Choice = (
        ('Team Leader', 'Team Leader'),
        ('Developer', 'Developer'),
    )
    position = models.CharField(max_length=30, choices=Position_Choice)

    def __str__(self):
        return str(self.username)
