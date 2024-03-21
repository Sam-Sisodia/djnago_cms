from django.db import models

# Create your models here.
from cms.models import CMSPlugin

class Sevices_Model(CMSPlugin):
    img = models.ImageField(upload_to="img", null=True,blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=False)
    on_leave = models.BooleanField(default=False) 
    
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
    availble = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    
    


