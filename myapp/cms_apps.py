from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from . import views
from django.urls import path

@apphook_pool.register  # register the application
class PollsApphook(CMSApp):
    app_name = "myapp"
    name = "Myapplication"

    def get_urls(self, page=None, language=None, **kwargs):
    #     return [  path("", views.BookAppointment.as_view() ,name="home"),
    #         path("my-data/", views.MyAppointments.as_view() ,name="my-data"),
    #         path("show-data/",views.Showdata.as_view(),name="show-data")
    # ]   
        return ["myapp.urls"]