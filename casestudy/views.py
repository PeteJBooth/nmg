from django.shortcuts import get_object_or_404
from django.utils import translation
# from django.utils.translation import ugettext_lazy as _

from django.http import Http404
from django.views.generic import DetailView, ListView
from .models import CaseStudy

class PortfolioListView(ListView):
    model = CaseStudy

    def get_queryset(self):
        return CaseStudy.objects.filter(active=True)

class PortfolioDetailView(DetailView):
    model = CaseStudy
    context_object_name = "casestudy"

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView,self).get_context_data(**kwargs)
        context['featured_casestudies'] = CaseStudy.objects.filter(active=True,featured=True)[:4]
        return context

