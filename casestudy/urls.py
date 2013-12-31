from django.conf.urls import patterns, url
from .views import PortfolioListView, PortfolioDetailView

urlpatterns = patterns('',
    url(r'^$', PortfolioListView.as_view(), name='portfolio_list'),
    url(r'^(?P<slug>[\w-]+)/$', PortfolioDetailView.as_view(), name='portfolio_detail'),
)