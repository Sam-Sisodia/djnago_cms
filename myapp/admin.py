from django.contrib import admin

# Register your models here.
from . models import Doctor ,Appointment ,Sevices_Model




@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","on_leave"]



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id","doctor","name","email","phone","message","date","time","availble"]








@admin.register(Sevices_Model)
class Sevices_ModelAdmin(admin.ModelAdmin):
    list_display = ["id","img","name","description"]
