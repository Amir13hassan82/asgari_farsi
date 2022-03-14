from django.db import models
from django.utils import timezone
from django import forms
from myapp.enums import Gender, Degree, Term, EmploymentStatus, TypeUniversity


class Student(models.Model):
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
    degree = models.CharField(max_length=1, choices=Degree.choices, default=Degree.FRESHMAN)
    term = models.CharField(max_length=2, choices=Term.choices, default=Term.ONE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class META:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Teacher(models.Model):
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
    status = models.CharField(max_length=1, choices=EmploymentStatus.choices, default=EmploymentStatus.FORMAL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class META:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Course(models.Model):
    name = models.CharField(max_length=155)
    the_need = models.ForeignKey("Course", on_delete=models.CASCADE)
    prerequisite = models.ForeignKey("Course", on_delete=models.CASCADE)
    address = models.TextField()


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


class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    type = models.CharField(max_length=1, choices=TypeUniversity.choices, default=TypeUniversity.STATE)
    department = models.CharField(max_length=1)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)


class Department(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)


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
    degree = models.CharField(max_length=1, choices=Degree.choices, default=Degree.DOCTOR)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class StudentTeacher(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    year = models.DateField(auto_now_add=True)


class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.DateField(auto_now_add=True)


class TeacherCourse(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.DateField(auto_now_add=True)
