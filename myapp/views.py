from django.shortcuts import render

from . models import Doctor , Department ,Appointment

from django.views import generic
from django.views import View

class GetDoctors(View):
    template_name = 'appointment.html'
    def get(self, request):
        doctors = Doctor.objects.all()
        departments = Department.objects.all()
        context = {
            "doctors": doctors,
            "departments": departments
        }
        return render(request, self.template_name, context)
    
    def post(self,request):
        doctor = request.POST.get("doctor")
        department = request.POST.get("department")
        name = request.POST.get("name")
        email = request.POST.get("email")
        time = request.POST.get("time")
        date = request.POST.get("date")
        Appointment.objects.create(doctor_id=doctor,department_id=department,name=name,email=email,
                                   time=time,date=date)


        return render(request, "appointment.html")

     


def content(request):
    return render(request,"contact.html")