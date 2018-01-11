# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='complete_date',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='dob',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='childattendance',
            name='complete_date',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, blank=True, choices=[('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Mail', 'MAIL')], max_length=8),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_date',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True),
        ),
    ]
