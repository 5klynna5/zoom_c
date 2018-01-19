# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0017_auto_20180119_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='volunteer_activity',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(null=True, max_length=16, choices=[('Call', 'CALL'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Do Not Contact', 'DO_NOT_CONTACT')], blank=True),
        ),
        migrations.AlterField(
            model_name='volunteergroup',
            name='volunteer_activity',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]
