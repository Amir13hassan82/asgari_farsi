from django.db import models
from .universitymodel import UniversityClass

__all__ = ("Department",)


class Department(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    university = models.ForeignKey(UniversityClass, on_delete=models.CASCADE,related_name='+')

    def __str__(self):
        return self.name
