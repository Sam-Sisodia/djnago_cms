from django.shortcuts import render

# Create your views here.
from django.views import View



class ApplyLeaveView(View):
    def get(self,request):
        return render(request,"leave.html")