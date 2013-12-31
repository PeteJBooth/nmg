# core
from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import TextField

# third-party
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor

# user-defined
from common.models import Callout, FullWidthImage, YouTubeVideo
#from common.models import DoubleImagePluginModel
#from common.models import LargeImagePluginModel
#from common.models import TripleTextPluginModel
#from common.models import TwoRowTextPluginModel
#from common.models import IframePluginModel
#from datetime import date

#-----------------------------------------------------------------------------

class FullWidthImagePlugin(CMSPluginBase):
    model = FullWidthImage
    name = 'Full width image'
    render_template = 'plugins/full_width_image.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder
        })
        return context

class CallOutOnLeftPlugin(CMSPluginBase):
    model = Callout
    name = 'Callout on left'
    render_template = 'plugins/callout_on_left.html'
    formfield_overrides = {
        TextField: {'widget': WYMEditor},
    }
    
    #=change_form_template = "product/plugins/simple_tinymce_change_form.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder
        })
        return context


class CallOutOnRightPlugin(CMSPluginBase):
    model = Callout
    name = 'Callout on right'
    render_template = 'plugins/callout_on_right.html'
    #change_form_template = "product/plugins/simple_tinymce_change_form.html"
    formfield_overrides = {
        TextField: {'widget': WYMEditor},
    }

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder
        })
        return context

class YouTubeVideoPlugin(CMSPluginBase):
    model = YouTubeVideo
    name = 'YouTube video'
    render_template = 'plugins/video.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder
        })
        return context

"""
class TripleTextBlockPlugin(CMSPluginBase):
    model = TripleTextPluginModel
    name = _('Row of three text blocks')
    render_template = 'work/plugins/triple_text_block.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context


class TwoRowTextBlockPlugin(CMSPluginBase):
    model = TwoRowTextPluginModel
    name = _('Two rows of text')
    render_template = 'common/plugins/two_row_text_block.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'weekday':date.today().strftime("%A")
        })
        return context


class IframePlugin(CMSPluginBase):
    model = IframePluginModel
    name = _('Iframe')
    render_template = 'common/plugins/iframe.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context
"""


plugin_pool.register_plugin(FullWidthImagePlugin)
plugin_pool.register_plugin(YouTubeVideoPlugin)
plugin_pool.register_plugin(CallOutOnLeftPlugin)
plugin_pool.register_plugin(CallOutOnRightPlugin)
#plugin_pool.register_plugin(TripleTextBlockPlugin)
#plugin_pool.register_plugin(TwoRowTextBlockPlugin)
#plugin_pool.register_plugin(IframePlugin)