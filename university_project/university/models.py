from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First name")
    last_name = models.CharField(max_length=200, verbose_name="Last name")
    birth_date = models.DateField(verbose_name="Date of birth")
    subject = models.CharField(max_length=150, verbose_name="Subject")
