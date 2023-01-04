from django.db import models

# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fone = models.CharField(max_length=20, unique=True)
    is_premium = models.BooleanField()
    is_offering = models.BooleanField()
    created_at = models.DateField(
        auto_now_add=True,
    )
    update_at = models.DateField(
        auto_now_add=True,
    )
