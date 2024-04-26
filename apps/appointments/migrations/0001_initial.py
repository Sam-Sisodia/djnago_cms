# Generated by Django 5.0.2 on 2024-04-26 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("name", models.CharField(max_length=200, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=15, null=True)),
                ("message", models.TextField(null=True)),
                ("date", models.DateField(null=True)),
                ("time", models.TimeField(null=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctors.doctor",
                    ),
                ),
            ],
        ),
    ]