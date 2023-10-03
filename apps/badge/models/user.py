from django.db import models
from django.contrib.auth.models import User


class BadgeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, verbose_name="Points")

    def __str__(self):
        return self.user.username
