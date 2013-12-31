from adminsortable.admin import SortableAdmin,SortableTabularInline
from django.contrib import admin
from .models import CaseStudy,CaseStudyImage

# ----------------------------------------------------------------------------
class CaseStudyImageAdmin(SortableTabularInline):
    model = CaseStudyImage
    extra = 1

class CaseStudyAdmin(SortableAdmin):
    model = CaseStudy
    list_display = ('__unicode__','fancyness','featured','active',)
    list_editable = ('fancyness','featured','active',)

    inlines = [CaseStudyImageAdmin,]

    def __init__(self, *args, **kwargs):
        super(CaseStudyAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('name',)}

admin.site.register(CaseStudy, CaseStudyAdmin)


