from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views import View

from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from apps.users.models import UserProfile

from django.contrib import messages
from apps.users.enums import UserType
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth  import get_user_model
User = get_user_model()


class Register(View):
    usertypes = UserType.usertypes() 
    context = {"usertypes":usertypes }

    def get(self,request):
        return render(request,"register.html",self.context)
    
    def post(self, request):
        try:
            name = request.POST.get("name")
            usertype = request.POST.get("usertype")
            email = request.POST.get("email")
            password = request.POST.get("password")
            if not self.validateform(request, usertype, email):
                return render(request, "register.html", self.context)
            obj = User.objects.create(username=email,email=email,password=password,first_name=name)
            obj.set_password(obj.password)
            obj.save()
            UserProfile.objects.create(user=obj, user_type=usertype)
            return redirect('login')
        except Exception as e:

            return render(request,"register.html",self.context)
    
    @staticmethod
    def validateform(request, usertype, email):
        user = User.objects.filter(username=email).exists()
        if user:
            messages.info(request, "Email is already registered")
            return False
        if not usertype:
            messages.info(request, "Please Select usertype")
            return False
        return True




def Login(request):
    if  request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
     
        user = authenticate(request,username=email,password=password)
        if user is not None:
            auth_login(request, user)
            user=request.user
            user =UserProfile.objects.filter(user=user).first()
            usertype = user.user_type
            
            if usertype =="Staff":
                return redirect('dashboard')
            if usertype =="Doctor":
                return redirect('doctor-appointments')
            if usertype =="Patient":
                return redirect('home')         
        else:
            messages.info(request ,"Incorrect Username or Password")
            return render(request, 'login.html')
    return render(request,'login.html')


def logout(request):
    user_logout(request)
    return redirect('/login')
