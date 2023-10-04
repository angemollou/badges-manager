from django.db import models


class Model3d(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    description = models.TextField(verbose_name="Description", blank=True, default="")
    image = models.ImageField(upload_to="images/", verbose_name="Image")
    file = models.FileField(upload_to="files/", verbose_name="File", blank=True, null=True)

    def __str__(self):
        return self.name