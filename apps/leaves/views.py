from django.shortcuts import render
from apps.leaves.enums import Leavetype,LeaveHours,Leaveduration
# Create your views here.
from django.views import View
from apps.leaves.models import Leave
from django.shortcuts import redirect
from datetime import datetime, timedelta, time
from apps.doctors.models import Doctor



def createLeave(request,leavetype,start_date,end_date,message,leavehour):
    current_time = datetime.now().strftime("%H:%M")
       
    current_date = datetime.now().date()
    # end_time = datetime.combine(current_date, datetime.min.time()) + timedelta(days=1)
    end_time = datetime.combine(current_date, time.min) + timedelta(days=1)
    doctor_obj = Doctor.objects.filter(user=request.user).first()


    if leavehour:
        leave_duration = Leaveduration.Hours.value
        current_date = datetime.now()
        new_datetime = current_date + timedelta(hours=int(leavehour))
        new_time = new_datetime.time()
        end_time = new_time.strftime("%H:%M")
        print("++++++++++++",end_time)
        
        leave = Leave(
                leave_type=leavetype,
                start_date=start_date,
                message=message,
                end_date = start_date,
                start_time = current_time,
                end_time = end_time,
                leave_duration =leave_duration,
                doctor = doctor_obj
            )
        leave.save()
        return leave
    

    if start_date and end_date:
        leave_duration = Leaveduration.Multipledays.value
        leave = Leave(
                leave_type=leavetype,
                start_date=start_date,
                message=message,
                end_date = end_date,
                start_time = current_time,
                end_time = end_time,
                leave_duration =leave_duration,
                doctor = doctor_obj

            )
        leave.save()
        return leave
        
        
    if start_date :
        leave_duration = Leaveduration.Singleday.value
        leave = Leave(
                leave_type=leavetype,
                start_date=start_date,
                message=message,
                end_date = start_date,
                start_time = current_time,
                end_time = end_time,
                leave_duration =leave_duration,
                doctor = doctor_obj

            )
        
        leave.save()
        return leave



class ApplyLeaveView(View):
    def get(self,request):
        leavetype = Leavetype.leavetypes()
        leavehours = LeaveHours.leave_hours()
        context = {
            "leavetypes":leavetype,
            "leavehours" : leavehours
        }
        return render(request,"leave.html",context)
    
    def post(self, request):
        leavetype = request.POST.get('leavetype')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        message = request.POST.get('message')
        leavehour = request.POST.get('leavehour')
        createLeave(request,leavetype,start_date,end_date,message,leavehour,)
        return redirect('my-leaves')
        


class AllAppiedLeave(View):
    def get(self,request):
        user =  request.user
        print(user.id)
        # leaves = Leave.objects.all()
        doctor_obj = Doctor.objects.filter(user=request.user).first()

        leaves = Leave.objects.filter(doctor = doctor_obj)
        context = {
            "leaves":leaves,
        }
        return render(request,"myleaves.html",context)
    