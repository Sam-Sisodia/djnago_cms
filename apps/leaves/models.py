from django.db import models
from apps.leaves.enums import Leaveduration,Leavetype
from apps.doctors.models import Doctor

# Create your models here.

class Leave(models.Model):
    leave_type = models.CharField(max_length=200,choices=Leavetype.leavetypes(),null=True,blank=False)
    leave_duration = models.CharField(max_length=200,choices=Leaveduration.leavedurations(),null=True,blank=False)
    start_date = models.DateField()
    end_date  = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    