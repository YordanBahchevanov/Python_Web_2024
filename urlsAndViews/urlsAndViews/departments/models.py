from django.db import models
from django.utils.text import slugify


class Department(models.Model):
    name = models.CharField(
        max_length=100,
    )

    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.pk}, Name: {self.name}"
