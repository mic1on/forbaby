from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
