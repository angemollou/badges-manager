from django.db import models
from .user import BadgeUser
from .model3d import Model3d


class Badge(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    type = models.CharField(max_length=255, verbose_name="Badge choice")
    icon = models.ForeignKey(Model3d, on_delete=models.PROTECT, verbose_name="Icon")
    description = models.TextField(verbose_name="Description")
    status = models.CharField(max_length=255, verbose_name="Status")
    issuer = models.ForeignKey(
        BadgeUser,
        on_delete=models.CASCADE,
        verbose_name="Issuer",
        related_name="issued_badges",
    )
    criteria = models.TextField(verbose_name="Criteria")

    def __str__(self):
        return self.name


class Assertion(models.Model):
    recipient = models.ForeignKey(
        BadgeUser,
        on_delete=models.CASCADE,
        verbose_name="Recipient",
        related_name="badges",
    )
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, verbose_name="Badge")
    start_date = models.DateTimeField(verbose_name="Start date")
    end_date = models.DateTimeField(verbose_name="End date")
    verifier = models.ForeignKey(
        BadgeUser,
        on_delete=models.CASCADE,
        verbose_name="Verifier",
        related_name="verified_badges",
    )
    verification_date = models.DateTimeField(verbose_name="Verification date")

    def __str__(self):
        return self.recipient.user.username + " - " + self.badge.name
