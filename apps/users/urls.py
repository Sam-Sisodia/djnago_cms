
from django.urls import path

from apps.users import views
urlpatterns = [
    path("register",views.Register.as_view(),name="register"),
    path('login/',views.Login, name = "login"),
  

]