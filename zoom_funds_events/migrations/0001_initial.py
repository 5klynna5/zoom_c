# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, null=True, max_length=25)),
                ('num_attendees', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
