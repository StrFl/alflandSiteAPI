from django.contrib.auth.models import User, AbstractUser
from django.db import models
import uuid


class UserFields(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    avatarId = models.UUIDField(
        default=uuid.uuid4,
        unique=True,

        editable=False,
    )
    isEnabled = models.BooleanField(default=True)

    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    verified = models.BooleanField(default=True)
    bannedUntil = models.DateTimeField(auto_now=True)

    activity = models.JSONField(default=dict)
    balance = models.JSONField(default=dict)




# class UserModel(AbstractUser):
#     ...


class SkinsFile(models.Model):
    file = models.FileField(upload_to='uploads/')


