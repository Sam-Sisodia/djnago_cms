from django.contrib import admin

# Register your models here.
from . models import Doctor ,Appointment ,Sevices_Model,UserProfile




@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","available","specialization","appointment_duration","created_at","updated_at"]



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id","doctor","name","email","phone","message","date","time"]

@admin.register(Sevices_Model)
class Sevices_ModelAdmin(admin.ModelAdmin):
    list_display = ["id","img","name","description"]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id","user_type","user"]
