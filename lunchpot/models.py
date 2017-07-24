# -*- coding: utf-8 -*-
from django.core.validators import MinLengthValidator
from django.db import models

from functions import format_currency


# static variable(s)
LUNCH_COST = 2.50


class Person(models.Model):
    @classmethod
    def create(cls, name, deposit=0, debt=0):
        person = cls(name=name, deposit=(deposit - debt))
        person.save()
        return person

    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    deposit = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'people'

    def __unicode__(self):
        return self.name

    def deposit_money(self, amount):
        self.deposit += amount
        self.save()

    def get_balance(self):
        return self.deposit - self.get_total_spent()

    def get_balance_formatted(self):
        return format_currency(self.get_balance())
    get_balance_formatted.short_description = "balance"

    def get_total_spent(self):
        return self.lunchevent_set.aggregate(models.Sum('cost'))['cost__sum']

    def has_debt(self):
        return self.get_balance() < 0

    def get_debt(self):
        return self.get_balance() * -1 if self.has_debt() else 0


class Event(models.Model):
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class GroceryEventManager(models.Manager):
    def total_price(self):
        return GroceryEvent.objects.all().aggregate(total=models.Sum('price'))['total']


class GroceryEvent(Event):
    objects = GroceryEventManager()
    price = models.FloatField()

    def __unicode__(self):
        return "{date}: {price}".format(date=self.date, price=format_currency(self.price))


class LunchEventManager(models.Manager):
    def total_cost(self):
        return LunchEvent.objects.all().aggregate(total=models.Sum('cost'))['total']


class LunchEvent(Event):
    objects = LunchEventManager()
    participants = models.ManyToManyField(Person)
    cost = models.FloatField(default=LUNCH_COST)

    def __unicode__(self):
        return "{date}: {participants}".format(date=self.date, participants=u', '.join([str(i) for i in self.participants.all()]))
