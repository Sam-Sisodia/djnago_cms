from django.db import models
from apps.hospital.models import Hospital
from apps.doctors.enums import AppointmentDuration
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=False)
    description = models.TextField(null=True,blank=True)
    
    doctor_image = models.ImageField(upload_to='static/doctorimage',null=True,blank=True)
    qualification = models.CharField(max_length=200,null=True,blank=False)
    specialization = models.CharField(max_length=200,null=True,blank=False)
    appointment_duration = models.CharField(max_length=200,choices=AppointmentDuration.appointment_time(),null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=False)
    hospital = models.ManyToManyField(Hospital, blank=True)
    


    @property
    def leave(self):
        pass
    @property
    def rating(self):
        pass
    
    def __str__(self) -> str:
        return self.name