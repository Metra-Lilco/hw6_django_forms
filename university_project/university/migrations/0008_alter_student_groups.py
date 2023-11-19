# Generated by Django 4.2.6 on 2023-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("university", "0007_remove_group_students"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="students", to="university.group"
            ),
        ),
    ]
