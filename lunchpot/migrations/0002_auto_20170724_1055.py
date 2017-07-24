# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lunchpot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groceryevent',
            name='date_created',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='groceryevent',
            name='date_modified',
            field=models.DateField(verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='lunchevent',
            name='date_created',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='lunchevent',
            name='date_modified',
            field=models.DateField(verbose_name=b'Date'),
        ),
    ]
