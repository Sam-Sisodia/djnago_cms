# from django.shortcuts import render
# from django.contrib.auth import get_user_model
# from . models import Doctor  ,Appointment

# from django.views import generic
# from django.views import View

# from django.shortcuts import render, redirect
# from django.views import View
# from datetime import datetime
# from .models import Doctor, Appointment,Sevices_Model,UserProfile,Hospital,Leave
# from .email import appointment_mail
# from django.contrib import messages
# from  myapp.enums import AppointmentDuration , UserType
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as user_logout
# from django.contrib.auth  import get_user_model
# User = get_user_model()
# from django.db.models import Q


# class Register(View):
#     usertypes = UserType.usertypes() 
#     context = {"usertypes":usertypes }

#     def get(self,request):
#         return render(request,"register.html",self.context)
    
#     def post(self, request):
#         try:
#             name = request.POST.get("name")
#             usertype = request.POST.get("usertype")
#             email = request.POST.get("email")
#             password = request.POST.get("password")
#             if not self.validateform(request, usertype, email):
#                 return render(request, "register.html", self.context)
#             obj = User.objects.create(username=email,email=email,password=password,first_name=name)
#             obj.set_password(obj.password)
#             obj.save()
#             UserProfile.objects.create(user=obj, user_type=usertype)
#             return redirect('login')
#         except Exception as e:

#             return render(request,"register.html",self.context)
    
#     @staticmethod
#     def validateform(request, usertype, email):
#         user = User.objects.filter(username=email).exists()
#         if user:
#             messages.info(request, "Email is already registered")
#             return False
#         if not usertype:
#             messages.info(request, "Please Select usertype")
#             return False
#         return True




# def Login(request):
#     if  request.method == "POST":
#         email = request.POST.get('email')
#         password =request.POST.get('password')
     
#         user = authenticate(request,username=email,password=password)
#         if user is not None:
#             auth_login(request, user)
#             user=request.user
#             user =UserProfile.objects.filter(user=user).first()
#             usertype = user.user_type
            
#             if usertype =="Staff":
#                 return redirect('dashboard')
#             if usertype =="Doctor":
#                 return redirect('doctor-appointments')
#             if usertype =="Patient":
#                 return redirect('home')         
#         else:
#             messages.info(request ,"Incorrect Username or Password")
#             return render(request, 'login.html')
#     return render(request,'login.html')


# def logout(request):
#     user_logout(request)
#     return redirect('/login')

        


# class BookAppointment(View):
#     doctors = Doctor.objects.all()
       
#     durations = AppointmentDuration.appointment_time() 
     
#     context = {
#         "doctors":doctors,
#         "durations":durations,
#     }
#     def get(self, request):
#         return render(request, "appointment.html", self.context)
    
#     def post(self, request):
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         email = request.POST.get("email")
#         doctor_id = request.POST.get("doctor")
#         message = request.POST.get("message")
#         date = request.POST.get("date")
#         time = request.POST.get("time")

#         validation_result = self.validate_appointment(doctor_id,date, time,)
#         if validation_result:
#             messages.error(request, f"{validation_result}.")
#             return render(request, "appointment.html",self.context)
        
#         if date:
#             doctor = Doctor.objects.get(id=doctor_id)
#             appointment = Appointment.objects.create(doctor=doctor, name=name, email=email, phone=phone,
#                                                       message=message, date=date, time=time)
#             appointment_mail(appointment, doctor)
#             appointment_time = datetime.strptime(appointment.time, '%H:%M').time()
#             formatted_time = appointment_time.strftime('%I:%M %p')
#             messages.success(request, f"Your appointment is booked at Date : {appointment.date} at the  Time {formatted_time}")
#             return render(request, "appointment.html",self.context)

        
#         return render(request, "appointment.html",self.context)
        
#     @staticmethod
#     def validate_appointment(doctor_id,date, time_str):
#         if Appointment.objects.filter(doctor= doctor_id, time=time_str,date=date).exists():
#             return "Already Booked please select another one slot of time "
        
#         if not doctor_id:
#             return "Select  Your Doctor "
        
#         exp = datetime.strptime(date, "%Y-%m-%d").date()  # Convert exp string to datetime.date
#         today_date = datetime.now().date()
#         if exp < today_date:  # Check if exp is in the past
#             return "Please select a Vaild date . "
        
         
#         selected_datetime = datetime.strptime(date + ' ' + time_str, '%Y-%m-%d %H:%M')
#         current_datetime = datetime.now()
#         if selected_datetime < current_datetime:
#             return "Choose Valid time ."
#         return None  # Return None if no validation errors occur


# class AdminAppointments(View):
#     def get(self,request):
#         appointments = Appointment.objects.all()
#         context = {
#             "appointments": appointments
#         }
#         return render(request,"dashboard/appointments.html",context )
#     def post(self,request):
#         text = request.POST.get("search")
#         appointments = Appointment.objects.filter(Q(doctor__name__icontains=text) | Q(name=text)| Q(email__icontains=text))
#         context = {
#             "appointments": appointments,
#         }
#         return render(request, "dashboard/appointments.html", context)


    
# class AllDoctorsView(View):
#     def get(self,request):
#         doctors = Doctor.objects.all()
#         context = {
#             "doctors": doctors
#         }
#         return render(request,"dashboard/doctors.html",context )

#     def post(self,request):
#         text = request.POST.get("search")
#         doctors = Doctor.objects.filter(Q(name__icontains=text) |  Q(email__icontains=text))
#         context = {
#             "doctors": doctors,
#         }
#         return render(request, "dashboard/doctors.html", context)


# # add-doctor


# class AddDoctors(View):
#     def get(self,request):
#         hospitals = Hospital.objects.all()  
#         context = {
#             "hospitals":hospitals
#         }
#         return render(request,"dashboard/add_doctors.html",context)
    
#     def post(self,request):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         description = request.POST.get('description')
#         qualification = request.POST.get('qualification')
#         specialization = request.POST.get('specialization')
#         appointment_duration = request.POST.get('appointment_duration')
#         hospital_ids = request.POST.getlist('hospital')  # Assuming hospital is a multi-select field
        
#         doctor = Doctor.objects.create(
#             name=name,
#             email=email,
#             description=description,
#             qualification=qualification,
#             specialization=specialization,
#             appointment_duration=appointment_duration,
#         )
        
#         # Add hospitals to the doctor object
#         for hospital_id in hospital_ids:
#             hospital = Hospital.objects.get(pk=hospital_id)
#             doctor.hospital.add(hospital)
#         doctor.save()
#         return redirect("all-doctors")
        


# class DoctorAppointments(View):
#     def get(self,request):
#         appointments = Appointment.objects.all()
#         context = {
#             "appointments": appointments
#         }
#         return render(request,"myappointments.html",context )

# class Showdata(View):
#     def get(self, request):
#         data = Sevices_Model.objects.all()
#         context ={
#             "data": data
#         }
#         # Render the template and return the HTTP response
#         return render(request, "show.html",context)


# from django.conf import settings
# class AdminDashboard(View):
#     def get(self, request):
#         data = Sevices_Model.objects.all()
#         installed_apps = [app.split('.')[-1] for app in settings.INSTALLED_APPS]
#         print("Installed Django +++++++++++++++++++++++++++++++applications:", ', '.join(installed_apps))
        
#         # Render the template and return the HTTP response
#         return render(request, "dashboard/dashboard.html",)
    




# def searchdoctor(request):
#     doctors = Doctor.objects.all()
#     durations = AppointmentDuration.appointment_time() 
#     if request.method == "POST":  # Add a colon here
#         text = request.POST.get("search")
#         search_doctors = Doctor.objects.filter(Q(name__icontains=text) | Q(email__icontains=text))
#         context = {
#             "search_doctors": search_doctors,
#             "doctors":doctors,
#             "durations":durations,
#         }
#         return render(request, "appointment.html", context)
#     context = {
#         "doctors":doctors,
#         "durations":durations,
#     }
#     return render(request, "appointment.html",context)


# class ApplyLeaveView(View):
    
#     def get(self,request):
    
#         return render(request,"leave.html")
    
#     # def post(self, request):
#     #     try:
#     #         name = request.POST.get("name")
#     #         usertype = request.POST.get("usertype")
#     #         email = request.POST.get("email")
#     #         password = request.POST.get("password")
#     #         if not self.validateform(request, usertype, email):
#     #             return render(request, "register.html", self.context)
#     #         obj = User.objects.create(username=email,email=email,password=password,first_name=name)
#     #         obj.set_password(obj.password)
#     #         obj.save()
#     #         UserProfile.objects.create(user=obj, user_type=usertype)
#     #         return redirect('login')
#     #     except Exception as e:

#     #         return render(request,"register.html",self.context)
