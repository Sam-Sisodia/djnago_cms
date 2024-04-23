from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from cms.models import CMSPlugin
from django.utils.translation import gettext_lazy as _
from  myapp.enums import AppointmentDuration , UserType
from  django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=False)    
    user_type = models.CharField(_('user type'), max_length=100, choices=UserType.usertypes())
    



   

class Sevices_Model(CMSPlugin):
    img = models.ImageField(upload_to="img", null=True,blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Hospital(models.Model):
    name = models.CharField(max_length=200,null=True,blank=False)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=False)
    # doctor_image = models.ImageField(upload_to='static/doctorimage',null=True,blank=True)
    # available = models.BooleanField(default=False) 
    # qualification = models.CharField(max_length=200,null=True,blank=False)
    specialization = models.CharField(max_length=200,null=True,blank=False)
    appointment_duration = models.CharField(max_length=200,choices=AppointmentDuration.appointment_time(),null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=False)
    # hospital = models.ManyToManyField(Hospital, blank=True)
    


    @property
    def leave(self):
        pass
    @property
    def rating(self):
        pass
    
    def __str__(self) -> str:
        return self.name




class DoctorSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    phone = models.CharField(max_length=15,null=True,blank=False)
    message = models.TextField(null=True,blank=False)
    date = models.DateField(null=True,blank=False)
    time=  models.TimeField(null=True,blank=False)
    upload_reports = models.FileField(upload_to='static/patientreports', null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    
    


class  Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    review = models.CharField(max_length=200)
    rating = models.IntegerField(null=True,blank=True)
    

class GeneralSetting(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    per_appointment_time = models.PositiveSmallIntegerField(choices=[(30, '30 minutes'), (60, '60 minutes'), (90, '90 minutes')])
    break_time = models.PositiveSmallIntegerField(default=0)  # in minutes




class Leave(models.Model):
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)
    whole_day = models.BooleanField(default=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
 
