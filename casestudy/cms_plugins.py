from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import CaseStudyPlugin,CaseStudyCarouselSlide

# ----------------------------------------------------------------------------


class CaseStudyPlugin(CMSPluginBase):
    model = CaseStudyPlugin
    name = "Casestudy"
    render_template = "casestudy/casestudy_promo.html"

    def render(self, context, instance, placeholder):
        context.update({
            'casestudy': instance.casestudy,
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CaseStudyPlugin)

class CaseStudyCarouselPlugin(CMSPluginBase):
    model = CaseStudyCarouselSlide
    name = "Casestudy carousel slide"
    render_template = "casestudy/casestudy_slide.html"

    def render(self, context, instance, placeholder):
        context.update({
            'casestudy': instance.casestudy,
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CaseStudyCarouselPlugin)


