from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import CaseStudyPlugin

# ----------------------------------------------------------------------------


class CaseStudyPlugin(CMSPluginBase):
    model = CaseStudyPlugin
    name = "Casestudy"
    render_template = "casestudy_promo.html"

    def render(self, context, instance, placeholder):
        context.update({
            'casestudy': instance.casestudy,
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CaseStudyPlugin)


