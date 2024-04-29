# Generated by Django 5.0.2 on 2024-04-29 09:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0002_rename_desciption_doctor_description"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="email",
        ),
        migrations.RemoveField(
            model_name="doctor",
            name="name",
        ),
        migrations.AddField(
            model_name="doctor",
            name="doctor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
