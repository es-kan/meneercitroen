from lunchpot.models import Person, LunchEvent, GroceryEvent
import datetime

'''
Execute this file if you want to initialize an empty database.
'''

people = {'Ad-Jan': 13, 'Alwin': 55, 'Rob': 16, 'Arthur': 2, 'Jeroen': 3, 'Helene': 36, 'Florian': 10, 'Mirko': 2, 'Sandra': 2}

for name in people:
    person = Person.objects.get(user__username=name)
    counter = 0
    for event in LunchEvent.objects.all():
        event.participants.add(person)
        event.save()
        counter += 1
        if counter >= people[name]:
            break

'''
57.90 in de pot!
588.31 totale inleg
36 totale schuld
552 totale balans

494.10 opgemaakt aan boodschappen dus.

99x boodschappen gedaan in totaal dus voor 5.00 per boodschap
'''
date = datetime.date.today()
for i in range(99):
    event = GroceryEvent(date_modified=date, notes="Placeholder vanwege migratie.", price=5.0)
    event.save()
