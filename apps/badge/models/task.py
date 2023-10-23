from django.db import models
from .user import BadgeUser


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    is_completed = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    points = models.IntegerField(default=100, blank=True)

    assignee = models.ForeignKey(
        BadgeUser,
        on_delete=models.SET_NULL,
        verbose_name="Assignee",
        related_name="assigned_tasks",
        null=True,
    )
    responsible = models.ForeignKey(
        BadgeUser,
        on_delete=models.SET_NULL,
        verbose_name="Responsible",
        related_name="managed_tasks",
        null=True,
    )

    def __str__(self):
        return self.name
