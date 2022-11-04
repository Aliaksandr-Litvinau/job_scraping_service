from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(City, self).save(*args, **kwargs)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Programming language"
        verbose_name_plural = "Programming languages"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(ProgrammingLanguage, self).save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    description = models.TextField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    prog_lang = models.ForeignKey('ProgrammingLanguage',
                                  on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
