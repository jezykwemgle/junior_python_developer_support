# Generated by Django 4.2.6 on 2023-11-01 11:23

from django.db import migrations, models
import users.constants


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("AD", "AD"), ("JR", "JR"), ("SR", "SR")],
                default=users.constants.Role["JUNIOR"],
                max_length=2,
            ),
        ),
    ]
