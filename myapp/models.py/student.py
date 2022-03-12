from django.db import models
from django.utils import timezone


class Student(models.Model):
    first_name = models.CharField(max_length=285)
    last_name = models.CharField(max_length=285)
    national_code = models.CharField(max_length=10, unique=True)
    age = models.PositiveIntegerField(max_length=2)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    birth_date = models.DateTimeField(timezone)
