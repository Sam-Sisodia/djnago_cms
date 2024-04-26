from django.contrib import admin

from apps.appointments.models import Appointment
# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id","doctor","name","email","phone","message","date","time"]