from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import ScholarshipInfo


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'scholarship_list'

    def get_queryset(self):
        return ScholarshipInfo.objects.order_by('vl_ano')


class DetailView(generic.DetailView):
    model = ScholarshipInfo
    template_name = 'pages/detail.html'