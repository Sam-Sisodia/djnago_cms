from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from cms.models import CMSPlugin
from django.utils.translation import gettext_lazy as _
from apps.users.enums import UserType
from  django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=False)    
    user_type = models.CharField(_('user type'), max_length=100, choices=UserType.usertypes())