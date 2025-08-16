import uuid
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import EmailField, UUIDField
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
    email = EmailField(unique=True)
    username = None  # type: ignore[assignment]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()
