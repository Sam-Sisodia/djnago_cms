
from . import views
from django.urls import path


urlpatterns = [
    
    path("apply-leave/",views.ApplyLeaveView.as_view(),name="apply-leave"),
    path("my-leaves/",views.AllAppiedLeave.as_view(),name="my-leaves"),
]