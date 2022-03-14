from django.db import models
from myapp.enums import TypeUniversity
# from .boss import Boss

__all__ = ("UniversityClass",)


class UniversityClass(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    type = models.CharField(max_length=1, choices=TypeUniversity.choices, default=TypeUniversity.STATE)
    department = models.CharField(max_length=1)

    def __str__(self):
        return self.name
