from django.db import models
from .user import BadgeUser
from .model3d import Model3d


class Badge(models.Model):
    STATUS = [
        ("active", "Active"),
        ("published", "Published"),
        ("draft", "Draft"),
    ]
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    icon = models.ForeignKey(Model3d, on_delete=models.PROTECT, verbose_name="Icon")
    description = models.TextField(verbose_name="Description", blank=True, default="")
    status = models.CharField(
        max_length=255,
        verbose_name="Status",
        blank=True,
        default="active",
        choices=STATUS,
    )
    criteria = models.IntegerField(verbose_name="Criteria", default=0)

    def __str__(self):
        return self.name


class Assertion(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["recipient", "badge"],
                name="unique_recipient_badge",
            )
        ]

    recipient = models.ForeignKey(
        BadgeUser,
        on_delete=models.CASCADE,
        verbose_name="Recipient",
        related_name="badges",
    )
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, verbose_name="Badge")
    start_date = models.DateTimeField(
        verbose_name="Start date", auto_now_add=True, blank=True
    )
    end_date = models.DateTimeField(verbose_name="End date", null=True, blank=True)
    verifier = models.ForeignKey(
        BadgeUser,
        on_delete=models.CASCADE,
        verbose_name="Verifier",
        related_name="verified_badges",
    )
    verification_date = models.DateTimeField(
        verbose_name="Verification date", blank=True, null=True
    )

    def __str__(self):
        return self.recipient.user.username + " - " + self.badge.name
