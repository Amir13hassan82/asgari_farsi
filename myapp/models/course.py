from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=155)
    number_of_unit = models.PositiveIntegerField()
    the_need = models.ForeignKey("Course", on_delete=models.CASCADE)
    prerequisite = models.ForeignKey("Course", on_delete=models.CASCADE)
    address = models.TextField()
