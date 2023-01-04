from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=127, unique=True)
    fone = models.CharField(max_length=20)
    is_premium = models.BooleanField(null=True, default=False)
    is_active = models.BooleanField(null=True, default=True)
    is_offering = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
