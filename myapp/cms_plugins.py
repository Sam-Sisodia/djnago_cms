from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from . models import Sevices_Model

@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "hello.html"
    cache = False



@plugin_pool.register_plugin
class ServicePlugIn(CMSPluginBase):
    model = Sevices_Model
    name = _("Service Plugin")
    render_template = "show.html"
    cache = False


    def render(self, context, instance, placeholder):
        data = Sevices_Model.objects.all()
        context ={
            "data": data
        }
        # Render the template and return the HTTP response
        return context
       
        # context = super().render(context, instance, placeholder)
       
        # return context

