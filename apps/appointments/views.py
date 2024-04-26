from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth  import get_user_model
User = get_user_model()
from django.db.models import Q
from apps.doctors.enums import AppointmentDuration
from apps.appointments.models import Appointment
from apps.doctors.models import Doctor
from apps.appointments.email import appointment_mail
from datetime import datetime

class BookAppointment(View):
    doctors = Doctor.objects.all()
    durations = AppointmentDuration.appointment_time() 
    context = {
        "doctors":doctors,
        "durations":durations,
    }
    def get(self, request):
        return render(request, "appointment.html", self.context)
    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        doctor_id = request.POST.get("doctor")
        message = request.POST.get("message")
        date = request.POST.get("date")
        time = request.POST.get("time")

        validation_result = self.validate_appointment(doctor_id,date, time,)
        if validation_result:
            messages.error(request, f"{validation_result}.")
            return render(request, "appointment.html",self.context)
        
        if date:
            doctor = Doctor.objects.get(id=doctor_id)
            appointment = Appointment.objects.create(doctor=doctor, name=name, email=email, phone=phone,
                                                      message=message, date=date, time=time)
            appointment_mail(appointment, doctor)
            appointment_time = datetime.strptime(appointment.time, '%H:%M').time()
            formatted_time = appointment_time.strftime('%I:%M %p')
            messages.success(request, f"Your appointment is booked at Date : {appointment.date} at the  Time {formatted_time}")
            return render(request, "appointment.html",self.context)

        
        return render(request, "appointment.html",self.context)
        
    @staticmethod
    def validate_appointment(doctor_id,date, time_str):
        if Appointment.objects.filter(doctor= doctor_id, time=time_str,date=date).exists():
            return "Already Booked please select another one slot of time "
        
        if not doctor_id:
            return "Select  Your Doctor "
        
        exp = datetime.strptime(date, "%Y-%m-%d").date()  # Convert exp string to datetime.date
        today_date = datetime.now().date()
        if exp < today_date:  # Check if exp is in the past
            return "Please select a Vaild date . "
        
         
        selected_datetime = datetime.strptime(date + ' ' + time_str, '%Y-%m-%d %H:%M')
        current_datetime = datetime.now()
        if selected_datetime < current_datetime:
            return "Choose Valid time ."
        return None  # Return None if no validation errors occur
    



def searchdoctor(request):
    doctors = Doctor.objects.all()
    durations = AppointmentDuration.appointment_time() 
    if request.method == "POST":  # Add a colon here
        text = request.POST.get("search")
        search_doctors = Doctor.objects.filter(Q(name__icontains=text) | Q(email__icontains=text))
        context = {
            "search_doctors": search_doctors,
            "doctors":doctors,
            "durations":durations,
        }
        return render(request, "appointment.html", context)
    context = {
        "doctors":doctors,
        "durations":durations,
    }
    return render(request, "appointment.html",context)
