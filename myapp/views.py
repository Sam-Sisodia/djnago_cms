from django.shortcuts import render
from django.contrib.auth import get_user_model
from . models import Doctor  ,Appointment

from django.views import generic
from django.views import View

from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from .models import Doctor, Appointment,Sevices_Model,User
from .email import appointment_mail
from django.contrib import messages
from  myapp.enums import AppointmentDuration , UserType
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout








class Register(View):
    def get(self,request):
        usertypes = UserType.usertypes() 
        context = {
            "usertypes":usertypes

        }
        return render(request,"register.html",context)
    
    def post(self, request):
        name = request.POST.get("name")
        usertype = request.POST.get("usertype")
        email = request.POST.get("email")
        password = request.POST.get("password")
        obj = User.objects.create(name=name,user_type=usertype,email=email,password=password)
        obj.set_password(obj.password)
        obj.save()
        return redirect('dashboard')


def Login(request):
    if  request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
     
        user = authenticate(request,email=email,password=password)
        print("use",email,password)
       

        if user is not None:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            auth_login(request, user)
            user=request.user
            print("++++++++++++++",user.user_type)
            if user:
                return render(request,'dashboard.html')

            else:
                messages.info(request ,"Please Verify Your Accounts ")
        else:
            messages.info(request ,"Incorrect Username or Password")
            return render(request, 'login.html')
    return render(request,'login.html')


def logout(request):
    user_logout(request)
    return redirect('/login')

        


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
            appointment_time = datetime.strptime(appointment.time, '%H:%M').time()
            formatted_time = appointment_time.strftime('%I:%M %p')
            messages.success(request, f"Your appointment is booked at Date : {appointment.date} at the  Time {formatted_time}")
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
        return render(request,"dashboard/tables.html",context )






class Showdata(View):
    def get(self, request):
        data = Sevices_Model.objects.all()
        context ={
            "data": data
        }
        # Render the template and return the HTTP response
        return render(request, "show.html",context)


from django.conf import settings
class AdminDashboard(View):
    def get(self, request):
        data = Sevices_Model.objects.all()
        installed_apps = [app.split('.')[-1] for app in settings.INSTALLED_APPS]
        print("Installed Django +++++++++++++++++++++++++++++++applications:", ', '.join(installed_apps))
        
        # Render the template and return the HTTP response
        return render(request, "dashboard/dashboard.html",)


