from django.db import models
from django import forms
from django.utils import timezone
from myapp.enums import Gender, Degree
from .department import Department
from .course import Course


class ManagerGroup(models.Model):
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
    degree = models.CharField(max_length=1, choices=Degree.choices, default=Degree.MASTER)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
