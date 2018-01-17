# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0023_auto_20180117_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysurvey',
            name='ADVOCATE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='OTHER_REC',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='PEOPLE',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, null=True, choices=[('Call', 'CALL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Text', 'TEXT')], blank=True),
        ),
    ]
