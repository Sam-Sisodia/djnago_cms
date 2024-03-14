
from . import views
from django.urls import path

app_name = "myapp"
urlpatterns = [
    path('', views.GetDoctors.as_view(), name='index'),
    path('contact/', views.content, name='index'),

]
