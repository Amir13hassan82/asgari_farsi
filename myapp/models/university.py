from django.db import models
from myapp.enums import TypeUniversity
from .boss import Boss


class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    type = models.CharField(max_length=1, choices=TypeUniversity.choices, default=TypeUniversity.STATE)
    department = models.CharField(max_length=1)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)
