from django.db import models


class Term(models.TextChoices):
    ONE = "1", "1"
    TWO = "2", "2"
    THREE = "3", "3"
    FOUR = "4", "4"
    FIVE = "5", "5"
    SIX = "6", "6"
    SEVEN = "7", "7"
    EIGHT = "8", "8"
    NINE = "9", "9"
    TEN = "10", "10"


class Gender(models.TextChoices):
    FEMALE = "F", "Female"
    MALE = "M", "Male"


class Degree(models.TextChoices):
    FRESHMAN = "F", "Freshman"
    BACHELOR = 'B', "Bachelor"
    MASTER = 'M', "master"
    DOCTOR = 'D', "Doctor"


class EmploymentStatus(models.TextChoices):
    FORMAL = "F", "Formal"
    INFORMAL = "I", "Informal"


class TypeUniversity(models.TextChoices):
    AZAD = "A", "Azad"
    STATE = "S", "State"
    NIGHT = "N", "Night"
