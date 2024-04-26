from django.contrib import admin
from apps.doctors.models import Doctor
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","specialization","appointment_duration","created_at","updated_at"]



