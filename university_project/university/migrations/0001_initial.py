# Generated by Django 4.2.6 on 2023-10-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_of_the_group",
                    models.CharField(max_length=200, verbose_name="Name of the group"),
                ),
                ("curator", models.CharField(max_length=120, verbose_name="Curator")),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=150, verbose_name="First name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=200, verbose_name="Last name"),
                ),
                (
                    "patronymic",
                    models.CharField(max_length=150, verbose_name="Patronymic"),
                ),
                ("birth_date", models.DateField(verbose_name="Date of birth")),
                ("subject", models.CharField(max_length=150, verbose_name="Subject")),
            ],
        ),
    ]
