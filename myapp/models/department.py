from django.db import models
from .university import University


class Department(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
