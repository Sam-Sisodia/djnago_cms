from django.shortcuts import render
from apps.leaves.enums import Leavetype,LeaveHours,Leaveduration
# Create your views here.
from django.views import View
from apps.leaves.models import Leave
from django.shortcuts import redirect
from datetime import datetime, timedelta
from apps.doctors.models import Doctor



def createLeave(request,leavetype,start_date,end_date,message,leavehour):
    if start_date :
        leave_duration = Leaveduration.Singleday.value
        # Set start time to current time
        current_time = datetime.now().strftime("%H:%M")
       
        current_date = datetime.now().date()
        end_time = datetime.combine(current_date, datetime.min.time()) + timedelta(days=1)
        print("+______________________________________________",request.user)
        u = Doctor.objects.filter(doctor=request.user).first()
        print("+++++++++77777777777777777777++++++",u)
    

        # Calculate end date based on start date

        # Set end time to midnight
       
        print("+++++++++++++",request.user.id , type(request.user.id))
     
        leave = Leave(
                leave_type=leavetype,
                start_date=start_date,
                message=message,
                end_date = start_date,
                start_time = current_time,
                end_time = end_time,
                leave_duration =leave_duration,
               
               

            )
        leave.save()



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
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++",leavetype)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        message = request.POST.get('message')
        leavehour = request.POST.get('leavehour')
        createLeave(request,leavetype,start_date,end_date,message,leavehour,)
      


        # Save the leave information to the database
  

        # Optionally, you can redirect the user to a success page
        return redirect('my-leaves')
        


class AllAppiedLeave(View):
    def get(self,request):
        user =  request.user
        print(user.id)
        leaves = Leave.objects.filter(doctor_id = user.id)
        context = {
            "leaves":leaves,
        }
        return render(request,"myleaves.html",context)
    