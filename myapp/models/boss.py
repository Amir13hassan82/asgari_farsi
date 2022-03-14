from django.db import models
from django import forms
from django.utils import timezone
from myapp.enums import Gender, Degree


class Boss(models.Model):
    first_name = models.CharField(max_length=285)
    last_name = models.CharField(max_length=285)
    passwords = forms.CharField(widget=forms.PasswordInput)
    national_code = models.CharField(max_length=10, unique=True)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField(default=timezone.now())
    address = models.TextField()
    Gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    degree = models.CharField(max_length=1, choices=Degree.choices, default=Degree.DOCTOR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
