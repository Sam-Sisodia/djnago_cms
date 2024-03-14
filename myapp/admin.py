from django.contrib import admin

# Register your models here.
from . models import Doctor , Department ,Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id","name"]



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
 





@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display= ["id","doctor",
"department",
"name",
"email",
"date",
"time",]