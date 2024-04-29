
from apps.doctors import views
from django.urls import path


urlpatterns = [
    
    path("",views.DoctorAppointments.as_view(),name="doctor-appointments"),

]