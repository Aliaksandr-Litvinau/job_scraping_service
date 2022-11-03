from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
