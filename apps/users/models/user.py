from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.base.timestamp import TimestampModel
from .managers import UserManager


class User(AbstractUser, TimestampModel):
    username = None

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
