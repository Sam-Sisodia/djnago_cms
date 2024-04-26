from django.contrib import admin
from apps.users.models import UserProfile

# Register your models here.



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id","user_type","user"]
