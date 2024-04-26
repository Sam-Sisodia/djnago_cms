from django.shortcuts import render
from django.views import View
from apps.appointments.models import Appointment

# Create your views here.
class DoctorAppointments(View):
    def get(self,request):
        appointments = Appointment.objects.all()
        context = {
            "appointments": appointments
        }
        return render(request,"myappointments.html",context )