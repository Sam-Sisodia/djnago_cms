# Generated by Django 5.0.2 on 2024-04-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hospital", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("desciption", models.TextField(blank=True, null=True)),
                (
                    "doctor_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="static/doctorimage"
                    ),
                ),
                ("qualification", models.CharField(max_length=200, null=True)),
                ("specialization", models.CharField(max_length=200, null=True)),
                (
                    "appointment_duration",
                    models.CharField(
                        choices=[
                            ("00:00", "00:00"),
                            ("01:00", "01:00"),
                            ("02:00", "02:00"),
                            ("03:00", "03:00"),
                            ("04:00", "04:00"),
                            ("05:00", "05:00"),
                            ("06:00", "06:00"),
                            ("07:00", "07:00"),
                            ("08:00", "08:00"),
                            ("09:00", "09:00"),
                            ("10:00", "10:00"),
                            ("11:00", "11:00"),
                            ("12:00", "12:00"),
                            ("13:00", "13:00"),
                            ("14:00", "14:00"),
                            ("15:00", "15:00"),
                            ("16:00", "16:00"),
                            ("17:00", "17:00"),
                            ("18:00", "18:00"),
                            ("19:00", "19:00"),
                            ("20:00", "20:00"),
                            ("21:00", "21:00"),
                            ("22:00", "22:00"),
                            ("23:00", "23:00"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "hospital",
                    models.ManyToManyField(blank=True, to="hospital.hospital"),
                ),
            ],
        ),
    ]
