from django.contrib import admin

from apps.leaves.models import Leave
# Register your models here.





@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ["id","leave_type","leave_duration","start_date","end_date","start_time","end_time","doctor"]