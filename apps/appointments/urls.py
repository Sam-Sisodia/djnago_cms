
from  apps.appointments import views
from django.urls import path

urlpatterns = [
    
    path("", views.BookAppointment.as_view() ,name="home"),
   
    path("search-doctor/",views.searchdoctor,name="search-doctor"),
    

]