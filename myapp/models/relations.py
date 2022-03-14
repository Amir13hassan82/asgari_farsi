from django.db import models
from .student import Student
from .course import Course
from .teacher import Teacher


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
