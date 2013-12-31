from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nmg.views.home', name='home'),
    # url(r'^nmg/', include('nmg.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf here ...



if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

urlpatterns += staticfiles_urlpatterns()