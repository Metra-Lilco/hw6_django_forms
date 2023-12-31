from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First name")
    last_name = models.CharField(max_length=200, verbose_name="Last name")
    patronymic = models.CharField(max_length=150, verbose_name="Patronymic")
    birth_date = models.DateField(verbose_name="Date of birth")
    subject = models.CharField(max_length=150, verbose_name="Subject")

    def __str__(self):
        return f"{self.first_name} {self.patronymic} {self.last_name}"


class Group(models.Model):
    name_of_the_group = models.CharField(
        max_length=200, verbose_name="Name of the group"
    )
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        if self.name_of_the_group:
            return self.name_of_the_group
        return "Не призначено"


# ДЗ 7. reverse, urls


class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First name")
    last_name = models.CharField(max_length=200, verbose_name="Last name")
    birth_date = models.DateField(verbose_name="Date of birth")
    phone = models.CharField(max_length=30, null=True, verbose_name="Phone number")
    groups = models.ManyToManyField(
        Group,
        related_name="students",
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
