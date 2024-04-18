from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from cms.models import CMSPlugin
from django.utils.translation import gettext_lazy as _
from  myapp.enums import AppointmentDuration , UserType

# class User(AbstractBaseUser):
#     name = models.CharField(_('User name '), max_length=100)
#     email = models.EmailField(_('email address'), unique=True)
#     user_type = models.CharField(_('user type'), max_length=100, choices=UserType.usertypes())
    
#     # Add other fields and methods as needed

#     objects = BaseUserManager()

#     USERNAME_FIELD = 'email'
    

#     def __str__(self):
#         return self.email

class Sevices_Model(CMSPlugin):
    img = models.ImageField(upload_to="img", null=True,blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name
    


# class Department(models.Model):
#     pass
    


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=False)
    available = models.BooleanField(default=False) 
    specialization = models.CharField(max_length=200,null=True,blank=False)
    appointment_duration = models.CharField(max_length=200,choices=AppointmentDuration.appointment_time(),null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=False)

    
    def __str__(self) -> str:
        return self.name




class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    phone = models.CharField(max_length=15,null=True,blank=False)
    message = models.TextField(null=True,blank=False)
    date = models.DateField(null=True,blank=False)
    time=  models.TimeField(null=True,blank=False)

    def __str__(self) -> str:
        return self.name

    
    


