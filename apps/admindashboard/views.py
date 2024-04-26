from django.shortcuts import render
from django.views import View
from apps.appointments.models import Appointment
from django.db.models import Q
from apps.doctors.models import Doctor
from apps.hospital.models import Hospital

from django.shortcuts import render, redirect



class AdminDashboard(View):
    def get(self, request):
        
        # Render the template and return the HTTP response
        return render(request, "dashboard/dashboard.html",)
    
# Create your views here.
class AdminAppointments(View):
    def get(self,request):
        appointments = Appointment.objects.all()
        context = {
            "appointments": appointments
        }
        return render(request,"dashboard/appointments.html",context )
    def post(self,request):
        text = request.POST.get("search")
        appointments = Appointment.objects.filter(Q(doctor__name__icontains=text) | Q(name=text)| Q(email__icontains=text))
        context = {
            "appointments": appointments,
        }
        return render(request, "dashboard/appointments.html", context)




class AllDoctorsView(View):
    def get(self,request):
        doctors = Doctor.objects.all()
        context = {
            "doctors": doctors
        }
        return render(request,"dashboard/doctors.html",context )

    def post(self,request):
        text = request.POST.get("search")
        doctors = Doctor.objects.filter(Q(name__icontains=text) |  Q(email__icontains=text))
        context = {
            "doctors": doctors,
        }
        return render(request, "dashboard/doctors.html", context)
    

class AddDoctors(View):
    def get(self,request):
        hospitals = Hospital.objects.all()  
        context = {
            "hospitals":hospitals
        }
        return render(request,"dashboard/add_doctors.html",context)
    
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        qualification = request.POST.get('qualification')
        specialization = request.POST.get('specialization')
        appointment_duration = request.POST.get('appointment_duration')
        hospital_ids = request.POST.getlist('hospital')  # Assuming hospital is a multi-select field
        
        doctor = Doctor.objects.create(
            name=name,
            email=email,
            description=description,
            qualification=qualification,
            specialization=specialization,
            appointment_duration=appointment_duration,
        )
        
        # Add hospitals to the doctor object
        for hospital_id in hospital_ids:
            hospital = Hospital.objects.get(pk=hospital_id)
            doctor.hospital.add(hospital)
        doctor.save()
        return redirect("all-doctors")
        
