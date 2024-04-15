
from . import views
from django.urls import path

# app_name = "myapp"

urlpatterns = [
    
    path("", views.BookAppointment.as_view() ,name="home"),
    path("my-data/", views.MyAppointments.as_view() ,name="my-data"),
    path("show-data/",views.Showdata.as_view(),name="show-data"),
    path("admin-dashboard/",views.AdminDashboard.as_view(), name="admin-dashboard")
    

]
