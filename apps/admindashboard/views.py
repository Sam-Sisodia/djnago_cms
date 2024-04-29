from django.shortcuts import render
from django.views import View
from apps.appointments.models import Appointment
from django.db.models import Q
from apps.doctors.models import Doctor
from apps.hospital.models import Hospital
from apps.doctors.enums import AppointmentDuration

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth import get_user_model
User = get_user_model()

from apps.users.models import UserProfile
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
        appointments = Appointment.objects.filter(Q(doctor__doctor__email__icontains=text) | Q(name=text)| Q(email__icontains=text))
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
        durations = AppointmentDuration.appointment_time() 
        user= UserProfile.objects.filter(user_type="Doctor")
        context = {
            "hospitals":hospitals,
            "appointment_duration": durations,
            "users": user,
        }
        return render(request,"dashboard/add_doctors.html",context)
    
    def post(self,request):
        doctor_user = request.POST.get('doctor_user')
        description = request.POST.get('description')
        qualification = request.POST.get('qualification')
        specialization = request.POST.get('specialization')
        appointment_duration = request.POST.get('appointment_duration')
        hospital_ids = request.POST.getlist('hospitals')  # Assuming hospital is a multi-select field
        
        doctor = Doctor.objects.create(
            user_id = doctor_user,
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
    
class EditDoctor(View):
    def get(self, request, doctor_id):
        doctor = get_object_or_404(Doctor, pk=doctor_id)
        hospitals = Hospital.objects.all()
        durations = AppointmentDuration.appointment_time()
        user= UserProfile.objects.filter(user_type="Doctor")
        context = {
            "doctor": doctor,
            "hospitals": hospitals,
            "appointment_duration": durations,
            "users": user,
        
        }
        return render(request, "dashboard/edit_doctors.html", context)
    
    def post(self, request, doctor_id):
        doctor = get_object_or_404(Doctor, pk=doctor_id)
        doctor.user_id = request.POST.get('doctor_user')
       
        doctor.description = request.POST.get('description')
        doctor.qualification = request.POST.get('qualification')
        doctor.specialization = request.POST.get('specialization')
        doctor.appointment_duration = request.POST.get('appointment_duration')
        hospital_ids = request.POST.getlist('hospitals')  # Assuming hospital is a multi-select field
        # doctor.hospitals.clear()
        for hospital_id in hospital_ids:
            hospital = Hospital.objects.get(pk=hospital_id)
            doctor.hospital.add(hospital)
        doctor.save()
        return redirect("all-doctors")  # Redirect to the list of all doctors view



def deletedoctor(request,doctor_id):

    doctor = get_object_or_404(Doctor, pk=doctor_id)
    print("++++++++++++",doctor)
    doctor.delete()
    return redirect("all-doctors") 


        



class HospitalsView(View):
    def get(self,request):
        hospitals = Hospital.objects.all()
        context = {
            "hospitals": hospitals
        }
        return render(request,"dashboard/hospitals.html",context )

    def post(self,request):
        text = request.POST.get("search")
        hospitals = Hospital.objects.filter(name__icontains=text) 
        context = {
            "hospitals": hospitals,
        }
        return render(request, "dashboard/hospitals.html", context)
    
class AddHostpital(View):
    def get(self,request):
        return render(request,"dashboard/add_hospitals.html",)
    
    def post(self,request):
        name = request.POST.get('name')
        doctor = Hospital.objects.create(
            name=name,)
        return redirect("hospitals")
    

class EditHospital(View):
    def get(self, request, doctor_id):
        hospitals = get_object_or_404(Hospital, pk=doctor_id)
        context = {
            "hospital": hospitals,
        }
        return render(request, "dashboard/edit_hospitals.html", context)
    
    def post(self, request, doctor_id):
        hospital = get_object_or_404(Hospital, pk=doctor_id)

        hospital.name = request.POST.get('name')

     
        hospital.save()
        return redirect("hospitals")  # Redirect to the list of all doctors view


def deletehospital(request,doctor_id):
    doctor = get_object_or_404(Hospital, pk=doctor_id)
    doctor.delete()
    return redirect("hospitals") 