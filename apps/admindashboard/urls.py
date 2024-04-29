
from . import views
from django.urls import path

from apps.admindashboard import views

urlpatterns = [
    
    path("all-appointments/", views.AdminAppointments.as_view() ,name="all-appointments"),
    path("",views.AdminDashboard.as_view(), name="dashboard"),
    path("all-doctors/",views.AllDoctorsView.as_view(),name="all-doctors"),
    path("add-doctors/",views.AddDoctors.as_view(),name="add-doctors"),
    path('edit-doctor/<int:doctor_id>/', views.EditDoctor.as_view(), name='edit-doctor'),
    path('delete-doctor/<int:doctor_id>/',views.deletedoctor, name='delete-doctor'),

    

]