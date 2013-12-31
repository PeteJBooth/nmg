from adminsortable.models import Sortable
from cms.models import CMSPlugin
from django.core.urlresolvers import reverse
from django.db import models
from common.models import Fancy   
from filer.fields.image import FilerImageField
#from adminsortable.models import Sortable


class CaseStudy(Sortable,Fancy):
    name = models.CharField(max_length=30, unique=True,
        help_text="Name of the case study. Can be anything up to 30 \
        characters.")
    slug = models.SlugField(null=True)
    project_type = models.CharField(max_length=7,blank=False,default='web', choices=(('web', 'Website design'),
        ('app', 'App design'),
        ('web-app', 'Website and app design'))
    )
    role = models.CharField(max_length=30,)
    agency = models.CharField(max_length=30,)
    promo_teaser =  models.CharField(max_length=100,)
    portfolio_introduction  = models.TextField()
    task = models.TextField()
    main_copy = models.TextField()  
    image = FilerImageField(null=True, blank=False, help_text="We recommend using the largest, highest quality image you can.\
        Images are automatically resized/cropped before being displayed on the site. Don't forget to set the location of the \
        subject via the image management interface")
    featured = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-fancyness']


class CaseStudyPlugin(CMSPlugin):
    #  The plugin model can have any fields it wants.
    #  They are the fields that get displayed if you edit the plugin.
    casestudy = models.ForeignKey(CaseStudy)

    def __unicode__(self):
        return self.casestudy.namey

class CaseStudyImage(Sortable):
    property = models.ForeignKey(CaseStudy,related_name='gallery', blank=True ,null=True)
    image = FilerImageField(related_name="casestudy_images")

    class Meta(Sortable.Meta):
        pass
