from django.db import models
from apps.doctors.models import Doctor

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    phone = models.CharField(max_length=15,null=True,blank=False)
    message = models.TextField(null=True,blank=False)
    date = models.DateField(null=True,blank=False)
    time=  models.TimeField(null=True,blank=False)
    # upload_reports = models.FileField(upload_to='static/patientreports', null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    