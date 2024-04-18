
from . import views
from django.urls import path

# app_name = "myapp"

urlpatterns = [
    
    path("", views.BookAppointment.as_view() ,name="home"),
    path("all-appointments/", views.MyAppointments.as_view() ,name="all-appointments"),
    path("show-data/",views.Showdata.as_view(),name="show-data"),
    path("dashboard/",views.AdminDashboard.as_view(), name="dashboard")
    

]
