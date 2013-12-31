import os
from django.db import models

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from cms.plugins.text.models import AbstractText

from filer.fields.image import FilerImageField
from filer.models.filemodels import File as FilerFile

# ----------------------------------------------------------------------------

class TimeStamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedActivate(TimeStamped):
    active = models.BooleanField(default=False, help_text="Controls whether \
        or not this item is live to the world.")

    class Meta:
        abstract = True

class Fancy(TimeStampedActivate):
    fancyness = models.IntegerField(blank=False,default=1,null=False,
        help_text="Fancyness is a measure of how high up a page a given object will be shown.\
            A higher fancyness value will put an object higher up the page/menu")

    class Meta:
        abstract = True



class AbstractCallout(AbstractText):
    """
    Abstract model that defines the common fields shared by all callout copy blocks
    """
    header = models.CharField(
        max_length=50, blank=True, null=False, help_text="Optional header \
        to appear above callout text.  50 characters max length.")
    #copy = models.TextField()

    class Meta :
        abstract = True

class Callout(AbstractCallout):
    """
    a model for the callout cms plugin with a 1 column, large numeric/% header, 
    followed by some highlighted copy
    """
    callout_header = models.CharField(
        max_length=4, blank=True, null=False, help_text="A short (4 character max) header to displayed in large\
        text about the Callout Copy.")
    callout_copy = models.CharField(
        max_length=50, blank=True, null=False, help_text="The text to display highlighted in the callout column.")


class FullWidthImage(CMSPlugin):
    image = FilerImageField(null=True, blank=False)

class SeoDataMixin(models.Model):
    seo_title = models.CharField(blank=True,default='',max_length=50,verbose_name="Page Title", help_text="Overwrites what is displayed at the top of your browser or in bookmarks")
    seo_meta_description = models.TextField(blank=True,default='',verbose_name="Description meta tag", help_text="A description of the page sometimes used by search engines.")
    seo_meta_keywords = models.CharField(blank=True,default='',max_length=300,verbose_name="Keywords meta tag", help_text="A list of comma separated keywords sometimes used by search engines.")

    class Meta:
        abstract = True

class IframePluginModel(CMSPlugin):
    src = models.CharField(blank=True,default='',max_length=200,verbose_name="Iframe URL", help_text="A fully qualified url for the content you wish to iframe into the site")
    height = models.IntegerField(blank=True, default=200, verbose_name="Iframe Height (px)", help_text="The height at which the Iframe will be rendered on the site. Width is set at 100% of the page width as standard.")

class YouTubeVideo(CMSPlugin):
    video_id = models.CharField(blank=True,default='',max_length=12,verbose_name="YouTube Video ID", help_text="The ID of the video to be\
        included in the page. e.g. http://www.youtube.com/watch?v=<strong>XlgQxK-HBGk</strong>")
    aspect_ratio = models.CharField(blank=False,max_length=5,default="16:9",help_text="The aspect ratio of the video to be included.\
     i.e. The ratio of it's width to height. If your not sure what the aspect ratio is, must widescreen videos are '16:9', whilst older\
     format videos are '4:3'." )

#class CustomFile(FilerFile):
#    @classmethod
#    def matches_file_type(cls, iname, ifile, request):
#        iext = os.path.splitext(iname)[1].lower()
#        return iext in ['.doc', '.xls', '.pdf', '.ppt']    
