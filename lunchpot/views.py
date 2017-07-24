# from django.shortcuts import render
from django.views.generic import TemplateView

from models import Person


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        return context
