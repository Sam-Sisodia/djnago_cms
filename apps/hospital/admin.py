from django.contrib import admin
from apps.hospital.models import Hospital
# Register your models here.



@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ["id","name"]