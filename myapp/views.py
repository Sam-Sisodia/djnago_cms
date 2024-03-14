from django.shortcuts import render

from . models import Doctor  ,Appointment

from django.views import generic
from django.views import View

from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from .models import Doctor, Appointment
from .email import appointment_mail
from django.contrib import messages

class BookAppointment(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        context = {
            "doctors": doctors
        }
        return render(request, "appointment.html", context)
    
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
            return render(request, "appointment.html")
        
        if date:
            doctor = Doctor.objects.get(id=doctor_id)
            appointment = Appointment.objects.create(doctor=doctor, name=name, email=email, phone=phone,
                                                      message=message, date=date, time=time)
            appointment_mail(appointment, doctor)
            messages.success(request, f"Your appointment is booked at Date : {appointment.date}  Time :{appointment.time}")
        return render(request, "appointment.html")
    
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


class MyAppointments(View):
    def get(self,request):
        appointments = Appointment.objects.all()
        context = {
            "appointments": appointments
        }
        return render(request,"myappointments.html",context )

        


