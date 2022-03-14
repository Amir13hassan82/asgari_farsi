from django.db import models

__all__ = ("Course",)


class Course(models.Model):
    name = models.CharField(max_length=155)
    number_of_unit = models.PositiveIntegerField()
    the_need = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='+')
    prerequisite = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='+')
    address = models.TextField()

    def __str__(self):
        return self.name
