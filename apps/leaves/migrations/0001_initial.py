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
            name="Leave",
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
                    "leave_type",
                    models.CharField(
                        choices=[
                            ("CasualLeave", "Casual Leave"),
                            ("MedicalLeave", "Medical Leave"),
                            ("PaidLeave", "Paid Leave"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "leave_duration",
                    models.CharField(
                        choices=[
                            ("Singleday", "Singleday"),
                            ("Multipledays", "Multipledays"),
                            ("hours", "hours"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("start_time", models.DateTimeField()),
                ("end_time", models.TimeField()),
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