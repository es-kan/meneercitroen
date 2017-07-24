# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField()),
                ('notes', models.TextField(null=True, blank=True)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LunchEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField()),
                ('notes', models.TextField(null=True, blank=True)),
                ('cost', models.FloatField(default=2.5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('deposit', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AddField(
            model_name='lunchevent',
            name='participants',
            field=models.ManyToManyField(to='lunchpot.Person'),
        ),
    ]
