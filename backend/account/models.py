from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.conf import settings

import uuid


class User(AbstractUser):
    gifts = models.IntegerField(verbose_name="Дары", default=0,
                                validators=[MinValueValidator(settings.MIN_GIFTS_VALUE)])
    avatar = models.ImageField(verbose_name="Аватарка", upload_to="images/uploads/users/photo/",
                               default="images/uploads/users/avatars"
                                       "/default.png")


class RegistrationLinkGenerator:
    url = models.URLField(default=uuid.uuid4().hex)
    alive_time = models.IntegerField(verbose_name="Время жизни ссылки", default=60)
