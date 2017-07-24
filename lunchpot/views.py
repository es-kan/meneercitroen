# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from operator import methodcaller

from models import Person, LunchEvent, GroceryEvent


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['lunches'] = LunchEvent.objects.all()
            context['people'] = sorted(Person.objects.all(), key=methodcaller('get_balance'), reverse=True)
            context['grocery_data'] = GroceryEvent.objects.get_data()
            context['total_balance'] = Person.objects.get_total_balance()
        else:
            context['lunches'] = LunchEvent.objects.with_person(self.request.user.person)
        context['groceries'] = GroceryEvent.objects.all()
        return context
