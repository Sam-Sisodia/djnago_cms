
from . import views
from django.urls import path

from apps.admindashboard import views

urlpatterns = [
    
    path("all-appointments/", views.AdminAppointments.as_view() ,name="all-appointments"),
    path("",views.AdminDashboard.as_view(), name="dashboard"),
    path("all-doctors/",views.AllDoctorsView.as_view(),name="all-doctors"),
    path("hospitals",views.HospitalsView.as_view(),name="hospitals"),
    path("add-doctors/",views.AddDoctors.as_view(),name="add-doctors"),
    path("add-hospital/",views.AddHostpital.as_view(),name="add-hospital"),

    path('edit-doctor/<int:doctor_id>/', views.EditDoctor.as_view(), name='edit-doctor'),
    path('delete-doctor/<int:doctor_id>/',views.deletedoctor, name='delete-doctor'),
    
    path('edit-hospital/<int:doctor_id>/', views.EditHospital.as_view(), name='edit-hospital'),
    path('delete-hospital/<int:doctor_id>/',views.deletehospital, name='delete-hospital'),



]

# AddHostpital
# EditHospital
# deletehospital