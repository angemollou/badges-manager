from django.db import models
from django.contrib.auth.models import User


class BadgeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    score = models.IntegerField(default=0, verbose_name="Points", blank=True)

    def __str__(self):
        return self.user.username

    def set_new_score(self, points):
        self.score += points
        self.save()
