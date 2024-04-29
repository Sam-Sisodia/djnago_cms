
from . import views
from django.urls import path


urlpatterns = [
    # path("my-leaves/",views.ApplyLeaveView.as_view(),name="my-leaves"),
    path("apply-leave/",views.ApplyLeaveView.as_view(),name="apply-leave"),
]