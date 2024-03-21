
from . import views
from django.urls import path

app_name = "myapp"

urlpatterns = [
    
    path("", views.BookAppointment.as_view() ,name="home"),
    path("my-data/", views.MyAppointments.as_view() ,name="my-data"),
    path("en/show-data/",views.Showdata.as_view(),name="show-data")

]
