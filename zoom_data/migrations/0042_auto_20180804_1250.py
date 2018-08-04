# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0041_auto_20180804_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, max_length=8, choices=[('Call', 'CALL'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Text', 'TEXT')], null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='shelter',
            field=models.ForeignKey(help_text='If a shelter was most recent location, please record name of shelter here.', null=True, blank=True, to='zoom_data.Shelter'),
        ),
    ]
