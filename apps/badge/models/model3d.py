from django.db import models


class Model3d(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to="images/", verbose_name="Image")
    file = models.FileField(upload_to="files/", verbose_name="File")

    def __str__(self):
        return self.name