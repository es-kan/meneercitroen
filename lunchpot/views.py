# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from models import Person, LunchEvent, GroceryEvent


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context['lunches'] = LunchEvent.objects.all()
        context['groceries'] = GroceryEvent.objects.all()
        return context
