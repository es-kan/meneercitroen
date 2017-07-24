from django.contrib import admin
from models import GroceryEvent, LunchEvent, Person


class EventAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, *args, **kwargs):
        return ("date_created", "date_modified",)


@admin.register(GroceryEvent)
class GroceryEventAdmin(EventAdmin):
    pass


@admin.register(LunchEvent)
class LunchEventAdmin(EventAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_balance_formatted')
