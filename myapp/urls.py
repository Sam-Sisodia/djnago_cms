
from . import views
from django.urls import path

# app_name = "myapp"

urlpatterns = [
    
    path("", views.BookAppointment.as_view() ,name="home"),
    path("all-appointments/", views.AdminAppointments.as_view() ,name="all-appointments"),
    path("show-data/",views.Showdata.as_view(),name="show-data"),
    path("dashboard/",views.AdminDashboard.as_view(), name="dashboard"),
    path("register",views.Register.as_view(),name="register"),
    path('login/',views.Login, name = "login"),
    path("doctor-appointments/",views.DoctorAppointments.as_view(),name="doctor-appointments"),
    path("search-doctor/",views.searchdoctor,name="search-doctor")

]
