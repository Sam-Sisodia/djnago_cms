from django.db import models

# Create your models here.
from cms.models import CMSPlugin

class Sevices_Model(CMSPlugin):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name



class Department(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name="doctor",  )
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="department",  )
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True,blank=True)
    date = models.DateField(null=True,blank=False)
    time = models.TimeField(null=True,blank=False)
    
    def __str__(self) -> str:
        return self.name

    
