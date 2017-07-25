# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.db import models

from functions import format_currency


# static variable(s)
LUNCH_COST = 2.50


class PersonManager(models.Manager):
    def get_total_balance(self):
        balance = 0.0
        for person in Person.objects.all():
            balance += person.deposit
            balance -= person.get_debt()
        for event in GroceryEvent.objects.all():
            balance -= event.price
        return balance


class Person(models.Model):
    @classmethod
    def create(cls, name, deposit=0, debt=0):
        person = cls(name=name, deposit=(deposit - debt))
        person.save()
        return person

    objects = PersonManager()
    deposit = models.FloatField(default=0)
    user = models.OneToOneField(User)

    class Meta:
        verbose_name_plural = 'people'

    def __unicode__(self):
        return self.user.username

    def get_name(self):
        return self.user.username

    def deposit_money(self, amount):
        self.deposit += amount
        self.save()

    def get_balance(self):
        return self.deposit - self.get_total_spent()

    def get_balance_formatted(self):
        return format_currency(self.get_balance())
    get_balance_formatted.short_description = "balance"

    def get_total_spent(self):
        if self.lunchevent_set.exists():
            return self.lunchevent_set.aggregate(models.Sum('cost'))['cost__sum']
        else:
            return 0

    def get_times_joined(self):
        return len(self.lunchevent_set.all())

    def has_debt(self):
        return self.get_balance() < 0

    def get_debt(self):
        return self.get_balance() * -1 if self.has_debt() else 0

    def get_positive_balance(self):
        return self.get_balance() if not self.has_debt() else 0


class Event(models.Model):
    date_created = models.DateField(editable=False)
    date_modified = models.DateField(verbose_name='Date')
    notes = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = datetime.date.today()
        return super(Event, self).save(*args, **kwargs)


class GroceryEventManager(models.Manager):
    def total_price(self):
        return GroceryEvent.objects.all().aggregate(total=models.Sum('price'))['total']

    def get_data(self):
        data = {'total_price': 0.0, 'average': 0.0, 'average_per_lunch': 0.0}
        if GroceryEvent.objects.all().exists():
            data['total_price'] = self.total_price()
            data['average'] = data['total_price'] / len(GroceryEvent.objects.all())
            data['average_per_lunch'] = data['total_price'] / len(LunchEvent.objects.all())
        return data


class GroceryEvent(Event):
    objects = GroceryEventManager()
    price = models.FloatField()

    def __unicode__(self):
        return "{date}: {price}".format(date=self.date_modified, price=format_currency(self.price))

    def get_price(self):
        return format_currency(self.price)


class LunchEventManager(models.Manager):
    def total_cost(self):
        return LunchEvent.objects.all().aggregate(total=models.Sum('cost'))['total']

    def with_person(self, person):
        return LunchEvent.objects.filter(participants=person)


class LunchEvent(Event):
    objects = LunchEventManager()
    participants = models.ManyToManyField(Person)
    cost = models.FloatField(default=LUNCH_COST)

    def __unicode__(self):
        return "{date}: {participants}".format(date=self.date_modified, participants=u', '.join([str(i) for i in self.participants.all()]))
