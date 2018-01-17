# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0022_auto_20180117_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysurvey',
            name='INCENTIVE',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, blank=True, choices=[('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Text', 'TEXT')], max_length=8),
        ),
    ]
